from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Medicao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def manter_medicao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        1. É possível inserir ou atualizar uma medição de contrato de material e/ou serviço.
        1.2. Se o número da medição for informado e essa medição existir, então ela será atualzada, caso contrário será inserida.
        2. Só poderão ser atualizadas as medições que estiverem em aberto, ou seja, sem nenhuma confirmação de aprovação.
        3. Os adiantamentos de contratos podem ser informados de duas formas, dependendo do tipo de vínculo de planejamento do contrato, se for vinculado por item, pode ser informado diretamente no item específico, 
           ou de forma geral, onde nesse caso será feito o cálculo proporcional, se o vínculo do planejamento for somente por contrato ou não possuir vínculo algum, só pode ser informado o adiantamento geral.
        
        Endpoint: `/api/v{version}/Medicao/ManterMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de inserir ou atualizar uma determinada medição de contrato de material e serviço
        
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
                            "Empresa",
                            "NumeroContrato"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "NumeroContrato": {
                                "format": "int32",
                                "description": "Código do contrato",
                                "type": "integer"
                            },
                            "NumeroMedicao": {
                                "format": "int32",
                                "description": "Codigo identificador da medição",
                                "type": "integer"
                            },
                            "CodigoFornecedor": {
                                "format": "int32",
                                "description": "1. Código do fornecedor - este fornecedor pode ser escolhido na medição em caso de contrato com múltiplos contratados, do contrário é o mesmo fornecedor do contrato.\r\n2. Deve ser informado o código do fornecedor, conforme cadastro ou o CNJP deste, se os dois forem informados, o código será considerado para a atualização da medição.",
                                "type": "integer"
                            },
                            "CNPJFornecedor": {
                                "description": "1. CNPJ do fornecedor - este fornecedor pode ser escolhido na medição em caso de contrato com múltiplos contratados, do contrário é o mesmo fornecedor do contrato.\r\n2. Deve ser informado o código do fornecedor, conforme cadastro ou o CNJP deste, se os dois forem informados, o código será considerado para a atualização da medição.",
                                "type": "string"
                            },
                            "NumCidadePrestacaoServ": {
                                "format": "int32",
                                "description": "Número da cidade do prestador de serviço",
                                "type": "integer"
                            },
                            "Observacao": {
                                "description": "Observação referente à medição",
                                "type": "string"
                            },
                            "UltimaMedicao": {
                                "format": "int32",
                                "description": "Indicativo de que se trata da última medição do contrato de material e serviço",
                                "type": "integer"
                            },
                            "DataBase": {
                                "format": "date-time",
                                "description": "Data base para cálculo dos acréscimos, conforme plano de reajuste",
                                "type": "string"
                            },
                            "UsrCadastro": {
                                "description": "Nome do usuário que está realizando o cadastro da medição",
                                "type": "string"
                            },
                            "DescontosMedicao": {
                                "description": "Lista dos descontos simples da medição",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Medicao.DescontoMedicaoRequest"
                                }
                            },
                            "Itens": {
                                "description": "Lista com os itens da medição",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Medicao.ItemMedicaoRequest"
                                }
                            },
                            "Adiantamentos": {
                                "description": "Lista com os adiantamentos da medição",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Medicao.AdiantamentoRequest"
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
            >>> api = Medicao()
            >>> response = api._manter_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ManterMedicao"
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

    def excluir_medicao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        1. Somente medições que estiverem abertas e sem nenhuma aprovação poderão ser excluídas.
        2. Nenhum processo de pagamento poderá estar vinculado à medição.
        3. Nâo pode haver vínculos dependentes entre os itens da medição (vínculo de item do tipo material com item de serviço).
        4. Não pode excluir medição que contenha itens que tenham gerado valores excedentes para itens de outras medições.
        
        Endpoint: `/api/v{version}/Medicao/ExcluirMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de excluir uma determinada medição de contrato de material e serviço
        
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
                            "Empresa",
                            "Contrato",
                            "NumeroMedicao"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa da medição",
                                "type": "integer"
                            },
                            "Contrato": {
                                "format": "int32",
                                "description": "Codigo do contrato de material ou serviço referente à medição",
                                "type": "integer"
                            },
                            "NumeroMedicao": {
                                "format": "int32",
                                "description": "Codigo identificador da medição (sempre sequencial)",
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
            >>> api = Medicao()
            >>> response = api._excluir_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ExcluirMedicao"
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

    def consultar_medicao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar medição por empresa, contrato e código da medição.
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato",
                                "type": "integer"
                            },
                            "medicao": {
                                "format": "int32",
                                "description": "Código da medição",
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
            >>> api = Medicao()
            >>> response = api._consultar_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarMedicao"
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

    def consultar_itens_medicao(
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
        1. Retorna uma lista de itens da medição por empresa, contrato e medição.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarItensMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens de medição por empresa, contrato e medição.
        
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
                            "contrato",
                            "medicao"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato",
                                "type": "integer"
                            },
                            "medicao": {
                                "format": "int32",
                                "description": "Código da medição",
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
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarItensMedicao"
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

    def aprovar_medicoes_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        1. O contrato precisa estar com status aprovado.
        2. É necessário permissão de aprovação para o programa OBMEDCONT
        
        Endpoint: `/api/v{version}/Medicao/AprovarMedicoesContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de aprovar medições de contrato de material e serviço
        
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
                            "Medicoes": {
                                "description": "Medições a serem aprovadas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Medicao.AprovaMedicaoContratoRequest"
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
            >>> api = Medicao()
            >>> response = api._aprovar_medicoes_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/AprovarMedicoesContrato"
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

    def consultar_boletim_medicao(
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
        1. Consulta boletim de medição dentro do sistema UAU.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarBoletimMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar boletim de medição.
        
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
                            "contrato",
                            "avancoFisico"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato.",
                                "type": "integer"
                            },
                            "avancoFisico": {
                                "description": "Exibir o avanço físico no relatório.",
                                "type": "boolean"
                            },
                            "medicao": {
                                "format": "int32",
                                "description": "Código da medição -&gt; (0 – Para retorna todas as medições ou o número específico da medição.)",
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
            >>> api = Medicao()
            >>> response = api._consultar_boletim_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarBoletimMedicao"
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

    def consultar_medicao_completa(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Para retornar as medições, podem ser feitas as seguintes combinações:
            1. Código da empresa e código do contrato
            2. Código da empresa, código do contrato e código da medição
            3. Código da empresa e CNPJ do contrato ou CNPJ do fornecedor (informado na medição)
            4. Código da empresa e período de geração da medição (data inicial e data final)
        
        Endpoint: `/api/v{version}/Medicao/ConsultarMedicaoCompleta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de consultar as medições de contrato de material e serviço
        
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
                            "Empresa"
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
                            "Medicao": {
                                "format": "int32",
                                "description": "Código da medição",
                                "type": "integer"
                            },
                            "CNPJContratado": {
                                "description": "CNPJ do contratado",
                                "type": "string"
                            },
                            "CNPJFornecedor": {
                                "description": "CNPJ do fornecedor",
                                "type": "string"
                            },
                            "DataInicial": {
                                "format": "date-time",
                                "description": "Data de início do primeiro acompanhamento da medição",
                                "type": "string"
                            },
                            "DataFinal": {
                                "format": "date-time",
                                "description": "Data de término do último acompanhamento da medição",
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
            >>> api = Medicao()
            >>> response = api._consultar_medicao_completa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarMedicaoCompleta"
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

    def consultar_medicao_por_serv_mat(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarMedicaoPorServMat`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar medição por empresa, contrato e código da medição.
        
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
                                "description": "Código da empresa da medição.",
                                "type": "integer"
                            },
                            "servMat": {
                                "description": "Código do serviço ou material da medição.",
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
            >>> api = Medicao()
            >>> response = api._consultar_medicao_por_serv_mat(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarMedicaoPorServMat"
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

    def consultar_medicoes_por_status(
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
        1. Retorna uma lista de medições por status e usuário.
        2. Os possíveis status de uma medição são: 
           0 - Aberta;
           1 - Aprovada;
           2 - Medida;
           3 - Proc. Serviço Gerado.
        3. O usuário é para indicar quais são as obras que ele possui permissão para retornar as medições pertinentes.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarMedicoesPorStatus`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar medições por status e usuário.
        
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
                            "status_med",
                            "login_usu"
                        ],
                        "type": "object",
                        "properties": {
                            "status_med": {
                                "format": "int32",
                                "description": "Status da medição",
                                "type": "integer"
                            },
                            "login_usu": {
                                "description": "Usuário da operação",
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
            >>> api = Medicao()
            >>> response = api._consultar_medicoes_por_status(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarMedicoesPorStatus"
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

    def validar_cnpjao_gravar_medicao(
        self,
        cnpj: Optional[str] = None,
        codigo_fornecedor: Optional[Dict] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            CNPJ (Dict[str, Any]): The c n p j
            codigoFornecedor (Dict[str, Any]): The fornecedor
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "CNPJ": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "codigoFornecedor": {
                    "definition": {
                        "type": "object",
                        "properties": {}
                    },
                    "in": "body",
                    "required": true
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
            >>> api = Medicao()
            >>> response = api._validarcnpj_ao_gravar_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Medicao/ValidarCNPJAoGravarMedicao"
        kwargs = {
            "CNPJ": cnpj,
            "codigoFornecedor": codigo_fornecedor,
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

    def consultar_medicao_por_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarMedicaoPorContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar medição por contrato.
        
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
                                "description": "Código da empresa da medição.",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato da medição.",
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
            >>> api = Medicao()
            >>> response = api._consultar_medicao_por_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarMedicaoPorContrato"
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

    def consultar_itens_medicao_por_medicao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarItensMedicaoPorMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens de medição por medição.
        
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
                            "contrato",
                            "medicao"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato",
                                "type": "integer"
                            },
                            "medicao": {
                                "format": "int32",
                                "description": "Código da medição",
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
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarItensMedicaoPorMedicao"
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

    def consultar_itens_medicao_por_serv_mat(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarItensMedicaoPorServMat`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens de medição por empresa e serviço/material.
        
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
                                "description": "Código da empresa da medição.",
                                "type": "integer"
                            },
                            "servMat": {
                                "description": "Código do serviço ou material da medição.",
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
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_serv_mat(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarItensMedicaoPorServMat"
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

    def consultar_itens_medicao_por_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarItensMedicaoPorContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens de medição por contrato.
        
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
                                "description": "Código da empresa da medição.",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato da medição.",
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
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarItensMedicaoPorContrato"
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

    def consultar_itens_medicao_por_item_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Medicao/ConsultarItensMedicaoPorItemContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar itens de medição por item de contrato.
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "contrato": {
                                "format": "int32",
                                "description": "Código do contrato",
                                "type": "integer"
                            },
                            "medicao": {
                                "format": "int32",
                                "description": "Código da medição",
                                "type": "integer"
                            },
                            "itemContrato": {
                                "format": "int32",
                                "description": "Código do item do contrato",
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
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_item_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Medicao/ConsultarItensMedicaoPorItemContrato"
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

