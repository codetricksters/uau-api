from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Espelho:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def alterar_status_unidade(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/AlterarStatusUnidade`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar unidade personalizada do produto
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do produto personalizado",
                                "type": "integer"
                            },
                            "codigoProduto": {
                                "format": "int32",
                                "description": "Codigo do produto personalizado",
                                "type": "integer"
                            },
                            "numeroPersonalizacao": {
                                "format": "int32",
                                "description": "Numero da personalização do produto",
                                "type": "integer"
                            },
                            "novoStatusUnidade": {
                                "format": "int32",
                                "description": "Novo status que será alterada a unidade de personalização\r\nApenas 0 - Disponível \r\n       7 - Suspenso\r\n       8  - Fora de venda\r\n       10 - Dação.",
                                "type": "integer"
                            },
                            "motivoAlteracao": {
                                "description": "Motivo da alteração do status da unidade de personalização",
                                "type": "string"
                            },
                            "categoriaStatusPersonalizacao": {
                                "format": "int32",
                                "description": "Categoria do status da unidade de personalização.",
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
            >>> api = Espelho()
            >>> response = api._alterar_status_unidade(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/AlterarStatusUnidade"
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

    def consultar_espelhos_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/ConsultarEspelhosVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta espelhos de venda as empresas que o usuário tem permissão.
        
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
                            "usuario_logado": {
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
            >>> api = Espelho()
            >>> response = api._consultar_espelhos_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/ConsultarEspelhosVenda"
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

    def retornar_menor_preco_person(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/RetornarMenorPrecoPerson`
        HTTP Method: `POST`
        
        Implementation Notes:
        Busca o valor do menor preço que pode ser inserido em um produto.
        
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
                            "tipoContrato": {
                                "format": "int32",
                                "description": "tipo de contrato  0 - Venda, 1 - Aluguel, 2 - PropostaVenda, 3 - MedicaoContratoVenda, 4 - Revenda, 5 - Todos",
                                "enum": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4,
                                    5
                                ],
                                "type": "integer"
                            },
                            "codProduto": {
                                "format": "int32",
                                "description": "código do produto",
                                "type": "integer"
                            },
                            "codCategPreco": {
                                "description": "código da categoria de preço",
                                "type": "string"
                            },
                            "numeroPerson": {
                                "format": "int32",
                                "description": "número da personalização",
                                "type": "integer"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "código da empresa",
                                "type": "integer"
                            },
                            "dataCategPrecoProduto": {
                                "format": "date-time",
                                "description": "data de cadastro da categoria de preço do produto",
                                "type": "string"
                            },
                            "porcPrecoMinimo": {
                                "format": "double",
                                "description": "Porcentagem do preço mínimo",
                                "type": "number"
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
            >>> api = Espelho()
            >>> response = api._retornar_menor_preco_person(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/RetornarMenorPrecoPerson"
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

    def atualizar_campos_customizados(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/AtualizarCamposCustomizados`
        HTTP Method: `POST`
        
        Implementation Notes:
        Rotina responsável por atualizar campos customizados
        
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
                            "campos_custom": {
                                "$ref": "#/definitions/UAUApi.Models.Espelho.CamposCustom",
                                "description": "Objeto que contém as informações necessárias para atualizar os campos customizados"
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
            >>> api = Espelho()
            >>> response = api._atualizar_campos_customizados(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/AtualizarCamposCustomizados"
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

    def consultar_unidade_per_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/ConsultarUnidadePerPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar unidade personalizada do produto
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do produto personalizado",
                                "type": "integer"
                            },
                            "codigoProduto": {
                                "format": "int32",
                                "description": "Codigo do produto personalizado",
                                "type": "integer"
                            },
                            "numeroPersonalizacao": {
                                "format": "int32",
                                "description": "Numero da personalização do produto",
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
            >>> api = Espelho()
            >>> response = api._consultar_unidade_per_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/ConsultarUnidadePerPorChave"
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

    def busca_unidades_de_acordo_com_where(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/BuscaUnidadesDeAcordoComWhere`
        HTTP Method: `POST`
        
        Implementation Notes:
        Rotina responsável por buscar os dados das unidades de acordo com o WHERE passado por parâmetro.
        
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
                            "where": {
                                "type": "string"
                            },
                            "retorna_venda": {
                                "type": "boolean"
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
            >>> api = Espelho()
            >>> response = api._busca_unidades_de_acordo_com_where(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/BuscaUnidadesDeAcordoComWhere"
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

    def alterar_data_entrega_chaves_unidade(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/AlterarDataEntregaChavesUnidade`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar a data de entrega das chaves da unidade
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do produto personalizado",
                                "type": "integer"
                            },
                            "codigoProduto": {
                                "format": "int32",
                                "description": "Codigo do produto personalizado",
                                "type": "integer"
                            },
                            "numeroPersonalizacao": {
                                "format": "int32",
                                "description": "Numero da personalização do produto",
                                "type": "integer"
                            },
                            "dataEntregaChaves": {
                                "format": "date-time",
                                "description": "Data de entrega das chaves",
                                "type": "string"
                            },
                            "observacao": {
                                "description": "Observação para a alteração da data de entrega das chaves",
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
            >>> api = Espelho()
            >>> response = api._alterar_data_entrega_chaves_unidade(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/AlterarDataEntregaChavesUnidade"
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

    def consultar_personalizacoes_com_precos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Espelho/ConsultarPersonalizacoesComPrecos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta uma personalização com preços.
        
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
                            "usuario": {
                                "description": "Usuário",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "num_produto": {
                                "format": "int32",
                                "description": "Número do produto",
                                "type": "integer"
                            },
                            "cod_obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "num_personalizacao": {
                                "format": "int32",
                                "description": "Número da personalização",
                                "type": "integer"
                            },
                            "consultarapenasnao_vendidos": {
                                "type": "boolean"
                            },
                            "tipo_contrato": {
                                "format": "int32",
                                "description": "Tipo de contrato",
                                "enum": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4,
                                    5
                                ],
                                "type": "integer"
                            },
                            "datatabela_preco": {
                                "format": "date-time",
                                "description": "Tabela de preço",
                                "type": "string"
                            },
                            "campos_person": {
                                "description": "Campos da personalização",
                                "type": "string"
                            },
                            "status_person": {
                                "description": "Status da personalização",
                                "type": "string"
                            },
                            "num_espelho": {
                                "format": "int32",
                                "description": "Número do espelho",
                                "type": "integer"
                            },
                            "tipocontrato_grafico": {
                                "format": "int32",
                                "description": "Filtro tipo de contrato - gráfico estatístico",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
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
            >>> api = Espelho()
            >>> response = api._consultar_personalizacoes_com_precos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/ConsultarPersonalizacoesComPrecos"
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

    def busca_unidades_de_acordo_com_where_detalhado(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Espelho/BuscaUnidadesDeAcordoComWhereDetalhado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar unidades de aacordo com o "where" informado
        
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
                            "where",
                            "data_tabela_preco"
                        ],
                        "type": "object",
                        "properties": {
                            "where": {
                                "description": "Cláusula Where",
                                "type": "string"
                            },
                            "retorna_venda": {
                                "type": "boolean"
                            },
                            "data_tabela_preco": {
                                "format": "date-time",
                                "description": "Data da tabela de Preço",
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
            >>> api = Espelho()
            >>> response = api._busca_unidades_de_acordo_com_where_detalhado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Espelho/BuscaUnidadesDeAcordoComWhereDetalhado"
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

