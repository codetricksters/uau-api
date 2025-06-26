from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class Shopping:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def grava_rendimentos(
        self,
        dia: Optional[datetime] = None,
        lojista: Optional[bool] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        valor_lancamento: Optional[int] = None,
        usuario: Optional[str] = None,
        tipo_usuario: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Shopping/GravaRendimentos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            dia (datetime): The dia
            lojista (int): The lojista
            empresa (int): The empresa
            obra (str): The obra
            venda (int): The venda
            valor_lancamento (int): The valor_lancamento
            usuario (str): The usuario
            tipo_usuario (int): The tipo_usuario
        
        Parameter Structure:
        
            {
                "dia": "2025-04-23T13:46:14.501Z",
                "lojista": true,
                "empresa": 0,
                "obra": "string",
                "venda": 0,
                "valor_lancamento": 0,
                "usuario": "string",
                "tipo_usuario": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Shopping()
            >>> response = api._grava_rendimentos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Shopping/GravaRendimentos"
        kwargs = {
            "dia": dia,
            "lojista": lojista,
            "empresa": empresa,
            "obra": obra,
            "venda": venda,
            "valor_lancamento": valor_lancamento,
            "usuario": usuario,
            "tipo_usuario": tipo_usuario,
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

    def importacao_de_parcelas(
        self,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Shopping/ImportacaoDeParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Importação de parcelas a receber/recebida para vendas do tipo Aluguel Shopping:
        URI + /api/v{version}/Shopping/ImportacaoDeParcelas
        
        
        
        Definição de Negócio:
        
        Permite importar parcelas a receber/recebida para vendas do tipo Aluguel Shopping com as seguintes regras:
        
        Para importação de parcelas A RECEBER, os seguintes campos devem ser desconsiderados ou não preenchidos:
          ValorJurosContrato,ValorCorrecao,ValorMulta,ValorCorrecaoAtraso,ValorJurosAtraso,ValorDesconto,ValorAcrescimo,DataRecebimento,
          DataCalculoReajuste,ValorRecebimento,BancoDeposito,ContaDeposito,Depositado,DataDeposito,Conciliado,DataConciliacao,ValorDescontoCondicional
        O campo ParcelaRecebida deve estar com o valor '0', indicando que a parcela não foi recebida.
        
        
        Para importação de parcelas RECEBIDAS, a maioria dos campos devem estar preenchidos, exceto nos casos de Parcela tipo Custa, Parcela Depositada ou Conciliada.
        
        O campo ParcelaRecebida deve estar com o valor '1', indicando que a parcela foi recebida.
        Caso a parcela seja do tipo Custa, os campos TipoDaCusta, ObservacaoCusta, OrigemCusta devem estar preenchidos.
        Caso o campo Depositado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito e DataDeposito devem estar preenchidos.
        Caso o campo Conciliado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito,DataDeposito e DataConciliacao devem estar preenchidos.
        
        
        
        Anexos:
        
        Link para download de exemplos para Postman:
        Exemplo de parcela a receber: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-a-Receber.postman_collection.zip
        Exemplo de parcela recebida: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-Recebida.postman_collection.zip
        
        
        
        Args:
            Parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "Parcelas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "Numero": 0,
                        "NumeroParcela": 0,
                        "TipoParcela": "string",
                        "NumeroParcelaGeral": 0,
                        "DataVencimento": "2025-04-23T13:46:14.507Z",
                        "ParcelaRecebida": 0,
                        "ValorPrincipal": 0,
                        "ValorJurosContrato": 0,
                        "ValorCorrecao": 0,
                        "ValorMulta": 0,
                        "ValorCorrecaoAtraso": 0,
                        "ValorJurosAtraso": 0,
                        "ValorDesconto": 0,
                        "ValorAcrescimo": 0,
                        "DataRecebimento": "2025-04-23T13:46:14.507Z",
                        "TaxaPrimeiroJuros": 0,
                        "FrequenciaVencimento": "string",
                        "IndiceReajuste": "string",
                        "Amortizacao": 0,
                        "BeginEndPrice": 0,
                        "DataInicioReajuste": "2025-04-23T13:46:14.507Z",
                        "DataInicioPrimeiroJuros": "2025-04-23T13:46:14.507Z",
                        "TotalParcelasDoGrupoInformado": 0,
                        "DataPrimeiraParcelaGrupo": "2025-04-23T13:46:14.507Z",
                        "GrupoPlanoIndexador": 0,
                        "CobrarJurosPrimeiroPeriodo": 0,
                        "DataCalculoReajuste": "2025-04-23T13:46:14.507Z",
                        "PadraoCobranca": 0,
                        "ValorRecebimento": 0,
                        "BancoDeposito": 0,
                        "ContaDeposito": "string",
                        "Depositado": 0,
                        "DataDeposito": "2025-04-23T13:46:14.507Z",
                        "Conciliado": 0,
                        "DataConciliacao": "2025-04-23T13:46:14.507Z",
                        "ValorResiduo": 0,
                        "DataInicioSegundoJuros": "2025-04-23T13:46:14.507Z",
                        "TaxaSegundoJuros": 0,
                        "CobrarCorrecaoCusta": 0,
                        "CobrarImpostoCusta": 0,
                        "CobrarJurosAtrasoCusta": 0,
                        "CobrarMultaCusta": 0,
                        "CobrarTaxaAdministracaoCusta": 0,
                        "TipoDaCusta": 0,
                        "ObservacaoCusta": "string",
                        "OrigemCusta": 0,
                        "RepassarValorLocadorCusta": 0,
                        "DiasCarenciaMultaJurosAtraso": 0,
                        "DiasCarenciaCorrecaoAtraso": 0,
                        "CobrarJurosProRata": 0,
                        "TipoSeguro": 0,
                        "CobrarJurosProRataPrimeiroMes": 0,
                        "ValorDescontoCondicional": 0,
                        "DataInicioPeriodoAluguel": "2025-04-23T13:46:14.507Z",
                        "HistoricoPadraoDeposito": "string",
                        "MeioPreferencialDeRecebimento": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Shopping()
            >>> response = api._importacao_de_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Shopping/ImportacaoDeParcelas"
        kwargs = {
            "Parcelas": parcelas,
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

    def consultar_rendimento_lojista(
        self,
        cod_empresa: Optional[int] = None,
        cod_obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        ini_lancamento: Optional[datetime] = None,
        fim_lancamento: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Shopping/ConsultarRendimentoLojista`
        HTTP Method: `POST`
        
        Args:
            cod_empresa (int): The cod_empresa
            cod_obra (str): The cod_obra
            num_venda (int): The num_venda
            ini_lancamento (datetime): The ini_lancamento
            fim_lancamento (datetime): The fim_lancamento
        
        Parameter Structure:
        
            {
                "cod_empresa": 0,
                "cod_obra": "string",
                "num_venda": 0,
                "ini_lancamento": "2025-04-23T13:46:14.515Z",
                "fim_lancamento": "2025-04-23T13:46:14.515Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Shopping()
            >>> response = api._consultar_rendimento_lojista(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Shopping/ConsultarRendimentoLojista"
        kwargs = {
            "cod_empresa": cod_empresa,
            "cod_obra": cod_obra,
            "num_venda": num_venda,
            "ini_lancamento": ini_lancamento,
            "fim_lancamento": fim_lancamento,
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

