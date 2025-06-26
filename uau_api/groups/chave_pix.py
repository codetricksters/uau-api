from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class ChavePix:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def by_cpfcnpj(
        self,
        cpf_cnpj: str,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Consultar/{cpfCnpj}`
        HTTP Method: `GET`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ChavePix()
            >>> response = api.{cpf_cnpj}(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"ChavePix/Pessoas/Consultar/{cpfCnpj}"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.get(
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

    def deletar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Deletar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        A chave pix deve ter no máximo 77 caracteres.
        
        
        
        Args:
            cpfCnpj (str): The cnpj
            chavePix (str): The pix
            tipoChavePix (int): The chave pix
        
        Parameter Structure:
        
            {
                "cpfCnpj": "string",
                "chavePix": "string",
                "tipoChavePix": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ChavePix()
            >>> response = api._deletar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ChavePix/Pessoas/Deletar"
        kwargs = {
            "cpfCnpj": cpf_cnpj,
            "chavePix": chave_pix,
            "tipoChavePix": tipo_chave_pix,
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

    def atualizar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None,
        chave_pix_padrao: Optional[int] = None,
        ativo_inativo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Atualizar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        A chave pix deve ter no máximo 77 caracteres.
        A chave padrão deve ser: 0 - NÃO, 1 - SIM.
        O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.
        
        
        
        Args:
            cpfCnpj (str): The cnpj
            chavePix (str): The pix
            tipoChavePix (int): The chave pix
            chavePixPadrao (int): The pix padrao
            ativoInativo (int): The inativo
        
        Parameter Structure:
        
            {
                "cpfCnpj": "string",
                "chavePix": "string",
                "tipoChavePix": 0,
                "chavePixPadrao": 0,
                "ativoInativo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ChavePix()
            >>> response = api._atualizar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ChavePix/Pessoas/Atualizar"
        kwargs = {
            "cpfCnpj": cpf_cnpj,
            "chavePix": chave_pix,
            "tipoChavePix": tipo_chave_pix,
            "chavePixPadrao": chave_pix_padrao,
            "ativoInativo": ativo_inativo,
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

    def cadastrar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None,
        chave_pix_padrao: Optional[int] = None,
        ativo_inativo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Cadastrar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        A chave pix deve ter no máximo 77 caracteres.
        A chave padrão deve ser: 0 - NÃO, 1 - SIM.
        O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.
        
        
        
        Args:
            cpfCnpj (str): The cnpj
            chavePix (str): The pix
            tipoChavePix (int): The chave pix
            chavePixPadrao (int): The pix padrao
            ativoInativo (int): The inativo
        
        Parameter Structure:
        
            {
                "cpfCnpj": "string",
                "chavePix": "string",
                "tipoChavePix": 0,
                "chavePixPadrao": 0,
                "ativoInativo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ChavePix()
            >>> response = api._cadastrar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ChavePix/Pessoas/Cadastrar"
        kwargs = {
            "cpfCnpj": cpf_cnpj,
            "chavePix": chave_pix,
            "tipoChavePix": tipo_chave_pix,
            "chavePixPadrao": chave_pix_padrao,
            "ativoInativo": ativo_inativo,
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

