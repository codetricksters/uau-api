from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Reserva:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gravar_reserva(
        self,
        dados_reserva_json: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Reserva/GravarReserva`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:  
        
        Preencher os parâmetros de request para uso do método.
        As contrabarras são impotantes para não encerrar a string antes do fim.
        As datas devem estar no formato: AAAA-MM-DD.
        SE O VALOR A SER PASSADO É NULL OU VAZIO, NÃO O INFORME NO JSON.
        Troque apenas os ❌ pelos valores desejados.
        o JSON deve ser uma string no seguinte formato:{
            "dados_reserva_json": 
            "[
              {
                \"reserva\": [
                  {
                    \"Empresa_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumProd_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumPer_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Num_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"CodDvg_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Vendedor_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Login_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Data_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Periodo_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Cliente_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Fone_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"TempoIndet_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Status_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumProposta_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"DataConfir_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"UsrConfir_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"UsrCancel_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"DataCancel_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumConf_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"CodPesConfir_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"GeraTaxaReserva_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"ValReserva_rsv\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"ReservaPaga_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Banco_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Conta_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumEs_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"EntSai_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"DataCad_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
                  },
                  {
                    \"Empresa_rsv\": \"❌\",
                    \"NumProd_rsv\": \"❌\",
                    \"NumPer_rsv\": \"❌\",
                    \"Num_rsv\": \"❌\",
                    \"CodDvg_rsv\": \"❌\",
                    \"Vendedor_rsv\": \"❌\",
                    \"Login_rsv\": \"❌\",
                    \"Data_rsv\": \"❌\",
                    \"Periodo_rsv\": \"❌\",
                    \"Cliente_rsv\": \"❌\",
                    \"Fone_rsv\": \"❌\",
                    \"TempoIndet_rsv\": \"❌\",
                    \"Status_rsv\": \"❌\",
                    \"NumProposta_rsv\": \"❌\",
                    \"DataConfir_rsv\": \"❌\",
                    \"UsrConfir_rsv\": \"❌\",
                    \"UsrCancel_rsv\": \"❌\",
                    \"DataCancel_rsv\": \"❌\",
                    \"NumConf_rsv\": \"❌\",
                    \"CodPesConfir_rsv\": \"❌\",
                    \"GeraTaxaReserva_rsv\": \"❌\",
                    \"ValReserva_rsv\": \"❌\",
                    \"ReservaPaga_rsv\": \"❌\",
                    \"Banco_rsv\": \"❌\",
                    \"Conta_rsv\": \"❌\",
                    \"NumEs_rsv\": \"❌\",
                    \"EntSai_rsv\": \"❌\",
                    \"DataCad_rsv\": \"❌\"
                  }
                ]
              },
              {
                \"Taxa\": [
                  {
                    \"Empresa_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Banco_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Conta_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Num_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"EntSai_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Obra_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Data_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Usuario_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Valor_es\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Natureza_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Cap_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"MesPL_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumDoc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"Emissao_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"HistLanc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"CategMovFin_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumAplic_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"StatusAplic_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"NumSeq_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                    \"DataCad_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
                  },
                  {
                    \"Empresa_es\": \"❌\",
                    \"Banco_es\": \"❌\",
                    \"Conta_es\": \"❌\",
                    \"Num_es\": \"❌\",
                    \"EntSai_es\": \"❌\",
                    \"Obra_es\": \"❌\",
                    \"Data_es\": \"❌\",
                    \"Usuario_es\": \"❌\",
                    \"Valor_es\": \"❌\",
                    \"Natureza_es\": \"❌\",
                    \"Cap_es\": \"❌\",
                    \"MesPL_es\": \"❌\",
                    \"NumDoc_es\": \"❌\",
                    \"Emissao_es\": \"❌\",
                    \"HistLanc_es\": \"❌\",
                    \"CategMovFin_es\": \"❌\",
                    \"NumAplic_es\": \"❌\",
                    \"StatusAplic_es\": \"❌\",
                    \"NumSeq_es\": \"❌\",
                    \"DataCad_es\": \"❌\"
                  }
                ]
              }
            ]"
          }
          
        
        
        
        
        
        Args:
            dados_reserva_json (str): The dados_reserva_json
        
        Parameter Structure:
        
            {
                "dados_reserva_json": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Reserva()
            >>> response = api._gravar_reserva(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Reserva/GravarReserva"
        kwargs = {
            "dados_reserva_json": dados_reserva_json,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def excluir_reserva(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_proposta: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        cod_reserva: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Reserva/ExcluirReserva`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Valida usuário e permissões
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_proposta (int): The num_proposta
            cod_produto (int): The cod_produto
            cod_person (int): The cod_person
            cod_reserva (int): The cod_reserva
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_proposta": 0,
                "cod_produto": 0,
                "cod_person": 0,
                "cod_reserva": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Reserva()
            >>> response = api._excluir_reserva(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Reserva/ExcluirReserva"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_proposta": num_proposta,
            "cod_produto": cod_produto,
            "cod_person": cod_person,
            "cod_reserva": cod_reserva,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_reservas(
        self,
        empresa: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Reserva/ConsultarReservas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consulta reservas da personalização que possuem o status informado na request.
        
        
        
        Args:
            empresa (int): The empresa
            cod_produto (int): The cod_produto
            cod_person (int): The cod_person
            status (str): The status
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "cod_produto": 0,
                "cod_person": 0,
                "status": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Reserva()
            >>> response = api._consultar_reservas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Reserva/ConsultarReservas"
        kwargs = {
            "empresa": empresa,
            "cod_produto": cod_produto,
            "cod_person": cod_person,
            "status": status,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_reserva_vendedor(
        self,
        empresa: Optional[int] = None,
        num_prod: Optional[int] = None,
        num_per: Optional[int] = None,
        vendedor: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Reserva/ConsultarReservaVendedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint
        
        Definição de Negócio:
        
        Valida usuário e permissões
        
        
        
        Args:
            empresa (int): The empresa
            num_prod (int): The num_prod
            num_per (int): The num_per
            vendedor (int): The vendedor
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "num_prod": 0,
                "num_per": 0,
                "vendedor": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Reserva()
            >>> response = api._consultar_reserva_vendedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Reserva/ConsultarReservaVendedor"
        kwargs = {
            "empresa": empresa,
            "num_prod": num_prod,
            "num_per": num_per,
            "vendedor": vendedor,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_reserva_por_codigo(
        self,
        empresa: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        cod_reserva: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Reserva/ConsultarReservaPorCodigo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consulta todas as reservas da personalização que tem o código informado.
        Valida usuário e suas permissões.
        
        
        
        Args:
            empresa (int): The empresa
            cod_produto (int): The cod_produto
            cod_person (int): The cod_person
            cod_reserva (int): The cod_reserva
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "cod_produto": 0,
                "cod_person": 0,
                "cod_reserva": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Reserva()
            >>> response = api._consultar_reserva_por_codigo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Reserva/ConsultarReservaPorCodigo"
        kwargs = {
            "empresa": empresa,
            "cod_produto": cod_produto,
            "cod_person": cod_person,
            "cod_reserva": cod_reserva,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consulta_reserva_por_proposta(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_proposta: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Reserva/ConsultaReservaPorProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Valida usuário e permissões
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_proposta (int): The num_proposta
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_proposta": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Reserva()
            >>> response = api._consulta_reserva_por_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Reserva/ConsultaReservaPorProposta"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_proposta": num_proposta,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_dados_controle_reserva(
        self,
        empresa: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Reserva/ConsultarDadosControleReserva`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Valida usuário e permissões.
        
        
        
        Args:
            empresa (int): The empresa
            cod_produto (int): The cod_produto
            cod_person (int): The cod_person
            status (str): The status
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "cod_produto": 0,
                "cod_person": 0,
                "status": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Reserva()
            >>> response = api._consultar_dados_controle_reserva(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Reserva/ConsultarDadosControleReserva"
        kwargs = {
            "empresa": empresa,
            "cod_produto": cod_produto,
            "cod_person": cod_person,
            "status": status,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

