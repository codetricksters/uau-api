from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Planejamento:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def atualizar_item_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        descricao_item: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AtualizarItemPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            DescricaoItem (str): The descricao item
            Usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "DescricaoItem": "string",
                "Usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._atualizar_item_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AtualizarItemPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "DescricaoItem": descricao_item,
            "Usuario": usuario,
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

    def consultar_item_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarItemPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_item_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarItemPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
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

    def consultar_saldo_siplanejada(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes_pl: Optional[str] = None,
        insumo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarSaldoSIPlanejada`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Necessário permissão de consulta no programa OBPLNOBR
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (int): The produto
            Contrato (int): The contrato
            Item (str): The item
            Servico (str): The servico
            MesPl (str): The mes pl
            Insumo (str): The insumo
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": 0,
                "Contrato": 0,
                "Item": "string",
                "Servico": "string",
                "MesPl": "string",
                "Insumo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_saldosi_planejada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarSaldoSIPlanejada"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "MesPl": mes_pl,
            "Insumo": insumo,
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

    def inserir_servico_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        tipo_de_custo: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/InserirServicoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            TipoDeCusto (str): The tipo de custo
            Usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "Servico": "string",
                "TipoDeCusto": "string",
                "Usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._inserir_servico_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/InserirServicoPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "TipoDeCusto": tipo_de_custo,
            "Usuario": usuario,
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

    def exportar_planejamento_produto(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contrato: Optional[int] = None,
        produto: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ExportarPlanejamentoProduto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Contrato (int): The contrato
            Produto (int): The produto
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Contrato": 0,
                "Produto": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._exportar_planejamento_produto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ExportarPlanejamentoProduto"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Contrato": contrato,
            "Produto": produto,
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

    def atualizar_insumos_planejamento(
        self,
        insumos: Optional[List[Dict]] = None,
        justificativa_aprovacao_pl: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AtualizarInsumosPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Necessário permissão de alteração no programa OBPLNOBR
        
        
        
        Args:
            Insumos (List[Dict[str, Any]]): The insumos
            justificativaAprovacaoPl (str): The aprovacao pl
        
        Parameter Structure:
        
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
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._atualizar_insumos_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AtualizarInsumosPlanejamento"
        kwargs = {
            "Insumos": insumos,
            "justificativaAprovacaoPl": justificativa_aprovacao_pl,
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

    def atualizar_servico_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        qtde: Optional[int] = None,
        data_inicio: Optional[str] = None,
        data_termino: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AtualizarServicoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            Qtde (int): The qtde
            DataInicio (str): The data inicio
            DataTermino (str): The data termino
            Usuario (str): The usuario
        
        Parameter Structure:
        
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
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._atualizar_servico_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AtualizarServicoPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "Qtde": qtde,
            "DataInicio": data_inicio,
            "DataTermino": data_termino,
            "Usuario": usuario,
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

    def consultar_servico_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarServicoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "Servico": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarServicoPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
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

    def consultar_solicitacao_insumo_pl(
        self,
        num_solicitacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarSolicitacaoInsumoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            numSolicitacao (int): The solicitacao
        
        Parameter Structure:
        
            {
                "numSolicitacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_solicitacao_insumopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarSolicitacaoInsumoPL"
        kwargs = {
            "numSolicitacao": num_solicitacao,
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

    def inserir_estrutura_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        sequencia: Optional[str] = None,
        codigo_item: Optional[str] = None,
        tipo: Optional[int] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/InserirEstruturaPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            Sequencia (str): The sequencia
            CodigoItem (str): The codigo item
            Tipo (int): The tipo
            Qtde (int): The qtde
            Usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "Servico": "string",
                "Sequencia": "string",
                "CodigoItem": "string",
                "Tipo": 0,
                "Qtde": 0,
                "Usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._inserir_estrutura_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/InserirEstruturaPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "Sequencia": sequencia,
            "CodigoItem": codigo_item,
            "Tipo": tipo,
            "Qtde": qtde,
            "Usuario": usuario,
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

    def consultar_solicitacao_servico_pl(
        self,
        num_solicitacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarSolicitacaoServicoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            numSolicitacao (int): The solicitacao
        
        Parameter Structure:
        
            {
                "numSolicitacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_solicitacao_servicopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarSolicitacaoServicoPL"
        kwargs = {
            "numSolicitacao": num_solicitacao,
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

    def inserir_servico_planejamento_mes(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/InserirServicoPlanejamentoMes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            Mes (str): The mes
            Qtde (int): The qtde
            Usuario (str): The usuario
        
        Parameter Structure:
        
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
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._inserir_servico_planejamento_mes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/InserirServicoPlanejamentoMes"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "Mes": mes,
            "Qtde": qtde,
            "Usuario": usuario,
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

    def aprovar_solicitacao_planejamento(
        self,
        num_solicitacao: Optional[int] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AprovarSolicitacaoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Exemplo do json de request:
         {
         "NumSolicitacao" 622,
           "Usuario": "root",
           "Departamento": "FIN",
           "Cargo": "10"
           }
        
        
        
        
        Args:
            NumSolicitacao (int): The num solicitacao
            Usuario (str): The usuario
            Departamento (str): The departamento
            Cargo (str): The cargo
        
        Parameter Structure:
        
            {
                "NumSolicitacao": 0,
                "Usuario": "string",
                "Departamento": "string",
                "Cargo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AprovarSolicitacaoPlanejamento"
        kwargs = {
            "NumSolicitacao": num_solicitacao,
            "Usuario": usuario,
            "Departamento": departamento,
            "Cargo": cargo,
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

    def atualizar_estrutura_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        sequencia: Optional[str] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AtualizarEstruturaPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            Sequencia (str): The sequencia
            Qtde (int): The qtde
            Usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "Servico": "string",
                "Sequencia": "string",
                "Qtde": 0,
                "Usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._atualizar_estrutura_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AtualizarEstruturaPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "Sequencia": sequencia,
            "Qtde": qtde,
            "Usuario": usuario,
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

    def consultar_estrutura_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        sequencia: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarEstruturaPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            Sequencia (str): The sequencia
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "Servico": "string",
                "Sequencia": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_estrutura_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarEstruturaPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "Sequencia": sequencia,
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

    def atualizar_servico_planejamento_mes(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AtualizarServicoPlanejamentoMes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            Mes (str): The mes
            Qtde (int): The qtde
            Usuario (str): The usuario
        
        Parameter Structure:
        
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
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._atualizar_servico_planejamento_mes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AtualizarServicoPlanejamentoMes"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "Mes": mes,
            "Qtde": qtde,
            "Usuario": usuario,
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

    def consultar_desembolso_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        mes_inicial: Optional[str] = None,
        mes_final: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarDesembolsoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        O mês inicial e final deverão ser informados no formato MM/YYYY. Exemplo: 01/2019, 12/2019.
        
        Definição de Negócio:
          Status:
        
        Projetado: Considera a data de pagamento (DtaRef) para realizar o cálculo dos valores.
        A pagar: Considera a data de prorrogação da parcela (DtaRef) para realizar o cálculo dos valores.
        Pago: Considera a data de pagamento da parcela (DtaRef) para realizar o cálculo dos valores.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            MesInicial (str): The mes inicial
            MesFinal (str): The mes final
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "MesInicial": "string",
                "MesFinal": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_desembolso_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarDesembolsoPlanejamento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "MesInicial": mes_inicial,
            "MesFinal": mes_final,
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

    def consultar_servico_planejamento_mes(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarServicoPlanejamentoMes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            Mes (str): The mes
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "Servico": "string",
                "Mes": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento_mes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarServicoPlanejamentoMes"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "Mes": mes,
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

    def consultar_servico_planejamento_por_obra(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarServicoPlanejamentoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarServicoPlanejamentoPorObra"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
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

    def inserir_servico_planejamento_integrado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        tipo_de_custo: Optional[str] = None,
        codigo_externo: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/InserirServicoPlanejamentoIntegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Produto (str): The produto
            Contrato (str): The contrato
            Item (str): The item
            Servico (str): The servico
            TipoDeCusto (str): The tipo de custo
            CodigoExterno (str): The codigo externo
            Usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Produto": "string",
                "Contrato": "string",
                "Item": "string",
                "Servico": "string",
                "TipoDeCusto": "string",
                "CodigoExterno": "string",
                "Usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._inserir_servico_planejamento_integrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/InserirServicoPlanejamentoIntegrado"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Produto": produto,
            "Contrato": contrato,
            "Item": item,
            "Servico": servico,
            "TipoDeCusto": tipo_de_custo,
            "CodigoExterno": codigo_externo,
            "Usuario": usuario,
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

    def recusar_solicitacao_planejamento_geral(
        self,
        num_solicitacao: Optional[int] = None,
        num_solicitacoes: Optional[List[Dict]] = None,
        ids_itens_solicitacao: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/RecusarSolicitacaoPlanejamentoGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            NumSolicitacao (int): The num solicitacao
            NumSolicitacoes (List[Dict[str, Any]]): The num solicitacoes
            IdsItensSolicitacao (List[Dict[str, Any]]): The ids itens solicitacao
            Usuario (str): The usuario
            Departamento (str): The departamento
            Cargo (str): The cargo
        
        Parameter Structure:
        
            {
                "NumSolicitacao": 0,
                "NumSolicitacoes": [
                    0
                ],
                "IdsItensSolicitacao": [
                    0
                ],
                "Usuario": "string",
                "Departamento": "string",
                "Cargo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._recusar_solicitacao_planejamento_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/RecusarSolicitacaoPlanejamentoGeral"
        kwargs = {
            "NumSolicitacao": num_solicitacao,
            "NumSolicitacoes": num_solicitacoes,
            "IdsItensSolicitacao": ids_itens_solicitacao,
            "Usuario": usuario,
            "Departamento": departamento,
            "Cargo": cargo,
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

    def aprovar_solicitacao_planejamento_em_lote(
        self,
        num_solicitacoes: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AprovarSolicitacaoPlanejamentoEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
         Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Exemplo do json de request:
         {
         "NumSolicitacoes" [
               625, 626
           ],
           "Usuario": "root",
           "Departamento": "FIN",
           "Cargo": "10"
          }
        
        
        
        
        Args:
            NumSolicitacoes (List[Dict[str, Any]]): The num solicitacoes
            Usuario (str): The usuario
            Departamento (str): The departamento
            Cargo (str): The cargo
        
        Parameter Structure:
        
            {
                "NumSolicitacoes": [
                    0
                ],
                "Usuario": "string",
                "Departamento": "string",
                "Cargo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AprovarSolicitacaoPlanejamentoEmLote"
        kwargs = {
            "NumSolicitacoes": num_solicitacoes,
            "Usuario": usuario,
            "Departamento": departamento,
            "Cargo": cargo,
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

    def atualizar_servico_planejamento_integrado(
        self,
        codigo_externo: Optional[str] = None,
        qtde: Optional[int] = None,
        data_inicio: Optional[str] = None,
        data_termino: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AtualizarServicoPlanejamentoIntegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            CodigoExterno (str): The codigo externo
            Qtde (int): The qtde
            DataInicio (str): The data inicio
            DataTermino (str): The data termino
            Usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "CodigoExterno": "string",
                "Qtde": 0,
                "DataInicio": "string",
                "DataTermino": "string",
                "Usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._atualizar_servico_planejamento_integrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AtualizarServicoPlanejamentoIntegrado"
        kwargs = {
            "CodigoExterno": codigo_externo,
            "Qtde": qtde,
            "DataInicio": data_inicio,
            "DataTermino": data_termino,
            "Usuario": usuario,
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

    def consultar_servico_planejado_desintegrado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarServicoPlanejadoDesintegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejado_desintegrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarServicoPlanejadoDesintegrado"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
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

    def consultar_servico_planejamento_integrado(
        self,
        codigo_externo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarServicoPlanejamentoIntegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            CodigoExterno (str): The codigo externo
        
        Parameter Structure:
        
            {
                "CodigoExterno": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento_integrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarServicoPlanejamentoIntegrado"
        kwargs = {
            "CodigoExterno": codigo_externo,
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

    def consultar_aprovacao_pl_pendente_por_usuario(
        self,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        empresas_obras: Optional[str] = None,
        tipo_consulta_aprovacao: Optional[str] = None,
        numero_dias: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarAprovacaoPlPendentePorUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            departamento (str): The departamento
            cargo (str): The cargo
            empresasObras (str): The obras
            tipoConsultaAprovacao (str): The consulta aprovacao
            numero_dias (int): The numero_dias
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "departamento": "string",
                "cargo": "string",
                "empresasObras": "string",
                "tipoConsultaAprovacao": "string",
                "numero_dias": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_aprovacao_pl_pendente_por_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarAprovacaoPlPendentePorUsuario"
        kwargs = {
            "usuario": usuario,
            "departamento": departamento,
            "cargo": cargo,
            "empresasObras": empresas_obras,
            "tipoConsultaAprovacao": tipo_consulta_aprovacao,
            "numero_dias": numero_dias,
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

    def recusar_solicitacao_planejamento_geral_em_lote(
        self,
        num_solicitacao: Optional[int] = None,
        num_solicitacoes: Optional[List[Dict]] = None,
        ids_itens_solicitacao: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/RecusarSolicitacaoPlanejamentoGeralEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            NumSolicitacao (int): The num solicitacao
            NumSolicitacoes (List[Dict[str, Any]]): The num solicitacoes
            IdsItensSolicitacao (List[Dict[str, Any]]): The ids itens solicitacao
            Usuario (str): The usuario
            Departamento (str): The departamento
            Cargo (str): The cargo
        
        Parameter Structure:
        
            {
                "NumSolicitacao": 0,
                "NumSolicitacoes": [
                    0
                ],
                "IdsItensSolicitacao": [
                    0
                ],
                "Usuario": "string",
                "Departamento": "string",
                "Cargo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._recusar_solicitacao_planejamento_geral_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/RecusarSolicitacaoPlanejamentoGeralEmLote"
        kwargs = {
            "NumSolicitacao": num_solicitacao,
            "NumSolicitacoes": num_solicitacoes,
            "IdsItensSolicitacao": ids_itens_solicitacao,
            "Usuario": usuario,
            "Departamento": departamento,
            "Cargo": cargo,
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

    def aprovar_solicitacao_planejamento_insumos_em_lote(
        self,
        ids_itens_solicitacao: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AprovarSolicitacaoPlanejamentoInsumosEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Exemplo do json de request:
        {
         "IdsItensSolicitacao" [
               1615, 1616, 1617            
           ],
           "Usuario": "root",
           "Departamento": "FIN",
           "Cargo": "10"
          }
        
        
        
        
        Args:
            IdsItensSolicitacao (List[Dict[str, Any]]): The ids itens solicitacao
            Usuario (str): The usuario
            Departamento (str): The departamento
            Cargo (str): The cargo
        
        Parameter Structure:
        
            {
                "IdsItensSolicitacao": [
                    0
                ],
                "Usuario": "string",
                "Departamento": "string",
                "Cargo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento_insumos_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AprovarSolicitacaoPlanejamentoInsumosEmLote"
        kwargs = {
            "IdsItensSolicitacao": ids_itens_solicitacao,
            "Usuario": usuario,
            "Departamento": departamento,
            "Cargo": cargo,
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

    def aprovar_solicitacao_planejamento_servicos_em_lote(
        self,
        num_solicitacao: Optional[int] = None,
        chaves_servico: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/AprovarSolicitacaoPlanejamentoServicosEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
         Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Exemplo do json de request:
        {
        "NumSolicitacao": 630,
          "ChavesServico": [
              {
                  "empresa": 1,
                  "obra": "00000",
                  "produto": 7,
                  "contrato": 1,
                  "item": "01.01.01.02",
                  "servico": "020201P",
                  "data": "01/09/2005"
              },
              {
                  "empresa": 1,
                  "obra": "00000",
                  "produto": 7,
                  "contrato": 1,
                  "item": "01.01.01.03",
                  "servico": "030109P",
                  "data": "01/09/2005"
              }
          ],
          "Usuario": "root",
          "Departamento": "FIN",
          "Cargo": "10"
          }
        
        
        
        
        Args:
            NumSolicitacao (int): The num solicitacao
            ChavesServico (List[Dict[str, Any]]): The chaves servico
            Usuario (str): The usuario
            Departamento (str): The departamento
            Cargo (str): The cargo
        
        Parameter Structure:
        
            {
                "NumSolicitacao": 0,
                "ChavesServico": [
                    {
                        "empresa": 0,
                        "obra": "string",
                        "produto": 0,
                        "contrato": 0,
                        "item": "string",
                        "servico": "string",
                        "data": "string"
                    }
                ],
                "Usuario": "string",
                "Departamento": "string",
                "Cargo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento_servicos_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/AprovarSolicitacaoPlanejamentoServicosEmLote"
        kwargs = {
            "NumSolicitacao": num_solicitacao,
            "ChavesServico": chaves_servico,
            "Usuario": usuario,
            "Departamento": departamento,
            "Cargo": cargo,
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

    def consultar_quantidade_aprovacao_pl_pendente_por_usuario(
        self,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        empresas_obras: Optional[str] = None,
        tipo_consulta_aprovacao: Optional[str] = None,
        numero_dias: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Planejamento/ConsultarQuantidadeAprovacaoPlPendentePorUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            departamento (str): The departamento
            cargo (str): The cargo
            empresasObras (str): The obras
            tipoConsultaAprovacao (str): The consulta aprovacao
            numero_dias (int): The numero_dias
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "departamento": "string",
                "cargo": "string",
                "empresasObras": "string",
                "tipoConsultaAprovacao": "string",
                "numero_dias": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Planejamento()
            >>> response = api._consultar_quantidade_aprovacao_pl_pendente_por_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Planejamento/ConsultarQuantidadeAprovacaoPlPendentePorUsuario"
        kwargs = {
            "usuario": usuario,
            "departamento": departamento,
            "cargo": cargo,
            "empresasObras": empresas_obras,
            "tipoConsultaAprovacao": tipo_consulta_aprovacao,
            "numero_dias": numero_dias,
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

