from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Cotacao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def atualizar_item_cotacao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarItemCotacao
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Permite atualizar os dados dos itens de cotação, seja ela de material ou de serviço.
        2. Para cotações específicas que forem pertencentes à cotação geral, serão alteradas somente a quantidade e a marca (no caso de cotação de material). 
           Os demais valores só serão alterados se a cotação geral for informada na requisição.
        3. Para cotações que forem pertencentes à cotação geral, durante a execução se não existir insumo para um dos itens da cotação informada a execução irá finalizar, efetivando somente a atualização dos itens de cotação anteriores.
        4. Informações de IPI, ICMS e Marca só estão relacionadas às cotações de material, portanto podem ser omitidas na requisição.
        
        Endpoint: `/api/v{version}/Cotacao/AtualizarItemCotacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar os dados dos itens de cotação de material, cotação de serviço e adiantamento de contrato.
        
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
                            "listaItensCotacao"
                        ],
                        "type": "object",
                        "properties": {
                            "listaItensCotacao": {
                                "description": "Lista de itens de cotação.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.ItensCotacaoForn"
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
            >>> api = Cotacao()
            >>> response = api._atualizar_item_cotacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/AtualizarItemCotacao"
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

    def conta_cotacoes_aprov_mob(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/ContaCotacoesMob
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consultar a quantidade de cotações de material e serviço que possuem simulações que o usuário pode aprovar.
        
        Endpoint: `/api/v{version}/Cotacao/ContaCotacoesAprovMob`
        HTTP Method: `POST`
        
        Implementation Notes:
        Conto as cotações que possuem simulações que o usuário pode aprovar.
        
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
            >>> api = Cotacao()
            >>> response = api._conta_cotacoes_aprov_mob(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ContaCotacoesAprovMob"
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

    def aprovar_simulacoes_compra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. É necessário permissão de aprovação para o programa ALSIMULCOT
        
        Endpoint: `/api/v{version}/Cotacao/AprovarSimulacoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar simulações de compra
        
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
                            "Simulacoes": {
                                "description": "Simulações a serem aprovadas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.AprovaSimulacaoCompraRequest"
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
            >>> api = Cotacao()
            >>> response = api._aprovar_simulacoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/AprovarSimulacoesCompra"
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

    def adicionar_fornecedor_cotacao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AdicionarFornecedorCotacao
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Permite vincular um fornecedor a uma cotação em aberto de material ou serviço.
        2. Para identificação do fornecedor, são aceitos o código ou CPF/CNPJ deste no sistema.
        3. Para vínculo do fornecedor a uma cotação específica, o código dessa cotação, empresa e, o CPF/CNPJ ou código do fornecedor devem ser informados.
        4. Para vínculo do fornecedor a uma cotação geral, somente o código da cotação geral e, o CPF/CNPJ ou código do fornecedor devem ser informados.
        
        Endpoint: `/api/v{version}/Cotacao/AdicionarFornecedorCotacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Adicionar fornecedor a uma cotação aberta.
        
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
                            "codFornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor. Necessário quando o CPF/CNPJ não for informado.",
                                "type": "integer"
                            },
                            "CNPJFornecedor": {
                                "description": "CPF ou CNPJ do fornecedor. Necessário quando o código do fornecedor não for informado.",
                                "type": "string"
                            },
                            "numeroCotacao": {
                                "format": "int32",
                                "description": "Número da cotação. Necessário para quando for cotação específica.",
                                "type": "integer"
                            },
                            "numeroCotacaoGeral": {
                                "format": "int32",
                                "description": "Número da cotação geral. Necessário quando for cotação geral.",
                                "type": "integer"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa. Necessário quando for cotação específica.",
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
            >>> api = Cotacao()
            >>> response = api._adicionar_fornecedor_cotacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/AdicionarFornecedorCotacao"
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

    def buscar_itens_cotacao_fornecedor(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/BuscarItensCotacaoFornecedor
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Permite consultar os dados de itens de cotação de material ou serviço por código do fornecedor.
        2. Somente cotações com status "0 - Criada" são retornadas.
        
        Endpoint: `/api/v{version}/Cotacao/BuscarItensCotacaoFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens de cotação por código do fornecedor.
        
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
                            "cotacao",
                            "fornecedor",
                            "origem"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa da cotação, sendo de informação obrigatória apenas para cotações específicas (origem: 0)",
                                "type": "integer"
                            },
                            "cotacao": {
                                "format": "int32",
                                "description": "Número da cotação",
                                "type": "integer"
                            },
                            "fornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor",
                                "type": "integer"
                            },
                            "origem": {
                                "format": "int32",
                                "description": "Origem da cotação: 0 - Específica; 1 - Geral;",
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
            >>> api = Cotacao()
            >>> response = api._buscar_itens_cotacao_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/BuscarItensCotacaoFornecedor"
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

    def consultar_itens_cotacao_por_obra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Permite consultar itens da cotação de material ou serviço que esteja aguardando confirmação por obra, filtrando por empresa, obra e número da cotação.
        
        Endpoint: `/api/v{version}/Cotacao/ConsultarItensCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens cotação por obra
        
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
                            "cotacao"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Empresa da cotação.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Obra da cotação.",
                                "type": "string"
                            },
                            "cotacao": {
                                "format": "int32",
                                "description": "Número da cotação.",
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
            >>> api = Cotacao()
            >>> response = api._consultar_itens_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ConsultarItensCotacaoPorObra"
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

    def buscar_cotacao_aberta_fornecedor(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio: 
        1. Permite consultar os dados de cotações de material ou serviço que estão disponíveis para o fornecedor. Os tipos de cotações retornadas são:
           - 0 - Cot. material regular
           - 1 - Cot. material adiant. contrato
           - 2 - Cot. serviço regular
           - 3 - Cot. patrimônio
           - 4 - Cot. material contrato
           - 5 - Cot. material emergencial
           - 6 - Cot. manutenção de patrimônio
           - 7 - Cot. material regularização
           - 8 - Cot. material complemento
           - 9 - Cot. serviço emergencial
           - 10 - Cot. serviço regularização
           - 11 - Cot. serviço complemento
           - 12 - Cot. serviço adiant. contrato
           - 13 - Cot. serviço contrato
        2. É obrigatório informar o CNPJ do fornecedor para realizar a consulta.
        
        Endpoint: `/api/v{version}/Cotacao/BuscarCotacaoAbertaFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar as cotações abertas para o fornecedor, por CNPJ do fornecedor.
        
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
                            "cnpj"
                        ],
                        "type": "object",
                        "properties": {
                            "cnpj": {
                                "description": "CNPJ do fornecedor (sem pontuação).",
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
            >>> api = Cotacao()
            >>> response = api._buscar_cotacao_aberta_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/BuscarCotacaoAbertaFornecedor"
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

    def aprovar_confirmacao_cotacao_por_obra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Possibilita aprovar a confirmação da cotação de material ou serviço por obra.
        
        Endpoint: `/api/v{version}/Cotacao/AprovarConfirmacaoCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar confirmação de cotação por obra
        
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
                            "listaConfirmarAprovacaoCotacao": {
                                "description": "Lista de dados de cotação para confirmar aprovação da mesma.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.CotacoesConfirmacaoAprovacao"
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
            >>> api = Cotacao()
            >>> response = api._aprovar_confirmacao_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/AprovarConfirmacaoCotacaoPorObra"
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

    def remover_aprovacao_simulacoes_compra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
        e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.
        
        Endpoint: `/api/v{version}/Cotacao/RemoverAprovacaoSimulacoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Remover aprovações das simulações de compra
        
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
                            "Simulacoes": {
                                "description": "Simulações de compra para remoção das aprovações",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.RemoverAprovacaoSimulacaoCompraRequest"
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
            >>> api = Cotacao()
            >>> response = api._remover_aprovacao_simulacoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/RemoverAprovacaoSimulacoesCompra"
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

    def atualizar_condicao_pagamento_entrega(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarCondicaoPagamentoEntrega
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Permite atualizar os dados de condição de entrega da cotação, bem como dias para entrega, quantidade de parcela, intervalo das parcelas, entre outros.
        2. A condição de pagamento utilizada será sempre SOBRE A ENTREGA.
        3. Para atualizar as condições de pagamento de uma cotação específica, o código dessa cotação e empresa devem ser informados.
        4. Para atualizar as condições de pagamento de uma cotação geral, somente o código da cotação geral deve ser informado.
        
        Endpoint: `/api/v{version}/Cotacao/AtualizarCondicaoPagamentoEntrega`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar as condições de entrega relacionado a cotação.
        
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
                            "fornecedor",
                            "quantidadeEntrega",
                            "quantidadeParcela"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa da cotação. Necessário quando for cotação específica.",
                                "type": "integer"
                            },
                            "cotacao": {
                                "format": "int32",
                                "description": "Número da cotação específica.",
                                "type": "integer"
                            },
                            "numeroCotacaoGeral": {
                                "format": "int32",
                                "description": "Número da cotação geral/agrupada.",
                                "type": "integer"
                            },
                            "fornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor da cotação",
                                "type": "integer"
                            },
                            "diasEntrega": {
                                "format": "int32",
                                "description": "Número de dias para entrega\r\nObs.: Valor máximo = 1000.",
                                "type": "integer"
                            },
                            "quantidadeEntrega": {
                                "format": "int32",
                                "description": "Quantidade de entregas\r\nObs.: Valor &gt;= 1 e valor máximo = 100.",
                                "type": "integer"
                            },
                            "intervaloEntrega": {
                                "format": "int32",
                                "description": "Dias de intervalo entre uma entrega e outra\r\nObs.: Valor &gt;= 0 e valor máximo = 1000.",
                                "type": "integer"
                            },
                            "diasPagamento": {
                                "format": "int32",
                                "description": "Dias para pagamento após entrega\r\nObs.: Valor &gt;= 0 e valor máximo = 1000.",
                                "type": "integer"
                            },
                            "quantidadeParcela": {
                                "format": "int32",
                                "description": "Quantidade de parcelas\r\nObs.: Valor &gt;= 1 e valor máximo = 255.",
                                "type": "integer"
                            },
                            "intervaloParcela": {
                                "format": "int32",
                                "description": "Dias de intervalo entre as parcelas\r\nObs.: Valor &gt;= 0 e valor máximo = 1000.",
                                "type": "integer"
                            },
                            "tipoFrete": {
                                "format": "int32",
                                "description": "Tipo do frete: CIF = 0 e FOB = 1",
                                "type": "integer"
                            },
                            "tipoPagamento": {
                                "format": "int32",
                                "description": "Tipo de pagamento: 0 -&gt; Nenhum, 1 -&gt; Em carteira, 2 -&gt; Em cobrança bancária, 3 -&gt; Crédito em conta, 4 -&gt; Depósito em conta, 5 -&gt; Cartão de crédito ou 6 -&gt; PIX\r\nSe não for informado então será considerado como 0 -&gt; Nenhum.",
                                "type": "integer"
                            },
                            "CondicaoPagamento": {
                                "description": "Condição de pagamento, quando preenchido irá sobrepor a condição gerada automaticamente.",
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
            >>> api = Cotacao()
            >>> response = api._atualizar_condicao_pagamento_entrega(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/AtualizarCondicaoPagamentoEntrega"
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

    def consultar_aprovacao_da_cotacao_por_obra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. São consultadas as aprovações já realizadas para uma determinada cotação de material ou serviço.
        
        Endpoint: `/api/v{version}/Cotacao/ConsultarAprovacaoDaCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar as aprovações da cotação por obra
        
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
                                "description": "Código da empresa que a cotação pertence.",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da obra que a cotação pertence.",
                                "type": "string"
                            },
                            "numeroSimulacao": {
                                "format": "int32",
                                "description": "Número da simulação confirmada que a cotação pertence.",
                                "type": "integer"
                            },
                            "numeroCotacao": {
                                "format": "int32",
                                "description": "Número da cotação.",
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
            >>> api = Cotacao()
            >>> response = api._consultar_aprovacao_da_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ConsultarAprovacaoDaCotacaoPorObra"
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

    def reprovar_confirmacoes_cotacao_por_obra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
        e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.
        
        Endpoint: `/api/v{version}/Cotacao/ReprovarConfirmacoesCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Reprovar as confirmações de cotação por obra
        
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
                            "justificativaReprovacao"
                        ],
                        "type": "object",
                        "properties": {
                            "ConfirmacoesCotacao": {
                                "description": "Reprovar confirmação de cotação.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.ReprovarConfirmacaoCotacaoPorObraRequest"
                                }
                            },
                            "justificativaReprovacao": {
                                "description": "Justificativa para a reprovação da simulação.",
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
            >>> api = Cotacao()
            >>> response = api._reprovar_confirmacoes_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ReprovarConfirmacoesCotacaoPorObra"
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

    def conta_cotacoes_mob(
        self,
        login_usuario: Optional[str] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/Cotacao/ContaCotacoesMob`
        HTTP Method: `POST`
        
        Implementation Notes:
        Conto as cotações que possuem simulações que o usuário pode aprovar.
        
        Args:
            login_usuario (Dict[str, Any]): login do usuário.
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "login_usuario": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": "login do usuário."
                },
                "api-version": {
                    "type": "string",
                    "in": "query",
                    "required": false,
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
            >>> api = Cotacao()
            >>> response = api._conta_cotacoes_mob(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Cotacao/ContaCotacoesMob"
        kwargs = {
            "login_usuario": login_usuario,
            "api-version": api_version,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_cotacoes_confirmacao_pendente(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consulta cotações de material e serviço que estão com as confirmações pendentes.
        
        Endpoint: `/api/v{version}/Cotacao/ConsultarCotacoesConfirmacaoPendente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar as cotações com confirmações pendentes
        
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
                            "usuario",
                            "listaEmpObras"
                        ],
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "description": "Usuário da aprovação.",
                                "type": "string"
                            },
                            "departamento": {
                                "description": "Departamento do usuário",
                                "type": "string"
                            },
                            "cargo": {
                                "description": "Cargo do usuário",
                                "type": "string"
                            },
                            "listaEmpObras": {
                                "description": "Lista das empresas e obras selecionadas pelo usuário",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.ObraCotacaoRequest"
                                }
                            },
                            "cotacao": {
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
            >>> api = Cotacao()
            >>> response = api._consultar_cotacoes_confirmacao_pendente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ConsultarCotacoesConfirmacaoPendente"
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

    def consultar_quantidade_cotacao_pendente_por_obra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Verifica a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.
        
        Endpoint: `/api/v{version}/Cotacao/ConsultarQuantidadeCotacaoPendentePorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar a quantidade de cotações pendentes de aprovação por obra
        
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
                            "loginUsuario"
                        ],
                        "type": "object",
                        "properties": {
                            "loginUsuario": {
                                "description": "Login do usuário da aprovação",
                                "type": "string"
                            },
                            "codigoDepartamento": {
                                "description": "Código do departamento que o usuário da aprovação está vinculado (opcional)",
                                "type": "string"
                            },
                            "codigoCargo": {
                                "description": "Código do cargo que o usuário da aprovação está vinculado (opcional)",
                                "type": "string"
                            },
                            "listaEmpObras": {
                                "description": "Lista das empresas e obras selecionadas que deseja consultar as aprovações pendentes (opcional)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.ObraCotacaoRequest"
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
            >>> api = Cotacao()
            >>> response = api._consultar_quantidade_cotacao_pendente_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ConsultarQuantidadeCotacaoPendentePorObra"
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

    def consultar_quantidade_cotacao_pendente_por_obra_mob(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consultar a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.
        
        Endpoint: `/api/v{version}/Cotacao/ConsultarQuantidadeCotacaoPendentePorObraMob`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar a quantidade de cotações pendentes de aprovação para a obra selecionada
        
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
                            "loginUsuario"
                        ],
                        "type": "object",
                        "properties": {
                            "loginUsuario": {
                                "description": "Login do usuário da aprovação",
                                "type": "string"
                            },
                            "codigoDepartamento": {
                                "description": "Código do departamento que o usuário da aprovação está vinculado (opcional)",
                                "type": "string"
                            },
                            "codigoCargo": {
                                "description": "Código do cargo que o usuário da aprovação está vinculado (opcional)",
                                "type": "string"
                            },
                            "listaEmpObras": {
                                "description": "Lista das empresas e obras selecionadas que deseja consultar as aprovações pendentes (opcional)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Cotacao.ObraCotacaoRequest"
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
            >>> api = Cotacao()
            >>> response = api._consultar_quantidade_cotacao_pendente_por_obra_mob(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ConsultarQuantidadeCotacaoPendentePorObraMob"
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

    def consultar_justificativas_aprovacao_fora_sequencia(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consultar as justificativas que podem ser utilizadas em aprovações de confirmação de cotação de material ou serviço que esteja fora da sequência do usuário (Controle de aprovações).
        
        Endpoint: `/api/v{version}/Cotacao/ConsultarJustificativasAprovacaoForaSequencia`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar as justificativas para aprovações de cotação fora da sequência do usuário.
        
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
            >>> api = Cotacao()
            >>> response = api._consultar_justificativas_aprovacao_fora_sequencia(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/ConsultarJustificativasAprovacaoForaSequencia"
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

    def inserir_altera_coment_forn_frete(
        self,
        version: str,
        request: Optional[Dict] = None,
        tipo_carencia_fixa: Optional[Any] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/InserirAlteraComentFornFrete
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Inserir um comentário ou atualizar um já existente.
        
        Endpoint: `/api/v{version}/Cotacao/InserirAlteraComentFornFrete`
        HTTP Method: `POST`
        
        Implementation Notes:
        Esta rotina inseri um comentario ou atualizar um ja existente."), SoapHeader("TicketAuth
        
        Args:
            request (Dict[str, Any]): The request
            tipoCarenciaFixa (Dict[str, Any]): The carencia fixa
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
                                "format": "int32",
                                "description": "Código da empresa da cotação",
                                "type": "integer"
                            },
                            "codigo_fornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor da cotação",
                                "type": "integer"
                            },
                            "cotacao": {
                                "format": "int32",
                                "description": "Número da cotação",
                                "type": "integer"
                            },
                            "cond_pagto": {
                                "format": "int32",
                                "description": "Condição de pagamento: 0, 1 ou 2",
                                "type": "integer"
                            },
                            "tipo_coment": {
                                "format": "int32",
                                "description": "Tipo de comentário: 0 - Fornecedor ou 1 - Frete",
                                "type": "integer"
                            },
                            "efet_pgto_parc": {
                                "format": "int32",
                                "description": "Efetua pagamento em parcela sobre: 0 - Vencimento da 1ª parcela, 1 - Entrega, 2 - Cotação ou 3 - Emissão da nota fiscal",
                                "type": "integer"
                            },
                            "dtvenc_ini": {
                                "description": "Data de vencimento",
                                "type": "string"
                            },
                            "qtde_parc": {
                                "format": "double",
                                "description": "Quantiade de Parcelas",
                                "type": "number"
                            },
                            "intev_parc": {
                                "format": "double",
                                "description": "Intervalo das parcelas",
                                "type": "number"
                            },
                            "obs_pgto": {
                                "description": "Observação de pagamento",
                                "type": "string"
                            },
                            "obs_entrega": {
                                "description": "Observação de Entrega",
                                "type": "string"
                            },
                            "tipo_pgto": {
                                "format": "int32",
                                "description": "Tipo de Pagamento: 0 - Nenhum, 1 - Em carteira, 2 - Em cobrança bancária, 3 - Crédito em conta, 4 - Depósito em conta, 5 - Cartão de crédito ou 6 - PIX",
                                "type": "integer"
                            },
                            "tem_frete": {
                                "format": "int32",
                                "description": "Informa o tipo de frete: 0 - FOB (material a retirar), 1 - CIF (Frete por conta do emitente), 2 - FOB (Frete a pagar incluso) ou 3 - FOB (Frete a pagar para transportadora)",
                                "type": "integer"
                            },
                            "diaini_venc": {
                                "format": "int32",
                                "description": "Dia inicial do vencimento",
                                "type": "integer"
                            },
                            "freteqtde_ent": {
                                "format": "int32",
                                "description": "Quantidade de Entrega",
                                "type": "integer"
                            },
                            "interv_ent": {
                                "format": "int32",
                                "description": "Intervalo entre as Entregas",
                                "type": "integer"
                            },
                            "diasEntrega": {
                                "format": "int32",
                                "description": "Dias para entrega",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "tipoCarenciaFixa": {
                    "type": "boolean",
                    "in": "query",
                    "required": false,
                    "description": ""
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
            >>> api = Cotacao()
            >>> response = api._inserir_altera_coment_forn_frete(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Cotacao/InserirAlteraComentFornFrete"
        kwargs = {
            "request": request,
            "tipoCarenciaFixa": tipo_carencia_fixa,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

