from datetime import datetime
from functools import wraps
from http import HTTPStatus
from pathlib import Path
from pydantic import BaseModel
from typing import List, Dict, Optional
import aiofiles
import aiohttp
import asyncio
import json
import logging
import random
import re
import requests
import requests.compat
import tqdm
from uau_api.settings import Settings
from uau_api.requestsapi import RequestsApi


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = logging.FileHandler('uau_api.log')
file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(log_format)

# Add handlers to the logger
logger.addHandler(file_handler)

class Processo(BaseModel):
    NumeroProcesso: int
    Empresa: int
    Obra: str


class EmpresaObra(BaseModel):
    Empresa: int
    Obra: str


class EmpresaObraPeriodo(BaseModel):
    EmpresaObra: List[EmpresaObra]
    PeriodoInicial: str
    PeriodoFinal: str


class Fornecedor(BaseModel):
    cnpjFornecedor: str


class DadosFornecedor(BaseModel):
    Fornecedor: List[Fornecedor]
    PeriodoInicial: str
    PeriodoFinal: str


class RootModel(BaseModel):
    Processos: List[Processo] | None = None
    EmpresaObraPeriodo: EmpresaObraPeriodo
    FornecedorPeriodo: DadosFornecedor | None = None

def exception_handler(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # Extract function arguments, excluding `self` or `cls`
            filtered_args = [arg for arg in args if not hasattr(arg, '__dict__')]
            response = getattr(e.response, 'json', lambda: None)() if hasattr(e, 'response') else None
            error = json.dumps({
                'error': str(e),
                'function': func.__name__,
                'args': filtered_args,  # Exclude `self`
                'kwargs': kwargs,
                'response': response
            })
            logger.error(error)
    return inner_function


# Assuming RequestsApi and Settings are defined elsewhere
class Uau(RequestsApi):
    def __init__(self, url):
        super().__init__(url)
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        self._authenticated = False
        self._api_key = Settings().API_KEY

    @property
    def is_authenticated(self):
        return self._authenticated

    def login(self, login: str, senha: str):
        """
        'Login': 'str',
        'Senha': 'str',
        'UsuarioUAUSite': 'str'
        """
        user = {
            'Login': login,
            'Senha': senha,
            'UsuarioUAUSite': login
        }
        self.headers['X-INTEGRATION-Authorization'] = self._api_key

        response = self.post(
            'Autenticador/AutenticarUsuario',
            headers=self.headers,
            data=json.dumps(user)
        )
        
        if response.status_code == HTTPStatus.OK:
            self.headers['Authorization'] = response.json()
            self.session.headers.update(self.headers)
            self._authenticated = True
        else:
            self.session.close()
            self._authenticated = False
            response.raise_for_status()

        return response

    def get_session(self):
        """Return the current session for use in other classes"""
        if not self.is_authenticated:
            raise ValueError("Must call login() before getting session")
        return self.session

    def get_headers(self):
        """Return the current headers with auth token for use in other classes"""
        if not self.is_authenticated:
            raise ValueError("Must call login() before getting headers") 
        return self.headers.copy()

    @staticmethod
    def query_construct(
        empresa_obra: List[dict],
        periodo_inicial: datetime,
        periodo_final: datetime,
        processos: Optional[List[int]] = None,
        fornecedores: Optional[List[dict]] = None,
    ) -> RootModel:
        """
        Constructs a RootModel object from the given parameters.

        Args:
            empresa_obra (List[dict]): List of dictionaries representing empresa_obra.
            periodo_inicial (str): Start period in ISO format.
            periodo_final (str): End period in ISO format.
            processos (Optional[List[dict]]): List of dictionaries representing processos.
            fornecedores (Optional[List[dict]]): List of dictionaries representing fornecedores.

        Returns:
            RootModel: A pydantic model populated with the provided data.
        """
        # Convert periodo_inicial and periodo_final to datetime
        periodo_inicial_dt = periodo_inicial.isoformat()
        periodo_final_dt = periodo_final.isoformat()

        # Create EmpresaObraPeriodo object
        empresa_obra_periodo = EmpresaObraPeriodo(
            EmpresaObra=[EmpresaObra(**obra) for obra in empresa_obra],
            PeriodoInicial=periodo_inicial_dt,
            PeriodoFinal=periodo_final_dt,
        )

        # Create FornecedorPeriodo object if fornecedores is provided
        fornecedor_periodo = None
        if fornecedores:
            fornecedor_periodo = DadosFornecedor(
                Fornecedor=[Fornecedor(**fornecedor) for fornecedor in fornecedores],
                PeriodoInicial=periodo_inicial_dt,
                PeriodoFinal=periodo_final_dt,
            )

        # Create processos list if provided
        processos_list = None
        if processos:
            processos_list = [Processo(**processo) for processo in processos]

        # Construct the RootModel
        return RootModel(
            Processos=processos_list,
            EmpresaObraPeriodo=empresa_obra_periodo,
            FornecedorPeriodo=fornecedor_periodo,
        )

    

    @exception_handler
    def get_users(self, username=None):
        payload = {'login_usuario': username} if username else {}
        response = self.post('Usuarios/ConsultarUsuariosAtivos', json=payload)
        response.raise_for_status()
        return response.json()

    @exception_handler
    def inserir_insumo(self, insumo):
        """
        Insere insumo no planejamento da obra.
        """
        consulta_servico = self.post(
            'Planejamento/ConsultarServicoPlanejamento', json=insumo
        ).json()

        servico_existe = len(consulta_servico) > 1

        if not servico_existe:
            return

        response = self.post(
            'Planejamento/AtualizarInsumosPlanejamento', json={'Insumos': [insumo]}
        )

        if response.status_code != HTTPStatus.OK:
            response.raise_for_status()

        return response.json()
    
    @exception_handler
    def gerar_itens_processo(
        self,
        item: str,
        quantidade: float,
        preco: float,
        cap: str,
        categoria_movimentacao_financeira: str,
        unidade: str,
        vinculo_pl_item: str,
        vinculo_pl_codigo_produto: int,
        vinculo_pl_contrato: int,
        vinculo_pl_servico: str,
        vinculo_pl_insumo: str,
        vinculo_pl_mes_planejamento: str,
        vinculo_pl_quantidade: float,
        vinculo_pl_preco: float,
    ):
        return [
            {
                'Item': item,
                'Quantidade': quantidade,
                'Preco': preco,
                'Cap': cap,
                'CategoriaMovimentacaoFinanceira': categoria_movimentacao_financeira,
                'Unidade': unidade,
                'VinculoPL': [
                    {
                        'Item': vinculo_pl_item,
                        'CodigoProduto': vinculo_pl_codigo_produto,
                        'Contrato': vinculo_pl_contrato,
                        'Servico': vinculo_pl_servico,
                        'Insumo': vinculo_pl_insumo,
                        'MesPlanejamento': vinculo_pl_mes_planejamento,
                        'Quantidade': vinculo_pl_quantidade,
                        'Preco': vinculo_pl_preco,
                    }
                ],
            }
        ]

    @exception_handler
    def gerar_processo_pagamento(
        self,
        empresa: int,
        obra: str,
        codigo_fornecedor: int,
        nome_fornecedor: str,
        tipo_processo: int,
        controlar_estoque: int,
        acompanha_entrega: int,
        tipo_item: int,
        parametro_codigo_departamento: str,
        parametro_taxa_juros: int,
        parametro_taxa_multa: int,
        parametro_tipo_juros: int,
        parametro_retroagir: int,
        parcelas_datavencimento: str,
        parcelas_valor: float,
        parcelas_banco: str,
        parcelas_conta: str,
        parcelas_tipo_emissao: str,
        parcelas_forma_pagamento: str,
        parcelas_tipo_pagamento: str,
        parcelas_codigo_de_barras: str,
        parcelas_observacao_pagamento: str,
        parcelas_data_documento_fiscal: str,
        parcelas_numero_documentofiscal: str,
        itens: List[Dict],
    ):
        {
            'Empresa': empresa,
            'Obra': obra,
            'CodigoFornecedor': codigo_fornecedor,
            'NomeFornecedor': nome_fornecedor,
            'TipoProcesso': tipo_processo,
            'ControlarEstoque': controlar_estoque,
            'AcompanhaEntrega': acompanha_entrega,
            'TipoItem': tipo_item,
            'Parametro': {
                'CodigoDepartamento': parametro_codigo_departamento,
                'TaxaJuros': parametro_taxa_juros,
                'TaxaMulta': parametro_taxa_multa,
                'TipoJuros': parametro_tipo_juros,
                'Retroagir': parametro_retroagir,
            },
            'Parcelas': [
                {
                    'Datavencimento': parcelas_datavencimento,
                    'Valor': parcelas_valor,
                    'Banco': parcelas_banco,
                    'Conta': parcelas_conta,
                    'TipoEmissao': parcelas_tipo_emissao,
                    'FormaPagamento': parcelas_forma_pagamento,
                    'TipoPagamento': parcelas_tipo_pagamento,
                    'CodigoDeBarras': parcelas_codigo_de_barras,
                    'ObservacaoPagamento': parcelas_observacao_pagamento,
                    'DataDocumentoFiscal': parcelas_data_documento_fiscal,
                    'NumeroDocumentofiscal': parcelas_numero_documentofiscal,
                }
            ],
            'Itens': itens,
        }

    @exception_handler
    def consultar_desembolso_planejamento(
        self, empresa: int, obra: str, mes_inicial: str, mes_final: str
    ):
        """
        Consulta o desembolso do planejamento para uma empresa/obra em um período.

        Args:
            empresa (int): Código da empresa
            obra (str): Código da obra
            mes_inicial (str): Mês inicial no formato MM/YYYY
            mes_final (str): Mês final no formato MM/YYYY

        Returns:
            Response: Resposta da requisição HTTP contendo os dados do planejamento
        """
        planejamento = self.post(
            'Planejamento/ConsultarDesembolsoPlanejamento',
            json={
                'Empresa': empresa,
                'Obra': obra,
                'MesInicial': mes_inicial,
                'MesFinal': mes_final,
            },
        )
        if not planejamento.status_code == HTTPStatus.OK:
            raise ValueError(planejamento.json())
        return planejamento.json()

    @exception_handler
    def atualizar_servico_planejamento(self, data: Dict) -> dict:
        """
            post /api/v{version}/Planejamento/AtualizarServicoPlanejamento

        {
        "Empresa": 0,
        "Obra": "string",
        "Produto": "string",
        "Contrato": "string",
        "Item": "string",
        "Servico": "string",
        "Qtde": 0,
        "DataInicio": "string",
        "DataTermino": "string",
        "Usuario": "string"
        }

        """
        response = self.post('Planejamento/AtualizarServicoPlanejamento', json=data)
        response.raise_for_status()
        return response.json()

    @exception_handler
    def inserir_servico_planejamento_mes(self, data: Dict):
        """
            post /api/v{version}/Planejamento/InserirServicoPlanejamentoMes

        {
        "Empresa": 0,
        "Obra": "string",
        "Produto": "string",
        "Contrato": "string",
        "Item": "string",
        "Servico": "string",
        "Mes": "string",
        "Qtde": 0,
        "Usuario": "string"
        }

        """
        response = self.post('Planejamento/InserirServicoPlanejamentoMes', json=data)
        if 'Já existe serviço cadastrado para os parâmetros informados, verifique.' in response.text:
            return response.text
        response.raise_for_status()
        return response.json()


    @exception_handler
    def atualizar_servico_planejamento_mes(self, data: Dict):
        """
            post /api/v{version}/Planejamento/AtualizarServicoPlanejamentoMes


        {
          "Empresa": 0,
          "Obra": "string",
          "Produto": "string",
          "Contrato": "string",
          "Item": "string",
          "Servico": "string",
          "Mes": "string",
          "Qtde": 0,
          "Usuario": "string"
        }

        """
        response = self.post('Planejamento/AtualizarServicoPlanejamentoMes', json=data)
        return response.text

    @exception_handler
    def atualizar_insumos_planejamento(self, data: Dict):
        """
            post /api/v{version}/Planejamento/AtualizarInsumosPlanejamento
            {
          "Insumos": [
            {
              "Empresa": 0,
              "Obra": "string",
              "Produto": 0,
              "Contrato": 0,
              "Item": "string",
              "Servico": "string",
              "MesPl": "string",
              "Insumo": "string",
              "quantidade": 0,
              "preco": 0
            }
          ],
          "justificativaAprovacaoPl": "string"
        }
        """
        if not isinstance(data, dict):
            raise TypeError('Os dados devem ser do tipo dict')

        response = self.post('Planejamento/AtualizarInsumosPlanejamento', json=data)
        response.raise_for_status()
        return response.json()
    
    
    @exception_handler
    def exportar_planejamento_produto(self, empresa: int, obra: str) -> dict:
        """post /api/v{version}/Planejamento/ExportarPlanejamentoProduto"""
        response = self.post(
            'Planejamento/ExportarPlanejamentoProduto',
            json={
                'Empresa': int(empresa),
                'Obra': str(obra),
                'Contrato': '-3',
                'Produto': '-3',
            },
        )
        response.raise_for_status()
        return response.json()

    @exception_handler
    def consultar_insumosGeral(self, insumo: str) -> dict:
        response = self.post(
            'InsumosGeral/ConsultarInsumosGeral', json={'codigo_insumo': insumo}
        ).json()
        if len(response[0]['Table1']) == 1:
            raise ValueError(
                f'Insumo {insumo} não encontrado ou contém parâmetros incorretos'
            )
        return response[0]['Table1'][-1]

    
    
    
    
    
    
    
    # Pessoas
    
    @exception_handler
    def consultar_pessoa_por_chave(self, codigo_pessoa: str) -> dict:
        response = self.post(
            'Pessoas/ConsultarPessoaPorChave', json={'codigo_pessoa': codigo_pessoa}
        )
        
        response.raise_for_status()
        response = response.json()[-1]['MyTable'][-1]
        
        if 'System' in str(response.get('cod_pes')):
            raise ValueError(f'{codigo_pessoa} - Pessoa não encontrada')
        
        return response
    
    @exception_handler
    def consultar_pessoas_por_cpf_cnpj(self, cpf_cnpj: str, status: str) -> dict:
        cpf_cnpj = re.sub(r'[\.\-]', '', cpf_cnpj)
        response = self.post(
            'Pessoas/ConsultarPessoasPorCPFCNPJ', json={'cpf_cnpj': cpf_cnpj, 'status': status}
        )
        response.raise_for_status()
        return response.json()
    
    @exception_handler
    def consultar_contas_bancarias(self, codigo: int) -> dict:
        """
        Consulta as contas bancárias de uma pessoa.
        """
        try:
            codigo = int(codigo)
        except (TypeError, ValueError):
            raise TypeError(f'codigo must be convertible to integer, got {type(codigo)}')

        response = self.post('Pessoas/ConsultarContasBancarias', json={'codigo': codigo})
        
        response.raise_for_status()
        return response.json()
    
    
    
    @exception_handler
    def obter_obras_ativas(self) -> dict:
        # post /api/v{version}/Obras/ObterObrasAtivas
        response = self.post('Obras/ObterObrasAtivas')
        response.raise_for_status()
        return response.json()
    
class ProcessoPagamento(Uau):
    @exception_handler
    def consultar_processos(
        self,
        empresa_obra: List[Dict],
        periodo_inicial: datetime,
        periodo_final: datetime,
        processos: Optional[List[dict]] = None,
        fornecedores: Optional[List[dict]] = None,
    ):
        """
                {
        "Processos": [
            {
            "NumeroProcesso": 0,
            "Empresa": 0,
            "Obra": "string"
            }
        ],
        "EmpresaObraPeriodo": {
            "EmpresaObra": [
            {
                "Empresa": 0,
                "Obra": "string"
            }
            ],
            "PeriodoInicial": "2025-01-10T10:50:05.464Z",
            "PeriodoFinal": "2025-01-10T10:50:05.464Z"
        },
        "FornecedorPeriodo": {
            "Fornecedor": [
            {
                "cnpjFornecedor": "string"
            }
            ],
            "PeriodoInicial": "2025-01-10T10:50:05.464Z",
            "PeriodoFinal": "2025-01-10T10:50:05.464Z"
        }
        }
        """

        data: BaseModel = self.query_construct(
            empresa_obra=empresa_obra,
            processos=processos,
            periodo_inicial=periodo_inicial,
            periodo_final=periodo_final,
            fornecedores=fornecedores,
        )
        response = self.post(
            'ProcessoPagamento/ConsultarProcessos', data=json.dumps(data.model_dump())
        )
        response.raise_for_status()
        return response.json()

    @exception_handler
    def manutencao_processo(self, data: Dict):
        response = self.post('ProcessoPagamento/ManutencaoProcesso', json=data)
        response.raise_for_status()
        return response.json()

    def gerar_nota_fiscal(self, data: Dict):
        response = self.post('ProcessoPagamento/GerarNotaFiscal', json=data)
        response.raise_for_status()
        return response.json()
    
    @exception_handler
    def gerar_processo(self, data: Dict):
        response = self.post('ProcessoPagamento/GerarProcesso', json=data)
        response.raise_for_status()
        return response.json()
    
async def async_download_file(session: aiohttp.ClientSession, url: str) -> bytes:
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.read()
            return None
    except Exception:
        return None


async def async_save_file(content: bytes, destination: Path) -> None:
    if content is None:
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        async with aiofiles.open(destination, mode="wb") as f:
            await f.write(content)


async def process_item(session: aiohttp.ClientSession, url: str, destination: Path|str) -> None:
    '''
    
    '''
    destination = Path(destination)

    if destination.exists():
        return

    content = await async_download_file(session, url)
    await async_save_file(content, destination)
    await asyncio.sleep(random.uniform(0.1, 0.3))

async def main(iterable, url, wd, destination):
    async with aiohttp.ClientSession() as session:
        tasks = []
        with tqdm(total=len(iterable), desc="Downloading covers") as pbar:
            for item in iterable:
                link = requests.compat.urljoin(url, item)
                destination = wd / destination
                task = asyncio.create_task(process_item(session, link, destination))
                task.add_done_callback(lambda _: pbar.update(1))
                tasks.append(task)
                
                # Process in chunks to avoid overwhelming the server
                if len(tasks) >= 10:
                    await asyncio.gather(*tasks)
                    tasks = []
            
            if tasks:
                await asyncio.gather(*tasks)

# Run the async main function
    await main()