from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class CessaoRecebiveis:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_contrato(
        self,
        version: str,
        data_contrato: Optional[str] = None,
        nome_contrato: Optional[str] = None,
        comprador: Optional[int] = None,
        chave_venda: Optional[str] = None,
        mostra_historico: Optional[Any] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <br>Dados básicos para o funcionamento da API.</br>
        <list type="bullet">
          <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
        </list>
        <b>Definição de Negócio:</b>
        <br>Consultar um contrato de cessão de recebíveis.</br>
        <list type="bullet">
          <item>1. É obrigatório informar ao menos um dos parâmetros da rota para realizar a busca.</item>
          <item>2. A data pode ser informada no padrão Dia/Mês/Ano.</item>
          <item>3. O comprador, deve ser informado o código do usuário no UAU.</item>
          <item>4. O nome contrato, deve ser informado igual ao número do contrato de cessão de recebíveis</item>
          <item>5. A chave da venda, dever ser informada no padrão Empresa|Obra|Venda.</item>
        </list>
        
        Endpoint: `/api/v{version}/CessaoRecebiveis/ConsultarContrato`
        HTTP Method: `GET`
        
        Implementation Notes:
        Consultar os dados dos contratos de cessão de recebíveis, conforme os parâmetros informado
        
        Args:
            dataContrato (Dict[str, Any]): Data do contrato
            nomeContrato (Dict[str, Any]): Nome do contrato
            comprador (Dict[str, Any]): ID do comprador
            chaveVenda (Dict[str, Any]): Chave da venda composta por Empresa|Obra|NumeroVenda. Ex.: 101|OBR01|1
            mostraHistorico (Dict[str, Any]): Controla de deverá exibir o historico de registros. O padrão é False
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "dataContrato": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": "Data do contrato"
                },
                "nomeContrato": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": "Nome do contrato"
                },
                "comprador": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": "ID do comprador"
                },
                "chaveVenda": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": "Chave da venda composta por Empresa|Obra|NumeroVenda. Ex.: 101|OBR01|1"
                },
                "mostraHistorico": {
                    "type": "boolean",
                    "in": "query",
                    "required": false,
                    "description": "Controla de deverá exibir o historico de registros. O padrão é False"
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
            >>> api = CessaoRecebiveis()
            >>> response = api._consultar_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/CessaoRecebiveis/ConsultarContrato"
        kwargs = {
            "dataContrato": data_contrato,
            "nomeContrato": nome_contrato,
            "comprador": comprador,
            "chaveVenda": chave_venda,
            "mostraHistorico": mostra_historico,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.get(
            path,
            json=params
        )
        return response

    def aprovar_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <br>Dados básicos para o funcionamento da API.</br>
        <list type="bullet">
          <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
          <item>2. Preencher os parâmetros de request para uso do método.</item>
        </list>
        <b>Definição de Negócio:</b>
        <br>Aprovar um contrato de cessão de recebíveis.</br>
        <list type="bullet">
          <item>1. É obrigatório informar os dados básicos do contrasto de cessão de recebíveis.</item>
          <item>2. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
        </list>
        
        Endpoint: `/api/v{version}/CessaoRecebiveis/AprovarContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar o contrato de cessão de recebível, conforme o identificador passado como parâmetro
        
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
                            "idContrato"
                        ],
                        "type": "object",
                        "properties": {
                            "idContrato": {
                                "format": "int32",
                                "description": "Código do contrato",
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
            >>> api = CessaoRecebiveis()
            >>> response = api._aprovar_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/CessaoRecebiveis/AprovarContrato"
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

    def inserir_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <br>Dados básicos para o funcionamento da API.</br>
        <list type="bullet">
          <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
          <item>2. Preencher os parâmetros de request para uso do método.</item>
        </list>
        <b>Definição de Negócio:</b>
        <br>Inserir um contrato de cessão de recebíveis.</br>
        <list type="bullet">
          <item>1. É obrigatório informar os dados básicos do contrasto de cessão de recebíveis.</item>
          <item>2. O usuário autenticado precisa ter acesso à empresa e obra que está fazendo a requisição.</item>
          <item>3. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
        </list>
        
        Endpoint: `/api/v{version}/CessaoRecebiveis/InserirContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Cadastra um novo contrato de cessão de recebíveis com os dados informados, que ficará pendente de aprovação caso não gere uma venda, pois aí precisará ficar aprovado
        
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
                            "Contrato",
                            "Descricao",
                            "Empresa",
                            "DataContrato",
                            "Comprador",
                            "PeriodoParcelas",
                            "ObraVenda",
                            "DataVenda",
                            "ModeloVendas",
                            "ProdutoVenda",
                            "ValorTotalVenda",
                            "RiscoContrato",
                            "PermitirRenegociacao",
                            "GerarVendaDoContrato"
                        ],
                        "type": "object",
                        "properties": {
                            "Contrato": {
                                "description": "Código do contrato",
                                "type": "string"
                            },
                            "Descricao": {
                                "description": "Drescrição do contrato",
                                "type": "string"
                            },
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "DataContrato": {
                                "format": "date-time",
                                "description": "Data do contrato",
                                "type": "string"
                            },
                            "Comprador": {
                                "description": "Informar o código ou o nome do comprador que está cadastrado no sistema",
                                "type": "string"
                            },
                            "PeriodoParcelas": {
                                "$ref": "#/definitions/UAUApi.Models.CessaoRecebiveis.PeriodoParcelas",
                                "description": "Periodo de vencimento das parcelas"
                            },
                            "Obras": {
                                "description": "Lista de obras para serem usadas como filtro na busca de parcelas.\r\n<list type=\"bullet\"><item>1. Ao informar as parcelas que faram parte do contrarto, a lista\r\n   de obras será montada conforme as empresas e obras contidas na parcela, considerando somente essas emrpesas e obras.</item></list>",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.CessaoRecebiveis.Obras"
                                }
                            },
                            "ObraVenda": {
                                "description": "Obra da venda",
                                "type": "string"
                            },
                            "DataVenda": {
                                "format": "date-time",
                                "description": "Data da venda",
                                "type": "string"
                            },
                            "ModeloVendas": {
                                "format": "int32",
                                "description": "Modelo de vendas",
                                "type": "integer"
                            },
                            "ProdutoVenda": {
                                "format": "int32",
                                "description": "O produto definido para gerar a venda do contrato",
                                "type": "integer"
                            },
                            "ValorTotalVenda": {
                                "format": "double",
                                "description": "Valor total da venda",
                                "type": "number"
                            },
                            "RiscoContrato": {
                                "description": "Contrato sem risco",
                                "type": "boolean"
                            },
                            "PermitirRenegociacao": {
                                "description": "Permitir renegociação",
                                "type": "boolean"
                            },
                            "GerarVendaDoContrato": {
                                "description": "Define se ao gerar o novo contrato de cessão de recebíveis, o sistema irá gerar a venda desse contrato automaticamente\r\n<list type=\"bullet\"><item>Serão validados as informações necessárias para gerar a venda, e também ao criar o contrato de cessebíbeis, \r\n   o mesmo já será criado aprovado, e o usuário de aprovação será o usuário que está fazendo a requisição.\r\n   A venda é gerada sobre o valor total do contrato informado, usando o modelo de venda e a obra da venda, mesmo\r\n   que não tenha parcela vincualda ao contrato, a venda será gerada.</item></list>",
                                "type": "boolean"
                            },
                            "Parcelas": {
                                "description": "Parcelas da venda de carteira",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.CessaoRecebiveis.Parcelas"
                                }
                            },
                            "GrupoCobranca": {
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
            >>> api = CessaoRecebiveis()
            >>> response = api._inserir_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/CessaoRecebiveis/InserirContrato"
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

    def gerar_venda_do_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <br>Dados básicos para o funcionamento da API.</br>
        <list type="bullet">
          <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
          <item>2. Preencher os parâmetros de request para uso do método.</item>
        </list>
        <b>Definição de Negócio:</b>
        <br>Gerar a venda um contrato de cessão de recebíveis.</br>
        <list type="bullet">
          <item>1. É obrigatório informar os dados básicos do contrasto de cessão de recebíveis.</item>
          <item>2. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
        </list>
        
        Endpoint: `/api/v{version}/CessaoRecebiveis/GerarVendaDoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar uma venda de um contrato de cessão de recebíveis, conforme o identificador passado como parâmetro
        
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
                            "idContrato"
                        ],
                        "type": "object",
                        "properties": {
                            "idContrato": {
                                "format": "int32",
                                "description": "Código do contrato",
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
            >>> api = CessaoRecebiveis()
            >>> response = api._gerar_venda_do_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/CessaoRecebiveis/GerarVendaDoContrato"
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

