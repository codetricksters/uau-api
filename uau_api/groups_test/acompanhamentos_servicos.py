from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class AcompanhamentosServicos:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def acompanhar_contrato(
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
        Grava o acompanhamento de contrato vinculado a um planejamento ou orçamento
        1. Informar os parâmetros dependendo do vinculo com orçamento ou planejamento
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/AcompanharContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Grava o acompanhamento de contrato vinculado a um planejamento ou orçamento
        
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
                            "empresa": {
                                "description": "Codigo da empresa",
                                "type": "string"
                            },
                            "obra": {
                                "description": "Codigo da obra",
                                "type": "string"
                            },
                            "produto": {
                                "format": "int32",
                                "description": "Codigo do produto (apenas para planejamento)",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Codigo do contrato (apenas para planejamento)",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Codigo do item do serviço (planejamento ou orçamento)",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "descricaoServico": {
                                "description": "Descrição do serviço",
                                "type": "string"
                            },
                            "mes": {
                                "format": "date-time",
                                "description": "Mês pl para planejamento ou Período Mensal, para orçamento. Obs informar data no formato Mês/Dia/Ano",
                                "type": "string"
                            },
                            "dataInicio": {
                                "format": "date-time",
                                "description": "Data inicio do acompanhamento do contrato. Obs informar data no formato Mês/Dia/Ano",
                                "type": "string"
                            },
                            "dataFim": {
                                "format": "date-time",
                                "description": "Data final do acompanhamento do contrato. Obs informar data no formato Mês/Dia/Ano",
                                "type": "string"
                            },
                            "usuario": {
                                "description": "Usuário logado",
                                "type": "string"
                            },
                            "qtde": {
                                "format": "double",
                                "description": "Quantidade a ser acompanhada",
                                "type": "number"
                            },
                            "sequencia": {
                                "description": "Sequencia da estrutura (para quando for acompanhamento de estrutura)",
                                "type": "string"
                            },
                            "codigoEstrutura": {
                                "description": "Código da estrutura (para quando for acompanhamento de estrutura)",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Código do orçamento (apenas para orçamento)",
                                "type": "integer"
                            },
                            "contratoVinculado": {
                                "format": "int32",
                                "description": "Código do contrato vinculado ao planejamento/orçamento",
                                "type": "integer"
                            },
                            "ordem": {
                                "format": "int32",
                                "description": "É o Item do Serv. no acompanhamento de execução de contrato",
                                "type": "integer"
                            },
                            "etapa": {
                                "description": "A descrição da etapa que está sendo acompanhada",
                                "type": "string"
                            },
                            "observacao": {
                                "description": "Campo livre",
                                "type": "string"
                            },
                            "aplicacaoMaterial": {
                                "description": "Lista para informar a quantidade que será aplicada por item de material. (Usada quando há vínculos entre itens do contrato)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentosServicos.QtdAplicadaPorMaterial"
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/AcompanharContrato"
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

    def acompanhar_servico_pl(
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
        Acompanhar serviço do planejamento solicitado.
        1. Valida se o usuário está cadastrado no sistema e ativo.
        2. Valida se já existe acompanhamento para o código externo de integração solicitado.
        3. Verifica se o fechamento do acompanhamento não foi realizado.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/AcompanharServicoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Acompanhamento de Serviços do planejamento.
        
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
                            "obra",
                            "usuario"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "description": "Codigo da empresa do serviço",
                                "type": "string"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "produto": {
                                "format": "int32",
                                "description": "Codigo do produto do serviço",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Codigo do contrato do serviço",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Codigo do item do serviço",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "mes": {
                                "description": "Mês pl do serviço",
                                "type": "string"
                            },
                            "usuario": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "qtde": {
                                "format": "double",
                                "description": "Quantidade do serviço",
                                "type": "number"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração do acompanhamento de serviço PL",
                                "type": "string"
                            },
                            "aprovaContrato": {
                                "description": "indica se deve aprovar o contrato vinculado",
                                "type": "boolean"
                            },
                            "contratoVinculado": {
                                "format": "int32",
                                "description": "contrato",
                                "type": "integer"
                            },
                            "descricaoServico": {
                                "type": "string"
                            },
                            "ordem": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "etapa": {
                                "type": "string"
                            },
                            "observacao": {
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servicopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/AcompanharServicoPL"
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

    def acompanhar_servico_orcado(
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
        Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.
        1. Deve montar uma estrutura seguindo o modelo.
        2. Valida se o usuário está cadastrado.
        3. Valida se o serviço não possui estruturas.
        4. Valida se possui distribuição no periodo acompanhado.
        5. Valida o saldo do orçamento que será acompanhado.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/AcompanharServicoOrcado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Acompanhar serviços de orçamento.
        
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
                            "obra",
                            "servico",
                            "item",
                            "usuario_logado"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serviço",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "item": {
                                "description": "Codigo do item do serviço",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Codigo do orçamento do serviço",
                                "type": "integer"
                            },
                            "periodo": {
                                "description": "Período do serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serviço",
                                "type": "number"
                            },
                            "usuario_logado": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao acompanhamento do serviço do orçamento",
                                "type": "string"
                            },
                            "aprovaContrato": {
                                "description": "indica se deve aprovar o contrato vinculado",
                                "type": "boolean"
                            },
                            "contratoVinculado": {
                                "format": "int32",
                                "description": "contrato",
                                "type": "integer"
                            },
                            "descricaoServico": {
                                "type": "string"
                            },
                            "ordem": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "etapa": {
                                "type": "string"
                            },
                            "mes": {
                                "type": "string"
                            },
                            "produto": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "observacao": {
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servico_orcado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/AcompanharServicoOrcado"
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

    def acompanhar_servico_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método do acordo com o modelo.
        
        Definição de Negócio:
        Permite consultar e portanto acompanhar serviços referentes aos contratos.
        1. Valida usuário.
        2. Valida prazo de validade do contrato.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/AcompanharServicoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Acompanhar serviços de contrato.
        
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
                            "obra",
                            "contrato_servico",
                            "item_contrato"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serivço",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "contrato_servico": {
                                "format": "int32",
                                "description": "Codigo do contrato do serviço",
                                "type": "integer"
                            },
                            "item_contrato": {
                                "format": "int32",
                                "description": "Codigo do item do contrato do serviço",
                                "type": "integer"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "data_inicio": {
                                "description": "Data início do serviço.",
                                "type": "string"
                            },
                            "data_fim": {
                                "description": "Data fim do serviço",
                                "type": "string"
                            },
                            "mes_pl": {
                                "description": "Mes pl do serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serivço",
                                "type": "number"
                            },
                            "porcentagem_acomp": {
                                "format": "double",
                                "description": "Porcentagem do serviço",
                                "type": "number"
                            },
                            "observacoes": {
                                "description": "Observações do serviço",
                                "type": "string"
                            },
                            "etapa": {
                                "description": "Etapa do serviço",
                                "type": "string"
                            },
                            "cod_estrutura": {
                                "description": "Codigo da estrutura do serviço. Deve ser passado como \"\" em caso de item sem estrutura.",
                                "type": "string"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço. Deve ser passado como \"\" em caso de item sem estrutura.",
                                "type": "string"
                            },
                            "usuario_logado": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "cod_acomp": {
                                "format": "double",
                                "description": "Código do acompanhamento",
                                "type": "number"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Código do orçamento para realizar o acompanhamento de execução em paralelo.",
                                "type": "integer"
                            },
                            "itemOrcamento": {
                                "description": "Item do orçamento para realizar o acompanhamento de execução em paralelo.",
                                "type": "string"
                            },
                            "aplicacaoMaterial": {
                                "description": "Lista para informar a quantidade que será aplicada por item de material. (Usada quando há vínculos entre itens do contrato)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentosServicos.QtdAplicadaPorMaterial"
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servico_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/AcompanharServicoContrato"
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

    def acompanhar_servico_orcado_em_lote(
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
        Acompanhar vários serviços do orçamento.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/AcompanharServicoOrcadoEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Acompanhar vários serviços do orçamento.
        
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
                            "obra",
                            "usuario_logado",
                            "servicos"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serviço",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Codigo do orçamento do serviço",
                                "type": "integer"
                            },
                            "usuario_logado": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "servicos": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentosServicos.ListaServicosOrcados"
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servico_orcado_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/AcompanharServicoOrcadoEmLote"
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

    def excluir_acompanhamento_servico_pl(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Permite excluir acompanhamento de Serviços do planejamento.
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio: 
        Acompanhar serviço do planejamento solicitado.
        1. Valida se existe acompanhamento para o código informado.
        2. Valida se existe acompanhamento para o registro informado.
        3. Valida se o acompanhamento se encontra aberto.
        4. Valida a quantidade informada para exclusão.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir acompanhamento de Serviços do planejamento.
        
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
                            "obra",
                            "contrato",
                            "usuario"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "description": "Codigo da empresa do serviço",
                                "type": "string"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "produto": {
                                "format": "int32",
                                "description": "Codigo do produto do serviço",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Codigo do contrato do serviço",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Codigo do item do serviço",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "mes": {
                                "description": "Mês pl do serviço",
                                "type": "string"
                            },
                            "usuario": {
                                "description": "login do usuário do serviço",
                                "type": "string"
                            },
                            "qtde": {
                                "format": "double",
                                "description": "Quantidade do serviço",
                                "type": "number"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração do acompanhamento de serviço PL",
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servicopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoPL"
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

    def acompanhar_servico_contrato_em_lote(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método do acordo com o modelo.
        
        Definição de Negócio:
        Permite acompanhar vários serviços referentes ao contrato.
        1. Valida usuário.
        2. Valida prazo de validade do contrato.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/AcompanharServicoContratoEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Acompanhar vários serviços do contrato.
        
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
                            "obra",
                            "contrato_servico",
                            "usuario_logado",
                            "servicos"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serivço",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "contrato_servico": {
                                "format": "int32",
                                "description": "Codigo do contrato do serviço",
                                "type": "integer"
                            },
                            "usuario_logado": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "servicos": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentosServicos.ListaServicos"
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servico_contrato_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/AcompanharServicoContratoEmLote"
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

    def excluir_acompanhamento_servico_orcado(
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
        Permite excluir acompanhamento de serviço orçado.
        1. Valida se a exclusão pode ser realizada.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir acompanhamento de serviço orçado.
        
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
                            "obra",
                            "servico"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serviço.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "item": {
                                "description": "Codigo do item do serviço",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Codigo do orçamento do serviço",
                                "type": "integer"
                            },
                            "periodo": {
                                "description": "Período do serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serviço",
                                "type": "number"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço.",
                                "type": "string"
                            },
                            "numAcomp": {
                                "format": "int32",
                                "description": "Numero do acompanhamento do serviço.",
                                "type": "integer"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao acompanhamento do serviço do orçamento",
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_orcado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcado"
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

    def alterar_acompanhamento_servico_contrato(
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
        Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.
        1. Deve montar uma estrutura seguindo o modelo.
        2. Valida se o usuário é cadastrado e se tem permissão para realizar a alteração.
        3. Valida se o serviço é controlado por tipologia de produção.
        4. Valida se a quantidade a acompanhar excede o saldo a acompanhar.
        5. Valida se o contrato é valido para aletrações.
        6. Valida o prazo de validade do contrato.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/AlterarAcompanhamentoServicoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar acompanhamento de serviços de contrato.
        
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
                            "obra",
                            "contrato_servico",
                            "item_contrato"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serivço",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "contrato_servico": {
                                "format": "int32",
                                "description": "Codigo do contrato do serviço",
                                "type": "integer"
                            },
                            "item_contrato": {
                                "format": "int32",
                                "description": "Codigo do item do contrato do serviço",
                                "type": "integer"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "data_inicio": {
                                "description": "Data início do serviço.",
                                "type": "string"
                            },
                            "data_fim": {
                                "description": "Data fim do serviço",
                                "type": "string"
                            },
                            "mes_pl": {
                                "description": "Mes pl do serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serivço",
                                "type": "number"
                            },
                            "porcentagem_acomp": {
                                "format": "double",
                                "description": "Porcentagem do serviço",
                                "type": "number"
                            },
                            "observacoes": {
                                "description": "Observações do serviço",
                                "type": "string"
                            },
                            "etapa": {
                                "description": "Etapa do serviço",
                                "type": "string"
                            },
                            "cod_estrutura": {
                                "description": "Codigo da estrutura do serviço. Deve ser passado como \"\" em caso de item sem estrutura.",
                                "type": "string"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço. Deve ser passado como \"\" em caso de item sem estrutura.",
                                "type": "string"
                            },
                            "usuario_logado": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "cod_acomp": {
                                "format": "double",
                                "description": "Código do acompanhamento",
                                "type": "number"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Código do orçamento para realizar o acompanhamento de execução em paralelo.",
                                "type": "integer"
                            },
                            "itemOrcamento": {
                                "description": "Item do orçamento para realizar o acompanhamento de execução em paralelo.",
                                "type": "string"
                            },
                            "aplicacaoMaterial": {
                                "description": "Lista para informar a quantidade que será aplicada por item de material. (Usada quando há vínculos entre itens do contrato)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentosServicos.QtdAplicadaPorMaterial"
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._alterar_acompanhamento_servico_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/AlterarAcompanhamentoServicoContrato"
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

    def excluir_acompanhamento_servico_de_contrato(
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
        Exclui o acompanhamento de serviço no contrato.
        1. Valida se o usuário tem permissão para excluir um acompanhamento.
        2. Valida se possui estrutura e se o status do acompanhamento está como "aberto". Neste caso não será excluido.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir acompanhamento de serviço de contrato.
        
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
                            "contrato_servico",
                            "item_contrato",
                            "servico",
                            "usuario_logado"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serviço",
                                "type": "integer"
                            },
                            "contrato_servico": {
                                "format": "int32",
                                "description": "Codigo do contrato do serviço",
                                "type": "integer"
                            },
                            "item_contrato": {
                                "format": "int32",
                                "description": "Codigo do item do serviço",
                                "type": "integer"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serviço",
                                "type": "number"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço",
                                "type": "string"
                            },
                            "codigo_estrutura": {
                                "description": "Codigo da estrutura do serviço",
                                "type": "string"
                            },
                            "usuario_logado": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "codAec": {
                                "format": "int32",
                                "description": "Codigo do acompanhamento de execução de contrato",
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_de_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContrato"
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

    def excluir_acompanhamento_servico_orcado_em_lote(
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
        Permite excluir acompanhamento de vários serviços orçados.
        1. Valida se a exclusão pode ser realizada.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir acompanhamento de serviços orçado.
        
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
                            "obra",
                            "avancos"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serviço.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Codigo do orçamento do serviço",
                                "type": "integer"
                            },
                            "avancos": {
                                "description": "Codigo do serviço",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentosServicos.ServicosOrcadoParaExcluir"
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_orcado_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoEmLote"
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

    def excluir_acompanhamento_servico_orcado_por_chave(
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
        Exclui o acompanhamento de serviço oraçado de acordo com a chave informada.
        1. Valida se o acompanhamento informado existe.
        2. Valida se a exclusão pode ser realizada.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir acompanhamento de serviço orçado por chave.
        
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
                            "obra",
                            "servico"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serviço.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do serviço",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Codigo do serviço",
                                "type": "string"
                            },
                            "item": {
                                "description": "Codigo do item do serviço",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Codigo do orçamento do serviço",
                                "type": "integer"
                            },
                            "periodo": {
                                "description": "Período do serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serviço",
                                "type": "number"
                            },
                            "sequencia": {
                                "description": "Sequencia do serviço.",
                                "type": "string"
                            },
                            "numAcomp": {
                                "format": "int32",
                                "description": "Numero do acompanhamento do serviço.",
                                "type": "integer"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao acompanhamento do serviço do orçamento",
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_orcado_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoPorChave"
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

    def excluir_acompanhamento_servico_de_contrato_em_lote(
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
        Exclui o acompanhamento de vários serviços no contrato.
        1. Valida se o usuário tem permissão para excluir um acompanhamento.
        2. Valida se possui estrutura e se o status do acompanhamento está como "aberto". Neste caso não será excluido.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContratoEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir acompanhamento de serviços do contrato.
        
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
                            "contrato_servico",
                            "usuario_logado",
                            "avancos"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do serviço",
                                "type": "integer"
                            },
                            "contrato_servico": {
                                "format": "int32",
                                "description": "Codigo do contrato do serviço",
                                "type": "integer"
                            },
                            "usuario_logado": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "avancos": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentosServicos.Avanco"
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_de_contrato_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContratoEmLote"
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

    def consultar_acompanhamento_contrato_servico_por_servico(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Consulta acompanhamento de contrato de serviço filtrando por serviço.
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Acompanhar contrato de serviço por empresa e serviço.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "required": [
                            "Empresa",
                            "Servico"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "Servico": {
                                "description": "Código do serviço",
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._consultar_acompanhamento_contrato_servico_por_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorServico"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_acompanhamento_contrato_servico_por_contrato_eservico(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        Definição de Negócio:
        Permite acompanhar contratos filtrando por:
            - Empresa
            - Contrato
            - Serviço
        
        Endpoint: `/api/v{version}/AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorContratoEServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Acompanhar contrato de serviço por empresa, contrato e serviço.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "required": [
                            "Empresa",
                            "Contrato",
                            "Servico"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "Contrato": {
                                "format": "int32",
                                "description": "Código do contrato",
                                "type": "integer"
                            },
                            "Servico": {
                                "description": "Código do serviço",
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
            >>> api = AcompanhamentosServicos()
            >>> response = api._consultar_acompanhamento_contrato_servico_por_contratoe_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorContratoEServico"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

