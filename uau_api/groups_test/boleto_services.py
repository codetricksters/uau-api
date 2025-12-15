from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class BoletoServices:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pdfcarne(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com os dados do usuário para uso do método.
        3. O retorno será um base64. Para poder visualizar os carnês, é necessário fazer uma conversão para PDF.
        
        Regras de Negócio:
        1. Para realizar a requisição, informar apenas um filtro. Caso o filtro de chaves do boleto for informado, o filtro de venda remessa, não deve ser informado. O mesmo para o caso contrário.
        2. CarneTresBoletosPaginaNaVertical, irá gerar três boletos por página
        3. CarneDoisBoletosPaginaNaHorizontal irá gerar dois boletos por página na horizontal
        4. Informar apenas um dos parametros de layout de carnê por página como true, caso um seja true, o outro deverá ser informado como false.
        5. No filtro de venda remessa, caso não deseje passar o numeroRemessa, não o inclua na chave ou passe o valor como 0.
        
        Endpoint: `/api/v{version}/BoletoServices/GerarPDFCarne`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna os carnês em formato base64 conforme os dados informados.
        
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
                            "CarneTresBoletosPaginaNaVertical",
                            "CarneDoisBoletosPaginaNaHorizontal"
                        ],
                        "type": "object",
                        "properties": {
                            "filtroChavesBoleto": {
                                "description": "Filtro de chaves do boleto",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.BoletoServices.FiltroChaveBoleto"
                                }
                            },
                            "filtroVendaRemessa": {
                                "$ref": "#/definitions/UAUApi.Models.BoletoServices.FiltroVendaRemessa",
                                "description": "Filtro de venda e remessa"
                            },
                            "CarneTresBoletosPaginaNaVertical": {
                                "description": "Indica se o carnê terá três boletos por página na vertical",
                                "type": "boolean"
                            },
                            "CarneDoisBoletosPaginaNaHorizontal": {
                                "description": "Indica se o carnê terá dois boletos por página na horizontal",
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
            >>> api = BoletoServices()
            >>> response = api._gerarpdf_carne(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/GerarPDFCarne"
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

    def gerar_pdfboleto(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Utilize em conversor de string Base64 para PDF.
        
        Definição de Negócio:
        Permite gerar boleto.
        
        1. O parâmetro booleano (true ou false) "ocultar_dados_pessoais" determina se <br />
        os dados pessoais do cliente (nome completo e endereço) serão exibidos no PDF do boleto gerado.
        2. O parâmetro inteiro "cod_banco" deve ser informado sem zeros a esquerda por se tratar de um número inteiro <br />
        
        Endpoint: `/api/v{version}/BoletoServices/GerarPDFBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar boleto
        
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
                            "cod_banco": {
                                "format": "int32",
                                "description": "Número do banco",
                                "type": "integer"
                            },
                            "seu_numero": {
                                "format": "int64",
                                "description": "Seu número do boleto",
                                "type": "integer"
                            },
                            "ocultar_dados_pessoais": {
                                "description": "Ocultar informações do pagador",
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
            >>> api = BoletoServices()
            >>> response = api._gerarpdf_boleto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/GerarPDFBoleto"
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

    def obter_codigo_de_barras(
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
        1. Busca o número do código de barras do boleto informado.
        2. Caso boleto que deseja consultar seja gerado via intermediário digital informar: código do banco e seu número
        
        Endpoint: `/api/v{version}/BoletoServices/ObterCodigoDeBarras`
        HTTP Method: `POST`
        
        Implementation Notes:
        Monta o valor do código de barras do boleto
        
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
                            "cod_banco": {
                                "description": "Identificação do Banco",
                                "type": "string"
                            },
                            "seu_numero": {
                                "description": "Identificação do Boleto seu número",
                                "type": "string"
                            },
                            "data_venc": {
                                "format": "date-time",
                                "description": "Data de Vencimento do boleto",
                                "type": "string"
                            },
                            "valor_nominal": {
                                "format": "double",
                                "description": "Valor Nominal do título",
                                "type": "number"
                            },
                            "campo_livre": {
                                "description": "Campo livre utilizado de acordo com a especificação interna do banco emissor",
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
            >>> api = BoletoServices()
            >>> response = api._obter_codigo_de_barras(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/ObterCodigoDeBarras"
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

    def obter_linha_digitavel(
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
        1. Consulta a linha digitável do código de barras.
        
        Endpoint: `/api/v{version}/BoletoServices/ObterLinhaDigitavel`
        HTTP Method: `POST`
        
        Implementation Notes:
        Monta a linha digitável descrição número do código de barras
        
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
                            "codigode_barras": {
                                "description": "Código de barras",
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
            >>> api = BoletoServices()
            >>> response = api._obter_linha_digitavel(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/ObterLinhaDigitavel"
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

    def alterar_data_vencimento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio: Permite alterar a data de vencimento de um boleto cadastrado no UAU.
        1. Não é permitido alterar a data de vencimento para um boleto excluído.
        2. Não é permitido alterar a data de vencimento para um boleto antecipado.
        3. Não é permito alterar data de vencimento de um boleto gerado via intermediario digital.
        4. Para manutenção de boleto, o campo Nosso Número não pode estar vazio.
        5. A nova data de vencimento do boleto não pode ser menor que a data original.
        6. Não é permitido alterar a data de vencimento para um boleto dos bancos 246-ABC, 353-SANTANDER e 425-SOCINAL.
        7. Não é permitido alterar a data de vencimento para um boleto com tipo de cobrança "Débito Automático" nos bancos; 1 (carteira 2), 341 (carteira 2) e 104 (carteira 5).
        8. Para boletos do banco "341 - Itau", "01 - Banco do Brasil", "425 - Banco Socinal"  ou "104 - Caixa Econômica Federal" débito automático, carteira "00 - Débito automático" só é permitido a ação "1 - Cancelamento".
        9. Alguns bancos não possuem a opção de alteração de vencimento implementada. A API informará se não puder realizar a alteração.
        
        
        Anexos:
        1. Exemplo Postman: https://ajuda.globaltec.com.br/wp-content/uploads/2019/06/BoletoUAU.postman_collection.zip
        2. Exemplo Retorno: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/AlterarDataVencimento.retorno.zip
        
        Endpoint: `/api/v{version}/BoletoServices/AlterarDataVencimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Altera a data de vencimento do boleto
        
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
                            "seuNumero",
                            "codBanco",
                            "codEmpresa",
                            "novaDataVenc"
                        ],
                        "type": "object",
                        "properties": {
                            "seuNumero": {
                                "format": "int64",
                                "description": "Seu número do boleto",
                                "type": "integer"
                            },
                            "codBanco": {
                                "format": "int32",
                                "description": "Código do banco do boleto",
                                "type": "integer"
                            },
                            "codEmpresa": {
                                "format": "int64",
                                "description": "Código da empresa cadastrada no UAU",
                                "type": "integer"
                            },
                            "novaDataVenc": {
                                "format": "date-time",
                                "description": "Nova data de vencimento do boleto",
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
            >>> api = BoletoServices()
            >>> response = api._alterar_data_vencimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/AlterarDataVencimento"
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

    def consultar_status_boleto(
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
        1. Possibilita consulta status do boleto.
        
        Endpoint: `/api/v{version}/BoletoServices/ConsultarStatusBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta status do boleto
        
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
                            "codigoBanco": {
                                "format": "int32",
                                "description": "Número do banco",
                                "type": "integer"
                            },
                            "seuNumero": {
                                "format": "int64",
                                "description": "Seu número do boleto",
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
            >>> api = BoletoServices()
            >>> response = api._consultar_status_boleto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/ConsultarStatusBoleto"
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

    def obter_mensagem_do_boleto(
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
        1. Consulta a mensagem do boleto informado nos parâmetros da request.
        
        Endpoint: `/api/v{version}/BoletoServices/ObterMensagemDoBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta a mensagem do boleto
        
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
                            "seu_numero": {
                                "format": "int64",
                                "description": "Seu número do boleto",
                                "type": "integer"
                            },
                            "cod_banco": {
                                "format": "int32",
                                "description": "Código do banco",
                                "type": "integer"
                            },
                            "cod_empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "instrucao": {
                                "description": "Instrução do boleto",
                                "type": "string"
                            },
                            "carteira": {
                                "description": "Carteira utilizada",
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
            >>> api = BoletoServices()
            >>> response = api._obter_mensagem_do_boleto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/ObterMensagemDoBoleto"
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

    def consultar_dados_do_boleto(
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
        1. Consulta informações contidas no boleto.
        
        Endpoint: `/api/v{version}/BoletoServices/ConsultarDadosDoBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Busca os dados vinculados a um boleto (inclui boletos agrupados)
        
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
                            "cod_banco": {
                                "description": "Número do Banco",
                                "type": "string"
                            },
                            "seu_numero": {
                                "description": "Seu Número - Uma das chaves para o boleto",
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
            >>> api = BoletoServices()
            >>> response = api._consultar_dados_do_boleto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/ConsultarDadosDoBoleto"
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

    def consultar_boletos_do_cliente(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Consulta ou não boletos vencidos.
        
        Definição de Negócio:
        
        Consulta boletos por cliente.
        1. Consulta boletos por cliente.
        2. Ao definir que não irá mostrar boletos vencidos, serão retornados apenas os boletos a vencer.
        3. Ao definir que deve mostrar boletos vencidos, serão retornados boletos vencidos e a vencer.
        4. Parcelas que possuem mais de um boleto ativo, não terão os boletos trazidos na consulta, 
           devido a quem For obter/utilizar o retorno, não saber qual dos boletos deve ser impresso e pago.
        5. Parcelas que possuem um único boleto ativo, terão os boletos trazidos na consulta.
        6. Os boletos serão listados em ordem crescente de vencimento.
        7. Os boletos que não tiverem o Nosso número banco preenchidos mão serão mostrados.
        8. Serão mostrados somente os boletos que estiverem com os status a seguir:
            - 0 - Normal
            - 1 - Pendente de confirmação de alteração de vencimento
            - 2 - Pendente de cancelamento de boleto
            - 3 - Confirmada alteração de vencimento/cancelamento
            - 4 - Confirmada alteração de vencimento
            - 6 - Registrado online
            - 10 - Pendente para confirmação de alteração de valor do boleto
            - 11 - Confirmada alteração de valor do boleto
        
        Endpoint: `/api/v{version}/BoletoServices/ConsultarBoletosDoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta boletos de cliente
        
        Consulta os boletos de um determinado cliente exibindo ou não boletos vencidos.
        
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
                            "codPessoa"
                        ],
                        "type": "object",
                        "properties": {
                            "codPessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "naoMostraBoletoVencido": {
                                "description": "Consultar boletos vencidos\r\nTrue  - Não consulta boletos que estiverem vencidos retorna somente os boletos a vencer\r\nFalse - Retorna os boletos vencidos e a vencer, obedecendo a regra de ter somente um boleto por parcela",
                                "type": "boolean"
                            },
                            "usuario": {
                                "description": "Login do usuário",
                                "type": "string"
                            },
                            "tipo_usuario": {
                                "format": "int32",
                                "description": "Tipo do usuário 0 = USUÁRIO UAU, 1 = USUÁRIO CLIENTE.",
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
            >>> api = BoletoServices()
            >>> response = api._consultar_boletos_do_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/ConsultarBoletosDoCliente"
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

    def consultar_boletos_reimpressao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio: Consultar boletos disponíveis para reimpressão.
        1. Valida usuário logado do tipo (pessoa/cliente).
        2. Valida código do usuário.
        3. Parcelas que possuem mais de um boleto ativo, não terão os boletos trazidos na consulta, 
           devido a quem for obter/utilizar o retorno, não saber qual dos boletos deve ser impresso e pago.
        4. Parcelas que possuem um único boleto ativo, terão os boletos trazidos na consulta.
        5. Os boletos serão listados em ordem crescente de vencimento'
        
        Endpoint: `/api/v{version}/BoletoServices/ConsultarBoletosReimpressao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar boletos disponíveis para reimpressão
        
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
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "num_venda": {
                                "format": "int32",
                                "description": "Número da venda/compra realizada pelo cliente",
                                "type": "integer"
                            },
                            "naomostraboleto_vencido": {
                                "description": "Indica se irá trazer boletos vencidos ou não\r\nTrue  - Exibe somente os boletos vencidos na data atual ou a vencer\r\nFalse - Exibe todos os boletos",
                                "type": "boolean"
                            },
                            "mostrarApenasUltimoBoleto": {
                                "description": "Opcional\r\nIndica se irá trazer último boleto para parcelas com mais de um boleto\r\nTrue  - Exibe somente o último boleto gerado de cada parcela\r\nFalse - Não exibe boletos de parcelas com mais de um boleto gerado",
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
            >>> api = BoletoServices()
            >>> response = api._consultar_boletos_reimpressao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/BoletoServices/ConsultarBoletosReimpressao"
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

