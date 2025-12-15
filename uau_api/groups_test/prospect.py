from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Prospect:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gravar_prospect(
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
        1. Grava as informações do prospect.
        2. Os dados informados passam por validações.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Prospect/GravarProspect`
        HTTP Method: `POST`
        
        Implementation Notes:
        Grava as informações do prospect
        
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
                            "permitirResponsavelSemEstrutura": {
                                "description": "Indica se deve permitir o responsável não estar em uma estrutura de comissão",
                                "type": "boolean"
                            },
                            "login": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "prospect": {
                                "$ref": "#/definitions/UAUApi.Models.Prospect.Prospect",
                                "description": "Dados do prospect"
                            },
                            "prospectFis": {
                                "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectFis",
                                "description": "Dados adicionais do prospect"
                            },
                            "prospectInteresse": {
                                "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectInteresse",
                                "description": "Dados dos interesses (pretensões) do prospect"
                            },
                            "prospectInteresseProdutos": {
                                "description": "Dados dos produtos dos interesses (pretensões) do prospect",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectInteresseProduto"
                                }
                            },
                            "prospectInteresseBairros": {
                                "description": "Dados dos bairros dos interesses (pretensões) do prospect",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectInteresseBairro"
                                }
                            },
                            "prospectTelefones": {
                                "description": "Dados dos telefones do prospect",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectTelefone"
                                }
                            },
                            "prospectEnderecoPrincipal": {
                                "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectEndereco",
                                "description": "Dados do endereço principal do prospect"
                            },
                            "prospectEnderecoCobranca": {
                                "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectEndereco",
                                "description": "Dados do endereço de cobrança do prospect"
                            },
                            "prospectEnderecoComercial": {
                                "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectEndereco",
                                "description": "Dados do endereço comercial do prospect"
                            },
                            "prospectDependente": {
                                "description": "Lista de dependentes do prospect",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectDependente"
                                }
                            },
                            "responsavel": {
                                "description": "Nome do Responsável pelo prospect",
                                "type": "string"
                            },
                            "buscouDePessoas": {
                                "description": "Indica se buscou os dados de pessoas",
                                "type": "boolean"
                            },
                            "atualizarPessoas": {
                                "description": "Indica se irá atualizar os dados de pessoas",
                                "type": "boolean"
                            },
                            "mensagemRetorno": {
                                "description": "Mensagem de retorno",
                                "type": "string"
                            },
                            "prospectDoc": {
                                "description": "Lista de documentos do prospect",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Prospect.ProspectDoc"
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
            >>> api = Prospect()
            >>> response = api._gravar_prospect(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/GravarProspect"
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

    def importar_prospect(
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
        1. Importa prospects para dentro do UAU.
        2. Valida usuário e permissões.
        3. Valida arquivo XML.
        
        Informação:
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Prospect/ImportarProspect`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a importação de prospects para o UAU
        
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
                            "xml"
                        ],
                        "type": "object",
                        "properties": {
                            "xml": {
                                "description": "Arquivo XML com os dados a serem importados.",
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
            >>> api = Prospect()
            >>> response = api._importar_prospect(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/ImportarProspect"
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

    def listar_grau_parentesco(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
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
            >>> api = Prospect()
            >>> response = api._listar_grau_parentesco(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/ListarGrauParentesco"
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

    def migrar_prospect_pessoa(
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
        1. Migra um prospect para pessoa.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Prospect/MigrarProspectPessoa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a migração dos dados do prospect para pessoa
        
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
                            "numeroProspect"
                        ],
                        "type": "object",
                        "properties": {
                            "numeroProspect": {
                                "format": "int32",
                                "description": "Número do prospect.",
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
            >>> api = Prospect()
            >>> response = api._migrar_prospect_pessoa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/MigrarProspectPessoa"
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

    def consultar_todos_prospects(
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
        1. Consulta os prospects de acordo com os parâmetros definidos na request.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Prospect/ConsultarTodosProspects`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar todos os prospects
        
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
                            "enumOpcaoTodos": {
                                "format": "int32",
                                "description": "Tipo de prospects\r\n0 - Todos os prospects, 1 - Todos os prospects, exceto os prospects informados, 2 - Somente os prospects informados, 3 - Todos os prospects sem responsável e do responsável informado, 4 - Todos os prospects sem responsável e do responsável informado, exceto os prospects informados.",
                                "enum": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4
                                ],
                                "type": "integer"
                            },
                            "codigoProspect": {
                                "description": "Filtra pelo código do prospect",
                                "type": "string"
                            },
                            "codigoVendedor": {
                                "format": "int32",
                                "description": "Filtra pelo código do vendedor",
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
            >>> api = Prospect()
            >>> response = api._consultar_todos_prospects(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/ConsultarTodosProspects"
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

    def consultar_prospect_por_chave(
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
        1. Consulta determinado prospect filtrando pelo número deste prospect.
        
        Informação:
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Prospect/ConsultarProspectPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar prospect por código
        
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
                            "codigoProspect"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoProspect": {
                                "format": "int32",
                                "description": "Número do prospect",
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
            >>> api = Prospect()
            >>> response = api._consultar_prospect_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/ConsultarProspectPorChave"
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

    def alterar_responsavel_prospect(
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
        1. Alterar responsável do prospect.
        2. Os dados informados passam por validações.
        3. O campo codEmpresa não é obrigatório, porém, se informado será validado se na configuração da empresa está marcado para 
        "Realizar venda somente se o vendedor estiver em uma estrutura de comissão", e caso o novo responsável não esteja em nenhuma
        estrutura de comissão, não será possível incluir. Caso não esteja marcado a configuração ou o codEmpresa não for informado,
        será possível alterar para qualquer novo responsável, desde que esteja ativo.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Prospect/AlterarResponsavelProspect`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar responsável do prospect
        
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
                            "novoResponsavel",
                            "numProspect"
                        ],
                        "type": "object",
                        "properties": {
                            "novoResponsavel": {
                                "format": "int32",
                                "description": "Código do novo responsável do prospect.",
                                "type": "integer"
                            },
                            "codEmpresa": {
                                "format": "int32",
                                "description": "código da empresa.",
                                "type": "integer"
                            },
                            "numProspect": {
                                "format": "int32",
                                "description": "Número do prospect.",
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
            >>> api = Prospect()
            >>> response = api._alterar_responsavel_prospect(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/AlterarResponsavelProspect"
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

    def consultar_prospect_com_filtro(
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
        1. Consulta prospect filtrando os parâmentros inseridos da request.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Prospect/ConsultarProspectComFiltro`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta prospect de acordo com as informações do request
        
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
                            "numeroOpcao": {
                                "format": "int32",
                                "description": "Numero da operação do prospect (0= Hierarquia, 1= CodProspect, 2= NomeProspect, 3= CPFProspect)",
                                "enum": [
                                    0,
                                    1,
                                    2,
                                    3
                                ],
                                "type": "integer"
                            },
                            "numeroVisao": {
                                "format": "int32",
                                "description": "Status do do prospect (0= EmAndamento, 1= Encerrado, 2= Todos)",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
                                "type": "integer"
                            },
                            "prospectSemResponsavel": {
                                "description": "Prospect com responsável = true. Prospect sem responsável = false",
                                "type": "boolean"
                            },
                            "codigoResponsavel": {
                                "description": "Código do responsável",
                                "type": "string"
                            },
                            "nomePessoa": {
                                "description": "Nome da pessoa",
                                "type": "string"
                            },
                            "telefone": {
                                "description": "Telefone do prospect",
                                "type": "string"
                            },
                            "cpfCnpj": {
                                "description": "CPF ou CNPJ do prospect",
                                "type": "string"
                            },
                            "trataSemResponsavel": {
                                "description": "tratar com responsável = true. tratar sem responsável = false",
                                "type": "boolean"
                            },
                            "ufProsp": {
                                "description": "UF (unidade da Federação) do prospect",
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
            >>> api = Prospect()
            >>> response = api._consultar_prospect_com_filtro(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/ConsultarProspectComFiltro"
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

    def buscar_grau_parentesco_por_codigo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
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
                            "Codigo"
                        ],
                        "type": "object",
                        "properties": {
                            "Codigo": {
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
            >>> api = Prospect()
            >>> response = api._buscar_grau_parentesco_por_codigo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Prospect/BuscarGrauParentescoPorCodigo"
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

