from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Composicoes:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def inserir_composicoes(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/InserirComposicoes`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de inserir dados das composições.
        
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
                            "codigo",
                            "descricao",
                            "unidade",
                            "prodEquipe",
                            "tipoCusto",
                            "civilPes"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo": {
                                "description": "Código da composição",
                                "type": "string"
                            },
                            "descricao": {
                                "description": "Descrição da composição",
                                "type": "string"
                            },
                            "unidade": {
                                "description": "Unidade da composição",
                                "type": "string"
                            },
                            "prodEquipe": {
                                "format": "double",
                                "description": "Produção de equipe",
                                "type": "number"
                            },
                            "tipoCusto": {
                                "description": "Tipo de custo da composição, onde: D - Direto; I - Indireto",
                                "type": "string"
                            },
                            "civilPes": {
                                "format": "int32",
                                "description": "Tipo da composição, onde: 0 - Civil; 1 - Pesada",
                                "type": "integer"
                            },
                            "status": {
                                "format": "int32",
                                "description": "Status do insumo, onde: 0 - Ativo; 1 - Inativo",
                                "type": "integer"
                            },
                            "categoria": {
                                "description": "Categoria da composição",
                                "type": "string"
                            },
                            "categoriaMovFin": {
                                "description": "Categoria de movimentação financeira.",
                                "type": "string"
                            },
                            "CAP": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal)",
                                "type": "string"
                            },
                            "CAPEstorno": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para estorno)",
                                "type": "string"
                            },
                            "CAPTransacaoFinanceira": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para transacao financeira)",
                                "type": "string"
                            },
                            "NCM": {
                                "description": "Nomenclatura comum do MERCOSUL",
                                "type": "string"
                            },
                            "CEST": {
                                "description": "Código Especificador da Substituição Tributária",
                                "type": "string"
                            },
                            "aplicacao": {
                                "description": "Código da aplicação fiscal da composição",
                                "type": "string"
                            },
                            "codigoServicoFiscal": {
                                "description": "Número do código de serviço fiscal",
                                "type": "string"
                            },
                            "controlaFVS": {
                                "description": "Controle de ficha de verififação de serviço (FVS), onde: true - Controla; false - Não controla\r\nPela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE\r\nPor tanto, ao informar um valor diferente de Zero sempre será gravado TRUE.",
                                "type": "boolean"
                            },
                            "confirmado": {
                                "format": "int32",
                                "description": "Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado",
                                "type": "integer"
                            },
                            "porcQtdeExcedidaEntrega": {
                                "description": "Percentual de tolerância para entregas com quantidade superior à que foi solicitada.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
                                "type": "string"
                            },
                            "porcPrecoExcedidoEntrega": {
                                "description": "Percentual de tolerância para entregas com preços superiores ao que foi solicitado.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
                                "type": "string"
                            },
                            "porcPrecoReduzidoEntrega": {
                                "description": "Percentual de tolerância para entregas com preços reduzidos ao que foi solicitado.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
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
            >>> api = Composicoes()
            >>> response = api._inserir_composicoes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/InserirComposicoes"
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

    def atualizar_composicoes(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Utilize "" (vazio) caso queira limpar os campos do cadastro sendo que, código, descrição e unidade padrão, não podem ficar vazios.
        
        Endpoint: `/api/v{version}/Composicoes/AtualizarComposicoes`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de atualizar dados das composições.
        
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
                            "listaComposicoesAtualizar": {
                                "description": "Lista dos insumos gerais para atualização dos dados.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Composicoes.ComposicoesRequest"
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
            >>> api = Composicoes()
            >>> response = api._atualizar_composicoes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/AtualizarComposicoes"
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

    def consultar_todas_composicoes(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/ConsultarTodasComposicoes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método responsável por retornar todas as composições gerais.
        
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
            >>> api = Composicoes()
            >>> response = api._consultar_todas_composicoes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/ConsultarTodasComposicoes"
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

    def consultar_composicoes_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/ConsultarComposicoesPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de consultar dados das composições por chave.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Obs&gt;: Para os campos que são possíveis de serem limpados, o parâmetro deve ser preenchido com \"\" (vazio) para que seja possível realizar esse tipo de atualização.",
                        "required": [
                            "codigo"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo": {
                                "description": "Código da composição",
                                "type": "string"
                            },
                            "descricao": {
                                "description": "Descrição da composição",
                                "type": "string"
                            },
                            "unidade": {
                                "description": "Unidade da composição",
                                "type": "string"
                            },
                            "status": {
                                "format": "int32",
                                "description": "Status do insumo, onde: 0 - Ativo; 1 - Inativo",
                                "type": "integer"
                            },
                            "prodEquipe": {
                                "format": "double",
                                "description": "Produção de equipe",
                                "type": "number"
                            },
                            "tipoCusto": {
                                "description": "Tipo de custo da composição, onde: D - Direto; I - Indireto",
                                "type": "string"
                            },
                            "civilPes": {
                                "format": "int32",
                                "description": "Tipo da composição, onde: 0 - Civil; 1 - Pesada",
                                "type": "integer"
                            },
                            "categoria": {
                                "description": "Categoria da composição",
                                "type": "string"
                            },
                            "categoriaMovFin": {
                                "description": "Categoria de movimentação financeira.",
                                "type": "string"
                            },
                            "CAP": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal)",
                                "type": "string"
                            },
                            "CAPEstorno": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para estorno)",
                                "type": "string"
                            },
                            "CAPTransacaoFinanceira": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para transacao financeira)",
                                "type": "string"
                            },
                            "NCM": {
                                "description": "Nomenclatura comum do MERCOSUL",
                                "type": "string"
                            },
                            "CEST": {
                                "description": "Código Especificador da Substituição Tributária",
                                "type": "string"
                            },
                            "aplicacao": {
                                "description": "Código da aplicação fiscal da composição",
                                "type": "string"
                            },
                            "codigoServicoFiscal": {
                                "description": "Número do código de serviço fiscal",
                                "type": "string"
                            },
                            "controlaFVS": {
                                "description": "Controle de ficha de verififação de serviço (FVS), onde: true - Controla; false - Não controla\r\nPela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE\r\nPor tanto, ao informar um valor diferente de Zero sempre será gravado TRUE.",
                                "type": "boolean"
                            },
                            "confirmado": {
                                "format": "int32",
                                "description": "Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado",
                                "type": "integer"
                            },
                            "porcQtdeExcedidaEntrega": {
                                "description": "Percentual de tolerância para entregas com quantidade superior à que foi solicitada.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
                                "type": "string"
                            },
                            "porcPrecoExcedidoEntrega": {
                                "description": "Percentual de tolerância para entregas com preços superiores ao que foi solicitado.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
                                "type": "string"
                            },
                            "porcPrecoReduzidoEntrega": {
                                "description": "Percentual de tolerância para entregas com preços reduzidos ao que foi solicitado.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
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
            >>> api = Composicoes()
            >>> response = api._consultar_composicoes_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/ConsultarComposicoesPorChave"
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

    def consultar_insumos_da_composicao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/ConsultarInsumosDaComposicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de consultar os insumos para uma determinada composição.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Obs&gt;: Para os campos que são possíveis de serem limpados, o parâmetro deve ser preenchido com \"\" (vazio) para que seja possível realizar esse tipo de atualização.",
                        "required": [
                            "codigo"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo": {
                                "description": "Código da composição",
                                "type": "string"
                            },
                            "descricao": {
                                "description": "Descrição da composição",
                                "type": "string"
                            },
                            "unidade": {
                                "description": "Unidade da composição",
                                "type": "string"
                            },
                            "status": {
                                "format": "int32",
                                "description": "Status do insumo, onde: 0 - Ativo; 1 - Inativo",
                                "type": "integer"
                            },
                            "prodEquipe": {
                                "format": "double",
                                "description": "Produção de equipe",
                                "type": "number"
                            },
                            "tipoCusto": {
                                "description": "Tipo de custo da composição, onde: D - Direto; I - Indireto",
                                "type": "string"
                            },
                            "civilPes": {
                                "format": "int32",
                                "description": "Tipo da composição, onde: 0 - Civil; 1 - Pesada",
                                "type": "integer"
                            },
                            "categoria": {
                                "description": "Categoria da composição",
                                "type": "string"
                            },
                            "categoriaMovFin": {
                                "description": "Categoria de movimentação financeira.",
                                "type": "string"
                            },
                            "CAP": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal)",
                                "type": "string"
                            },
                            "CAPEstorno": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para estorno)",
                                "type": "string"
                            },
                            "CAPTransacaoFinanceira": {
                                "description": "O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para transacao financeira)",
                                "type": "string"
                            },
                            "NCM": {
                                "description": "Nomenclatura comum do MERCOSUL",
                                "type": "string"
                            },
                            "CEST": {
                                "description": "Código Especificador da Substituição Tributária",
                                "type": "string"
                            },
                            "aplicacao": {
                                "description": "Código da aplicação fiscal da composição",
                                "type": "string"
                            },
                            "codigoServicoFiscal": {
                                "description": "Número do código de serviço fiscal",
                                "type": "string"
                            },
                            "controlaFVS": {
                                "description": "Controle de ficha de verififação de serviço (FVS), onde: true - Controla; false - Não controla\r\nPela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE\r\nPor tanto, ao informar um valor diferente de Zero sempre será gravado TRUE.",
                                "type": "boolean"
                            },
                            "confirmado": {
                                "format": "int32",
                                "description": "Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado",
                                "type": "integer"
                            },
                            "porcQtdeExcedidaEntrega": {
                                "description": "Percentual de tolerância para entregas com quantidade superior à que foi solicitada.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
                                "type": "string"
                            },
                            "porcPrecoExcedidoEntrega": {
                                "description": "Percentual de tolerância para entregas com preços superiores ao que foi solicitado.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
                                "type": "string"
                            },
                            "porcPrecoReduzidoEntrega": {
                                "description": "Percentual de tolerância para entregas com preços reduzidos ao que foi solicitado.\r\n Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração.",
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
            >>> api = Composicoes()
            >>> response = api._consultar_insumos_da_composicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/ConsultarInsumosDaComposicao"
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

    def alterar_insumo_composicoes_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/AlterarInsumoComposicoesGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de alterar dados dos insumos na composição geral (composição civil).
        
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
                            "codComposicao": {
                                "type": "string"
                            },
                            "codInsumo": {
                                "type": "string"
                            },
                            "tipoItem": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "coeficiente": {
                                "format": "double",
                                "type": "number"
                            },
                            "preco": {
                                "format": "double",
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
            >>> api = Composicoes()
            >>> response = api._alterar_insumo_composicoes_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/AlterarInsumoComposicoesGeral"
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

    def inserir_insumo_composicoes_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/InserirInsumoComposicoesGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de inserir dados dos insumos na composição geral.
        - Método com finalidade de inserir dados dos insumos na composição geral (composição civil).
        
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
                            "codComposicao": {
                                "type": "string"
                            },
                            "codInsumo": {
                                "type": "string"
                            },
                            "tipoItem": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "coeficiente": {
                                "format": "double",
                                "type": "number"
                            },
                            "preco": {
                                "format": "double",
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
            >>> api = Composicoes()
            >>> response = api._inserir_insumo_composicoes_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/InserirInsumoComposicoesGeral"
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

    def consultar_composicoes_por_descricao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/ConsultarComposicoesPorDescricao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar a tabela Composicoes pela sua descrição
        
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
                            "descricao": {
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
            >>> api = Composicoes()
            >>> response = api._consultar_composicoes_por_descricao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/ConsultarComposicoesPorDescricao"
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

    def consultar_composicoes_com_filtro_livre(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        Permite consultar os registros de composições gerais utilizando um filtro livre com qualquer um dos campos existentes
        
        Exemplo de filtro a ser utilizado: 
        1. "filtro": "Cod_comp = '10.50'"
        2. "filtro": "Descr_comp LIKE 'TERRAPLANAGEM%'" 
        3. "filtro": "Cod_comp = '10.50' AND Descr_comp LIKE 'TERRAPLANAGEM%'" 
        4. "filtro": "Cod_comp = '10.50' OR Descr_comp LIKE 'TERRAPLANAGEM%'"
        
        Endpoint: `/api/v{version}/Composicoes/ConsultarComposicoesComFiltroLivre`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar registros de composições gerais utilizando um filtro livre com qualquer um dos campos desta
        
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
                            "filtro": {
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
            >>> api = Composicoes()
            >>> response = api._consultar_composicoes_com_filtro_livre(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/ConsultarComposicoesComFiltroLivre"
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

    def alterar_insumo_composicoes_geral_pesada(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/AlterarInsumoComposicoesGeralPesada`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de alterar dados dos insumos na composição geral (para composições pesadas).
        
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
                            "codComposicao": {
                                "type": "string"
                            },
                            "codInsumo": {
                                "type": "string"
                            },
                            "tipoItem": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "coeficiente": {
                                "format": "double",
                                "type": "number"
                            },
                            "preco": {
                                "format": "double",
                                "type": "number"
                            },
                            "coefProd": {
                                "format": "double",
                                "type": "number"
                            },
                            "coefImProd": {
                                "format": "double",
                                "type": "number"
                            },
                            "dMT": {
                                "format": "double",
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
            >>> api = Composicoes()
            >>> response = api._alterar_insumo_composicoes_geral_pesada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/AlterarInsumoComposicoesGeralPesada"
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

    def inserir_insumo_composicoes_geral_pesada(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Composicoes/InserirInsumoComposicoesGeralPesada`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de inserir dados dos insumos na composição geral (para composições pesadas).
        
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
                            "codComposicao": {
                                "type": "string"
                            },
                            "codInsumo": {
                                "type": "string"
                            },
                            "tipoItem": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "coeficiente": {
                                "format": "double",
                                "type": "number"
                            },
                            "preco": {
                                "format": "double",
                                "type": "number"
                            },
                            "coefProd": {
                                "format": "double",
                                "type": "number"
                            },
                            "coefImProd": {
                                "format": "double",
                                "type": "number"
                            },
                            "dMT": {
                                "format": "double",
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
            >>> api = Composicoes()
            >>> response = api._inserir_insumo_composicoes_geral_pesada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Composicoes/InserirInsumoComposicoesGeralPesada"
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

