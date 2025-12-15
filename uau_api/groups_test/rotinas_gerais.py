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
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        1. Consulta campos personalizados de empresa e produto.
        2. Valida permissão de consulta (2) para o usuário autenticado
        
        Endpoint: `/api/v{version}/RotinasGerais/BuscaCamposPerson`
        HTTP Method: `POST`
        
        Implementation Notes:
        Busca campos personalizados de uma empresa e produto
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "empresa",
                            "produto"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "description": "Código da empresa",
                                "type": "string"
                            },
                            "produto": {
                                "description": "Código do produto",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/BuscaCamposPerson"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def busca_capvenda_empresa(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Irá retornar as configurações de CAPs de uma determinada empresa.
        2. Existem dois estados para o request:
            1. Caso o request seja nulo, irá retornar todas as configurações de CAPs existentes no sistema.
            2. Caso seja determinado um número de empresa, irá retornar as configurações de CAPs dessa empresa.
        
        Endpoint: `/api/v{version}/RotinasGerais/BuscaCAPVendaEmpresa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta e detalha as configurações de CAPs de determinada empresa.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "CodigoEmpresa": {
                                "format": "int32",
                                "description": "Código da Empresa",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/BuscaCAPVendaEmpresa"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def inserir_consulta_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        A Globaltec não se responsabiliza:
        1. Pela compatibilidade entre as alterações do banco de dados e as consultas personalizadas efetuadas pelos clientes.
        2. Pelos dados informados nos geradores de resultado que utilizam consultas personalizadas criadas pelos clientes.
        
        Definição de Negócio:
        
        1. Irá realizar a inserção da consulta geral.
        2. Será necessario permissão de INCLUSÃO no programa GECONSGER.
          
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/como-realizar-o-cadastro-de-consultas-gerais/
        
        Endpoint: `/api/v{version}/RotinasGerais/InserirConsultaGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir consulta geral
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "ClausulaSql": {
                                "description": "Clausula SQL",
                                "type": "string"
                            },
                            "Descricao": {
                                "description": "Descrição da consulta",
                                "type": "string"
                            },
                            "CodigoPasta": {
                                "description": "Código da pasta",
                                "type": "string"
                            },
                            "Status": {
                                "format": "int32",
                                "description": "Status da consulta\r\n[0 - Ativo, 1 - Inativo]",
                                "type": "integer"
                            },
                            "Parametros": {
                                "description": "Lista de parâmetros",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.RotinasGerais.Parametros"
                                }
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/InserirConsultaGeral"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def executar_consulta_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente
        
        Definição de Negócio:
        1. Consulta campos personalizados de empresa e produto.
        2. Valida permissão de consulta (2) para o usuário autenticado 
        3. Os parâmetros de cada consulta geral podem ser consultados através da rota RotinasGerais/ConsultarParamConsultaGeral
        4. Retorna valores dinâmicos da respectiva query armazenada como ConsultaGeral.
        
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
        
        - https://ajuda.globaltec.com.br/virtuau/consultas-gerais/
        
         Anexos:
         
        - Exemplo Postman json request:
        
        <a href="http://www.globaltec.com.br/wp-content/uploads/2019/09/ExecutarConsultaGeral.postman_collection.zip">ExecutarConsultaGeral</a>
        
        Endpoint: `/api/v{version}/RotinasGerais/ExecutarConsultaGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Executa query armazenada
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Personalizado": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Parameters": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/ExecutarConsultaGeral"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_indices_de_reajuste(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Busca a lista de índices de reajuste ativos do sistema
        
        Endpoint: `/api/v{version}/RotinasGerais/BuscarIndicesDeReajuste`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista de índices de reajuste ativos
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/BuscarIndicesDeReajuste"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_tipos_de_vencimento(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Possibilita consultar os tipo de vencimento que estão ativos.
        
        Endpoint: `/api/v{version}/RotinasGerais/BuscarTiposDeVencimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os tipos de vencimento ativos
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/BuscarTiposDeVencimento"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_padroes_cobranca(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. O único campo obrigatório do request é o Status.
        2. Irá retornar os padrões de cobrança de acordo com o(s) filtro(s).
        3. As informações personalizadas da cobrança virão como Configuracao_01 até a Configuracao_08.
        
        Endpoint: `/api/v{version}/RotinasGerais/ConsultarPadroesCobranca`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar os padrões de cobrança disponíveis
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "Status"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "Status": {
                                "format": "int32",
                                "description": "Status do padrão de cobrança\r\n[0 - Ativo, 1 - Inativo, 2 - Ambos]",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
                                "type": "integer"
                            },
                            "Banco": {
                                "format": "int32",
                                "description": "Número do banco",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/ConsultarPadroesCobranca"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_categorias_de_produto(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Consulta a lista de categorias de produtos com status ativos.
        
        Endpoint: `/api/v{version}/RotinasGerais/BuscarCategoriasDeProduto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista de categorias de produto ativos
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/BuscarCategoriasDeProduto"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_finalidades_de_compra(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Este endpoint não necessita de parâmetros no request.
        
        Definição de Negócio:
        1. Consulta a lista de finalidades para compras com status ativo.
        
        Endpoint: `/api/v{version}/RotinasGerais/BuscarFinalidadesDeCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar com finalidades de compra ativas
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/BuscarFinalidadesDeCompra"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_veiculos_de_divulgacao(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         Definição Técnica:
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         
         Definição de Negócio:
         1. Consulta veículos de divulgação que estão ativos.
        
        Endpoint: `/api/v{version}/RotinasGerais/BuscarVeiculosDeDivulgacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar veículos de divulgação ativos
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/BuscarVeiculosDeDivulgacao"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_param_consulta_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente
        3. Retorna uma lista de parâmetros dinâmicos, apresentando o nome do parâmetro e sua descrição, se ele é restrito, multiseleção e OrigemDados
        com pressuposição do uso dessas informações em "ExecutarConsultaGeral
        
        Definição de Negócio:
        
        1. Permite visualizar o padrão de parâmetros da ConsultaGeral informada de forma detalhada
        2. Valida permissão de consulta (2) para o usuário autenticado
        
         VirtUau:
        
        - https://ajuda.globaltec.com.br/virtuau/consultas-gerais/
        
         Exemplo:
         
        - Json request: 
        
        {
        "Id": "1",
        "Personalizado": "0",
        "Parameters":["P01", "1"]
        }
        
        "Personalizado": 1 - True / 0 - False
        
        Endpoint: `/api/v{version}/RotinasGerais/ConsultarParamConsultaGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consutar parâmetros necessários e seus atributos da ConsultaGeral
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Id": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Personalizado": {
                                "format": "int32",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/RotinasGerais/ConsultarParamConsultaGeral"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

