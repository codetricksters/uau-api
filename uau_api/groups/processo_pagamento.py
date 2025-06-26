from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class ProcessoPagamento:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_processo(
        self,
        empresa: Optional[Any] = None,
        obra: Optional[str] = None,
        codigo_fornecedor: Optional[Any] = None,
        tipo_processo: Optional[Any] = None,
        controlar_estoque: Optional[Any] = None,
        acompanha_entrega: Optional[Any] = None,
        data_previsao_entrega: Optional[datetime] = None,
        tipo_item: Optional[Any] = None,
        historico_lanc_contabil: Optional[str] = None,
        historico_lanc_contabil_pago: Optional[str] = None,
        categoria_movimentacao_financeira: Optional[str] = None,
        numero_contrato: Optional[Any] = None,
        parametro: Optional[Dict] = None,
        parcelas: Optional[List[Dict]] = None,
        itens: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/GerarProcesso`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        Dados básicos para o funcionamento da API.
        
        Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Gera um processo de pagamento.
        
        É obrigatório informar os dados básicos do processo de pagamento.
        O usuário autenticado precisa ter acesso à empresa e obra que está fazendo a requisição.
        O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.
        
        Args:
            Empresa (Any): The empresa
            Obra (str): The obra
            CodigoFornecedor (Any): The codigo fornecedor
            TipoProcesso (Any): The tipo processo
            ControlarEstoque (Any): The controlar estoque
            AcompanhaEntrega (Any): The acompanha entrega
            DataPrevisaoEntrega (datetime): The data previsao entrega
            TipoItem (Any): The tipo item
            HistoricoLancContabil (str): The historico lanc contabil
            HistoricoLancContabilPago (str): The historico lanc contabil pago
            CategoriaMovimentacaoFinanceira (str): The categoria movimentacao financeira
            NumeroContrato (Any): The numero contrato
            Parametro (Dict[str, Any]): The parametro
            Parcelas (List[Dict[str, Any]]): The parcelas
            Itens (List[Dict[str, Any]]): The itens
        
        Parameter Structure:
        
            {
                "Empresa": "int",
                "Obra": "string",
                "CodigoFornecedor": "int",
                "TipoProcesso": "int",
                "ControlarEstoque": "int",
                "AcompanhaEntrega": "int",
                "DataPrevisaoEntrega": "2025-04-23T14:40:27.862Z",
                "TipoItem": "int",
                "HistoricoLancContabil": "string",
                "HistoricoLancContabilPago": "string",
                "CategoriaMovimentacaoFinanceira": "string",
                "NumeroContrato": "int",
                "Parametro": {
                    "CodigoDepartamento": "string",
                    "TaxaJuros": "int",
                    "TaxaMulta": "int",
                    "TipoJuros": "int",
                    "Retroagir": "int"
                },
                "Parcelas": [
                    {
                        "Datavencimento": "2025-04-23T14:40:27.862Z",
                        "Valor": "float",
                        "Descontos": [
                            {
                                "Descricao": "string",
                                "Valor": "float",
                                "DataVencimento": "2025-04-23T14:40:27.862Z",
                                "Cap": "string",
                                "HistoricoLancamentoContabil": "string"
                            }
                        ],
                        "DocumentoFiscal": {
                            "NumeroNota": "int",
                            "SerieNota": "string",
                            "EspecieNota": "string",
                            "TipoNota": "int",
                            "NFEletronica": "int",
                            "ChaveNFe": "string"
                        }
                    }
                ],
                "Itens": [
                    {
                        "Item": "string",
                        "Quantidade": "float",
                        "Preco": "float",
                        "Cap": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "Unidade": "string",
                        "VinculoPL": [
                            {
                                "Item": "string",
                                "CodigoProduto": "int",
                                "Contrato": "int",
                                "Servico": "string",
                                "Insumo": "string",
                                "MesPlanejamento": "2025-04-23T14:40:27.862Z",
                                "Quantidade": "float",
                                "Preco": "float"
                            }
                        ]
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_processo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/GerarProcesso"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "CodigoFornecedor": codigo_fornecedor,
            "TipoProcesso": tipo_processo,
            "ControlarEstoque": controlar_estoque,
            "AcompanhaEntrega": acompanha_entrega,
            "DataPrevisaoEntrega": data_previsao_entrega,
            "TipoItem": tipo_item,
            "HistoricoLancContabil": historico_lanc_contabil,
            "HistoricoLancContabilPago": historico_lanc_contabil_pago,
            "CategoriaMovimentacaoFinanceira": categoria_movimentacao_financeira,
            "NumeroContrato": numero_contrato,
            "Parametro": parametro,
            "Parcelas": parcelas,
            "Itens": itens,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_processos(
        self,
        processos: Optional[List[Dict]] = None,
        empresa_obra_periodo: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/ConsultarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Permite consultar processos por diversos filtros.
        
        Args:
            Processos (List[Dict[str, Any]]): The processos
            EmpresaObraPeriodo (Dict[str, Any]): The empresa obra periodo
        
        Parameter Structure:
        
            {
                "Processos": [
                    {
                        "NumeroProcesso": "int",
                        "Empresa": "int",
                        "Obra": "string"
                    }
                ],
                "EmpresaObraPeriodo": {
                    "EmpresaObra": [
                        {
                            "Empresa": "int",
                            "Obra": "string"
                        }
                    ],
                    "PeriodoInicial": "2025-04-23T14:40:27.862Z",
                    "PeriodoFinal": "2025-04-23T14:40:27.862Z"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._consultar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/ConsultarProcessos"
        kwargs = {
            "Processos": processos,
            "EmpresaObraPeriodo": empresa_obra_periodo,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def aprovar_dvq(
        self,
        dvq: Optional[str] = None,
        aprovar: Optional[bool] = None,
        usuario: Optional[str] = None,
        sobrepor_aprovacoes_de_outros_usuarios: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/AprovarDVQ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Permite a aprovação DVQ de parcelas específicas.
        
        No request [dvq] deve ser informado qual a letra que será aprovada ou não.
        Os seguintes parâmetros obrigatórios para aprovação da letra "D":  Confirmação de data
        usrConfirmou
        codigoEmpresa
        codigoObra
        numeroProcesso
        numeroParcela 
        
        
        Os seguintes parâmetros obrigatórios para aprovação da letra "V" : Confirmação do valor
        usrConfirmou
        codigo_empresa
        codigo_obra
        numero_processo
        codigo_departamento
        numero_parcela
        status_processo
        valor_parcela      
        
        
        Os seguintes parâmetros obrigatórios para aprovação da letra "Q" : Confirmação da quantidade
        usrConfirmou
        codigo_empresa
        codigo_obra
        numero_processo
        numero_parcela
        status_processo
        tipo_Docprocesso
        adiantamento_parcela       
        
        
        
        
        Será validado as permissões do usuário informado. Verifique as permissões caso esteja sendo retornado erro na requisição;
        FID : Permissão para aprovar "D"
        FIV : Permissão para aprovar "V"
        FIQ : Permissão para aprovar "Q"
        
        
        O usuário autenticado precisa ter acesso a empresa e a obra da qual está fazendo a requisição.   
        Será apenas validado a aprovação DVQ das parcelas informadas. Recomendado utilizar a API [RetornarParcelasDVQ] para retornar as informações das parcelas.
        
        
        
        Args:
            dvq (str): The dvq
            aprovar (int): The aprovar
            usuario (str): The usuario
            sobreporAprovacoesDeOutrosUsuarios (int): The aprovacoes de outros usuarios
            parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "dvq": "string",
                "aprovar": true,
                "usuario": "string",
                "sobreporAprovacoesDeOutrosUsuarios": true,
                "parcelas": [
                    {
                        "numero_processo": 0,
                        "numero_parcela": 0,
                        "codigo_empresa": 0,
                        "nome_empresa": "string",
                        "codigo_obra": "string",
                        "nome_obra": "string",
                        "valor_total": 0,
                        "status_d": "string",
                        "status_v": "string",
                        "status_q": "string",
                        "codigo_departamento": "string",
                        "status_processo": 0,
                        "tipo_DocProcesso": 0,
                        "adiantamento_parcela": 0,
                        "valor_parcela": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._aprovardvq(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/AprovarDVQ"
        kwargs = {
            "dvq": dvq,
            "aprovar": aprovar,
            "usuario": usuario,
            "sobreporAprovacoesDeOutrosUsuarios": sobrepor_aprovacoes_de_outros_usuarios,
            "parcelas": parcelas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_processo(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        codigo_fornecedor: Optional[int] = None,
        tipo_processo: Optional[int] = None,
        controlar_estoque: Optional[int] = None,
        acompanha_entrega: Optional[int] = None,
        data_previsao_entrega: Optional[datetime] = None,
        tipo_item: Optional[int] = None,
        historico_lanc_contabil: Optional[str] = None,
        historico_lanc_contabil_pago: Optional[str] = None,
        categoria_movimentacao_financeira: Optional[str] = None,
        numero_contrato: Optional[int] = None,
        parametro: Optional[Dict] = None,
        parcelas: Optional[List[Dict]] = None,
        itens: Optional[List[Dict]] = None,
        desconto_vinculado: Optional[List[Dict]] = None,
        solicitacao_caixa_obra: Optional[Dict] = None,
        permite_boleto_vencido: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/GerarProcesso`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        Dados básicos para o funcionamento da API.
        
        Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Documentação API - Gerar Processo (Clique Aqui)
        
        Definição de Negócio:
        Gera um processo de pagamento.
        
        É obrigatório informar os dados básicos do processo de pagamento.
        O usuário autenticado precisa ter acesso à empresa e obra que está fazendo a requisição.
        O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.
        Só aceita os tipos de processo de pagamento: composições e insumos, insumos planejados, adiantamento de caixa de obra, patrimônio vinculado ao planejamento.
        Você pode informar uma parcela ou uma lista de parcelas.
        Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de DocumentoFiscal; o documento deve existir.
        Você pode aplicar desconto normal à parcela, informe os dados de desconto no objeto Descontos.
        Quando o insumo PL for do tipo 1 - quantidade, será considerado o preço do item.
        Somente podem ser gerados processos dos tipos: 1 - Processo de Pagamento, 11 - Compra de patrimônio, 13 - Adiantamento de caixa de obra.
        Processos de pagamento de serviços gerarão automaticamente os descontos vinculados (impostos) caso estejam configurados.
        Categoria de movimentação financeira na propriedade de Item:
          Deve adicionar a propriedade CategoriaMovimentacaoFinanceira na propriedade de Item, para armazenar o código da categoria de movimentação financeira.Não é obrigatório informar o parâmetro CategoriaMovimentacaoFinanceira.
        Caso não seja informado o tipo de pagamento TipoPagamento ou tipo de emissão TipoEmissao, será considerada a configuração padrão do processo de pagamento.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            CodigoFornecedor (int): The codigo fornecedor
            TipoProcesso (int): The tipo processo
            ControlarEstoque (int): The controlar estoque
            AcompanhaEntrega (int): The acompanha entrega
            DataPrevisaoEntrega (datetime): The data previsao entrega
            TipoItem (int): The tipo item
            HistoricoLancContabil (str): The historico lanc contabil
            HistoricoLancContabilPago (str): The historico lanc contabil pago
            CategoriaMovimentacaoFinanceira (str): The categoria movimentacao financeira
            NumeroContrato (int): The numero contrato
            Parametro (Dict[str, Any]): The parametro
            Parcelas (List[Dict[str, Any]]): The parcelas
            Itens (List[Dict[str, Any]]): The itens
            DescontoVinculado (List[Dict[str, Any]]): The desconto vinculado
            SolicitacaoCaixaObra (Dict[str, Any]): The solicitacao caixa obra
            PermiteBoletoVencido (int): The permite boleto vencido
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "CodigoFornecedor": 0,
                "TipoProcesso": 0,
                "ControlarEstoque": 0,
                "AcompanhaEntrega": 0,
                "DataPrevisaoEntrega": "2025-04-23T13:46:14.007Z",
                "TipoItem": 0,
                "HistoricoLancContabil": "string",
                "HistoricoLancContabilPago": "string",
                "CategoriaMovimentacaoFinanceira": "string",
                "NumeroContrato": 0,
                "Parametro": {
                    "CodigoDepartamento": "string",
                    "TaxaJuros": 0,
                    "TaxaMulta": 0,
                    "TipoJuros": 0,
                    "Retroagir": 0,
                    "IndiceReajuste": "string",
                    "DataIncioReajuste": "2025-04-23T13:46:14.007Z",
                    "CodigoMunicipio": 0,
                    "VincularDocFiscalTodosProcessos": true
                },
                "Parcelas": [
                    {
                        "Datavencimento": "2025-04-23T13:46:14.007Z",
                        "Valor": 0,
                        "Descontos": [
                            {
                                "Descricao": "string",
                                "Valor": 0,
                                "DataVencimento": "2025-04-23T13:46:14.007Z",
                                "Cap": "string",
                                "HistoricoLancamentoContabil": "string"
                            }
                        ],
                        "DocumentoFiscal": {
                            "NumeroNota": 0,
                            "SerieNota": "string",
                            "EspecieNota": "string",
                            "TipoNota": 0,
                            "NFEletronica": 0,
                            "ChaveNFe": "string"
                        },
                        "Banco": "string",
                        "Conta": "string",
                        "Convenio": "string",
                        "TipoEmissao": "string",
                        "FormaPagamento": "string",
                        "TipoPagamento": "string",
                        "CodigoDeBarras": "string",
                        "PixCopiaCola": "string",
                        "TXID": "string"
                    }
                ],
                "Itens": [
                    {
                        "Item": "string",
                        "Quantidade": 0,
                        "Preco": 0,
                        "Cap": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "Unidade": "string",
                        "VinculoPL": [
                            {
                                "Item": "string",
                                "CodigoProduto": 0,
                                "Contrato": 0,
                                "Servico": "string",
                                "Insumo": "string",
                                "MesPlanejamento": "2025-04-23T13:46:14.007Z",
                                "Quantidade": 0,
                                "Preco": 0,
                                "NumeroItemContrato": 0
                            }
                        ],
                        "CodJustificativa": 0,
                        "Justificativa": "string"
                    }
                ],
                "DescontoVinculado": [
                    {
                        "Descricao": "string",
                        "DataVencimento": "2025-04-23T13:46:14.007Z",
                        "Valor": 0,
                        "Cap": "string",
                        "CodigoFornecedor": 0,
                        "Nominal": "string",
                        "ItemProcesso": "string",
                        "ObraFiscal": "string",
                        "HistoricoLancamentoContabilPagar": "string",
                        "HistoricoLancamentoContabilPago": "string",
                        "CategoriaMovimentacaoFinanceira": "string"
                    }
                ],
                "SolicitacaoCaixaObra": {
                    "NumeroSolicitacao": 0,
                    "UsuarioAprovacao": "string",
                    "Empresa": 0,
                    "Obra": "string",
                    "NumeroProcesso": 0
                },
                "PermiteBoletoVencido": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_processo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/GerarProcesso"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "CodigoFornecedor": codigo_fornecedor,
            "TipoProcesso": tipo_processo,
            "ControlarEstoque": controlar_estoque,
            "AcompanhaEntrega": acompanha_entrega,
            "DataPrevisaoEntrega": data_previsao_entrega,
            "TipoItem": tipo_item,
            "HistoricoLancContabil": historico_lanc_contabil,
            "HistoricoLancContabilPago": historico_lanc_contabil_pago,
            "CategoriaMovimentacaoFinanceira": categoria_movimentacao_financeira,
            "NumeroContrato": numero_contrato,
            "Parametro": parametro,
            "Parcelas": parcelas,
            "Itens": itens,
            "DescontoVinculado": desconto_vinculado,
            "SolicitacaoCaixaObra": solicitacao_caixa_obra,
            "PermiteBoletoVencido": permite_boleto_vencido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_nota_fiscal(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        numero_processo: Optional[int] = None,
        parcela: Optional[int] = None,
        tiponf: Optional[int] = None,
        especie: Optional[str] = None,
        serie: Optional[str] = None,
        nf_eletronica: Optional[bool] = None,
        chave_nfe: Optional[str] = None,
        numero_nota_fiscal: Optional[str] = None,
        codigo_remetente: Optional[int] = None,
        data_emissao: Optional[datetime] = None,
        data_de_emissao_maior_que_cadastro: Optional[bool] = None,
        data_entrada: Optional[datetime] = None,
        data_de_entrada_maior_que_cadastro: Optional[bool] = None,
        modelonf: Optional[int] = None,
        arq_nota_fiscal: Optional[str] = None,
        caminho_origem_arquivo_local: Optional[str] = None,
        caminho_destino_arquivo: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        copiar_arquivo: Optional[bool] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/GerarNotaFiscal`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Gerar nota fiscal de entrada de acordo com os dados do processo
        
        É obrigatório informar os dados básicos da nota fiscal.
        O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
        O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção;
        Serão utilizadas as informações fiscais de tributo cadastradas no produto ou na empresa.
        Especies disponíveis para geração do documento fiscal (NF - Nota fiscal, CT - Conhecimento de transporte, RE - Recibo, OU - Outros, CF - Cupom fiscal)
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            NumeroProcesso (int): The numero processo
            Parcela (int): The parcela
            TipoNF (int): The tipo n f
            Especie (str): The especie
            Serie (str): The serie
            NFEletronica (int): The n f eletronica
            ChaveNfe (str): The chave nfe
            NumeroNotaFiscal (str): The numero nota fiscal
            CodigoRemetente (int): The codigo remetente
            DataEmissao (datetime): The data emissao
            DataDeEmissaoMaiorQueCadastro (int): The data de emissao maior que cadastro
            DataEntrada (datetime): The data entrada
            DataDeEntradaMaiorQueCadastro (int): The data de entrada maior que cadastro
            ModeloNF (int): The modelo n f
            ArqNotaFiscal (str): The arq nota fiscal
            CaminhoOrigemArquivoLocal (str): The caminho origem arquivo local
            CaminhoDestinoArquivo (str): The caminho destino arquivo
            NomeArquivo (str): The nome arquivo
            CopiarArquivo (int): The copiar arquivo
            VincularADescontos (int): The vincular a descontos
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "NumeroProcesso": 0,
                "Parcela": 0,
                "TipoNF": 0,
                "Especie": "string",
                "Serie": "string",
                "NFEletronica": true,
                "ChaveNfe": "string",
                "NumeroNotaFiscal": "string",
                "CodigoRemetente": 0,
                "DataEmissao": "2025-04-23T13:46:14.015Z",
                "DataDeEmissaoMaiorQueCadastro": true,
                "DataEntrada": "2025-04-23T13:46:14.015Z",
                "DataDeEntradaMaiorQueCadastro": true,
                "ModeloNF": 0,
                "ArqNotaFiscal": "string",
                "CaminhoOrigemArquivoLocal": "string",
                "CaminhoDestinoArquivo": "string",
                "NomeArquivo": "string",
                "CopiarArquivo": true,
                "VincularADescontos": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/GerarNotaFiscal"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "NumeroProcesso": numero_processo,
            "Parcela": parcela,
            "TipoNF": tiponf,
            "Especie": especie,
            "Serie": serie,
            "NFEletronica": nf_eletronica,
            "ChaveNfe": chave_nfe,
            "NumeroNotaFiscal": numero_nota_fiscal,
            "CodigoRemetente": codigo_remetente,
            "DataEmissao": data_emissao,
            "DataDeEmissaoMaiorQueCadastro": data_de_emissao_maior_que_cadastro,
            "DataEntrada": data_entrada,
            "DataDeEntradaMaiorQueCadastro": data_de_entrada_maior_que_cadastro,
            "ModeloNF": modelonf,
            "ArqNotaFiscal": arq_nota_fiscal,
            "CaminhoOrigemArquivoLocal": caminho_origem_arquivo_local,
            "CaminhoDestinoArquivo": caminho_destino_arquivo,
            "NomeArquivo": nome_arquivo,
            "CopiarArquivo": copiar_arquivo,
            "VincularADescontos": vinculara_descontos,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def aprovar_processos(
        self,
        processos: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/AprovarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        
        O Usuário informado precisa ter a permissão [FICHEQUE] para aprovar as parcelas do processo.
        A(s) parcela(s) precisam estar no "Emissão de Pagamentos" para serem aprovadas.
        Todos os parâmetros são obrigatórios.
        
        
        
        Args:
            processos (List[Dict[str, Any]]): The processos
        
        Parameter Structure:
        
            {
                "processos": [
                    {
                        "cod_empresa": 0,
                        "cod_obra": "string",
                        "numero_processo": "string",
                        "numero_parcela": "string",
                        "tipo_processo": 0,
                        "aprovaro_processo": 0,
                        "login_usuario": "string",
                        "departamento": "string",
                        "cargo": "string",
                        "codigoJustificativa": 0,
                        "observacaoJustificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._aprovar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/AprovarProcessos"
        kwargs = {
            "processos": processos,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_processos(
        self,
        processos: Optional[List[Dict]] = None,
        empresa_obra_periodo: Optional[Dict] = None,
        fornecedor_periodo: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/ConsultarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Permite que você consulte o(s) processo(s) de pagamento por um número e/ou período específico.
        
        Você pode consultar informando uma lista dos números dos processos de pagamento, código da empresa e código da obra cadastrados no UAU.
        Você pode consultar processos de pagamento informado uma lista de código da empresa e código da obra cadastrado no UAU por um determinado período.
        Você pode consultar processos de pagamento informado uma lista de fornecedores cadastrado no UAU por um determinado período.
        O usuário autenticado precisa ter acesso as empresas e obras das quais ele está fazendo a requisição.   
        Caso consulte vários processos ou informe um longo período, sugerimos que consulte o serviço de maneira assíncrona. 
        NovoBeneficiario: O campo Parametro/NovoBeneficiario sempre retornará o valor null. A informação é retornada no campo Parcelas/NovoBeneficiario.
        Caso passe uma mistura de todos os filtros, o filtro de data que será utilizado será o do busca por cnpj a frente do busca por empresas e obras.
          7.1 Caso queria buscar por períodos diferentes recomendamos utilizar requests separados para respeitar os períodos por grupo separado.
        
        
        
        Args:
            Processos (List[Dict[str, Any]]): The processos
            EmpresaObraPeriodo (Dict[str, Any]): The empresa obra periodo
            FornecedorPeriodo (Dict[str, Any]): The fornecedor periodo
        
        Parameter Structure:
        
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
                    "PeriodoInicial": "2025-04-23T13:46:14.060Z",
                    "PeriodoFinal": "2025-04-23T13:46:14.060Z"
                },
                "FornecedorPeriodo": {
                    "Fornecedor": [
                        {
                            "cnpjFornecedor": "string"
                        }
                    ],
                    "PeriodoInicial": "2025-04-23T13:46:14.060Z",
                    "PeriodoFinal": "2025-04-23T13:46:14.060Z"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._consultar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/ConsultarProcessos"
        kwargs = {
            "Processos": processos,
            "EmpresaObraPeriodo": empresa_obra_periodo,
            "FornecedorPeriodo": fornecedor_periodo,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def manutencao_processo(
        self,
        numero: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        codigo_fornecedor: Optional[int] = None,
        codigo_novo_beneficiario: Optional[int] = None,
        antecipado: Optional[bool] = None,
        retroacao: Optional[int] = None,
        codigo_departamento: Optional[str] = None,
        tipo_juros: Optional[int] = None,
        taxa_juros_atraso: Optional[int] = None,
        taxa_multa_atraso: Optional[int] = None,
        chave_nfe: Optional[str] = None,
        parcela: Optional[Dict] = None,
        numero_protocolo: Optional[int] = None,
        permite_boleto_vencido: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/ManutencaoProcesso`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        Dados básicos para o funcionamento da API.
        
        Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os dados de um processo de pagamento: URI + /api/v{version}/ProcessoPagamento/ConsultarProcessos
        Preencher os parâmetros de request para uso do método.
        Documentação API - Manutenção de Processo (Clique Aqui)
        
        Definição de Negócio:
        Permite ajustar informações básicas do processo de pagamento, como vencimento, data de prorrogação, novo beneficiário, fornecedor, etc.
           Consulte a documentação do objeto de request.
        
        É obrigatório informar os dados básicos do processo de pagamento.
        Para alterar informações da parcela do processo, preencha o objeto de Parcelas.
        Todas as alterações gerarão um comentário de alteração no processo.
        O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a alteração.
        O parâmetro CodigoNovoBeneficiario altera todas as parcelas a pagar do processo informado, independentemente da parcela informada.
          Ao informar esse valor no processo, na resposta da request o valor será null, mas estará indicado nas parcelas. Isso ocorre porque esse campo pertence à parcela.
        O parâmetro NovoBeneficiario altera apenas a parcela informada, se ela estiver a pagar.
          Se preencher o parâmetro de beneficiário no processo e na parcela, o parâmetro do processo será desconsiderado, alterando apenas os beneficiários das parcelas informadas.
        Se preencher o valor zero ou vazio para o novo beneficiário, a alteração não será considerada. A API não limpa valores de novo beneficiário.
        
        
        
        Args:
            Numero (int): The numero
            Empresa (int): The empresa
            Obra (str): The obra
            CodigoFornecedor (int): The codigo fornecedor
            CodigoNovoBeneficiario (int): The codigo novo beneficiario
            Antecipado (int): The antecipado
            Retroacao (int): The retroacao
            CodigoDepartamento (str): The codigo departamento
            TipoJuros (int): The tipo juros
            TaxaJurosAtraso (int): The taxa juros atraso
            TaxaMultaAtraso (int): The taxa multa atraso
            ChaveNfe (str): The chave nfe
            Parcela (Dict[str, Any]): The parcela
            NumeroProtocolo (int): The numero protocolo
            PermiteBoletoVencido (int): The permite boleto vencido
        
        Parameter Structure:
        
            {
                "Numero": 0,
                "Empresa": 0,
                "Obra": "string",
                "CodigoFornecedor": 0,
                "CodigoNovoBeneficiario": 0,
                "Antecipado": true,
                "Retroacao": 0,
                "CodigoDepartamento": "string",
                "TipoJuros": 0,
                "TaxaJurosAtraso": 0,
                "TaxaMultaAtraso": 0,
                "ChaveNfe": "string",
                "Parcela": {
                    "Numero": 0,
                    "Prioridade": 0,
                    "Provisionado": 0,
                    "TipoEmissao": "string",
                    "DataVencimento": "2025-04-23T13:46:14.074Z",
                    "DataProrrogacao": "2025-04-23T13:46:14.074Z",
                    "FormaPagamento": "string",
                    "TipoPagamento": "string",
                    "Nominal": "string",
                    "CodigoDeBarras": "string",
                    "ObservacaoPagamento": "string",
                    "ObservacaoEntrega": "string",
                    "ObraFiscal": "string",
                    "HistoricoLancContabil": "string",
                    "CategoriaMovFinanceira": "string",
                    "HistoricoLancContabilPago": "string",
                    "Banco": 0,
                    "Conta": "string",
                    "Convenio": "string",
                    "DataInicioReajuste": "2025-04-23T13:46:14.074Z",
                    "IndiceReajuste": "string",
                    "NovoBeneficiario": 0,
                    "PixCopiaCola": "string"
                },
                "NumeroProtocolo": 0,
                "PermiteBoletoVencido": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._manutencao_processo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/ManutencaoProcesso"
        kwargs = {
            "Numero": numero,
            "Empresa": empresa,
            "Obra": obra,
            "CodigoFornecedor": codigo_fornecedor,
            "CodigoNovoBeneficiario": codigo_novo_beneficiario,
            "Antecipado": antecipado,
            "Retroacao": retroacao,
            "CodigoDepartamento": codigo_departamento,
            "TipoJuros": tipo_juros,
            "TaxaJurosAtraso": taxa_juros_atraso,
            "TaxaMultaAtraso": taxa_multa_atraso,
            "ChaveNfe": chave_nfe,
            "Parcela": parcela,
            "NumeroProtocolo": numero_protocolo,
            "PermiteBoletoVencido": permite_boleto_vencido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def retornar_parcelas_dvq(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        numeroproc: Optional[int] = None,
        fornecedor: Optional[str] = None,
        notafiscal: Optional[int] = None,
        inicial: Optional[str] = None,
        final: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/RetornarParcelasDVQ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Os campos empresa, obra e usuário são obrigatórios.
        É validado se o usuário existe no banco de dados, e se tem permissão na empresa e obra informada.
        Data e Fornecedor devem está vazio ou sem o parâmetro informado na requisição para não serem considerados na consulta.
        Número processo(numeroproc) e notafiscal devem está como 0 ou sem o parâmetro informado na requisição para não serem considerados na consulta.
        O parâmetro nota fiscal é o número de controle interno da nota fiscal.
        Status atual da aprovação status_d, status_v e status_q.
        Valor [A]: aprovado
        Valor [D]: não aprovado
        
        
        
        
        
        Args:
            Usuario (str): The usuario
            Empresa (int): The empresa
            Obra (str): The obra
            numeroproc (int): The numeroproc
            fornecedor (str): The fornecedor
            notafiscal (int): The notafiscal
            inicial (str): The inicial
            final (str): The final
        
        Parameter Structure:
        
            {
                "Usuario": "string",
                "Empresa": 0,
                "Obra": "string",
                "numeroproc": 0,
                "fornecedor": "string",
                "notafiscal": 0,
                "inicial": "string",
                "final": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._retornar_parcelasdvq(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/RetornarParcelasDVQ"
        kwargs = {
            "Usuario": usuario,
            "Empresa": empresa,
            "Obra": obra,
            "numeroproc": numeroproc,
            "fornecedor": fornecedor,
            "notafiscal": notafiscal,
            "inicial": inicial,
            "final": final,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_processo_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None,
        mes_planejamento: Optional[datetime] = None,
        controlar_estoque: Optional[int] = None,
        acompanha_entrega: Optional[int] = None,
        data_previsao_entrega: Optional[datetime] = None,
        historico_lanc_contabil_apagar: Optional[str] = None,
        historico_lanc_contabil_pago: Optional[str] = None,
        historico_lanc_contabil_desc_normal_med: Optional[str] = None,
        categoria_movimentacao_financeira: Optional[str] = None,
        parametro: Optional[Dict] = None,
        documento_fiscal: Optional[Dict] = None,
        parcelas: Optional[List[Dict]] = None,
        itens: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/GerarProcessoMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Gerar processo de pagamento de medição de contrato de material/serviço
        
        É obrigatório informar os dados básicos do processo de pagamento;
        O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
        O usuário autenticado precisa ter acesso a aos programas de permissão necessários para fazer a inserção;
        Você pode informar uma parcela ou uma lista de parcelas;
        Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de “DocumentoFiscal”, o documento deve existir;
        Você pode aplicar desconto normal a parcela, informe os dados de desconto no objeto “Descontos”;
        Quando o insumo PL for do tipo 1 - quantidade será considerado o preço do item;
        
        
        
        Args:
            Empresa (int): The empresa
            Contrato (int): The contrato
            Medicao (int): The medicao
            MesPlanejamento (datetime): The mes planejamento
            ControlarEstoque (int): The controlar estoque
            AcompanhaEntrega (int): The acompanha entrega
            DataPrevisaoEntrega (datetime): The data previsao entrega
            HistoricoLancContabilApagar (str): The historico lanc contabil apagar
            HistoricoLancContabilPago (str): The historico lanc contabil pago
            HistoricoLancContabilDescNormalMed (str): The historico lanc contabil desc normal med
            CategoriaMovimentacaoFinanceira (str): The categoria movimentacao financeira
            Parametro (Dict[str, Any]): The parametro
            DocumentoFiscal (Dict[str, Any]): The documento fiscal
            Parcelas (List[Dict[str, Any]]): The parcelas
            Itens (List[Dict[str, Any]]): The itens
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Contrato": 0,
                "Medicao": 0,
                "MesPlanejamento": "2025-04-23T13:46:14.096Z",
                "ControlarEstoque": 0,
                "AcompanhaEntrega": 0,
                "DataPrevisaoEntrega": "2025-04-23T13:46:14.096Z",
                "HistoricoLancContabilApagar": "string",
                "HistoricoLancContabilPago": "string",
                "HistoricoLancContabilDescNormalMed": "string",
                "CategoriaMovimentacaoFinanceira": "string",
                "Parametro": {
                    "CodigoDepartamento": "string",
                    "TaxaJuros": 0,
                    "TaxaMulta": 0,
                    "TipoJuros": 0,
                    "Retroagir": 0,
                    "IndiceReajuste": "string",
                    "DataIncioReajuste": "2025-04-23T13:46:14.096Z",
                    "CodigoMunicipio": 0,
                    "VincularDocFiscalTodosProcessos": true
                },
                "DocumentoFiscal": {
                    "DocumentoFiscalServico": {
                        "NumeroNota": 0,
                        "SerieNota": "string",
                        "EspecieNota": "string",
                        "TipoNota": 0,
                        "NFEletronica": 0,
                        "ChaveNFe": "string"
                    },
                    "DocumentoFiscalMaterial": {
                        "NumeroNota": 0,
                        "SerieNota": "string",
                        "EspecieNota": "string",
                        "TipoNota": 0,
                        "NFEletronica": 0,
                        "ChaveNFe": "string"
                    }
                },
                "Parcelas": [
                    {
                        "Datavencimento": "2025-04-23T13:46:14.096Z",
                        "Valor": 0,
                        "Descontos": [
                            {
                                "Descricao": "string",
                                "Valor": 0,
                                "DataVencimento": "2025-04-23T13:46:14.096Z",
                                "Cap": "string",
                                "HistoricoLancamentoContabil": "string"
                            }
                        ],
                        "Banco": "string",
                        "Conta": "string",
                        "Convenio": "string",
                        "TipoEmissao": "string",
                        "FormaPagamento": "string",
                        "TipoPagamento": "string"
                    }
                ],
                "Itens": [
                    {
                        "NumeroItemContrato": 0,
                        "ItemMedicao": "string",
                        "Quantidade": 0,
                        "Preco": 0,
                        "Cap": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "VinculoPL": [
                            {
                                "Item": "string",
                                "CodigoProduto": 0,
                                "Contrato": 0,
                                "Servico": "string",
                                "Insumo": "string",
                                "Quantidade": 0,
                                "Preco": 0,
                                "numeroItemContrato": 0
                            }
                        ]
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_processo_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/GerarProcessoMedicao"
        kwargs = {
            "Empresa": empresa,
            "Contrato": contrato,
            "Medicao": medicao,
            "MesPlanejamento": mes_planejamento,
            "ControlarEstoque": controlar_estoque,
            "AcompanhaEntrega": acompanha_entrega,
            "DataPrevisaoEntrega": data_previsao_entrega,
            "HistoricoLancContabilApagar": historico_lanc_contabil_apagar,
            "HistoricoLancContabilPago": historico_lanc_contabil_pago,
            "HistoricoLancContabilDescNormalMed": historico_lanc_contabil_desc_normal_med,
            "CategoriaMovimentacaoFinanceira": categoria_movimentacao_financeira,
            "Parametro": parametro,
            "DocumentoFiscal": documento_fiscal,
            "Parcelas": parcelas,
            "Itens": itens,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def manutencao_parcelas_processo(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_processo: Optional[int] = None,
        data_vencimento: Optional[datetime] = None,
        qtde_parcelas: Optional[int] = None,
        intervalo_parcelas: Optional[int] = None,
        lista_parcelas_manutencao: Optional[List[Dict]] = None,
        lista_valores_novas_parcelas: Optional[List[Dict]] = None,
        lista_valores_acrescimo_novas_parcelas: Optional[List[Dict]] = None,
        lista_data_vencimento_novas_parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/ManutencaoParcelasProcesso`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite dar manutenção nas parcelas do processo de pagamento. Ao informar os dados para as novas parcelas, será simulado e gerado automaticamente as novas parcelas
          com novas numerações, valores e data de vencimento. Será excluido a(s) parcela(s) informadas no request, pois foram substituídas pelas novas parcelas geradas.
        
        É obrigatório informar os dados básicos da parcela e do processo de pagamento;
        O usuário autenticado precisa ter acesso aos programas de permissão necessários (FIANALISE) para fazer a alteração.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            numeroProcesso (int): The processo
            dataVencimento (datetime): The vencimento
            qtdeParcelas (int): The parcelas
            intervaloParcelas (int): The parcelas
            listaParcelasManutencao (List[Dict[str, Any]]): The parcelas manutencao
            listaValoresNovasParcelas (List[Dict[str, Any]]): The valores novas parcelas
            listaValoresAcrescimoNovasParcelas (List[Dict[str, Any]]): The valores acrescimo novas parcelas
            listaDataVencimentoNovasParcelas (List[Dict[str, Any]]): The data vencimento novas parcelas
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "numeroProcesso": 0,
                "dataVencimento": "2025-04-23T13:46:14.107Z",
                "qtdeParcelas": 0,
                "intervaloParcelas": 0,
                "listaParcelasManutencao": [
                    {
                        "numeroParcela": 0
                    }
                ],
                "listaValoresNovasParcelas": [
                    {
                        "valorParcela": 0
                    }
                ],
                "listaValoresAcrescimoNovasParcelas": [
                    {
                        "valorAcrescimo": 0,
                        "sequenciaParcela": 0
                    }
                ],
                "listaDataVencimentoNovasParcelas": [
                    {
                        "dataVencimento": "2025-04-23T13:46:14.107Z",
                        "sequenciaParcela": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._manutencao_parcelas_processo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/ManutencaoParcelasProcesso"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "numeroProcesso": numero_processo,
            "dataVencimento": data_vencimento,
            "qtdeParcelas": qtde_parcelas,
            "intervaloParcelas": intervalo_parcelas,
            "listaParcelasManutencao": lista_parcelas_manutencao,
            "listaValoresNovasParcelas": lista_valores_novas_parcelas,
            "listaValoresAcrescimoNovasParcelas": lista_valores_acrescimo_novas_parcelas,
            "listaDataVencimentoNovasParcelas": lista_data_vencimento_novas_parcelas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_nota_fiscal_produto_pelo_xml(
        self,
        chaven_fe: Optional[str] = None,
        arquivoxml: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        parcela: Optional[int] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/GerarNotaFiscalProdutoPeloXML`
        HTTP Method: `POST`
        
        Implementation Notes:
        Criação   : Augusto Rabelo Barbosa                 Data: 28/05/2022
          Projeto   : 442112
          Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
          Projeto   : 443200
          Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
        Alteração  : Augusto Rabelo Barbosa      data: 04/01/2023
          Projeto    : 443200
          Manutenção  : Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais
        Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
          Projeto   : 454022
          Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
        Alteração : Juliana Oliveira Souza    Data: 19/06/2023
          Projeto   : 467593
          Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
        Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
          Projeto   : 442322 - SPT 10-2024 - US 359545
          Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].
        
        
        Args:
            ChaveNFe (str): The chave n fe
            ArquivoXML (str): The arquivo x m l
            Empresa (int): The empresa
            Obra (str): The obra
            Processo (int): The processo
            Parcela (int): The parcela
            VincularADescontos (int): The vincular a descontos
        
        Parameter Structure:
        
            {
                "ChaveNFe": "string",
                "ArquivoXML": "string",
                "Empresa": 0,
                "Obra": "string",
                "Processo": 0,
                "Parcela": 0,
                "VincularADescontos": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal_produto_peloxml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/GerarNotaFiscalProdutoPeloXML"
        kwargs = {
            "ChaveNFe": chaven_fe,
            "ArquivoXML": arquivoxml,
            "Empresa": empresa,
            "Obra": obra,
            "Processo": processo,
            "Parcela": parcela,
            "VincularADescontos": vinculara_descontos,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_nota_fiscal_servico_pelo_xml(
        self,
        codigo_fornecedor: Optional[int] = None,
        numero: Optional[str] = None,
        chavenf_se: Optional[str] = None,
        arquivoxml: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        parcela: Optional[int] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/GerarNotaFiscalServicoPeloXML`
        HTTP Method: `POST`
        
        Implementation Notes:
        Criação   : Augusto Rabelo Barbosa                 Data: 03/11/2022
          Projeto   : 442112
        Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
          Projeto   : 443200
          Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
        Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
          Projeto   : 454022
          Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
        Alteração : Juliana Oliveira Souza    Data: 19/06/2023
          Projeto   : 467593
          Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
        Alteração : Rogério Adriano           Data: 31/07/2023
          Projeto   : 475869
          Manutenção: Foi inserido validação após o preenchimento da classe de nota fiscal
                      para verificar se foi preenchido com sucesso, caso contrario irá retornar o erro.
        Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
          Projeto   : 442322 - SPT 10-2024 - US 359545
          Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].
        
        
        Args:
            CodigoFornecedor (int): The codigo fornecedor
            Numero (str): The numero
            ChaveNFSe (str): The chave n f se
            ArquivoXML (str): The arquivo x m l
            Empresa (int): The empresa
            Obra (str): The obra
            Processo (int): The processo
            Parcela (int): The parcela
            VincularADescontos (int): The vincular a descontos
        
        Parameter Structure:
        
            {
                "CodigoFornecedor": 0,
                "Numero": "string",
                "ChaveNFSe": "string",
                "ArquivoXML": "string",
                "Empresa": 0,
                "Obra": "string",
                "Processo": 0,
                "Parcela": 0,
                "VincularADescontos": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal_servico_peloxml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/GerarNotaFiscalServicoPeloXML"
        kwargs = {
            "CodigoFornecedor": codigo_fornecedor,
            "Numero": numero,
            "ChaveNFSe": chavenf_se,
            "ArquivoXML": arquivoxml,
            "Empresa": empresa,
            "Obra": obra,
            "Processo": processo,
            "Parcela": parcela,
            "VincularADescontos": vinculara_descontos,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def integrar_processo_pagamento_uauws(
        self,
        xml_proc: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/IntegrarProcessoPagamentoUAUWS`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Deve seguir arquivo XSD como formato aceito.
        Os campos do tipo data devem obedecer o formato específico (yyyy-MM-dd).
        
        Definição de negócio:
        
        Realiza a importação dos dados de processo de pagamento para o UAU de acordo com o arquivo XML.
        Será validado os dados do XML para realizar a importação, bem como tipagem de dados, dados obrigatórios, entre outros. 
        Virtuau: https://ajuda.globaltec.com.br/virtuau/como-integrar-meus-processos-de-pagamento/
        
        Anexos:
        
        XML: https://ajuda.globaltec.com.br/download/777734/
        XSD: https://ajuda.globaltec.com.br/download/777719/
        Postman: https://ajuda.globaltec.com.br/download/777737/
        
        
        
        Args:
            xml_proc (str): The xml_proc
        
        Parameter Structure:
        
            {
                "xml_proc": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._integrar_processo_pagamentouauws(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/IntegrarProcessoPagamentoUAUWS"
        kwargs = {
            "xml_proc": xml_proc,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_nota_fiscal_transporte_pelo_xml(
        self,
        chavec_te: Optional[str] = None,
        arquivoxml: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        parcela: Optional[int] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ProcessoPagamento/GerarNotaFiscalTransportePeloXML`
        HTTP Method: `POST`
        
        Implementation Notes:
        Criação   : Augusto Rabelo Barbosa                 Data: 03/11/2022
          Projeto   : 442112
        Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
          Projeto   : 443200
          Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
        Alteração: Augusto Rabelo Barbosa      data: 04/01/2023
          Projeto: 443200
          Manutenção: Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais
        Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
          Projeto   : 454022
          Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
        Alteração : Juliana Oliveira Souza    Data: 19/06/2023
          Projeto   : 467593
          Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
        Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
          Projeto   : 442322 - SPT 10-2024 - US 359545
          Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].
        
        
        Args:
            ChaveCTe (str): The chave c te
            ArquivoXML (str): The arquivo x m l
            Empresa (int): The empresa
            Obra (str): The obra
            Processo (int): The processo
            Parcela (int): The parcela
            VincularADescontos (int): The vincular a descontos
        
        Parameter Structure:
        
            {
                "ChaveCTe": "string",
                "ArquivoXML": "string",
                "Empresa": 0,
                "Obra": "string",
                "Processo": 0,
                "Parcela": 0,
                "VincularADescontos": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal_transporte_peloxml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ProcessoPagamento/GerarNotaFiscalTransportePeloXML"
        kwargs = {
            "ChaveCTe": chavec_te,
            "ArquivoXML": arquivoxml,
            "Empresa": empresa,
            "Obra": obra,
            "Processo": processo,
            "Parcela": parcela,
            "VincularADescontos": vinculara_descontos,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

