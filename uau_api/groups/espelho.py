from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Espelho:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def alterar_status_unidade(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None,
        novo_status_unidade: Optional[int] = None,
        motivo_alteracao: Optional[str] = None,
        categoria_status_personalizacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/AlterarStatusUnidade`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoProduto (int): The produto
            numeroPersonalizacao (int): The personalizacao
            novoStatusUnidade (int): The status unidade
            motivoAlteracao (str): The alteracao
            categoriaStatusPersonalizacao (int): The status personalizacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoProduto": 0,
                "numeroPersonalizacao": 0,
                "novoStatusUnidade": 0,
                "motivoAlteracao": "string",
                "categoriaStatusPersonalizacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._alterar_status_unidade(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/AlterarStatusUnidade"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoEmpresa": codigo_empresa,
                    "codigoProduto": codigo_produto,
                    "numeroPersonalizacao": numero_personalizacao,
                    "novoStatusUnidade": novo_status_unidade,
                    "motivoAlteracao": motivo_alteracao,
                    "categoriaStatusPersonalizacao": categoria_status_personalizacao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_espelhos_venda(
        self,
        usuario_logado: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/ConsultarEspelhosVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario_logado (str): The usuario_logado
        
        Parameter Structure:
        
            {
                "usuario_logado": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._consultar_espelhos_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/ConsultarEspelhosVenda"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario_logado": usuario_logado,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def retornar_menor_preco_person(
        self,
        tipo_contrato: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_categ_preco: Optional[str] = None,
        numero_person: Optional[int] = None,
        empresa: Optional[int] = None,
        data_categ_preco_produto: Optional[datetime] = None,
        porc_preco_minimo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/RetornarMenorPrecoPerson`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            tipoContrato (int): The contrato
            codProduto (int): The produto
            codCategPreco (str): The categ preco
            numeroPerson (int): The person
            empresa (int): The empresa
            dataCategPrecoProduto (datetime): The categ preco produto
            porcPrecoMinimo (int): The preco minimo
        
        Parameter Structure:
        
            {
                "tipoContrato": 0,
                "codProduto": 0,
                "codCategPreco": "string",
                "numeroPerson": 0,
                "empresa": 0,
                "dataCategPrecoProduto": "2025-04-23T13:46:13.128Z",
                "porcPrecoMinimo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._retornar_menor_preco_person(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/RetornarMenorPrecoPerson"
        try:
            response = self.api.post(
                path,
                json={
                    "tipoContrato": tipo_contrato,
                    "codProduto": cod_produto,
                    "codCategPreco": cod_categ_preco,
                    "numeroPerson": numero_person,
                    "empresa": empresa,
                    "dataCategPrecoProduto": data_categ_preco_produto,
                    "porcPrecoMinimo": porc_preco_minimo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def atualizar_campos_customizados(
        self,
        campos_custom: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/AtualizarCamposCustomizados`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            campos_custom (Dict[str, Any]): The campos_custom
        
        Parameter Structure:
        
            {
                "campos_custom": {
                    "ListChavesUnid": [
                        {
                            "Empresa": 0,
                            "Obra": "string",
                            "Produto": 0,
                            "CodPerson": 0
                        }
                    ],
                    "ListValoresUnid": [
                        {
                            "CampoCustom": "string",
                            "CampoCustomValor": "string"
                        }
                    ]
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._atualizar_campos_customizados(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/AtualizarCamposCustomizados"
        try:
            response = self.api.post(
                path,
                json={
                    "campos_custom": campos_custom,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_unidade_per_por_chave(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/ConsultarUnidadePerPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoProduto (int): The produto
            numeroPersonalizacao (int): The personalizacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoProduto": 0,
                "numeroPersonalizacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._consultar_unidade_per_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/ConsultarUnidadePerPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoEmpresa": codigo_empresa,
                    "codigoProduto": codigo_produto,
                    "numeroPersonalizacao": numero_personalizacao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def busca_unidades_de_acordo_com_where(
        self,
        where: Optional[str] = None,
        retorna_venda: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/BuscaUnidadesDeAcordoComWhere`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            where (str): The where
            retorna_venda (int): The retorna_venda
        
        Parameter Structure:
        
            {
                "where": "string",
                "retorna_venda": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._busca_unidades_de_acordo_com_where(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/BuscaUnidadesDeAcordoComWhere"
        try:
            response = self.api.post(
                path,
                json={
                    "where": where,
                    "retorna_venda": retorna_venda,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def alterar_data_entrega_chaves_unidade(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None,
        data_entrega_chaves: Optional[datetime] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/AlterarDataEntregaChavesUnidade`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoProduto (int): The produto
            numeroPersonalizacao (int): The personalizacao
            dataEntregaChaves (datetime): The entrega chaves
            observacao (str): The observacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoProduto": 0,
                "numeroPersonalizacao": 0,
                "dataEntregaChaves": "2025-04-23T13:46:13.149Z",
                "observacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._alterar_data_entrega_chaves_unidade(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/AlterarDataEntregaChavesUnidade"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoEmpresa": codigo_empresa,
                    "codigoProduto": codigo_produto,
                    "numeroPersonalizacao": numero_personalizacao,
                    "dataEntregaChaves": data_entrega_chaves,
                    "observacao": observacao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_personalizacoes_com_precos(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        num_produto: Optional[int] = None,
        cod_obra: Optional[str] = None,
        num_personalizacao: Optional[int] = None,
        consultarapenasnao_vendidos: Optional[bool] = None,
        tipo_contrato: Optional[int] = None,
        datatabela_preco: Optional[datetime] = None,
        campos_person: Optional[str] = None,
        status_person: Optional[str] = None,
        num_espelho: Optional[int] = None,
        tipocontrato_grafico: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/ConsultarPersonalizacoesComPrecos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            empresa (int): The empresa
            num_produto (int): The num_produto
            cod_obra (str): The cod_obra
            num_personalizacao (int): The num_personalizacao
            consultarapenasnao_vendidos (int): The consultarapenasnao_vendidos
            tipo_contrato (int): The tipo_contrato
            datatabela_preco (datetime): The datatabela_preco
            campos_person (str): The campos_person
            status_person (str): The status_person
            num_espelho (int): The num_espelho
            tipocontrato_grafico (int): The tipocontrato_grafico
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "empresa": 0,
                "num_produto": 0,
                "cod_obra": "string",
                "num_personalizacao": 0,
                "consultarapenasnao_vendidos": true,
                "tipo_contrato": 0,
                "datatabela_preco": "2025-04-23T13:46:13.153Z",
                "campos_person": "string",
                "status_person": "string",
                "num_espelho": 0,
                "tipocontrato_grafico": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._consultar_personalizacoes_com_precos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/ConsultarPersonalizacoesComPrecos"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "empresa": empresa,
                    "num_produto": num_produto,
                    "cod_obra": cod_obra,
                    "num_personalizacao": num_personalizacao,
                    "consultarapenasnao_vendidos": consultarapenasnao_vendidos,
                    "tipo_contrato": tipo_contrato,
                    "datatabela_preco": datatabela_preco,
                    "campos_person": campos_person,
                    "status_person": status_person,
                    "num_espelho": num_espelho,
                    "tipocontrato_grafico": tipocontrato_grafico,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def busca_unidades_de_acordo_com_where_detalhado(
        self,
        where: Optional[str] = None,
        retorna_venda: Optional[bool] = None,
        data_tabela_preco: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/BuscaUnidadesDeAcordoComWhereDetalhado`
        HTTP Method: `POST`
        
        Implementation Notes:
        
        parâmetros de request da classe BuscaUnidadesDeAcordoComWhereDetalhadoRequest
        
        
        
        Args:
            where (str): The where
            retorna_venda (int): The retorna_venda
            data_tabela_preco (datetime): The data_tabela_preco
        
        Parameter Structure:
        
            {
                "where": "string",
                "retorna_venda": true,
                "data_tabela_preco": "2025-04-23T13:46:13.157Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._busca_unidades_de_acordo_com_where_detalhado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/BuscaUnidadesDeAcordoComWhereDetalhado"
        try:
            response = self.api.post(
                path,
                json={
                    "where": where,
                    "retorna_venda": retorna_venda,
                    "data_tabela_preco": data_tabela_preco,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

