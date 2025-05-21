from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class NotasFiscais:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_nfentrada(
        self,
        listanf_entrada: Optional[List[Dict]] = None,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        cnpj_fornecedor: Optional[str] = None,
        codigo_fornecedor: Optional[str] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
        tipo_periodo: Optional[Any] = None
    ) -> dict:
        """
        
        Endpoint: `NotasFiscais/ConsultarNFEntrada`
        HTTP Method: `POST`
        
        Implementation Notes:
         Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Ao menos uma chave de pesquisa deve ser preenchida sendo elas ([CodigoEmpresa],
          [CnpjFornecedor], [CodigoFornecedor], [DataInicial], [ListaNFEntrada]).
        Caso tenha informado a propriedade da Obra, a Empresa torna-se obrigatória.
        Preenchimento da [DataInicial] torna [DataFinal] obrigatória.
        Preenchimento da [DataFinal] torna [DataInicial] obrigatória.
        Obra só vai achar informação se a nota estiver vinculada a um processo.
        [ListaNFEntrada] Cada objeto deve ter obrigatoriamente o [CodigoEmpresa] e o [NumeroNotaFiscal ou NumeroNotaFiscalEletronica]
          6.1 NumeroNotaFiscal = Número de controle da nota fiscal (Obs: no retorno dos dados esse valor fica no campo Numero)
          6.2 NumeroNotaFiscalEletronica = Número da nota fiscal eletrônica, informado na DANFE ou NFS-e (Obs: no retorno dos dados esse valor fica no campo NumeroNotaFiscal)
        
        
        
        Args:
            ListaNFEntrada (List[Dict[str, Any]]): The lista n f entrada
            CodigoEmpresa (int): The codigo empresa
            CodigoObra (str): The codigo obra
            CnpjFornecedor (str): The cnpj fornecedor
            CodigoFornecedor (str): The codigo fornecedor
            DataInicial (datetime): The data inicial
            DataFinal (datetime): The data final
            TipoPeriodo (int): The tipo periodo
        
        Parameter Structure:
        
            {
                "ListaNFEntrada": [
                    {
                        "CodigoEmpresa": 0,
                        "NumeroNotaFiscal": 0,
                        "NumeroNotaFiscalEletronica": "string"
                    }
                ],
                "CodigoEmpresa": 0,
                "CodigoObra": "string",
                "CnpjFornecedor": "string",
                "CodigoFornecedor": "string",
                "DataInicial": "2025-04-23T13:46:13.469Z",
                "DataFinal": "2025-04-23T13:46:13.469Z",
                "TipoPeriodo": 1
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = NotasFiscais()
            >>> response = api._consultarnf_entrada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "NotasFiscais/ConsultarNFEntrada"
        try:
            response = self.api.post(
                path,
                json={
                    "ListaNFEntrada": listanf_entrada,
                    "CodigoEmpresa": codigo_empresa,
                    "CodigoObra": codigo_obra,
                    "CnpjFornecedor": cnpj_fornecedor,
                    "CodigoFornecedor": codigo_fornecedor,
                    "DataInicial": data_inicial,
                    "DataFinal": data_final,
                    "TipoPeriodo": tipo_periodo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def salvar_arquivo_xmlnotafiscal_entrada(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `NotasFiscais/SalvarArquivoXMLnotafiscalEntrada`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Poderá ser enviado uma lista de arquivos XML.
        Será permitido no máximo uma lista com 20 arquivos.
        Tipo do arquivo XML [TipoXML]
           0 para NF-e
           1 para CT-e
           2 para NFS-e,
        Arquivo XML da nota fiscal (Texto do arquivo) [ArquivoXML].
        
        
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "TipoXML": 0,
                    "ArquivoXML": "string"
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = NotasFiscais()
            >>> response = api._salvar_arquivoxm_lnotafiscal_entrada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "NotasFiscais/SalvarArquivoXMLnotafiscalEntrada"
        try:
            response = self.api.post(
                path,
                json=parameters if parameters is not None else {}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

