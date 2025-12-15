from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ModeloVenda:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def buscar_plano_indexador(
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
        1. Consulta o plano indexador vinculado ao modelo da venda.
        
        Endpoint: `/api/v{version}/ModeloVenda/BuscarPlanoIndexador`
        HTTP Method: `POST`
        
        Implementation Notes:
        Seleciona os dados do plano Indexador de um modelo de venda
        
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
                            "nummodelo_venda"
                        ],
                        "type": "object",
                        "properties": {
                            "nummodelo_venda": {
                                "format": "int32",
                                "description": "Número do modelo de venda",
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
            >>> api = ModeloVenda()
            >>> response = api._buscar_plano_indexador(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ModeloVenda/BuscarPlanoIndexador"
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

    def consultar_modelo_venda(
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
        1. Consulta o modelo de vendo filtrando pelo código do modelo.
        
        Tipos de Caps:
        
        Tipo Parcelamento: 0 - Contrato                  
        1. 0 - Principal                                 
        2. 1 - Corr. por atraso                          
        3. 2 - Juros contratual                          
        4. 3 - Correção                                  
        5. 4 - Multa por atraso                          
        6. 5 - Juros por atraso                          
        7. 6 - Acrescimo                                 
        8. 7 - Desconto                                  
        9. 8 - Desconto por antecipação                  
        10. 9 - Taxa de boleto                           
        11. 10 - Desconto custas                         
        12. 11 - Repasse                                 
        13. 12 - Desconto condicional                    
        
        Tipo Parcelamento: 1 - Custas | 3 - Honorário
        1. 0 - Principal
        2. 1 - Juros contratual
        3. 2 - Correção
        4. 3 - Multa por atraso
        5. 4 - Juros por atraso
        6. 5 - Corr. por atraso
        7. 6 - Acréscimo
        8. 7 - Desconto
        9. 8 - Desconto por antecipação
        10. 9 - Taxa de boleto
        11. 10 - Desconto custa
        12. 11 - Repasse
        13. 12 - Desconto condicional
        
        Endpoint: `/api/v{version}/ModeloVenda/ConsultarModeloVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar o modelo de venda por chave
        
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
                            "codModeloVenda": {
                                "format": "int32",
                                "description": "Código modelo de venda",
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
            >>> api = ModeloVenda()
            >>> response = api._consultar_modelo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ModeloVenda/ConsultarModeloVenda"
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

    def gerar_parcelas_proposta(
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
        1. Gera parcelas da proposta baseado nos parametros de parcelas informado.
        2. Valida os campos passados na request.
        
        Endpoint: `/api/v{version}/ModeloVenda/GerarParcelasProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar parcelas da proposta baseado em parametros de parcelas. Pode ser usado para propostas e vendas.
        
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
                            "parametromodelovenda",
                            "codigoEmpresa",
                            "codigoObra"
                        ],
                        "type": "object",
                        "properties": {
                            "parametromodelovenda": {
                                "description": "Lista com os parametro para gerar as parcelas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ModeloVenda.PropostaParamModeloVenda"
                                }
                            },
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código do modelo de venda",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "redistribuirValor": {
                                "description": "Irá redistribuir valor da parcela",
                                "type": "boolean"
                            },
                            "utilizarCap": {
                                "description": "Irá utlizar cap para gerar as parcelas",
                                "type": "boolean"
                            },
                            "tipoVenda": {
                                "format": "int32",
                                "description": "Tipo da venda",
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
            >>> api = ModeloVenda()
            >>> response = api._gerar_parcelas_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ModeloVenda/GerarParcelasProposta"
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

    def consultar_modelo_de_venda(
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
        1. Consulta o modelo da venda filtrando os parâmetros informados na request.
        
        Endpoint: `/api/v{version}/ModeloVenda/ConsultarModeloDeVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta o modelo de venda
        
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
                            "obra",
                            "empresa",
                            "nummodelo_venda",
                            "tipo"
                        ],
                        "type": "object",
                        "properties": {
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "nummodelo_venda": {
                                "format": "int32",
                                "description": "Código do Modelo de venda",
                                "type": "integer"
                            },
                            "eat_inat": {
                                "format": "int32",
                                "description": "Status 0-Ativos 1-Inativos 2-Ambos",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
                                "type": "integer"
                            },
                            "campos_retornados": {
                                "description": "Nome dos campos a serem retornados",
                                "type": "string"
                            },
                            "tipo": {
                                "format": "int32",
                                "description": "Tipo do modelo de venda 0 - Venda 1 - Renegociação",
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
            >>> api = ModeloVenda()
            >>> response = api._consultar_modelo_de_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ModeloVenda/ConsultarModeloDeVenda"
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

    def montar_modelo_renegociacao(
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
        
        Permite gerar parâmetros do modelo e as parcelas para uma renegociação.
        1. Somente usuários autenticados podem ter acesso a essa rota.
        2. As informações recebidas no request devem existirem no UAU.
        3. O modelo de venda deve estar aprovado para ser utilizado.
        4. O modelo de venda informada está vinculado a empresa/obra informada.
        5. Os valores de custas, seguros e contratos devem estar configurados para o modelo.
        
        Atenção:
        1. Os campos DtIdxParc e DtJurParc são postos como o dia atual da venda caso o modelo esteja configurada para receber a data da venda.
        
        Anexos:
        
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777189/
        - Exemplo Retorno: https://ajuda.globaltec.com.br/download/777192/
        
        Endpoint: `/api/v{version}/ModeloVenda/MontarModeloRenegociacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Monta modelo de renegociação com os parâmetros das parcelas e as parcelas.
        
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
                            "codModeloVenda",
                            "empresa",
                            "obra",
                            "numVenda"
                        ],
                        "type": "object",
                        "properties": {
                            "codModeloVenda": {
                                "format": "int32",
                                "description": "Código do modelo de renegociação",
                                "type": "integer"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra da empresa",
                                "type": "string"
                            },
                            "numVenda": {
                                "format": "int64",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "ValorRenegContrato": {
                                "format": "double",
                                "description": "Valor da renegociação do contrato",
                                "type": "number"
                            },
                            "ValorRenegCustas": {
                                "format": "double",
                                "description": "Valor da renegociação das custas",
                                "type": "number"
                            },
                            "ValorRenegSeguroMIP": {
                                "format": "double",
                                "description": "Valor da renegociação do seguro MIP",
                                "type": "number"
                            },
                            "ValorRenegSeguroDFI": {
                                "format": "double",
                                "description": "Valor da renegociação do seguro DFI",
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
            >>> api = ModeloVenda()
            >>> response = api._montar_modelo_renegociacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ModeloVenda/MontarModeloRenegociacao"
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

    def consultar_parcelas_modelo_venda(
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
        1. Consultar todos os tipo de parcelas do modelo de venda filtrando pela chave/número do modelo.
        
        Endpoint: `/api/v{version}/ModeloVenda/ConsultarParcelasModeloVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar parcelas do modelo de vendas
        
        
        De to´do tipo de parcelamento.
        
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
                            "nummodelo_venda"
                        ],
                        "type": "object",
                        "properties": {
                            "nummodelo_venda": {
                                "format": "int32",
                                "description": "Número do modelo de vendas",
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
            >>> api = ModeloVenda()
            >>> response = api._consultar_parcelas_modelo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ModeloVenda/ConsultarParcelasModeloVenda"
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

    def consultar_modelo_de_venda_seguro_por_chave(
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
        1. Consulta o mo seguro do modelo de venda filtrando pela chave/número do modelo.
        
        Endpoint: `/api/v{version}/ModeloVenda/ConsultarModeloDeVendaSeguroPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta o seguro do modelo de venda
        
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
                            "nummodelo_venda"
                        ],
                        "type": "object",
                        "properties": {
                            "nummodelo_venda": {
                                "format": "int32",
                                "description": "Número do modelo de vendas",
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
            >>> api = ModeloVenda()
            >>> response = api._consultar_modelo_de_venda_seguro_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ModeloVenda/ConsultarModeloDeVendaSeguroPorChave"
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

