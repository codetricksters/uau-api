from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class RotinasGerais:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def busca_campos_person(
        self,
        empresa: Optional[str] = None,
        produto: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/BuscaCamposPerson`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta campos personalizados de empresa e produto.
        Valida permissão de consulta (2) para o usuário autenticado
        
        
        
        Args:
            empresa (str): The empresa
            produto (str): The produto
        
        Parameter Structure:
        
            {
                "empresa": "string",
                "produto": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RotinasGerais()
            >>> response = api._busca_campos_person(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/BuscaCamposPerson"
        kwargs = {
            "empresa": empresa,
            "produto": produto,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def busca_capvenda_empresa(
        self,
        codigo_empresa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/BuscaCAPVendaEmpresa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Irá retornar as configurações de CAPs de uma determinada empresa.
        Existem dois estados para o request:
        Caso o request seja nulo, irá retornar todas as configurações de CAPs existentes no sistema.
        Caso seja determinado um número de empresa, irá retornar as configurações de CAPs dessa empresa.
        
        
        
        
        
        Args:
            CodigoEmpresa (int): The codigo empresa
        
        Parameter Structure:
        
            {
                "CodigoEmpresa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RotinasGerais()
            >>> response = api._buscacap_venda_empresa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/BuscaCAPVendaEmpresa"
        kwargs = {
            "CodigoEmpresa": codigo_empresa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def inserir_consulta_geral(
        self,
        clausula_sql: Optional[str] = None,
        descricao: Optional[str] = None,
        codigo_pasta: Optional[str] = None,
        status: Optional[int] = None,
        parametros: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/InserirConsultaGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        A Globaltec não se responsabiliza:
        
        Pela compatibilidade entre as alterações do banco de dados e as consultas personalizadas efetuadas pelos clientes.
        Pelos dados informados nos geradores de resultado que utilizam consultas personalizadas criadas pelos clientes.
        
        Definição de Negócio:
        
        Irá realizar a inserção da consulta geral.
        Será necessario permissão de INCLUSÃO no programa GECONSGER.
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/como-realizar-o-cadastro-de-consultas-gerais/
        
        
        
        Args:
            ClausulaSql (str): The clausula sql
            Descricao (str): The descricao
            CodigoPasta (str): The codigo pasta
            Status (int): The status
            Parametros (List[Dict[str, Any]]): The parametros
        
        Parameter Structure:
        
            {
                "ClausulaSql": "string",
                "Descricao": "string",
                "CodigoPasta": "string",
                "Status": 0,
                "Parametros": [
                    {
                        "Parametro": "string",
                        "Descricao": "string",
                        "Tipo": 0,
                        "Origem": 0,
                        "Restrito": 0,
                        "MultiSelecao": 0,
                        "Valor": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RotinasGerais()
            >>> response = api._inserir_consulta_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/InserirConsultaGeral"
        kwargs = {
            "ClausulaSql": clausula_sql,
            "Descricao": descricao,
            "CodigoPasta": codigo_pasta,
            "Status": status,
            "Parametros": parametros,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def executar_consulta_geral(
        self,
        id: Optional[int] = None,
        personalizado: Optional[int] = None,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/ExecutarConsultaGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente
        
        Definição de Negócio:
        
        Consulta campos personalizados de empresa e produto.
        Valida permissão de consulta (2) para o usuário autenticado 
        Os parâmetros de cada consulta geral podem ser consultados através da rota RotinasGerais/ConsultarParamConsultaGeral
        Retorna valores dinâmicos da respectiva query armazenada como ConsultaGeral.
        
        Deve ser enviado o ID da ConsultaGeral e seus respectivos parâmetros, sendo o preenchimento da propriedade Parameters,
          um array de string, e se necessário notações sql que atribuem características de tipagem. Por exemplo, apóstrofo entre uma string, considerando que 
          em situações que usam um inteiro, podem funcionar com apóstrofo ou sem, mas em cláusulas como IN(params), 
          o uso de apóstrofo pode gerar um erro, e ainda para atribuir uma lista de inteiros nesta, deve ser usado a vírgula.
          Seguindo esta padrão comum,   "Parameters":["Nome do parâmetro", "Valor do parâmetro", "Nome do segundo parâmetro", "valor do segundo parâmetro"]
        Apóstrofo = '
        Datas devem ser acompanhadas de Apóstrofo, exceto em ocasiões especiais que devem ser analisadas na query, sendo
          um destes, o uso da cláusula IN
        Exemplo formato json da body
        {
          "Id": "1",
          "Personalizado": "0",
          "Parameters":["P01", "1"]
          }
        {
           "Id": "2",
           "Personalizado": "0",
           "Parameters":["EmpresaObra", " '1|1' ", "Status", "1"]
          }
        "Personalizado": 1 - True / 0 - False
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/consultas-gerais/
        Anexos:
        
        Exemplo Postman json request:
        
        
        ExecutarConsultaGeral
        
        
        Args:
            Id (int): The id
            Personalizado (int): The personalizado
            Parameters (List[Dict[str, Any]]): The parameters
        
        Parameter Structure:
        
            {
                "Id": 0,
                "Personalizado": 0,
                "Parameters": [
                    "string"
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RotinasGerais()
            >>> response = api._executar_consulta_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/ExecutarConsultaGeral"
        kwargs = {
            "Id": id,
            "Personalizado": personalizado,
            "Parameters": parameters,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_indices_de_reajuste(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/BuscarIndicesDeReajuste`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Busca a lista de índices de reajuste ativos do sistema
        
        
        
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
            >>> api = RotinasGerais()
            >>> response = api._buscar_indices_de_reajuste(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/BuscarIndicesDeReajuste"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_tipos_de_vencimento(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/BuscarTiposDeVencimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Possibilita consultar os tipo de vencimento que estão ativos.
        
        
        
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
            >>> api = RotinasGerais()
            >>> response = api._buscar_tipos_de_vencimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/BuscarTiposDeVencimento"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_padroes_cobranca(
        self,
        empresa: Optional[int] = None,
        status: Optional[int] = None,
        banco: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/ConsultarPadroesCobranca`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        O único campo obrigatório do request é o Status.
        Irá retornar os padrões de cobrança de acordo com o(s) filtro(s).
        As informações personalizadas da cobrança virão como Configuracao_01 até a Configuracao_08.
        
        
        
        Args:
            Empresa (int): The empresa
            Status (int): The status
            Banco (int): The banco
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Status": 0,
                "Banco": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RotinasGerais()
            >>> response = api._consultar_padroes_cobranca(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/ConsultarPadroesCobranca"
        kwargs = {
            "Empresa": empresa,
            "Status": status,
            "Banco": banco,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_categorias_de_produto(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/BuscarCategoriasDeProduto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta a lista de categorias de produtos com status ativos.
        
        
        
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
            >>> api = RotinasGerais()
            >>> response = api._buscar_categorias_de_produto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/BuscarCategoriasDeProduto"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_finalidades_de_compra(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/BuscarFinalidadesDeCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Este endpoint não necessita de parâmetros no request.
        
        Definição de Negócio:
        
        Consulta a lista de finalidades para compras com status ativo.
        
        
        
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
            >>> api = RotinasGerais()
            >>> response = api._buscar_finalidades_de_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/BuscarFinalidadesDeCompra"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_veiculos_de_divulgacao(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/BuscarVeiculosDeDivulgacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Lista de Veículos de divulgação.
           Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Definição de Negócio:
        
        Consulta veículos de divulgação que estão ativos.
        
        
        
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
            >>> api = RotinasGerais()
            >>> response = api._buscar_veiculos_de_divulgacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/BuscarVeiculosDeDivulgacao"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_param_consulta_geral(
        self,
        id: Optional[int] = None,
        personalizado: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `RotinasGerais/ConsultarParamConsultaGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente
        Retorna uma lista de parâmetros dinâmicos, apresentando o nome do parâmetro e sua descrição, se ele é restrito, multiseleção e OrigemDados
          com pressuposição do uso dessas informações em "ExecutarConsultaGeral
        
        Definição de Negócio:
        
        Permite visualizar o padrão de parâmetros da ConsultaGeral informada de forma detalhada
        Valida permissão de consulta (2) para o usuário autenticado
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/consultas-gerais/
        Exemplo:
        
        Json request: 
        
        
        {
          "Id": "1",
          "Personalizado": "0",
          "Parameters":["P01", "1"]
          }
        "Personalizado": 1 - True / 0 - False
        
        
        Args:
            Id (int): The id
            Personalizado (int): The personalizado
        
        Parameter Structure:
        
            {
                "Id": 0,
                "Personalizado": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RotinasGerais()
            >>> response = api._consultar_param_consulta_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RotinasGerais/ConsultarParamConsultaGeral"
        kwargs = {
            "Id": id,
            "Personalizado": personalizado,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

