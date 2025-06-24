from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class RelatorioIRPF:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pdfrel_irpf(
        self,
        vendasobras_empresa: Optional[List[Dict]] = None,
        ano_base: Optional[int] = None,
        naomostradados_venda: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `RelatorioIRPF/GerarPDFRelIRPF`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
        
        A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
        Substituir cada parâmetro pelo valor correspondente:
        
        "Venda" - Número da Venda.
        "Obra" - Código da Obra.
        "Empresa" - Número da Empresa.
        "ano_base" - ano base para geração do IRPF.
        "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
          {
                "vendasobras_empresa" [
                    [
                    "Venda", 
                    "Obra", 
                    "Empresa"
                    ]
                ],
                    "ano_base": 2018,
                    "naomostradados_venda": true
            }
          
        
        
        Segue exemplo  após substituição dos parâmetros:
              {
                     "vendasobras_empresa" [
                       [
                       "838",
                       "424V",
                       "308"
                       ]
                   ],
                     "ano_base": 2021,
                     "naomostradados_venda": false
                }
          
        
        
        
        
        
        Args:
            vendasobras_empresa (List[Dict[str, Any]]): The vendasobras_empresa
            ano_base (int): The ano_base
            naomostradados_venda (int): The naomostradados_venda
        
        Parameter Structure:
        
            {
                "vendasobras_empresa": [
                    {}
                ],
                "ano_base": 0,
                "naomostradados_venda": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RelatorioIRPF()
            >>> response = api._gerarpdf_relirpf(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RelatorioIRPF/GerarPDFRelIRPF"
        try:
            response = self.api.post(
                path,
                json={
                    "vendasobras_empresa": vendasobras_empresa,
                    "ano_base": ano_base,
                    "naomostradados_venda": naomostradados_venda,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gerar_pdfrel_irpfv2(
        self,
        vendasobras_empresa: Optional[List[Dict]] = None,
        ano_base: Optional[int] = None,
        naomostradados_venda: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `RelatorioIRPF/GerarPDFRelIRPFV2`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
        
        A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
        Substituir cada parâmetro pelo valor correspondente:
        
        "Venda" - Número da Venda.
        "Obra" - Código da Obra.
        "Empresa" - Número da Empresa.
        "ano_base" - ano base para geração do IRPF.
        "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
          {
                "vendasobras_empresa" [
                    [
                    "Venda", 
                    "Obra", 
                    "Empresa"
                    ]
                ],
                    "ano_base": 2018,
                    "naomostradados_venda": true
            }
          
        
        
        Segue exemplo  após substituição dos parâmetros:
              {
                     "vendasobras_empresa" [
                       [
                       "838",
                       "424V",
                       "308"
                       ]
                   ],
                     "ano_base": 2021,
                     "naomostradados_venda": false
                }
          
        
        
        
        
        
        Args:
            vendasobras_empresa (List[Dict[str, Any]]): The vendasobras_empresa
            ano_base (int): The ano_base
            naomostradados_venda (int): The naomostradados_venda
        
        Parameter Structure:
        
            {
                "vendasobras_empresa": [
                    {}
                ],
                "ano_base": 0,
                "naomostradados_venda": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RelatorioIRPF()
            >>> response = api._gerarpdf_relirpfv2(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RelatorioIRPF/GerarPDFRelIRPFV2"
        try:
            response = self.api.post(
                path,
                json={
                    "vendasobras_empresa": vendasobras_empresa,
                    "ano_base": ano_base,
                    "naomostradados_venda": naomostradados_venda,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

