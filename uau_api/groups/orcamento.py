from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Orcamento:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def alterar_insumo_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        composicao: Optional[str] = None,
        insumo: Optional[str] = None,
        usuario: Optional[str] = None,
        quantidade: Optional[int] = None,
        preco: Optional[int] = None,
        tipo_insumo: Optional[int] = None,
        encargo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/AlterarInsumoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            orcamento (int): The orcamento
            composicao (str): The composicao
            insumo (str): The insumo
            usuario (str): The usuario
            quantidade (int): The quantidade
            preco (int): The preco
            tipoInsumo (int): The insumo
            encargo (int): The encargo
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "orcamento": 0,
                "composicao": "string",
                "insumo": "string",
                "usuario": "string",
                "quantidade": 0,
                "preco": 0,
                "tipoInsumo": 0,
                "encargo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._alterar_insumo_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/AlterarInsumoOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "orcamento": orcamento,
                    "composicao": composicao,
                    "insumo": insumo,
                    "usuario": usuario,
                    "quantidade": quantidade,
                    "preco": preco,
                    "tipoInsumo": tipo_insumo,
                    "encargo": encargo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def excluir_insumo_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        composicao: Optional[str] = None,
        insumo: Optional[str] = None,
        usuario: Optional[str] = None,
        quantidade: Optional[int] = None,
        preco: Optional[int] = None,
        tipo_insumo: Optional[int] = None,
        encargo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ExcluirInsumoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            orcamento (int): The orcamento
            composicao (str): The composicao
            insumo (str): The insumo
            usuario (str): The usuario
            quantidade (int): The quantidade
            preco (int): The preco
            tipoInsumo (int): The insumo
            encargo (int): The encargo
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "orcamento": 0,
                "composicao": "string",
                "insumo": "string",
                "usuario": "string",
                "quantidade": 0,
                "preco": 0,
                "tipoInsumo": 0,
                "encargo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._excluir_insumo_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ExcluirInsumoOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "orcamento": orcamento,
                    "composicao": composicao,
                    "insumo": insumo,
                    "usuario": usuario,
                    "quantidade": quantidade,
                    "preco": preco,
                    "tipoInsumo": tipo_insumo,
                    "encargo": encargo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def inserir_insumo_orcamento(
        self,
        insumos_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/InserirInsumoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            InsumosOrcamento (List[Dict[str, Any]]): The insumos orcamento
        
        Parameter Structure:
        
            {
                "InsumosOrcamento": [
                    {
                        "empresa": 0,
                        "obra": "string",
                        "orcamento": 0,
                        "composicao": "string",
                        "insumo": "string",
                        "usuario": "string",
                        "quantidade": 0,
                        "preco": 0,
                        "tipoInsumo": 0,
                        "encargo": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._inserir_insumo_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/InserirInsumoOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "InsumosOrcamento": insumos_orcamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def alterar_servico_orcamento(
        self,
        usuario: Optional[str] = None,
        quantidade: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/AlterarServicoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            quantidade (int): The quantidade
            dataInicio (datetime): The inicio
            dataFim (datetime): The fim
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "quantidade": 0,
                "dataInicio": "2025-04-23T13:46:13.523Z",
                "dataFim": "2025-04-23T13:46:13.523Z",
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._alterar_servico_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/AlterarServicoOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "quantidade": quantidade,
                    "dataInicio": data_inicio,
                    "dataFim": data_fim,
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def excluir_servico_orcamento(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ExcluirServicoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._excluir_servico_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ExcluirServicoOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def inserir_servico_orcamento(
        self,
        servicos_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/InserirServicoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            ServicosOrcamento (List[Dict[str, Any]]): The servicos orcamento
        
        Parameter Structure:
        
            {
                "ServicosOrcamento": [
                    {
                        "usuario": "string",
                        "quantidade": 0,
                        "dataInicio": "2025-04-23T13:46:13.532Z",
                        "dataFim": "2025-04-23T13:46:13.532Z",
                        "descricaoServico": "string",
                        "empresa": 0,
                        "obra": "string",
                        "numOrcamento": 0,
                        "item": "string",
                        "servico": "string",
                        "codExternoIntegracao": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._inserir_servico_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/InserirServicoOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "ServicosOrcamento": servicos_orcamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_insumos_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        composicao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ConsultarInsumosPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            orcamento (int): The orcamento
            composicao (str): The composicao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "orcamento": 0,
                "composicao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._consultar_insumos_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ConsultarInsumosPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "orcamento": orcamento,
                    "composicao": composicao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def alterar_planilha_cronograma(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/AlterarPlanilhaCronograma`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            periodo (str): The periodo
            quantidade (int): The quantidade
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "periodo": "string",
                "quantidade": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._alterar_planilha_cronograma(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/AlterarPlanilhaCronograma"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "periodo": periodo,
                    "quantidade": quantidade,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def excluir_planilha_cronograma(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ExcluirPlanilhaCronograma`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            periodo (str): The periodo
            quantidade (int): The quantidade
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "periodo": "string",
                "quantidade": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._excluir_planilha_cronograma(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ExcluirPlanilhaCronograma"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "periodo": periodo,
                    "quantidade": quantidade,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def inserir_planilha_cronograma(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/InserirPlanilhaCronograma`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            periodo (str): The periodo
            quantidade (int): The quantidade
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "periodo": "string",
                "quantidade": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._inserir_planilha_cronograma(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/InserirPlanilhaCronograma"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "periodo": periodo,
                    "quantidade": quantidade,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def exportar_orcamento_estrutura(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ExportarOrcamentoEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            orcamento (int): The orcamento
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "orcamento": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._exportar_orcamento_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ExportarOrcamentoEstrutura"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "orcamento": orcamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_estrutura_orca_por_chave(
        self,
        sequencia: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ConsultarEstruturaOrcaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            sequencia (str): The sequencia
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "sequencia": "string",
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._consultar_estrutura_orca_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ConsultarEstruturaOrcaPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "sequencia": sequencia,
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_estrutura_orca_por_servico(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ConsultarEstruturaOrcaPorServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._consultar_estrutura_orca_por_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ConsultarEstruturaOrcaPorServico"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_servico_orcamento_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ConsultarServicoOrcamentoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._consultar_servico_orcamento_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ConsultarServicoOrcamentoPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_servico_orcado_desintegrado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ConsultarServicoOrcadoDesintegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._consultar_servico_orcado_desintegrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ConsultarServicoOrcadoDesintegrado"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def excluir_estrutura_servico_de_orcamento(
        self,
        estruturas_de_servico_de_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ExcluirEstruturaServicoDeOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite excluir níveis ou itens de estruturas do serviço do orçamento.
        
        Deve preencher os parâmetros de acordo com a estrutura que deseja excluir.
          1.1 Informar se é nível ou item que esta excluindo, a sequencia e os dados do orçamento e serviço.
        Valida se a estrutura poderá ser excluída.
        Valida campos obrigatórios.
        Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem excluídas.
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/776140/
        
        
        
        Args:
            EstruturasDeServicoDeOrcamento (List[Dict[str, Any]]): The estruturas de servico de orcamento
        
        Parameter Structure:
        
            {
                "EstruturasDeServicoDeOrcamento": [
                    {
                        "sequencia": "string",
                        "empresa": 0,
                        "obra": "string",
                        "numOrcamento": 0,
                        "item": "string",
                        "servico": "string",
                        "codExternoIntegracao": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._excluir_estrutura_servico_de_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ExcluirEstruturaServicoDeOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "EstruturasDeServicoDeOrcamento": estruturas_de_servico_de_orcamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def inserir_estrutura_servico_de_orcamento(
        self,
        estruturas_de_servico_de_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/InserirEstruturaServicoDeOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite inserir níveis ou itens de estruturas no serviço existente no orçamento.
        
        Deve preencher os parâmetros de acordo com a estrutura que deseja inserir.
          1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
        Valida se a estrutura poderá ser inserida.
        Valida campos obrigatórios.
        Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/776144/
        
        
        
        Args:
            EstruturasDeServicoDeOrcamento (List[Dict[str, Any]]): The estruturas de servico de orcamento
        
        Parameter Structure:
        
            {
                "EstruturasDeServicoDeOrcamento": [
                    {
                        "tipoEstrutura": 0,
                        "codigo": "string",
                        "qtde": 0,
                        "valor": 0,
                        "usuario": "string",
                        "sequencia": "string",
                        "empresa": 0,
                        "obra": "string",
                        "numOrcamento": 0,
                        "item": "string",
                        "servico": "string",
                        "codExternoIntegracao": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._inserir_estrutura_servico_de_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/InserirEstruturaServicoDeOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "EstruturasDeServicoDeOrcamento": estruturas_de_servico_de_orcamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_planilha_cronograma_por_chave(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ConsultarPlanilhaCronogramaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            item (str): The item
            servico (str): The servico
            periodo (str): The periodo
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "item": "string",
                "servico": "string",
                "periodo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._consultar_planilha_cronograma_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ConsultarPlanilhaCronogramaPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "item": item,
                    "servico": servico,
                    "periodo": periodo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def atualizar_estrutura_servico_de_orcamento(
        self,
        estruturas_de_servico_de_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/AtualizarEstruturaServicoDeOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite alterar níveis ou itens de uma estrutura do serviço existente no orçamento
        
        Deve preencher os parâmetros de acordo com a estrutura que deseja alterar .
          1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
        Valida se a estrutura poderá ser alterada.
        Valida campos obrigatórios.
        Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/776147/
        
        
        
        Args:
            EstruturasDeServicoDeOrcamento (List[Dict[str, Any]]): The estruturas de servico de orcamento
        
        Parameter Structure:
        
            {
                "EstruturasDeServicoDeOrcamento": [
                    {
                        "tipoEstrutura": 0,
                        "codigo": "string",
                        "qtde": 0,
                        "valor": 0,
                        "usuario": "string",
                        "sequencia": "string",
                        "empresa": 0,
                        "obra": "string",
                        "numOrcamento": 0,
                        "item": "string",
                        "servico": "string",
                        "codExternoIntegracao": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._atualizar_estrutura_servico_de_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/AtualizarEstruturaServicoDeOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "EstruturasDeServicoDeOrcamento": estruturas_de_servico_de_orcamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_servico_orcamento_por_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        tipo_item: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Orcamento/ConsultarServicoOrcamentoPorOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            numOrcamento (int): The orcamento
            tipoItem (int): The item
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "numOrcamento": 0,
                "tipoItem": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Orcamento()
            >>> response = api._consultar_servico_orcamento_por_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Orcamento/ConsultarServicoOrcamentoPorOrcamento"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "numOrcamento": num_orcamento,
                    "tipoItem": tipo_item,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

