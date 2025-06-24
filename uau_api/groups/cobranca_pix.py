from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class CobrancaPix:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def pix_por_parcelas(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/PixPorParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API é permitir a consulta e retorno das informações dos PIX gerados para uma determinada parcela ou lista de parcelas
        Serão retornados os dados do PIX, caso tenha sido gerado para a(s) parcela(s) requisitada(s)
        Limite máximo de 50 parcelas por requisição
        
        
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "Empresa": 0,
                    "Obra": "string",
                    "NumeroVenda": 0,
                    "NumeroParcela": 0,
                    "TipoParcela": "string",
                    "NumeroParcelaGeral": 0
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._pix_por_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/PixPorParcelas"
        try:
            response = self.api.post(
                path,
                json=parameters if parameters is not None else {}
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def reimpressao_pix(
        self,
        tx_id: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/ReimpressaoPix`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API é permitir a consulta e retorno das informações do pix de modo que o usuário possa fazer a impressão 
          dos dados de cobrança.
        Será retornado o PDF completo e o QRCode em base64.
        Será retornado o texto do Pix Copia e Cola.
        
        Instituições bancárias suportadas: 
        
        341 = Banco Itaú
        
        756 = Banco Sicoob
        
        237 = Banco Bradesco
        
        246 = Banco Abc
        
        
        
        
        Args:
            TxId (str): The tx id
        
        Parameter Structure:
        
            {
                "TxId": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._reimpressao_pix(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/ReimpressaoPix"
        try:
            response = self.api.post(
                path,
                json={
                    "TxId": tx_id,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_pix_status(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/ConsultarPixStatus`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API e permitir a consulta do status do PIX 
        
        Instituições bancárias suportadas: 
        
        341 = Banco Itaú
        246 = Banco Abc
        341 = Banco Itaú
        756 = Banco Sicoob
        237 = Banco Bradesco
        
        Pré requisito:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Pix/GerarCobrancaPIX 
          Anexos:
        
        
        Exemplo Postman: [ALTERAR EXEMPLO]
        
        
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "TxId": "string"
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._consultar_pix_status(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/ConsultarPixStatus"
        try:
            response = self.api.post(
                path,
                json=parameters if parameters is not None else {}
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gerar_cobranca_venda(
        self,
        data_de_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        usar_padrao_pix_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        padrao_cobranca: Optional[int] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/GerarCobrancaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        O objetivo desta rota de API é permitir o registro de cobrança por PIX junto à instituição financeira.
        O BASE64 gerado é somente o QR Code do PIX.
        Instituições bancárias suportadas:
        
        341 Banco Itaú
        756 Banco Sicoob
        237 Banco Bradesco
        246 Banco ABC
        
        
        
        Pré Requisitos:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Venda/GerarCobrancaPIX
        
        
        
        
        Args:
            DataDeCalculo (datetime): The data de calculo
            Antecipar (int): The antecipar
            UsarPadraoPixAvulso (int): The usar padrao pix avulso
            AgruparParcelas (int): The agrupar parcelas
            PadraoCobranca (int): The padrao cobranca
            Parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "DataDeCalculo": "2025-04-23T13:46:12.715Z",
                "Antecipar": true,
                "UsarPadraoPixAvulso": true,
                "AgruparParcelas": true,
                "PadraoCobranca": 0,
                "Parcelas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumeroVenda": 0,
                        "NumeroParcela": 0,
                        "TipoParcela": "string",
                        "NumeroParcelaGeral": 0,
                        "ValorDesconto": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._gerar_cobranca_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/GerarCobrancaVenda"
        try:
            response = self.api.post(
                path,
                json={
                    "DataDeCalculo": data_de_calculo,
                    "Antecipar": antecipar,
                    "UsarPadraoPixAvulso": usar_padrao_pix_avulso,
                    "AgruparParcelas": agrupar_parcelas,
                    "PadraoCobranca": padrao_cobranca,
                    "Parcelas": parcelas,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gerar_cobranca_proposta(
        self,
        data_de_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        usar_padrao_pix_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        padrao_cobranca: Optional[int] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/GerarCobrancaProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API é permitir o registro de cobrança por PIX junto a instituição financeira 
        O BASE64 gerado é somente o QRCODE do PIX
        
        Instituições bancárias suportadas: 
        
        341 = Banco Itaú
        756 = Banco Sicoob
        237 = Banco Bradesco
        246 = Banco Abc
        
        Pré requisito:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Venda/GerarCobrancaPIX
        
        
        
        
        
        Args:
            DataDeCalculo (datetime): The data de calculo
            Antecipar (int): The antecipar
            UsarPadraoPixAvulso (int): The usar padrao pix avulso
            AgruparParcelas (int): The agrupar parcelas
            PadraoCobranca (int): The padrao cobranca
            Parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "DataDeCalculo": "2025-04-23T13:46:12.721Z",
                "Antecipar": true,
                "UsarPadraoPixAvulso": true,
                "AgruparParcelas": true,
                "PadraoCobranca": 0,
                "Parcelas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumeroProposta": 0,
                        "NumeroParcela": 0,
                        "TipoParcela": "string",
                        "NumeroParcelaGeral": 0,
                        "ValorDesconto": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._gerar_cobranca_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/GerarCobrancaProposta"
        try:
            response = self.api.post(
                path,
                json={
                    "DataDeCalculo": data_de_calculo,
                    "Antecipar": antecipar,
                    "UsarPadraoPixAvulso": usar_padrao_pix_avulso,
                    "AgruparParcelas": agrupar_parcelas,
                    "PadraoCobranca": padrao_cobranca,
                    "Parcelas": parcelas,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

