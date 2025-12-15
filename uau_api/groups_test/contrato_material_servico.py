from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ContratoMaterialServico:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_itens_contrato(
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
        1. Consultar itens presentes em um contrato.
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarItensContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens de contrato
        
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
                                "format": "int32",
                                "description": "Código da empresa do contrato.",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato.",
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_itens_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarItensContrato"
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

    def consultar_contrato_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna os dados do contrato.
        
        Definição de Negócio:
        1. Consulta contrato filtrando pela chave.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarContratoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar contrato
        
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
                            "contrato"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa do contrato.",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato.",
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contrato_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarContratoPorChave"
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

    def consultar_contrato_por_fornecedor(
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
        1. Consulta os contratos de um fornecedor.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarContratoPorFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar contratos por fornecedor
        
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
                            "fornecedor"
                        ],
                        "type": "object",
                        "properties": {
                            "fornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor do contrato.",
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contrato_por_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarContratoPorFornecedor"
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

    def consultar_contrato_por_servico_material(
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
        1. Consulta contrato filtrando por:
            1. Empresa;
            2. Serviço ou material;
            
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarContratoPorServicoMaterial`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar contrato por serviço/material e empresa
        
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
                                "format": "int32",
                                "description": "Código da empresa do contrato.",
                                "type": "integer"
                            },
                            "servicoMaterial": {
                                "description": "Código do serviço ou material do contrato.",
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contrato_por_servico_material(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarContratoPorServicoMaterial"
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

    def consultar_itens_vinculo_orcamento_servico(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.
        
        Definição de Negócio:
        1. Consultar os itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
        2. Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarItensVinculoOrcamentoServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar os itens  do vinculo com o orçamento - SERVIÇOS
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa do contrato.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "item": {
                                "description": "Código do item.",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço.",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Código do orçamento",
                                "type": "integer"
                            },
                            "somenteContratosAprovados": {
                                "description": "Indica se deseja retornar somente os itens de contratos que estejam aprovados",
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_itens_vinculo_orcamento_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarItensVinculoOrcamentoServico"
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

    def consultar_saldo_reajustado_por_item_contrato(
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
        1. Consultar valores aprovados e saldo reajustado de itens do contrato.
        2. Consulta contrato filtrando por:
            1. Empresa (obrigatório)
            2. Obra;
            3. Situacoes (pode ser informado uma lista de situações): 
                - 0 - Andamento
                - 1 - Paralisado
                - 2 - Cancelado
                - 3 - Concluído
                - 4 - Em encerramento
            4. Contratos (pode ser informada uma lista de contratos);
            
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarSaldoReajustadoPorItemContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de consultar valores aprovados e saldo reajustado de itens do contrato.
        
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
                            "empresa"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa do contrato.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "contratos": {
                                "description": "Códigos dos contratos.",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "situacoes": {
                                "description": "Códigos das situações.",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_saldo_reajustado_por_item_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarSaldoReajustadoPorItemContrato"
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

    def consultar_itens_vinculo_planejamento_servico(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarItensVinculoPlanejamentoServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar os itens  do vinculo com o planejamento - SERVIÇOS
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa do contrato.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "item": {
                                "description": "Código do item.",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço.",
                                "type": "string"
                            },
                            "produto": {
                                "format": "int32",
                                "description": "Código do produto",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato no planejamento",
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_itens_vinculo_planejamento_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarItensVinculoPlanejamentoServico"
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

    def consultar_contratos_itens_vinculado_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.
        
        Definição de Negócio:
        1. Consultar os contratos e itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
        2. Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        Endpoint: `/api/v{version}/ContratoMaterialServico/ConsultarContratosItensVinculadoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar os contratos e itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa do contrato.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Código do orçamento",
                                "type": "integer"
                            },
                            "somenteContratosAprovados": {
                                "description": "Indica se deseja retornar somente os itens de contratos que estejam aprovados",
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contratos_itens_vinculado_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ContratoMaterialServico/ConsultarContratosItensVinculadoOrcamento"
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

    def obter_lista_estrutura_aprovacoes(
        self,
        int_num_aprov: Optional[int] = None,
        tipo_aprovacao: Optional[int] = None,
        tipo_pedido: Optional[int] = None,
        api_version: Optional[str] = None,
        ger_aprov_lista_estrutura_de_aprovacao: Optional[Any] = None,
        ger_aprov_codigo_da_empresa: Optional[int] = None,
        ger_aprov_codigo_da_obra: Optional[str] = None,
        ger_aprov_tipo_do_processo: Optional[int] = None,
        ger_aprov_quantidade_aprovacao: Optional[int] = None,
        ger_aprov_valor_solicitado: Optional[Any] = None,
        ger_aprov_usuario_logado: Optional[str] = None,
        ger_aprov_acao: Optional[int] = None,
        ger_aprov_estrutura_aprovacao: Optional[int] = None,
        ger_aprov_estrutura_aprov_faixa_valor: Optional[int] = None,
        ger_aprov_codigo_departamento: Optional[str] = None,
        ger_aprov_codigo_cargo: Optional[str] = None,
        ger_aprov_lista_seq_pend_aprov_abaixo_seq_usuario_log: Optional[Any] = None,
        ger_aprov_is_aprov_fora_sequencia: Optional[Any] = None,
        ger_aprov_chave_justificativa_aprovacao: Optional[str] = None,
        rep_aprov_simula_conf_string_format: Optional[str] = None,
        rep_aprov_simula_conf_empresa_apsc: Optional[int] = None,
        rep_aprov_simula_conf_obra_apsc: Optional[str] = None,
        rep_aprov_simula_conf_numero_sim_apsc: Optional[int] = None,
        rep_aprov_simula_conf_num_cot_apsc: Optional[int] = None,
        rep_aprov_simula_conf_usr_aprov_apsc: Optional[str] = None,
        rep_aprov_simula_conf_data_aprov_apsc: Optional[str] = None,
        rep_aprov_simula_conf_cod_cargo_apsc: Optional[str] = None,
        rep_aprov_simula_conf_cod_dep_apsc: Optional[str] = None,
        rep_aprov_simula_conf_num_jus_aprov_apsc: Optional[int] = None,
        rep_aprov_simula_conf_num_apsc: Optional[int] = None,
        rep_aprov_simula_conf_s_empresa_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_obra_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_numero_sim_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_num_cot_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_usr_aprov_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_data_aprov_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_cod_cargo_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_cod_dep_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_num_jus_aprov_apsc: Optional[str] = None,
        rep_aprov_simula_conf_s_num_apsc: Optional[str] = None,
        rep_aprov_simula_conf_query_source: Optional[str] = None,
        rep_aprov_simula_conf_mapping_name: Optional[str] = None,
        rep_aprov_simula_conf_schema_global: Optional[str] = None,
        rep_aprov_simula_conf_schema_table_view: Optional[str] = None,
        rep_aprov_simula_conf_schema_stored_procedure: Optional[str] = None,
        rep_aprov_simula_conf_not_recommended_connection_connection_string: Optional[str] = None,
        rep_aprov_simula_conf_not_recommended_connection_command_timeout: Optional[int] = None,
        rep_aprov_simula_conf_not_recommended_connection_connection_timeout: Optional[int] = None,
        rep_aprov_simula_conf_not_recommended_connection_default_database: Optional[str] = None,
        rep_aprov_simula_conf_not_recommended_connection_isolation_level: Optional[int] = None,
        rep_aprov_simula_conf_not_recommended_connection_attributes: Optional[int] = None,
        rep_aprov_simula_conf_not_recommended_connection_cursor_location: Optional[int] = None,
        rep_aprov_simula_conf_not_recommended_connection_mode: Optional[int] = None,
        rep_aprov_simula_conf_not_recommended_connection_provider: Optional[str] = None,
        rep_aprov_simula_conf_connection_string: Optional[str] = None,
        rep_aprov_simula_conf_connection_string_config: Optional[str] = None,
        rep_aprov_simula_conf_filter: Optional[str] = None,
        rep_aprov_simula_conf_sort: Optional[str] = None,
        rep_aprov_cont_string_format: Optional[str] = None,
        rep_aprov_cont_empresa_ap_cont: Optional[int] = None,
        rep_aprov_cont_cod_cont_ap_cont: Optional[int] = None,
        rep_aprov_cont_usr_aprov_ap_cont: Optional[str] = None,
        rep_aprov_cont_data_aprov_ap_cont: Optional[str] = None,
        rep_aprov_cont_cod_cargo_ap_cont: Optional[str] = None,
        rep_aprov_cont_cod_dep_ap_cont: Optional[str] = None,
        rep_aprov_cont_num_jus_aprov_ap_cont: Optional[int] = None,
        rep_aprov_cont_num_ap_cont: Optional[int] = None,
        rep_aprov_cont_s_empresa_ap_cont: Optional[str] = None,
        rep_aprov_cont_s_cod_cont_ap_cont: Optional[str] = None,
        rep_aprov_cont_s_usr_aprov_ap_cont: Optional[str] = None,
        rep_aprov_cont_s_data_aprov_ap_cont: Optional[str] = None,
        rep_aprov_cont_s_cod_cargo_ap_cont: Optional[str] = None,
        rep_aprov_cont_s_cod_dep_ap_cont: Optional[str] = None,
        rep_aprov_cont_s_num_jus_aprov_ap_cont: Optional[str] = None,
        rep_aprov_cont_s_num_ap_cont: Optional[str] = None,
        rep_aprov_cont_query_source: Optional[str] = None,
        rep_aprov_cont_mapping_name: Optional[str] = None,
        rep_aprov_cont_schema_global: Optional[str] = None,
        rep_aprov_cont_schema_table_view: Optional[str] = None,
        rep_aprov_cont_schema_stored_procedure: Optional[str] = None,
        rep_aprov_cont_not_recommended_connection_connection_string: Optional[str] = None,
        rep_aprov_cont_not_recommended_connection_command_timeout: Optional[int] = None,
        rep_aprov_cont_not_recommended_connection_connection_timeout: Optional[int] = None,
        rep_aprov_cont_not_recommended_connection_default_database: Optional[str] = None,
        rep_aprov_cont_not_recommended_connection_isolation_level: Optional[int] = None,
        rep_aprov_cont_not_recommended_connection_attributes: Optional[int] = None,
        rep_aprov_cont_not_recommended_connection_cursor_location: Optional[int] = None,
        rep_aprov_cont_not_recommended_connection_mode: Optional[int] = None,
        rep_aprov_cont_not_recommended_connection_provider: Optional[str] = None,
        rep_aprov_cont_connection_string: Optional[str] = None,
        rep_aprov_cont_connection_string_config: Optional[str] = None,
        rep_aprov_cont_filter: Optional[str] = None,
        rep_aprov_cont_sort: Optional[str] = None,
        rep_aprov_med_string_format: Optional[str] = None,
        rep_aprov_med_empresa_apmed: Optional[int] = None,
        rep_aprov_med_cod_cont_apmed: Optional[int] = None,
        rep_aprov_med_cod_med_apmed: Optional[int] = None,
        rep_aprov_med_usr_aprov_apmed: Optional[str] = None,
        rep_aprov_med_data_aprov_apmed: Optional[str] = None,
        rep_aprov_med_cod_cargo_apmed: Optional[str] = None,
        rep_aprov_med_cod_dep_apmed: Optional[str] = None,
        rep_aprov_med_num_jus_aprov_apmed: Optional[int] = None,
        rep_aprov_med_num_apmed: Optional[int] = None,
        rep_aprov_med_s_empresa_apmed: Optional[str] = None,
        rep_aprov_med_s_cod_cont_apmed: Optional[str] = None,
        rep_aprov_med_s_cod_med_apmed: Optional[str] = None,
        rep_aprov_med_s_usr_aprov_apmed: Optional[str] = None,
        rep_aprov_med_s_data_aprov_apmed: Optional[str] = None,
        rep_aprov_med_s_cod_cargo_apmed: Optional[str] = None,
        rep_aprov_med_s_cod_dep_apmed: Optional[str] = None,
        rep_aprov_med_s_num_jus_aprov_apmed: Optional[str] = None,
        rep_aprov_med_s_num_apmed: Optional[str] = None,
        rep_aprov_med_query_source: Optional[str] = None,
        rep_aprov_med_mapping_name: Optional[str] = None,
        rep_aprov_med_schema_global: Optional[str] = None,
        rep_aprov_med_schema_table_view: Optional[str] = None,
        rep_aprov_med_schema_stored_procedure: Optional[str] = None,
        rep_aprov_med_not_recommended_connection_connection_string: Optional[str] = None,
        rep_aprov_med_not_recommended_connection_command_timeout: Optional[int] = None,
        rep_aprov_med_not_recommended_connection_connection_timeout: Optional[int] = None,
        rep_aprov_med_not_recommended_connection_default_database: Optional[str] = None,
        rep_aprov_med_not_recommended_connection_isolation_level: Optional[int] = None,
        rep_aprov_med_not_recommended_connection_attributes: Optional[int] = None,
        rep_aprov_med_not_recommended_connection_cursor_location: Optional[int] = None,
        rep_aprov_med_not_recommended_connection_mode: Optional[int] = None,
        rep_aprov_med_not_recommended_connection_provider: Optional[str] = None,
        rep_aprov_med_connection_string: Optional[str] = None,
        rep_aprov_med_connection_string_config: Optional[str] = None,
        rep_aprov_med_filter: Optional[str] = None,
        rep_aprov_med_sort: Optional[str] = None,
        rep_aprov_simula_string_format: Optional[str] = None,
        rep_aprov_simula_empresa_apsim: Optional[int] = None,
        rep_aprov_simula_num_sim_apsim: Optional[int] = None,
        rep_aprov_simula_num_cot_apsim: Optional[int] = None,
        rep_aprov_simula_usr_aprov_apsim: Optional[str] = None,
        rep_aprov_simula_data_aprov_apsim: Optional[str] = None,
        rep_aprov_simula_cod_cargo_apsim: Optional[str] = None,
        rep_aprov_simula_cod_dep_apsim: Optional[str] = None,
        rep_aprov_simula_num_jus_aprov_apsim: Optional[int] = None,
        rep_aprov_simula_num_apsim: Optional[int] = None,
        rep_aprov_simula_s_empresa_apsim: Optional[str] = None,
        rep_aprov_simula_s_num_sim_apsim: Optional[str] = None,
        rep_aprov_simula_s_num_cot_apsim: Optional[str] = None,
        rep_aprov_simula_s_usr_aprov_apsim: Optional[str] = None,
        rep_aprov_simula_s_data_aprov_apsim: Optional[str] = None,
        rep_aprov_simula_s_cod_cargo_apsim: Optional[str] = None,
        rep_aprov_simula_s_cod_dep_apsim: Optional[str] = None,
        rep_aprov_simula_s_num_jus_aprov_apsim: Optional[str] = None,
        rep_aprov_simula_s_num_apsim: Optional[str] = None,
        rep_aprov_simula_query_source: Optional[str] = None,
        rep_aprov_simula_mapping_name: Optional[str] = None,
        rep_aprov_simula_schema_global: Optional[str] = None,
        rep_aprov_simula_schema_table_view: Optional[str] = None,
        rep_aprov_simula_schema_stored_procedure: Optional[str] = None,
        rep_aprov_simula_not_recommended_connection_connection_string: Optional[str] = None,
        rep_aprov_simula_not_recommended_connection_command_timeout: Optional[int] = None,
        rep_aprov_simula_not_recommended_connection_connection_timeout: Optional[int] = None,
        rep_aprov_simula_not_recommended_connection_default_database: Optional[str] = None,
        rep_aprov_simula_not_recommended_connection_isolation_level: Optional[int] = None,
        rep_aprov_simula_not_recommended_connection_attributes: Optional[int] = None,
        rep_aprov_simula_not_recommended_connection_cursor_location: Optional[int] = None,
        rep_aprov_simula_not_recommended_connection_mode: Optional[int] = None,
        rep_aprov_simula_not_recommended_connection_provider: Optional[str] = None,
        rep_aprov_simula_connection_string: Optional[str] = None,
        rep_aprov_simula_connection_string_config: Optional[str] = None,
        rep_aprov_simula_filter: Optional[str] = None,
        rep_aprov_simula_sort: Optional[str] = None,
        rs_aprov_requisicao_compra_sort: Optional[str] = None,
        rep_aprovacoespl_string_format: Optional[str] = None,
        rep_aprovacoespl_num_sap_ap_plan: Optional[int] = None,
        rep_aprovacoespl_usr_aprov_ap_plan: Optional[str] = None,
        rep_aprovacoespl_data_aprov_ap_plan: Optional[str] = None,
        rep_aprovacoespl_cod_cargo_ap_plan: Optional[str] = None,
        rep_aprovacoespl_cod_dep_ap_plan: Optional[str] = None,
        rep_aprovacoespl_num_jus_aprov_ap_plan: Optional[int] = None,
        rep_aprovacoespl_num_ap_plan: Optional[int] = None,
        rep_aprovacoespl_s_num_sap_ap_plan: Optional[str] = None,
        rep_aprovacoespl_s_usr_aprov_ap_plan: Optional[str] = None,
        rep_aprovacoespl_s_data_aprov_ap_plan: Optional[str] = None,
        rep_aprovacoespl_s_cod_cargo_ap_plan: Optional[str] = None,
        rep_aprovacoespl_s_cod_dep_ap_plan: Optional[str] = None,
        rep_aprovacoespl_s_num_jus_aprov_ap_plan: Optional[str] = None,
        rep_aprovacoespl_s_num_ap_plan: Optional[str] = None,
        rep_aprovacoespl_query_source: Optional[str] = None,
        rep_aprovacoespl_mapping_name: Optional[str] = None,
        rep_aprovacoespl_schema_global: Optional[str] = None,
        rep_aprovacoespl_schema_table_view: Optional[str] = None,
        rep_aprovacoespl_schema_stored_procedure: Optional[str] = None,
        rep_aprovacoespl_not_recommended_connection_connection_string: Optional[str] = None,
        rep_aprovacoespl_not_recommended_connection_command_timeout: Optional[int] = None,
        rep_aprovacoespl_not_recommended_connection_connection_timeout: Optional[int] = None,
        rep_aprovacoespl_not_recommended_connection_default_database: Optional[str] = None,
        rep_aprovacoespl_not_recommended_connection_isolation_level: Optional[int] = None,
        rep_aprovacoespl_not_recommended_connection_attributes: Optional[int] = None,
        rep_aprovacoespl_not_recommended_connection_cursor_location: Optional[int] = None,
        rep_aprovacoespl_not_recommended_connection_mode: Optional[int] = None,
        rep_aprovacoespl_not_recommended_connection_provider: Optional[str] = None,
        rep_aprovacoespl_connection_string: Optional[str] = None,
        rep_aprovacoespl_connection_string_config: Optional[str] = None,
        rep_aprovacoespl_filter: Optional[str] = None,
        rep_aprovacoespl_sort: Optional[str] = None,
        rep_ger_aprovacao_mat_string_format: Optional[str] = None,
        rep_ger_aprovacao_mat_empresa_ap_pedm: Optional[int] = None,
        rep_ger_aprovacao_mat_obra_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_insumo_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_num_pedido_ap_pedm: Optional[int] = None,
        rep_ger_aprovacao_mat_item_ped_ap_pedm: Optional[int] = None,
        rep_ger_aprovacao_mat_usr_aprov_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_data_aprov_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_cod_cargo_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_cod_dep_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_num_jus_aprov_ap_pedm: Optional[int] = None,
        rep_ger_aprovacao_mat_num_ap_pedm: Optional[int] = None,
        rep_ger_aprovacao_mat_s_empresa_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_obra_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_insumo_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_num_pedido_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_item_ped_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_usr_aprov_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_data_aprov_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_cod_cargo_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_cod_dep_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_num_jus_aprov_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_s_num_ap_pedm: Optional[str] = None,
        rep_ger_aprovacao_mat_query_source: Optional[str] = None,
        rep_ger_aprovacao_mat_mapping_name: Optional[str] = None,
        rep_ger_aprovacao_mat_schema_global: Optional[str] = None,
        rep_ger_aprovacao_mat_schema_table_view: Optional[str] = None,
        rep_ger_aprovacao_mat_schema_stored_procedure: Optional[str] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_connection_string: Optional[str] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_command_timeout: Optional[int] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_connection_timeout: Optional[int] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_default_database: Optional[str] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_isolation_level: Optional[int] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_attributes: Optional[int] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_cursor_location: Optional[int] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_mode: Optional[int] = None,
        rep_ger_aprovacao_mat_not_recommended_connection_provider: Optional[str] = None,
        rep_ger_aprovacao_mat_connection_string: Optional[str] = None,
        rep_ger_aprovacao_mat_connection_string_config: Optional[str] = None,
        rep_ger_aprovacao_mat_filter: Optional[str] = None,
        rep_ger_aprovacao_mat_sort: Optional[str] = None,
        rep_ger_aprovacao_serv_string_format: Optional[str] = None,
        rep_ger_aprovacao_serv_num_pedido_ap_peds: Optional[int] = None,
        rep_ger_aprovacao_serv_empresa_ap_peds: Optional[int] = None,
        rep_ger_aprovacao_serv_obra_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_serv_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_usr_aprov_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_data_aprov_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_cod_cargo_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_cod_dep_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_num_jus_aprov_ap_peds: Optional[int] = None,
        rep_ger_aprovacao_serv_num_ap_peds: Optional[int] = None,
        rep_ger_aprovacao_serv_s_num_pedido_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_empresa_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_obra_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_serv_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_usr_aprov_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_data_aprov_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_cod_cargo_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_cod_dep_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_num_jus_aprov_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_s_num_ap_peds: Optional[str] = None,
        rep_ger_aprovacao_serv_query_source: Optional[str] = None,
        rep_ger_aprovacao_serv_mapping_name: Optional[str] = None,
        rep_ger_aprovacao_serv_schema_global: Optional[str] = None,
        rep_ger_aprovacao_serv_schema_table_view: Optional[str] = None,
        rep_ger_aprovacao_serv_schema_stored_procedure: Optional[str] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_connection_string: Optional[str] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_command_timeout: Optional[int] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_connection_timeout: Optional[int] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_default_database: Optional[str] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_isolation_level: Optional[int] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_attributes: Optional[int] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_cursor_location: Optional[int] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_mode: Optional[int] = None,
        rep_ger_aprovacao_serv_not_recommended_connection_provider: Optional[str] = None,
        rep_ger_aprovacao_serv_connection_string: Optional[str] = None,
        rep_ger_aprovacao_serv_connection_string_config: Optional[str] = None,
        rep_ger_aprovacao_serv_filter: Optional[str] = None,
        rep_ger_aprovacao_serv_sort: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            intNumAprov (Dict[str, Any]): The num aprov
            tipoAprovacao (Dict[str, Any]): The aprovacao
            tipoPedido (Dict[str, Any]): The pedido
            api-version (Dict[str, Any]): The api-version
            gerAprov._listaEstruturaDeAprovacao (Dict[str, Any]): The aprov._lista estrutura de aprovacao
            gerAprov.codigoDaEmpresa (Dict[str, Any]): The aprov.codigo da empresa
            gerAprov.codigoDaObra (Dict[str, Any]): The aprov.codigo da obra
            gerAprov.tipoDoProcesso (Dict[str, Any]): The aprov.tipo do processo
            gerAprov.quantidadeAprovacao (Dict[str, Any]): The aprov.quantidade aprovacao
            gerAprov.valorSolicitado (Dict[str, Any]): The aprov.valor solicitado
            gerAprov.usuarioLogado (Dict[str, Any]): The aprov.usuario logado
            gerAprov.acao (Dict[str, Any]): The aprov.acao
            gerAprov.estruturaAprovacao (Dict[str, Any]): The aprov.estrutura aprovacao
            gerAprov.estruturaAprovFaixaValor (Dict[str, Any]): The aprov.estrutura aprov faixa valor
            gerAprov.codigoDepartamento (Dict[str, Any]): The aprov.codigo departamento
            gerAprov.codigoCargo (Dict[str, Any]): The aprov.codigo cargo
            gerAprov.listaSeqPendAprovAbaixoSeqUsuarioLog (Dict[str, Any]): The aprov.lista seq pend aprov abaixo seq usuario log
            gerAprov.isAprovForaSequencia (Dict[str, Any]): The aprov.is aprov fora sequencia
            gerAprov.chaveJustificativaAprovacao (Dict[str, Any]): The aprov.chave justificativa aprovacao
            repAprovSimulaConf.stringFormat (Dict[str, Any]): The aprov simula conf.string format
            repAprovSimulaConf.empresa_apSC (Dict[str, Any]): The aprov simula conf.empresa_ap s c
            repAprovSimulaConf.obra_apSC (Dict[str, Any]): The aprov simula conf.obra_ap s c
            repAprovSimulaConf.numeroSim_apSC (Dict[str, Any]): The aprov simula conf.numero sim_ap s c
            repAprovSimulaConf.numCot_apSC (Dict[str, Any]): The aprov simula conf.num cot_ap s c
            repAprovSimulaConf.usrAprov_apSC (Dict[str, Any]): The aprov simula conf.usr aprov_ap s c
            repAprovSimulaConf.dataAprov_apSC (Dict[str, Any]): The aprov simula conf.data aprov_ap s c
            repAprovSimulaConf.codCargo_ApSC (Dict[str, Any]): The aprov simula conf.cod cargo_ ap s c
            repAprovSimulaConf.codDep_ApSC (Dict[str, Any]): The aprov simula conf.cod dep_ ap s c
            repAprovSimulaConf.numJusAprov_apSC (Dict[str, Any]): The aprov simula conf.num jus aprov_ap s c
            repAprovSimulaConf.num_apSC (Dict[str, Any]): The aprov simula conf.num_ap s c
            repAprovSimulaConf.s_Empresa_apSC (Dict[str, Any]): The aprov simula conf.s_ empresa_ap s c
            repAprovSimulaConf.s_Obra_apSC (Dict[str, Any]): The aprov simula conf.s_ obra_ap s c
            repAprovSimulaConf.s_NumeroSim_apSC (Dict[str, Any]): The aprov simula conf.s_ numero sim_ap s c
            repAprovSimulaConf.s_NumCot_apSC (Dict[str, Any]): The aprov simula conf.s_ num cot_ap s c
            repAprovSimulaConf.s_UsrAprov_apSC (Dict[str, Any]): The aprov simula conf.s_ usr aprov_ap s c
            repAprovSimulaConf.s_DataAprov_apSC (Dict[str, Any]): The aprov simula conf.s_ data aprov_ap s c
            repAprovSimulaConf.s_CodCargo_ApSC (Dict[str, Any]): The aprov simula conf.s_ cod cargo_ ap s c
            repAprovSimulaConf.s_CodDep_ApSC (Dict[str, Any]): The aprov simula conf.s_ cod dep_ ap s c
            repAprovSimulaConf.s_NumJusAprov_apSC (Dict[str, Any]): The aprov simula conf.s_ num jus aprov_ap s c
            repAprovSimulaConf.s_Num_apSC (Dict[str, Any]): The aprov simula conf.s_ num_ap s c
            repAprovSimulaConf.querySource (Dict[str, Any]): The aprov simula conf.query source
            repAprovSimulaConf.mappingName (Dict[str, Any]): The aprov simula conf.mapping name
            repAprovSimulaConf.schemaGlobal (Dict[str, Any]): The aprov simula conf.schema global
            repAprovSimulaConf.schemaTableView (Dict[str, Any]): The aprov simula conf.schema table view
            repAprovSimulaConf.schemaStoredProcedure (Dict[str, Any]): The aprov simula conf.schema stored procedure
            repAprovSimulaConf.notRecommendedConnection.connectionString (Dict[str, Any]): The aprov simula conf.not recommended connection.connection string
            repAprovSimulaConf.notRecommendedConnection.commandTimeout (Dict[str, Any]): The aprov simula conf.not recommended connection.command timeout
            repAprovSimulaConf.notRecommendedConnection.connectionTimeout (Dict[str, Any]): The aprov simula conf.not recommended connection.connection timeout
            repAprovSimulaConf.notRecommendedConnection.defaultDatabase (Dict[str, Any]): The aprov simula conf.not recommended connection.default database
            repAprovSimulaConf.notRecommendedConnection.isolationLevel (Dict[str, Any]): The aprov simula conf.not recommended connection.isolation level
            repAprovSimulaConf.notRecommendedConnection.attributes (Dict[str, Any]): The aprov simula conf.not recommended connection.attributes
            repAprovSimulaConf.notRecommendedConnection.cursorLocation (Dict[str, Any]): The aprov simula conf.not recommended connection.cursor location
            repAprovSimulaConf.notRecommendedConnection.mode (Dict[str, Any]): The aprov simula conf.not recommended connection.mode
            repAprovSimulaConf.notRecommendedConnection.provider (Dict[str, Any]): The aprov simula conf.not recommended connection.provider
            repAprovSimulaConf.connectionString (Dict[str, Any]): The aprov simula conf.connection string
            repAprovSimulaConf.connectionStringConfig (Dict[str, Any]): The aprov simula conf.connection string config
            repAprovSimulaConf.filter (Dict[str, Any]): The aprov simula conf.filter
            repAprovSimulaConf.sort (Dict[str, Any]): The aprov simula conf.sort
            repAprovCont.stringFormat (Dict[str, Any]): The aprov cont.string format
            repAprovCont.empresa_ApCont (Dict[str, Any]): The aprov cont.empresa_ ap cont
            repAprovCont.codCont_ApCont (Dict[str, Any]): The aprov cont.cod cont_ ap cont
            repAprovCont.usrAprov_ApCont (Dict[str, Any]): The aprov cont.usr aprov_ ap cont
            repAprovCont.dataAprov_ApCont (Dict[str, Any]): The aprov cont.data aprov_ ap cont
            repAprovCont.codCargo_ApCont (Dict[str, Any]): The aprov cont.cod cargo_ ap cont
            repAprovCont.codDep_ApCont (Dict[str, Any]): The aprov cont.cod dep_ ap cont
            repAprovCont.numJusAprov_ApCont (Dict[str, Any]): The aprov cont.num jus aprov_ ap cont
            repAprovCont.num_ApCont (Dict[str, Any]): The aprov cont.num_ ap cont
            repAprovCont.s_Empresa_ApCont (Dict[str, Any]): The aprov cont.s_ empresa_ ap cont
            repAprovCont.s_CodCont_ApCont (Dict[str, Any]): The aprov cont.s_ cod cont_ ap cont
            repAprovCont.s_UsrAprov_ApCont (Dict[str, Any]): The aprov cont.s_ usr aprov_ ap cont
            repAprovCont.s_DataAprov_ApCont (Dict[str, Any]): The aprov cont.s_ data aprov_ ap cont
            repAprovCont.s_CodCargo_ApCont (Dict[str, Any]): The aprov cont.s_ cod cargo_ ap cont
            repAprovCont.s_CodDep_ApCont (Dict[str, Any]): The aprov cont.s_ cod dep_ ap cont
            repAprovCont.s_NumJusAprov_ApCont (Dict[str, Any]): The aprov cont.s_ num jus aprov_ ap cont
            repAprovCont.s_Num_ApCont (Dict[str, Any]): The aprov cont.s_ num_ ap cont
            repAprovCont.querySource (Dict[str, Any]): The aprov cont.query source
            repAprovCont.mappingName (Dict[str, Any]): The aprov cont.mapping name
            repAprovCont.schemaGlobal (Dict[str, Any]): The aprov cont.schema global
            repAprovCont.schemaTableView (Dict[str, Any]): The aprov cont.schema table view
            repAprovCont.schemaStoredProcedure (Dict[str, Any]): The aprov cont.schema stored procedure
            repAprovCont.notRecommendedConnection.connectionString (Dict[str, Any]): The aprov cont.not recommended connection.connection string
            repAprovCont.notRecommendedConnection.commandTimeout (Dict[str, Any]): The aprov cont.not recommended connection.command timeout
            repAprovCont.notRecommendedConnection.connectionTimeout (Dict[str, Any]): The aprov cont.not recommended connection.connection timeout
            repAprovCont.notRecommendedConnection.defaultDatabase (Dict[str, Any]): The aprov cont.not recommended connection.default database
            repAprovCont.notRecommendedConnection.isolationLevel (Dict[str, Any]): The aprov cont.not recommended connection.isolation level
            repAprovCont.notRecommendedConnection.attributes (Dict[str, Any]): The aprov cont.not recommended connection.attributes
            repAprovCont.notRecommendedConnection.cursorLocation (Dict[str, Any]): The aprov cont.not recommended connection.cursor location
            repAprovCont.notRecommendedConnection.mode (Dict[str, Any]): The aprov cont.not recommended connection.mode
            repAprovCont.notRecommendedConnection.provider (Dict[str, Any]): The aprov cont.not recommended connection.provider
            repAprovCont.connectionString (Dict[str, Any]): The aprov cont.connection string
            repAprovCont.connectionStringConfig (Dict[str, Any]): The aprov cont.connection string config
            repAprovCont.filter (Dict[str, Any]): The aprov cont.filter
            repAprovCont.sort (Dict[str, Any]): The aprov cont.sort
            repAprovMed.stringFormat (Dict[str, Any]): The aprov med.string format
            repAprovMed.empresa_apmed (Dict[str, Any]): The aprov med.empresa_apmed
            repAprovMed.codCont_apmed (Dict[str, Any]): The aprov med.cod cont_apmed
            repAprovMed.codMed_apmed (Dict[str, Any]): The aprov med.cod med_apmed
            repAprovMed.usrAprov_apmed (Dict[str, Any]): The aprov med.usr aprov_apmed
            repAprovMed.dataAprov_apmed (Dict[str, Any]): The aprov med.data aprov_apmed
            repAprovMed.codCargo_apmed (Dict[str, Any]): The aprov med.cod cargo_apmed
            repAprovMed.codDep_apmed (Dict[str, Any]): The aprov med.cod dep_apmed
            repAprovMed.numJusAprov_apmed (Dict[str, Any]): The aprov med.num jus aprov_apmed
            repAprovMed.num_apmed (Dict[str, Any]): The aprov med.num_apmed
            repAprovMed.s_Empresa_apmed (Dict[str, Any]): The aprov med.s_ empresa_apmed
            repAprovMed.s_CodCont_apmed (Dict[str, Any]): The aprov med.s_ cod cont_apmed
            repAprovMed.s_CodMed_apmed (Dict[str, Any]): The aprov med.s_ cod med_apmed
            repAprovMed.s_UsrAprov_apmed (Dict[str, Any]): The aprov med.s_ usr aprov_apmed
            repAprovMed.s_DataAprov_apmed (Dict[str, Any]): The aprov med.s_ data aprov_apmed
            repAprovMed.s_CodCargo_apmed (Dict[str, Any]): The aprov med.s_ cod cargo_apmed
            repAprovMed.s_CodDep_apmed (Dict[str, Any]): The aprov med.s_ cod dep_apmed
            repAprovMed.s_NumJusAprov_apmed (Dict[str, Any]): The aprov med.s_ num jus aprov_apmed
            repAprovMed.s_Num_apmed (Dict[str, Any]): The aprov med.s_ num_apmed
            repAprovMed.querySource (Dict[str, Any]): The aprov med.query source
            repAprovMed.mappingName (Dict[str, Any]): The aprov med.mapping name
            repAprovMed.schemaGlobal (Dict[str, Any]): The aprov med.schema global
            repAprovMed.schemaTableView (Dict[str, Any]): The aprov med.schema table view
            repAprovMed.schemaStoredProcedure (Dict[str, Any]): The aprov med.schema stored procedure
            repAprovMed.notRecommendedConnection.connectionString (Dict[str, Any]): The aprov med.not recommended connection.connection string
            repAprovMed.notRecommendedConnection.commandTimeout (Dict[str, Any]): The aprov med.not recommended connection.command timeout
            repAprovMed.notRecommendedConnection.connectionTimeout (Dict[str, Any]): The aprov med.not recommended connection.connection timeout
            repAprovMed.notRecommendedConnection.defaultDatabase (Dict[str, Any]): The aprov med.not recommended connection.default database
            repAprovMed.notRecommendedConnection.isolationLevel (Dict[str, Any]): The aprov med.not recommended connection.isolation level
            repAprovMed.notRecommendedConnection.attributes (Dict[str, Any]): The aprov med.not recommended connection.attributes
            repAprovMed.notRecommendedConnection.cursorLocation (Dict[str, Any]): The aprov med.not recommended connection.cursor location
            repAprovMed.notRecommendedConnection.mode (Dict[str, Any]): The aprov med.not recommended connection.mode
            repAprovMed.notRecommendedConnection.provider (Dict[str, Any]): The aprov med.not recommended connection.provider
            repAprovMed.connectionString (Dict[str, Any]): The aprov med.connection string
            repAprovMed.connectionStringConfig (Dict[str, Any]): The aprov med.connection string config
            repAprovMed.filter (Dict[str, Any]): The aprov med.filter
            repAprovMed.sort (Dict[str, Any]): The aprov med.sort
            repAprovSimula.stringFormat (Dict[str, Any]): The aprov simula.string format
            repAprovSimula.empresa_apsim (Dict[str, Any]): The aprov simula.empresa_apsim
            repAprovSimula.numSim_apsim (Dict[str, Any]): The aprov simula.num sim_apsim
            repAprovSimula.numCot_apsim (Dict[str, Any]): The aprov simula.num cot_apsim
            repAprovSimula.usrAprov_apsim (Dict[str, Any]): The aprov simula.usr aprov_apsim
            repAprovSimula.dataAprov_apsim (Dict[str, Any]): The aprov simula.data aprov_apsim
            repAprovSimula.codCargo_apsim (Dict[str, Any]): The aprov simula.cod cargo_apsim
            repAprovSimula.codDep_apsim (Dict[str, Any]): The aprov simula.cod dep_apsim
            repAprovSimula.numJusAprov_apsim (Dict[str, Any]): The aprov simula.num jus aprov_apsim
            repAprovSimula.num_apsim (Dict[str, Any]): The aprov simula.num_apsim
            repAprovSimula.s_Empresa_apsim (Dict[str, Any]): The aprov simula.s_ empresa_apsim
            repAprovSimula.s_NumSim_apsim (Dict[str, Any]): The aprov simula.s_ num sim_apsim
            repAprovSimula.s_NumCot_apsim (Dict[str, Any]): The aprov simula.s_ num cot_apsim
            repAprovSimula.s_UsrAprov_apsim (Dict[str, Any]): The aprov simula.s_ usr aprov_apsim
            repAprovSimula.s_DataAprov_apsim (Dict[str, Any]): The aprov simula.s_ data aprov_apsim
            repAprovSimula.s_CodCargo_apsim (Dict[str, Any]): The aprov simula.s_ cod cargo_apsim
            repAprovSimula.s_CodDep_apsim (Dict[str, Any]): The aprov simula.s_ cod dep_apsim
            repAprovSimula.s_NumJusAprov_apsim (Dict[str, Any]): The aprov simula.s_ num jus aprov_apsim
            repAprovSimula.s_Num_apsim (Dict[str, Any]): The aprov simula.s_ num_apsim
            repAprovSimula.querySource (Dict[str, Any]): The aprov simula.query source
            repAprovSimula.mappingName (Dict[str, Any]): The aprov simula.mapping name
            repAprovSimula.schemaGlobal (Dict[str, Any]): The aprov simula.schema global
            repAprovSimula.schemaTableView (Dict[str, Any]): The aprov simula.schema table view
            repAprovSimula.schemaStoredProcedure (Dict[str, Any]): The aprov simula.schema stored procedure
            repAprovSimula.notRecommendedConnection.connectionString (Dict[str, Any]): The aprov simula.not recommended connection.connection string
            repAprovSimula.notRecommendedConnection.commandTimeout (Dict[str, Any]): The aprov simula.not recommended connection.command timeout
            repAprovSimula.notRecommendedConnection.connectionTimeout (Dict[str, Any]): The aprov simula.not recommended connection.connection timeout
            repAprovSimula.notRecommendedConnection.defaultDatabase (Dict[str, Any]): The aprov simula.not recommended connection.default database
            repAprovSimula.notRecommendedConnection.isolationLevel (Dict[str, Any]): The aprov simula.not recommended connection.isolation level
            repAprovSimula.notRecommendedConnection.attributes (Dict[str, Any]): The aprov simula.not recommended connection.attributes
            repAprovSimula.notRecommendedConnection.cursorLocation (Dict[str, Any]): The aprov simula.not recommended connection.cursor location
            repAprovSimula.notRecommendedConnection.mode (Dict[str, Any]): The aprov simula.not recommended connection.mode
            repAprovSimula.notRecommendedConnection.provider (Dict[str, Any]): The aprov simula.not recommended connection.provider
            repAprovSimula.connectionString (Dict[str, Any]): The aprov simula.connection string
            repAprovSimula.connectionStringConfig (Dict[str, Any]): The aprov simula.connection string config
            repAprovSimula.filter (Dict[str, Any]): The aprov simula.filter
            repAprovSimula.sort (Dict[str, Any]): The aprov simula.sort
            rsAprovRequisicaoCompra.sort (Dict[str, Any]): The aprov requisicao compra.sort
            repAprovacoesPL.stringFormat (Dict[str, Any]): The aprovacoes p l.string format
            repAprovacoesPL.numSap_ApPlan (Dict[str, Any]): The aprovacoes p l.num sap_ ap plan
            repAprovacoesPL.usrAprov_ApPlan (Dict[str, Any]): The aprovacoes p l.usr aprov_ ap plan
            repAprovacoesPL.dataAprov_ApPlan (Dict[str, Any]): The aprovacoes p l.data aprov_ ap plan
            repAprovacoesPL.codCargo_ApPlan (Dict[str, Any]): The aprovacoes p l.cod cargo_ ap plan
            repAprovacoesPL.codDep_ApPlan (Dict[str, Any]): The aprovacoes p l.cod dep_ ap plan
            repAprovacoesPL.numJusAprov_ApPlan (Dict[str, Any]): The aprovacoes p l.num jus aprov_ ap plan
            repAprovacoesPL.num_ApPlan (Dict[str, Any]): The aprovacoes p l.num_ ap plan
            repAprovacoesPL.s_NumSap_ApPlan (Dict[str, Any]): The aprovacoes p l.s_ num sap_ ap plan
            repAprovacoesPL.s_UsrAprov_ApPlan (Dict[str, Any]): The aprovacoes p l.s_ usr aprov_ ap plan
            repAprovacoesPL.s_DataAprov_ApPlan (Dict[str, Any]): The aprovacoes p l.s_ data aprov_ ap plan
            repAprovacoesPL.s_CodCargo_ApPlan (Dict[str, Any]): The aprovacoes p l.s_ cod cargo_ ap plan
            repAprovacoesPL.s_CodDep_ApPlan (Dict[str, Any]): The aprovacoes p l.s_ cod dep_ ap plan
            repAprovacoesPL.s_NumJusAprov_ApPlan (Dict[str, Any]): The aprovacoes p l.s_ num jus aprov_ ap plan
            repAprovacoesPL.s_Num_ApPlan (Dict[str, Any]): The aprovacoes p l.s_ num_ ap plan
            repAprovacoesPL.querySource (Dict[str, Any]): The aprovacoes p l.query source
            repAprovacoesPL.mappingName (Dict[str, Any]): The aprovacoes p l.mapping name
            repAprovacoesPL.schemaGlobal (Dict[str, Any]): The aprovacoes p l.schema global
            repAprovacoesPL.schemaTableView (Dict[str, Any]): The aprovacoes p l.schema table view
            repAprovacoesPL.schemaStoredProcedure (Dict[str, Any]): The aprovacoes p l.schema stored procedure
            repAprovacoesPL.notRecommendedConnection.connectionString (Dict[str, Any]): The aprovacoes p l.not recommended connection.connection string
            repAprovacoesPL.notRecommendedConnection.commandTimeout (Dict[str, Any]): The aprovacoes p l.not recommended connection.command timeout
            repAprovacoesPL.notRecommendedConnection.connectionTimeout (Dict[str, Any]): The aprovacoes p l.not recommended connection.connection timeout
            repAprovacoesPL.notRecommendedConnection.defaultDatabase (Dict[str, Any]): The aprovacoes p l.not recommended connection.default database
            repAprovacoesPL.notRecommendedConnection.isolationLevel (Dict[str, Any]): The aprovacoes p l.not recommended connection.isolation level
            repAprovacoesPL.notRecommendedConnection.attributes (Dict[str, Any]): The aprovacoes p l.not recommended connection.attributes
            repAprovacoesPL.notRecommendedConnection.cursorLocation (Dict[str, Any]): The aprovacoes p l.not recommended connection.cursor location
            repAprovacoesPL.notRecommendedConnection.mode (Dict[str, Any]): The aprovacoes p l.not recommended connection.mode
            repAprovacoesPL.notRecommendedConnection.provider (Dict[str, Any]): The aprovacoes p l.not recommended connection.provider
            repAprovacoesPL.connectionString (Dict[str, Any]): The aprovacoes p l.connection string
            repAprovacoesPL.connectionStringConfig (Dict[str, Any]): The aprovacoes p l.connection string config
            repAprovacoesPL.filter (Dict[str, Any]): The aprovacoes p l.filter
            repAprovacoesPL.sort (Dict[str, Any]): The aprovacoes p l.sort
            repGerAprovacaoMat.stringFormat (Dict[str, Any]): The ger aprovacao mat.string format
            repGerAprovacaoMat.empresa_ApPedM (Dict[str, Any]): The ger aprovacao mat.empresa_ ap ped m
            repGerAprovacaoMat.obra_ApPedM (Dict[str, Any]): The ger aprovacao mat.obra_ ap ped m
            repGerAprovacaoMat.insumo_ApPedM (Dict[str, Any]): The ger aprovacao mat.insumo_ ap ped m
            repGerAprovacaoMat.numPedido_ApPedM (Dict[str, Any]): The ger aprovacao mat.num pedido_ ap ped m
            repGerAprovacaoMat.itemPed_ApPedM (Dict[str, Any]): The ger aprovacao mat.item ped_ ap ped m
            repGerAprovacaoMat.usrAprov_ApPedM (Dict[str, Any]): The ger aprovacao mat.usr aprov_ ap ped m
            repGerAprovacaoMat.dataAprov_ApPedM (Dict[str, Any]): The ger aprovacao mat.data aprov_ ap ped m
            repGerAprovacaoMat.codCargo_ApPedM (Dict[str, Any]): The ger aprovacao mat.cod cargo_ ap ped m
            repGerAprovacaoMat.codDep_ApPedM (Dict[str, Any]): The ger aprovacao mat.cod dep_ ap ped m
            repGerAprovacaoMat.numJusAprov_ApPedM (Dict[str, Any]): The ger aprovacao mat.num jus aprov_ ap ped m
            repGerAprovacaoMat.num_ApPedM (Dict[str, Any]): The ger aprovacao mat.num_ ap ped m
            repGerAprovacaoMat.s_Empresa_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ empresa_ ap ped m
            repGerAprovacaoMat.s_Obra_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ obra_ ap ped m
            repGerAprovacaoMat.s_Insumo_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ insumo_ ap ped m
            repGerAprovacaoMat.s_NumPedido_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ num pedido_ ap ped m
            repGerAprovacaoMat.s_ItemPed_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ item ped_ ap ped m
            repGerAprovacaoMat.s_UsrAprov_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ usr aprov_ ap ped m
            repGerAprovacaoMat.s_DataAprov_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ data aprov_ ap ped m
            repGerAprovacaoMat.s_CodCargo_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ cod cargo_ ap ped m
            repGerAprovacaoMat.s_CodDep_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ cod dep_ ap ped m
            repGerAprovacaoMat.s_NumJusAprov_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ num jus aprov_ ap ped m
            repGerAprovacaoMat.s_Num_ApPedM (Dict[str, Any]): The ger aprovacao mat.s_ num_ ap ped m
            repGerAprovacaoMat.querySource (Dict[str, Any]): The ger aprovacao mat.query source
            repGerAprovacaoMat.mappingName (Dict[str, Any]): The ger aprovacao mat.mapping name
            repGerAprovacaoMat.schemaGlobal (Dict[str, Any]): The ger aprovacao mat.schema global
            repGerAprovacaoMat.schemaTableView (Dict[str, Any]): The ger aprovacao mat.schema table view
            repGerAprovacaoMat.schemaStoredProcedure (Dict[str, Any]): The ger aprovacao mat.schema stored procedure
            repGerAprovacaoMat.notRecommendedConnection.connectionString (Dict[str, Any]): The ger aprovacao mat.not recommended connection.connection string
            repGerAprovacaoMat.notRecommendedConnection.commandTimeout (Dict[str, Any]): The ger aprovacao mat.not recommended connection.command timeout
            repGerAprovacaoMat.notRecommendedConnection.connectionTimeout (Dict[str, Any]): The ger aprovacao mat.not recommended connection.connection timeout
            repGerAprovacaoMat.notRecommendedConnection.defaultDatabase (Dict[str, Any]): The ger aprovacao mat.not recommended connection.default database
            repGerAprovacaoMat.notRecommendedConnection.isolationLevel (Dict[str, Any]): The ger aprovacao mat.not recommended connection.isolation level
            repGerAprovacaoMat.notRecommendedConnection.attributes (Dict[str, Any]): The ger aprovacao mat.not recommended connection.attributes
            repGerAprovacaoMat.notRecommendedConnection.cursorLocation (Dict[str, Any]): The ger aprovacao mat.not recommended connection.cursor location
            repGerAprovacaoMat.notRecommendedConnection.mode (Dict[str, Any]): The ger aprovacao mat.not recommended connection.mode
            repGerAprovacaoMat.notRecommendedConnection.provider (Dict[str, Any]): The ger aprovacao mat.not recommended connection.provider
            repGerAprovacaoMat.connectionString (Dict[str, Any]): The ger aprovacao mat.connection string
            repGerAprovacaoMat.connectionStringConfig (Dict[str, Any]): The ger aprovacao mat.connection string config
            repGerAprovacaoMat.filter (Dict[str, Any]): The ger aprovacao mat.filter
            repGerAprovacaoMat.sort (Dict[str, Any]): The ger aprovacao mat.sort
            repGerAprovacaoServ.stringFormat (Dict[str, Any]): The ger aprovacao serv.string format
            repGerAprovacaoServ.numPedido_ApPedS (Dict[str, Any]): The ger aprovacao serv.num pedido_ ap ped s
            repGerAprovacaoServ.empresa_ApPedS (Dict[str, Any]): The ger aprovacao serv.empresa_ ap ped s
            repGerAprovacaoServ.obra_ApPedS (Dict[str, Any]): The ger aprovacao serv.obra_ ap ped s
            repGerAprovacaoServ.serv_ApPedS (Dict[str, Any]): The ger aprovacao serv.serv_ ap ped s
            repGerAprovacaoServ.usrAprov_ApPedS (Dict[str, Any]): The ger aprovacao serv.usr aprov_ ap ped s
            repGerAprovacaoServ.dataAprov_ApPedS (Dict[str, Any]): The ger aprovacao serv.data aprov_ ap ped s
            repGerAprovacaoServ.codCargo_ApPedS (Dict[str, Any]): The ger aprovacao serv.cod cargo_ ap ped s
            repGerAprovacaoServ.codDep_ApPedS (Dict[str, Any]): The ger aprovacao serv.cod dep_ ap ped s
            repGerAprovacaoServ.numJusAprov_ApPedS (Dict[str, Any]): The ger aprovacao serv.num jus aprov_ ap ped s
            repGerAprovacaoServ.num_ApPedS (Dict[str, Any]): The ger aprovacao serv.num_ ap ped s
            repGerAprovacaoServ.s_NumPedido_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ num pedido_ ap ped s
            repGerAprovacaoServ.s_Empresa_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ empresa_ ap ped s
            repGerAprovacaoServ.s_Obra_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ obra_ ap ped s
            repGerAprovacaoServ.s_Serv_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ serv_ ap ped s
            repGerAprovacaoServ.s_UsrAprov_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ usr aprov_ ap ped s
            repGerAprovacaoServ.s_DataAprov_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ data aprov_ ap ped s
            repGerAprovacaoServ.s_CodCargo_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ cod cargo_ ap ped s
            repGerAprovacaoServ.s_CodDep_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ cod dep_ ap ped s
            repGerAprovacaoServ.s_NumJusAprov_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ num jus aprov_ ap ped s
            repGerAprovacaoServ.s_Num_ApPedS (Dict[str, Any]): The ger aprovacao serv.s_ num_ ap ped s
            repGerAprovacaoServ.querySource (Dict[str, Any]): The ger aprovacao serv.query source
            repGerAprovacaoServ.mappingName (Dict[str, Any]): The ger aprovacao serv.mapping name
            repGerAprovacaoServ.schemaGlobal (Dict[str, Any]): The ger aprovacao serv.schema global
            repGerAprovacaoServ.schemaTableView (Dict[str, Any]): The ger aprovacao serv.schema table view
            repGerAprovacaoServ.schemaStoredProcedure (Dict[str, Any]): The ger aprovacao serv.schema stored procedure
            repGerAprovacaoServ.notRecommendedConnection.connectionString (Dict[str, Any]): The ger aprovacao serv.not recommended connection.connection string
            repGerAprovacaoServ.notRecommendedConnection.commandTimeout (Dict[str, Any]): The ger aprovacao serv.not recommended connection.command timeout
            repGerAprovacaoServ.notRecommendedConnection.connectionTimeout (Dict[str, Any]): The ger aprovacao serv.not recommended connection.connection timeout
            repGerAprovacaoServ.notRecommendedConnection.defaultDatabase (Dict[str, Any]): The ger aprovacao serv.not recommended connection.default database
            repGerAprovacaoServ.notRecommendedConnection.isolationLevel (Dict[str, Any]): The ger aprovacao serv.not recommended connection.isolation level
            repGerAprovacaoServ.notRecommendedConnection.attributes (Dict[str, Any]): The ger aprovacao serv.not recommended connection.attributes
            repGerAprovacaoServ.notRecommendedConnection.cursorLocation (Dict[str, Any]): The ger aprovacao serv.not recommended connection.cursor location
            repGerAprovacaoServ.notRecommendedConnection.mode (Dict[str, Any]): The ger aprovacao serv.not recommended connection.mode
            repGerAprovacaoServ.notRecommendedConnection.provider (Dict[str, Any]): The ger aprovacao serv.not recommended connection.provider
            repGerAprovacaoServ.connectionString (Dict[str, Any]): The ger aprovacao serv.connection string
            repGerAprovacaoServ.connectionStringConfig (Dict[str, Any]): The ger aprovacao serv.connection string config
            repGerAprovacaoServ.filter (Dict[str, Any]): The ger aprovacao serv.filter
            repGerAprovacaoServ.sort (Dict[str, Any]): The ger aprovacao serv.sort
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "intNumAprov": {
                    "type": "integer",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "tipoAprovacao": {
                    "type": "integer",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "tipoPedido": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "api-version": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov._listaEstruturaDeAprovacao": {
                    "type": "array",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.codigoDaEmpresa": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.codigoDaObra": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.tipoDoProcesso": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.quantidadeAprovacao": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.valorSolicitado": {
                    "type": "number",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.usuarioLogado": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.acao": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.estruturaAprovacao": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.estruturaAprovFaixaValor": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.codigoDepartamento": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.codigoCargo": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.listaSeqPendAprovAbaixoSeqUsuarioLog": {
                    "type": "array",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.isAprovForaSequencia": {
                    "type": "boolean",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "gerAprov.chaveJustificativaAprovacao": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.stringFormat": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.empresa_apSC": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.obra_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.numeroSim_apSC": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.numCot_apSC": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.usrAprov_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.dataAprov_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.codCargo_ApSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.codDep_ApSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.numJusAprov_apSC": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.num_apSC": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_Empresa_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_Obra_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_NumeroSim_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_NumCot_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_UsrAprov_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_DataAprov_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_CodCargo_ApSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_CodDep_ApSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_NumJusAprov_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.s_Num_apSC": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.querySource": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.mappingName": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.schemaGlobal": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.schemaTableView": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.schemaStoredProcedure": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.commandTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.connectionTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.defaultDatabase": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.isolationLevel": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.attributes": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.cursorLocation": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.mode": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.notRecommendedConnection.provider": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.connectionStringConfig": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.filter": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimulaConf.sort": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.stringFormat": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.empresa_ApCont": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.codCont_ApCont": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.usrAprov_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.dataAprov_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.codCargo_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.codDep_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.numJusAprov_ApCont": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.num_ApCont": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_Empresa_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_CodCont_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_UsrAprov_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_DataAprov_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_CodCargo_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_CodDep_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_NumJusAprov_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.s_Num_ApCont": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.querySource": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.mappingName": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.schemaGlobal": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.schemaTableView": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.schemaStoredProcedure": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.commandTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.connectionTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.defaultDatabase": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.isolationLevel": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.attributes": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.cursorLocation": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.mode": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.notRecommendedConnection.provider": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.connectionStringConfig": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.filter": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovCont.sort": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.stringFormat": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.empresa_apmed": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.codCont_apmed": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.codMed_apmed": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.usrAprov_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.dataAprov_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.codCargo_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.codDep_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.numJusAprov_apmed": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.num_apmed": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_Empresa_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_CodCont_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_CodMed_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_UsrAprov_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_DataAprov_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_CodCargo_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_CodDep_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_NumJusAprov_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.s_Num_apmed": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.querySource": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.mappingName": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.schemaGlobal": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.schemaTableView": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.schemaStoredProcedure": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.commandTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.connectionTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.defaultDatabase": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.isolationLevel": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.attributes": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.cursorLocation": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.mode": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.notRecommendedConnection.provider": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.connectionStringConfig": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.filter": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovMed.sort": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.stringFormat": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.empresa_apsim": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.numSim_apsim": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.numCot_apsim": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.usrAprov_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.dataAprov_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.codCargo_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.codDep_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.numJusAprov_apsim": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.num_apsim": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_Empresa_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_NumSim_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_NumCot_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_UsrAprov_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_DataAprov_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_CodCargo_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_CodDep_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_NumJusAprov_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.s_Num_apsim": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.querySource": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.mappingName": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.schemaGlobal": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.schemaTableView": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.schemaStoredProcedure": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.commandTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.connectionTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.defaultDatabase": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.isolationLevel": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.attributes": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.cursorLocation": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.mode": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.notRecommendedConnection.provider": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.connectionStringConfig": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.filter": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovSimula.sort": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "rsAprovRequisicaoCompra.sort": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.stringFormat": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.numSap_ApPlan": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.usrAprov_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.dataAprov_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.codCargo_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.codDep_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.numJusAprov_ApPlan": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.num_ApPlan": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.s_NumSap_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.s_UsrAprov_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.s_DataAprov_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.s_CodCargo_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.s_CodDep_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.s_NumJusAprov_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.s_Num_ApPlan": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.querySource": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.mappingName": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.schemaGlobal": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.schemaTableView": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.schemaStoredProcedure": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.commandTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.connectionTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.defaultDatabase": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.isolationLevel": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.attributes": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.cursorLocation": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.mode": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.notRecommendedConnection.provider": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.connectionStringConfig": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.filter": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repAprovacoesPL.sort": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.stringFormat": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.empresa_ApPedM": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.obra_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.insumo_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.numPedido_ApPedM": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.itemPed_ApPedM": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.usrAprov_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.dataAprov_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.codCargo_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.codDep_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.numJusAprov_ApPedM": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.num_ApPedM": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_Empresa_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_Obra_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_Insumo_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_NumPedido_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_ItemPed_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_UsrAprov_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_DataAprov_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_CodCargo_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_CodDep_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_NumJusAprov_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.s_Num_ApPedM": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.querySource": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.mappingName": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.schemaGlobal": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.schemaTableView": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.schemaStoredProcedure": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.commandTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.connectionTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.defaultDatabase": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.isolationLevel": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.attributes": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.cursorLocation": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.mode": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.notRecommendedConnection.provider": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.connectionStringConfig": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.filter": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoMat.sort": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.stringFormat": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.numPedido_ApPedS": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.empresa_ApPedS": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.obra_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.serv_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.usrAprov_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.dataAprov_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.codCargo_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.codDep_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.numJusAprov_ApPedS": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.num_ApPedS": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_NumPedido_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_Empresa_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_Obra_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_Serv_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_UsrAprov_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_DataAprov_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_CodCargo_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_CodDep_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_NumJusAprov_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.s_Num_ApPedS": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.querySource": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.mappingName": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.schemaGlobal": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.schemaTableView": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.schemaStoredProcedure": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.commandTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.connectionTimeout": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.defaultDatabase": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.isolationLevel": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.attributes": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.cursorLocation": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.mode": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.notRecommendedConnection.provider": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.connectionString": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.connectionStringConfig": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.filter": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": ""
                },
                "repGerAprovacaoServ.sort": {
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
            >>> api = ContratoMaterialServico()
            >>> response = api.obter_lista_estrutura_aprovacoes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/ContratoMaterialServico/obterListaEstruturaAprovacoes"
        kwargs = {
            "intNumAprov": int_num_aprov,
            "tipoAprovacao": tipo_aprovacao,
            "tipoPedido": tipo_pedido,
            "api-version": api_version,
            "gerAprov._listaEstruturaDeAprovacao": ger_aprov_lista_estrutura_de_aprovacao,
            "gerAprov.codigoDaEmpresa": ger_aprov_codigo_da_empresa,
            "gerAprov.codigoDaObra": ger_aprov_codigo_da_obra,
            "gerAprov.tipoDoProcesso": ger_aprov_tipo_do_processo,
            "gerAprov.quantidadeAprovacao": ger_aprov_quantidade_aprovacao,
            "gerAprov.valorSolicitado": ger_aprov_valor_solicitado,
            "gerAprov.usuarioLogado": ger_aprov_usuario_logado,
            "gerAprov.acao": ger_aprov_acao,
            "gerAprov.estruturaAprovacao": ger_aprov_estrutura_aprovacao,
            "gerAprov.estruturaAprovFaixaValor": ger_aprov_estrutura_aprov_faixa_valor,
            "gerAprov.codigoDepartamento": ger_aprov_codigo_departamento,
            "gerAprov.codigoCargo": ger_aprov_codigo_cargo,
            "gerAprov.listaSeqPendAprovAbaixoSeqUsuarioLog": ger_aprov_lista_seq_pend_aprov_abaixo_seq_usuario_log,
            "gerAprov.isAprovForaSequencia": ger_aprov_is_aprov_fora_sequencia,
            "gerAprov.chaveJustificativaAprovacao": ger_aprov_chave_justificativa_aprovacao,
            "repAprovSimulaConf.stringFormat": rep_aprov_simula_conf_string_format,
            "repAprovSimulaConf.empresa_apSC": rep_aprov_simula_conf_empresa_apsc,
            "repAprovSimulaConf.obra_apSC": rep_aprov_simula_conf_obra_apsc,
            "repAprovSimulaConf.numeroSim_apSC": rep_aprov_simula_conf_numero_sim_apsc,
            "repAprovSimulaConf.numCot_apSC": rep_aprov_simula_conf_num_cot_apsc,
            "repAprovSimulaConf.usrAprov_apSC": rep_aprov_simula_conf_usr_aprov_apsc,
            "repAprovSimulaConf.dataAprov_apSC": rep_aprov_simula_conf_data_aprov_apsc,
            "repAprovSimulaConf.codCargo_ApSC": rep_aprov_simula_conf_cod_cargo_apsc,
            "repAprovSimulaConf.codDep_ApSC": rep_aprov_simula_conf_cod_dep_apsc,
            "repAprovSimulaConf.numJusAprov_apSC": rep_aprov_simula_conf_num_jus_aprov_apsc,
            "repAprovSimulaConf.num_apSC": rep_aprov_simula_conf_num_apsc,
            "repAprovSimulaConf.s_Empresa_apSC": rep_aprov_simula_conf_s_empresa_apsc,
            "repAprovSimulaConf.s_Obra_apSC": rep_aprov_simula_conf_s_obra_apsc,
            "repAprovSimulaConf.s_NumeroSim_apSC": rep_aprov_simula_conf_s_numero_sim_apsc,
            "repAprovSimulaConf.s_NumCot_apSC": rep_aprov_simula_conf_s_num_cot_apsc,
            "repAprovSimulaConf.s_UsrAprov_apSC": rep_aprov_simula_conf_s_usr_aprov_apsc,
            "repAprovSimulaConf.s_DataAprov_apSC": rep_aprov_simula_conf_s_data_aprov_apsc,
            "repAprovSimulaConf.s_CodCargo_ApSC": rep_aprov_simula_conf_s_cod_cargo_apsc,
            "repAprovSimulaConf.s_CodDep_ApSC": rep_aprov_simula_conf_s_cod_dep_apsc,
            "repAprovSimulaConf.s_NumJusAprov_apSC": rep_aprov_simula_conf_s_num_jus_aprov_apsc,
            "repAprovSimulaConf.s_Num_apSC": rep_aprov_simula_conf_s_num_apsc,
            "repAprovSimulaConf.querySource": rep_aprov_simula_conf_query_source,
            "repAprovSimulaConf.mappingName": rep_aprov_simula_conf_mapping_name,
            "repAprovSimulaConf.schemaGlobal": rep_aprov_simula_conf_schema_global,
            "repAprovSimulaConf.schemaTableView": rep_aprov_simula_conf_schema_table_view,
            "repAprovSimulaConf.schemaStoredProcedure": rep_aprov_simula_conf_schema_stored_procedure,
            "repAprovSimulaConf.notRecommendedConnection.connectionString": rep_aprov_simula_conf_not_recommended_connection_connection_string,
            "repAprovSimulaConf.notRecommendedConnection.commandTimeout": rep_aprov_simula_conf_not_recommended_connection_command_timeout,
            "repAprovSimulaConf.notRecommendedConnection.connectionTimeout": rep_aprov_simula_conf_not_recommended_connection_connection_timeout,
            "repAprovSimulaConf.notRecommendedConnection.defaultDatabase": rep_aprov_simula_conf_not_recommended_connection_default_database,
            "repAprovSimulaConf.notRecommendedConnection.isolationLevel": rep_aprov_simula_conf_not_recommended_connection_isolation_level,
            "repAprovSimulaConf.notRecommendedConnection.attributes": rep_aprov_simula_conf_not_recommended_connection_attributes,
            "repAprovSimulaConf.notRecommendedConnection.cursorLocation": rep_aprov_simula_conf_not_recommended_connection_cursor_location,
            "repAprovSimulaConf.notRecommendedConnection.mode": rep_aprov_simula_conf_not_recommended_connection_mode,
            "repAprovSimulaConf.notRecommendedConnection.provider": rep_aprov_simula_conf_not_recommended_connection_provider,
            "repAprovSimulaConf.connectionString": rep_aprov_simula_conf_connection_string,
            "repAprovSimulaConf.connectionStringConfig": rep_aprov_simula_conf_connection_string_config,
            "repAprovSimulaConf.filter": rep_aprov_simula_conf_filter,
            "repAprovSimulaConf.sort": rep_aprov_simula_conf_sort,
            "repAprovCont.stringFormat": rep_aprov_cont_string_format,
            "repAprovCont.empresa_ApCont": rep_aprov_cont_empresa_ap_cont,
            "repAprovCont.codCont_ApCont": rep_aprov_cont_cod_cont_ap_cont,
            "repAprovCont.usrAprov_ApCont": rep_aprov_cont_usr_aprov_ap_cont,
            "repAprovCont.dataAprov_ApCont": rep_aprov_cont_data_aprov_ap_cont,
            "repAprovCont.codCargo_ApCont": rep_aprov_cont_cod_cargo_ap_cont,
            "repAprovCont.codDep_ApCont": rep_aprov_cont_cod_dep_ap_cont,
            "repAprovCont.numJusAprov_ApCont": rep_aprov_cont_num_jus_aprov_ap_cont,
            "repAprovCont.num_ApCont": rep_aprov_cont_num_ap_cont,
            "repAprovCont.s_Empresa_ApCont": rep_aprov_cont_s_empresa_ap_cont,
            "repAprovCont.s_CodCont_ApCont": rep_aprov_cont_s_cod_cont_ap_cont,
            "repAprovCont.s_UsrAprov_ApCont": rep_aprov_cont_s_usr_aprov_ap_cont,
            "repAprovCont.s_DataAprov_ApCont": rep_aprov_cont_s_data_aprov_ap_cont,
            "repAprovCont.s_CodCargo_ApCont": rep_aprov_cont_s_cod_cargo_ap_cont,
            "repAprovCont.s_CodDep_ApCont": rep_aprov_cont_s_cod_dep_ap_cont,
            "repAprovCont.s_NumJusAprov_ApCont": rep_aprov_cont_s_num_jus_aprov_ap_cont,
            "repAprovCont.s_Num_ApCont": rep_aprov_cont_s_num_ap_cont,
            "repAprovCont.querySource": rep_aprov_cont_query_source,
            "repAprovCont.mappingName": rep_aprov_cont_mapping_name,
            "repAprovCont.schemaGlobal": rep_aprov_cont_schema_global,
            "repAprovCont.schemaTableView": rep_aprov_cont_schema_table_view,
            "repAprovCont.schemaStoredProcedure": rep_aprov_cont_schema_stored_procedure,
            "repAprovCont.notRecommendedConnection.connectionString": rep_aprov_cont_not_recommended_connection_connection_string,
            "repAprovCont.notRecommendedConnection.commandTimeout": rep_aprov_cont_not_recommended_connection_command_timeout,
            "repAprovCont.notRecommendedConnection.connectionTimeout": rep_aprov_cont_not_recommended_connection_connection_timeout,
            "repAprovCont.notRecommendedConnection.defaultDatabase": rep_aprov_cont_not_recommended_connection_default_database,
            "repAprovCont.notRecommendedConnection.isolationLevel": rep_aprov_cont_not_recommended_connection_isolation_level,
            "repAprovCont.notRecommendedConnection.attributes": rep_aprov_cont_not_recommended_connection_attributes,
            "repAprovCont.notRecommendedConnection.cursorLocation": rep_aprov_cont_not_recommended_connection_cursor_location,
            "repAprovCont.notRecommendedConnection.mode": rep_aprov_cont_not_recommended_connection_mode,
            "repAprovCont.notRecommendedConnection.provider": rep_aprov_cont_not_recommended_connection_provider,
            "repAprovCont.connectionString": rep_aprov_cont_connection_string,
            "repAprovCont.connectionStringConfig": rep_aprov_cont_connection_string_config,
            "repAprovCont.filter": rep_aprov_cont_filter,
            "repAprovCont.sort": rep_aprov_cont_sort,
            "repAprovMed.stringFormat": rep_aprov_med_string_format,
            "repAprovMed.empresa_apmed": rep_aprov_med_empresa_apmed,
            "repAprovMed.codCont_apmed": rep_aprov_med_cod_cont_apmed,
            "repAprovMed.codMed_apmed": rep_aprov_med_cod_med_apmed,
            "repAprovMed.usrAprov_apmed": rep_aprov_med_usr_aprov_apmed,
            "repAprovMed.dataAprov_apmed": rep_aprov_med_data_aprov_apmed,
            "repAprovMed.codCargo_apmed": rep_aprov_med_cod_cargo_apmed,
            "repAprovMed.codDep_apmed": rep_aprov_med_cod_dep_apmed,
            "repAprovMed.numJusAprov_apmed": rep_aprov_med_num_jus_aprov_apmed,
            "repAprovMed.num_apmed": rep_aprov_med_num_apmed,
            "repAprovMed.s_Empresa_apmed": rep_aprov_med_s_empresa_apmed,
            "repAprovMed.s_CodCont_apmed": rep_aprov_med_s_cod_cont_apmed,
            "repAprovMed.s_CodMed_apmed": rep_aprov_med_s_cod_med_apmed,
            "repAprovMed.s_UsrAprov_apmed": rep_aprov_med_s_usr_aprov_apmed,
            "repAprovMed.s_DataAprov_apmed": rep_aprov_med_s_data_aprov_apmed,
            "repAprovMed.s_CodCargo_apmed": rep_aprov_med_s_cod_cargo_apmed,
            "repAprovMed.s_CodDep_apmed": rep_aprov_med_s_cod_dep_apmed,
            "repAprovMed.s_NumJusAprov_apmed": rep_aprov_med_s_num_jus_aprov_apmed,
            "repAprovMed.s_Num_apmed": rep_aprov_med_s_num_apmed,
            "repAprovMed.querySource": rep_aprov_med_query_source,
            "repAprovMed.mappingName": rep_aprov_med_mapping_name,
            "repAprovMed.schemaGlobal": rep_aprov_med_schema_global,
            "repAprovMed.schemaTableView": rep_aprov_med_schema_table_view,
            "repAprovMed.schemaStoredProcedure": rep_aprov_med_schema_stored_procedure,
            "repAprovMed.notRecommendedConnection.connectionString": rep_aprov_med_not_recommended_connection_connection_string,
            "repAprovMed.notRecommendedConnection.commandTimeout": rep_aprov_med_not_recommended_connection_command_timeout,
            "repAprovMed.notRecommendedConnection.connectionTimeout": rep_aprov_med_not_recommended_connection_connection_timeout,
            "repAprovMed.notRecommendedConnection.defaultDatabase": rep_aprov_med_not_recommended_connection_default_database,
            "repAprovMed.notRecommendedConnection.isolationLevel": rep_aprov_med_not_recommended_connection_isolation_level,
            "repAprovMed.notRecommendedConnection.attributes": rep_aprov_med_not_recommended_connection_attributes,
            "repAprovMed.notRecommendedConnection.cursorLocation": rep_aprov_med_not_recommended_connection_cursor_location,
            "repAprovMed.notRecommendedConnection.mode": rep_aprov_med_not_recommended_connection_mode,
            "repAprovMed.notRecommendedConnection.provider": rep_aprov_med_not_recommended_connection_provider,
            "repAprovMed.connectionString": rep_aprov_med_connection_string,
            "repAprovMed.connectionStringConfig": rep_aprov_med_connection_string_config,
            "repAprovMed.filter": rep_aprov_med_filter,
            "repAprovMed.sort": rep_aprov_med_sort,
            "repAprovSimula.stringFormat": rep_aprov_simula_string_format,
            "repAprovSimula.empresa_apsim": rep_aprov_simula_empresa_apsim,
            "repAprovSimula.numSim_apsim": rep_aprov_simula_num_sim_apsim,
            "repAprovSimula.numCot_apsim": rep_aprov_simula_num_cot_apsim,
            "repAprovSimula.usrAprov_apsim": rep_aprov_simula_usr_aprov_apsim,
            "repAprovSimula.dataAprov_apsim": rep_aprov_simula_data_aprov_apsim,
            "repAprovSimula.codCargo_apsim": rep_aprov_simula_cod_cargo_apsim,
            "repAprovSimula.codDep_apsim": rep_aprov_simula_cod_dep_apsim,
            "repAprovSimula.numJusAprov_apsim": rep_aprov_simula_num_jus_aprov_apsim,
            "repAprovSimula.num_apsim": rep_aprov_simula_num_apsim,
            "repAprovSimula.s_Empresa_apsim": rep_aprov_simula_s_empresa_apsim,
            "repAprovSimula.s_NumSim_apsim": rep_aprov_simula_s_num_sim_apsim,
            "repAprovSimula.s_NumCot_apsim": rep_aprov_simula_s_num_cot_apsim,
            "repAprovSimula.s_UsrAprov_apsim": rep_aprov_simula_s_usr_aprov_apsim,
            "repAprovSimula.s_DataAprov_apsim": rep_aprov_simula_s_data_aprov_apsim,
            "repAprovSimula.s_CodCargo_apsim": rep_aprov_simula_s_cod_cargo_apsim,
            "repAprovSimula.s_CodDep_apsim": rep_aprov_simula_s_cod_dep_apsim,
            "repAprovSimula.s_NumJusAprov_apsim": rep_aprov_simula_s_num_jus_aprov_apsim,
            "repAprovSimula.s_Num_apsim": rep_aprov_simula_s_num_apsim,
            "repAprovSimula.querySource": rep_aprov_simula_query_source,
            "repAprovSimula.mappingName": rep_aprov_simula_mapping_name,
            "repAprovSimula.schemaGlobal": rep_aprov_simula_schema_global,
            "repAprovSimula.schemaTableView": rep_aprov_simula_schema_table_view,
            "repAprovSimula.schemaStoredProcedure": rep_aprov_simula_schema_stored_procedure,
            "repAprovSimula.notRecommendedConnection.connectionString": rep_aprov_simula_not_recommended_connection_connection_string,
            "repAprovSimula.notRecommendedConnection.commandTimeout": rep_aprov_simula_not_recommended_connection_command_timeout,
            "repAprovSimula.notRecommendedConnection.connectionTimeout": rep_aprov_simula_not_recommended_connection_connection_timeout,
            "repAprovSimula.notRecommendedConnection.defaultDatabase": rep_aprov_simula_not_recommended_connection_default_database,
            "repAprovSimula.notRecommendedConnection.isolationLevel": rep_aprov_simula_not_recommended_connection_isolation_level,
            "repAprovSimula.notRecommendedConnection.attributes": rep_aprov_simula_not_recommended_connection_attributes,
            "repAprovSimula.notRecommendedConnection.cursorLocation": rep_aprov_simula_not_recommended_connection_cursor_location,
            "repAprovSimula.notRecommendedConnection.mode": rep_aprov_simula_not_recommended_connection_mode,
            "repAprovSimula.notRecommendedConnection.provider": rep_aprov_simula_not_recommended_connection_provider,
            "repAprovSimula.connectionString": rep_aprov_simula_connection_string,
            "repAprovSimula.connectionStringConfig": rep_aprov_simula_connection_string_config,
            "repAprovSimula.filter": rep_aprov_simula_filter,
            "repAprovSimula.sort": rep_aprov_simula_sort,
            "rsAprovRequisicaoCompra.sort": rs_aprov_requisicao_compra_sort,
            "repAprovacoesPL.stringFormat": rep_aprovacoespl_string_format,
            "repAprovacoesPL.numSap_ApPlan": rep_aprovacoespl_num_sap_ap_plan,
            "repAprovacoesPL.usrAprov_ApPlan": rep_aprovacoespl_usr_aprov_ap_plan,
            "repAprovacoesPL.dataAprov_ApPlan": rep_aprovacoespl_data_aprov_ap_plan,
            "repAprovacoesPL.codCargo_ApPlan": rep_aprovacoespl_cod_cargo_ap_plan,
            "repAprovacoesPL.codDep_ApPlan": rep_aprovacoespl_cod_dep_ap_plan,
            "repAprovacoesPL.numJusAprov_ApPlan": rep_aprovacoespl_num_jus_aprov_ap_plan,
            "repAprovacoesPL.num_ApPlan": rep_aprovacoespl_num_ap_plan,
            "repAprovacoesPL.s_NumSap_ApPlan": rep_aprovacoespl_s_num_sap_ap_plan,
            "repAprovacoesPL.s_UsrAprov_ApPlan": rep_aprovacoespl_s_usr_aprov_ap_plan,
            "repAprovacoesPL.s_DataAprov_ApPlan": rep_aprovacoespl_s_data_aprov_ap_plan,
            "repAprovacoesPL.s_CodCargo_ApPlan": rep_aprovacoespl_s_cod_cargo_ap_plan,
            "repAprovacoesPL.s_CodDep_ApPlan": rep_aprovacoespl_s_cod_dep_ap_plan,
            "repAprovacoesPL.s_NumJusAprov_ApPlan": rep_aprovacoespl_s_num_jus_aprov_ap_plan,
            "repAprovacoesPL.s_Num_ApPlan": rep_aprovacoespl_s_num_ap_plan,
            "repAprovacoesPL.querySource": rep_aprovacoespl_query_source,
            "repAprovacoesPL.mappingName": rep_aprovacoespl_mapping_name,
            "repAprovacoesPL.schemaGlobal": rep_aprovacoespl_schema_global,
            "repAprovacoesPL.schemaTableView": rep_aprovacoespl_schema_table_view,
            "repAprovacoesPL.schemaStoredProcedure": rep_aprovacoespl_schema_stored_procedure,
            "repAprovacoesPL.notRecommendedConnection.connectionString": rep_aprovacoespl_not_recommended_connection_connection_string,
            "repAprovacoesPL.notRecommendedConnection.commandTimeout": rep_aprovacoespl_not_recommended_connection_command_timeout,
            "repAprovacoesPL.notRecommendedConnection.connectionTimeout": rep_aprovacoespl_not_recommended_connection_connection_timeout,
            "repAprovacoesPL.notRecommendedConnection.defaultDatabase": rep_aprovacoespl_not_recommended_connection_default_database,
            "repAprovacoesPL.notRecommendedConnection.isolationLevel": rep_aprovacoespl_not_recommended_connection_isolation_level,
            "repAprovacoesPL.notRecommendedConnection.attributes": rep_aprovacoespl_not_recommended_connection_attributes,
            "repAprovacoesPL.notRecommendedConnection.cursorLocation": rep_aprovacoespl_not_recommended_connection_cursor_location,
            "repAprovacoesPL.notRecommendedConnection.mode": rep_aprovacoespl_not_recommended_connection_mode,
            "repAprovacoesPL.notRecommendedConnection.provider": rep_aprovacoespl_not_recommended_connection_provider,
            "repAprovacoesPL.connectionString": rep_aprovacoespl_connection_string,
            "repAprovacoesPL.connectionStringConfig": rep_aprovacoespl_connection_string_config,
            "repAprovacoesPL.filter": rep_aprovacoespl_filter,
            "repAprovacoesPL.sort": rep_aprovacoespl_sort,
            "repGerAprovacaoMat.stringFormat": rep_ger_aprovacao_mat_string_format,
            "repGerAprovacaoMat.empresa_ApPedM": rep_ger_aprovacao_mat_empresa_ap_pedm,
            "repGerAprovacaoMat.obra_ApPedM": rep_ger_aprovacao_mat_obra_ap_pedm,
            "repGerAprovacaoMat.insumo_ApPedM": rep_ger_aprovacao_mat_insumo_ap_pedm,
            "repGerAprovacaoMat.numPedido_ApPedM": rep_ger_aprovacao_mat_num_pedido_ap_pedm,
            "repGerAprovacaoMat.itemPed_ApPedM": rep_ger_aprovacao_mat_item_ped_ap_pedm,
            "repGerAprovacaoMat.usrAprov_ApPedM": rep_ger_aprovacao_mat_usr_aprov_ap_pedm,
            "repGerAprovacaoMat.dataAprov_ApPedM": rep_ger_aprovacao_mat_data_aprov_ap_pedm,
            "repGerAprovacaoMat.codCargo_ApPedM": rep_ger_aprovacao_mat_cod_cargo_ap_pedm,
            "repGerAprovacaoMat.codDep_ApPedM": rep_ger_aprovacao_mat_cod_dep_ap_pedm,
            "repGerAprovacaoMat.numJusAprov_ApPedM": rep_ger_aprovacao_mat_num_jus_aprov_ap_pedm,
            "repGerAprovacaoMat.num_ApPedM": rep_ger_aprovacao_mat_num_ap_pedm,
            "repGerAprovacaoMat.s_Empresa_ApPedM": rep_ger_aprovacao_mat_s_empresa_ap_pedm,
            "repGerAprovacaoMat.s_Obra_ApPedM": rep_ger_aprovacao_mat_s_obra_ap_pedm,
            "repGerAprovacaoMat.s_Insumo_ApPedM": rep_ger_aprovacao_mat_s_insumo_ap_pedm,
            "repGerAprovacaoMat.s_NumPedido_ApPedM": rep_ger_aprovacao_mat_s_num_pedido_ap_pedm,
            "repGerAprovacaoMat.s_ItemPed_ApPedM": rep_ger_aprovacao_mat_s_item_ped_ap_pedm,
            "repGerAprovacaoMat.s_UsrAprov_ApPedM": rep_ger_aprovacao_mat_s_usr_aprov_ap_pedm,
            "repGerAprovacaoMat.s_DataAprov_ApPedM": rep_ger_aprovacao_mat_s_data_aprov_ap_pedm,
            "repGerAprovacaoMat.s_CodCargo_ApPedM": rep_ger_aprovacao_mat_s_cod_cargo_ap_pedm,
            "repGerAprovacaoMat.s_CodDep_ApPedM": rep_ger_aprovacao_mat_s_cod_dep_ap_pedm,
            "repGerAprovacaoMat.s_NumJusAprov_ApPedM": rep_ger_aprovacao_mat_s_num_jus_aprov_ap_pedm,
            "repGerAprovacaoMat.s_Num_ApPedM": rep_ger_aprovacao_mat_s_num_ap_pedm,
            "repGerAprovacaoMat.querySource": rep_ger_aprovacao_mat_query_source,
            "repGerAprovacaoMat.mappingName": rep_ger_aprovacao_mat_mapping_name,
            "repGerAprovacaoMat.schemaGlobal": rep_ger_aprovacao_mat_schema_global,
            "repGerAprovacaoMat.schemaTableView": rep_ger_aprovacao_mat_schema_table_view,
            "repGerAprovacaoMat.schemaStoredProcedure": rep_ger_aprovacao_mat_schema_stored_procedure,
            "repGerAprovacaoMat.notRecommendedConnection.connectionString": rep_ger_aprovacao_mat_not_recommended_connection_connection_string,
            "repGerAprovacaoMat.notRecommendedConnection.commandTimeout": rep_ger_aprovacao_mat_not_recommended_connection_command_timeout,
            "repGerAprovacaoMat.notRecommendedConnection.connectionTimeout": rep_ger_aprovacao_mat_not_recommended_connection_connection_timeout,
            "repGerAprovacaoMat.notRecommendedConnection.defaultDatabase": rep_ger_aprovacao_mat_not_recommended_connection_default_database,
            "repGerAprovacaoMat.notRecommendedConnection.isolationLevel": rep_ger_aprovacao_mat_not_recommended_connection_isolation_level,
            "repGerAprovacaoMat.notRecommendedConnection.attributes": rep_ger_aprovacao_mat_not_recommended_connection_attributes,
            "repGerAprovacaoMat.notRecommendedConnection.cursorLocation": rep_ger_aprovacao_mat_not_recommended_connection_cursor_location,
            "repGerAprovacaoMat.notRecommendedConnection.mode": rep_ger_aprovacao_mat_not_recommended_connection_mode,
            "repGerAprovacaoMat.notRecommendedConnection.provider": rep_ger_aprovacao_mat_not_recommended_connection_provider,
            "repGerAprovacaoMat.connectionString": rep_ger_aprovacao_mat_connection_string,
            "repGerAprovacaoMat.connectionStringConfig": rep_ger_aprovacao_mat_connection_string_config,
            "repGerAprovacaoMat.filter": rep_ger_aprovacao_mat_filter,
            "repGerAprovacaoMat.sort": rep_ger_aprovacao_mat_sort,
            "repGerAprovacaoServ.stringFormat": rep_ger_aprovacao_serv_string_format,
            "repGerAprovacaoServ.numPedido_ApPedS": rep_ger_aprovacao_serv_num_pedido_ap_peds,
            "repGerAprovacaoServ.empresa_ApPedS": rep_ger_aprovacao_serv_empresa_ap_peds,
            "repGerAprovacaoServ.obra_ApPedS": rep_ger_aprovacao_serv_obra_ap_peds,
            "repGerAprovacaoServ.serv_ApPedS": rep_ger_aprovacao_serv_serv_ap_peds,
            "repGerAprovacaoServ.usrAprov_ApPedS": rep_ger_aprovacao_serv_usr_aprov_ap_peds,
            "repGerAprovacaoServ.dataAprov_ApPedS": rep_ger_aprovacao_serv_data_aprov_ap_peds,
            "repGerAprovacaoServ.codCargo_ApPedS": rep_ger_aprovacao_serv_cod_cargo_ap_peds,
            "repGerAprovacaoServ.codDep_ApPedS": rep_ger_aprovacao_serv_cod_dep_ap_peds,
            "repGerAprovacaoServ.numJusAprov_ApPedS": rep_ger_aprovacao_serv_num_jus_aprov_ap_peds,
            "repGerAprovacaoServ.num_ApPedS": rep_ger_aprovacao_serv_num_ap_peds,
            "repGerAprovacaoServ.s_NumPedido_ApPedS": rep_ger_aprovacao_serv_s_num_pedido_ap_peds,
            "repGerAprovacaoServ.s_Empresa_ApPedS": rep_ger_aprovacao_serv_s_empresa_ap_peds,
            "repGerAprovacaoServ.s_Obra_ApPedS": rep_ger_aprovacao_serv_s_obra_ap_peds,
            "repGerAprovacaoServ.s_Serv_ApPedS": rep_ger_aprovacao_serv_s_serv_ap_peds,
            "repGerAprovacaoServ.s_UsrAprov_ApPedS": rep_ger_aprovacao_serv_s_usr_aprov_ap_peds,
            "repGerAprovacaoServ.s_DataAprov_ApPedS": rep_ger_aprovacao_serv_s_data_aprov_ap_peds,
            "repGerAprovacaoServ.s_CodCargo_ApPedS": rep_ger_aprovacao_serv_s_cod_cargo_ap_peds,
            "repGerAprovacaoServ.s_CodDep_ApPedS": rep_ger_aprovacao_serv_s_cod_dep_ap_peds,
            "repGerAprovacaoServ.s_NumJusAprov_ApPedS": rep_ger_aprovacao_serv_s_num_jus_aprov_ap_peds,
            "repGerAprovacaoServ.s_Num_ApPedS": rep_ger_aprovacao_serv_s_num_ap_peds,
            "repGerAprovacaoServ.querySource": rep_ger_aprovacao_serv_query_source,
            "repGerAprovacaoServ.mappingName": rep_ger_aprovacao_serv_mapping_name,
            "repGerAprovacaoServ.schemaGlobal": rep_ger_aprovacao_serv_schema_global,
            "repGerAprovacaoServ.schemaTableView": rep_ger_aprovacao_serv_schema_table_view,
            "repGerAprovacaoServ.schemaStoredProcedure": rep_ger_aprovacao_serv_schema_stored_procedure,
            "repGerAprovacaoServ.notRecommendedConnection.connectionString": rep_ger_aprovacao_serv_not_recommended_connection_connection_string,
            "repGerAprovacaoServ.notRecommendedConnection.commandTimeout": rep_ger_aprovacao_serv_not_recommended_connection_command_timeout,
            "repGerAprovacaoServ.notRecommendedConnection.connectionTimeout": rep_ger_aprovacao_serv_not_recommended_connection_connection_timeout,
            "repGerAprovacaoServ.notRecommendedConnection.defaultDatabase": rep_ger_aprovacao_serv_not_recommended_connection_default_database,
            "repGerAprovacaoServ.notRecommendedConnection.isolationLevel": rep_ger_aprovacao_serv_not_recommended_connection_isolation_level,
            "repGerAprovacaoServ.notRecommendedConnection.attributes": rep_ger_aprovacao_serv_not_recommended_connection_attributes,
            "repGerAprovacaoServ.notRecommendedConnection.cursorLocation": rep_ger_aprovacao_serv_not_recommended_connection_cursor_location,
            "repGerAprovacaoServ.notRecommendedConnection.mode": rep_ger_aprovacao_serv_not_recommended_connection_mode,
            "repGerAprovacaoServ.notRecommendedConnection.provider": rep_ger_aprovacao_serv_not_recommended_connection_provider,
            "repGerAprovacaoServ.connectionString": rep_ger_aprovacao_serv_connection_string,
            "repGerAprovacaoServ.connectionStringConfig": rep_ger_aprovacao_serv_connection_string_config,
            "repGerAprovacaoServ.filter": rep_ger_aprovacao_serv_filter,
            "repGerAprovacaoServ.sort": rep_ger_aprovacao_serv_sort,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

