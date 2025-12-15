from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Autenticador:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def logout_usuario(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Autenticador/LogoutUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza o logout de um usuário destruíndo a sessão do usuário logado
        
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
            >>> api = Autenticador()
            >>> response = api._logout_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Autenticador/LogoutUsuario"
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

    def autenticar_usuario(
        self,
        version: str,
        param: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        1. Verifica o método de Login configurado no Sistema Uau https://ajuda.globaltec.com.br/virtuau/configuracao-de-seguranca/ 
        2. Empresa configurada com Autenticação AD e utilizar este serviço a autenticação será como Cliente/Pessoa.
        3. Empresa configurada com Autenticação Uau
           - Login do usuário maior que 8 caracteres a autenticação será como Cliente/Pessoa.
           - Login do usuário menor que 8 caracteres a autenticação será Uau.
        4. Para utilizar o recurso de GerarBoleto deve-se informar a propriedade UsuarioUAUSite.
           
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_Uau
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_via_Active_Directory
        
        Anexos: 
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/774812/
        
        Endpoint: `/api/v{version}/Autenticador/AutenticarUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Autenticação padrão do Uau via usuário e senha cadastrados no banco de dados.
        
        Args:
            param (Dict[str, Any]): The param
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "param": {
                    "definition": {
                        "description": "Essa classe está como exemplo das validações usando o DataAnnotation e o FluentValidation \r\nsendo que o mesmo pode ser usado dentro do projeto simultaneamente",
                        "required": [
                            "Login",
                            "Senha"
                        ],
                        "type": "object",
                        "properties": {
                            "Login": {
                                "description": "Login do usuário",
                                "type": "string"
                            },
                            "Senha": {
                                "description": "Senha do usuário",
                                "type": "string"
                            },
                            "UsuarioUAUSite": {
                                "description": "Login de usuário do UAU que tem\r\npermissão de gerar boletos.",
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
                    "required": false,
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
            >>> api = Autenticador()
            >>> response = api._autenticar_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Autenticador/AutenticarUsuario"
        kwargs = {
            "param": param,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def autenticar_usuario_app(
        self,
        version: str,
        param: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        caso contrário será validado como usuário UAU ou Cliente.
        Atualmente utilizado pela API do Mobile.
        
        Endpoint: `/api/v{version}/Autenticador/AutenticarUsuarioApp`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a autenticação do usuário e senha verificando o método de login sendo AD será autenticado o usuário corporativo,
        caso contrário será validado como usuário UAU ou Cliente.
        Atualmente utilizado pela API do Mobile.
        
        Args:
            param (Dict[str, Any]): The param
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "param": {
                    "definition": {
                        "description": "Essa classe está como exemplo das validações usando o DataAnnotation e o FluentValidation \r\nsendo que o mesmo pode ser usado dentro do projeto simultaneamente",
                        "required": [
                            "Login",
                            "Senha"
                        ],
                        "type": "object",
                        "properties": {
                            "Login": {
                                "description": "Login do usuário",
                                "type": "string"
                            },
                            "Senha": {
                                "description": "Senha do usuário",
                                "type": "string"
                            },
                            "UsuarioUAUSite": {
                                "description": "Login de usuário do UAU que tem\r\npermissão de gerar boletos.",
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
                    "required": false,
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
            >>> api = Autenticador()
            >>> response = api._autenticar_usuario_app(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Autenticador/AutenticarUsuarioApp"
        kwargs = {
            "param": param,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def verifica_usuario_logado(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Autenticador/VerificaUsuarioLogado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Verifica se um usuário está logado
        
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
                    "required": false,
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
            >>> api = Autenticador()
            >>> response = api._verifica_usuario_logado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Autenticador/VerificaUsuarioLogado"
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

    def consultar_dados_usr_logado(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Permite consultar os dados do usuário do tipo cliente do Cadastro de Pessoas do Uau.
        1. O usuário cliente deve estar autenticado.
        2. Retorna as informações do cliente logado, conforme a estrutura abaixo.
        
        - Estrutura do Retorno: https://ajuda.globaltec.com.br/download/774818/
        3. Dados Pessoais: 
            - codigo = Código do cliente
            - nome = Nome completo
            - cpf = CPF
            - dtnasc = Data de nascimento
            - email = E-mail
            - login = Login do Cliente no UAU Web
            - senha = Senha do cliente
        4. Dados do Telefone:
            - codigo = Código do cliente
            - numero = Número do telefone do cliente
            - ddd = DDD do telefone
            - ramal = Ramal do telefone do cliente
            - tipo = Tipo do telefone (0-residencial;1-comercial;2-celular;3-recado;4-fax;5-bip;6-telex;7-outros;8-fone/fax)
        5. Dados do Endereço:
            - codPes = Código do cliente
            - tipoEndereco = 0-Principal 1-Cobrança 2-Comercial
            - endereco = Endereço do cliente
            - complemento = Complemento do endereço
            - numero = Número do endereço do cliente
            - referencia = Referência do endereço
            - bairro = Bairro
            - cep = CEP
            - cidade = Cidade
            - uf = UF
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Consultar_dados_do_Usuario_Logado
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/774809/
        - Exemplo Retorno: https://ajuda.globaltec.com.br/download/774818/
        
        Endpoint: `/api/v{version}/Autenticador/ConsultarDadosUsrLogado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os dados pessoais, endereço e telefone do usuário logado. Só consulta os dados caso o
        usuário logado seja do tipo pessoa. Caso contrário uma exceção é lançada informando que
        o usuário logado precisa ser do tipo pessoa para este método.
        
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
            >>> api = Autenticador()
            >>> response = api._consultar_dados_usr_logado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Autenticador/ConsultarDadosUsrLogado"
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

    def autentificar_usuario_titanium(
        self,
        version: str,
        param: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Autenticador/AutentificarUsuarioTitanium`
        HTTP Method: `POST`
        
        Implementation Notes:
        Faz a autenticação de um usuário titanium
        
        Args:
            param (Dict[str, Any]): The param
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "param": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "type": "string"
                            },
                            "senha": {
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
                    "required": false,
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
            >>> api = Autenticador()
            >>> response = api._autentificar_usuario_titanium(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Autenticador/AutentificarUsuarioTitanium"
        kwargs = {
            "param": param,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def autenticar_usuario_corporativo(
        self,
        version: str,
        param: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        1. Verifica o método de Login configurado no Sistema Uau https://ajuda.globaltec.com.br/virtuau/configuracao-de-seguranca/ 
        2. Empresa configurada para método de Login Uau via banco de dados
           - Será realizada a verificação se existe o usuário com a senha informada.
        3. Empresa configurada para método de Login via AD
           - Será realizada a autenticação validando no Active Directory
        4. No parâmetro login_uau do corpo da requisição, deve ser informado o login que é utilizado no uau quando o Active Directory não está habilitado. 
           - A informação do login do usuário está no módulo segurança.  
           
        VirtUau: 
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_via_Active_Directory
        
        Anexos: 
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/774812/
        
        Endpoint: `/api/v{version}/Autenticador/AutenticarUsuarioCorporativo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a autenticação do usuário através do Active Directory
        
        Args:
            param (Dict[str, Any]): The param
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "param": {
                    "definition": {
                        "required": [
                            "login_ad",
                            "senha",
                            "login_uau"
                        ],
                        "type": "object",
                        "properties": {
                            "login_ad": {
                                "description": "Login de rede AD",
                                "type": "string"
                            },
                            "senha": {
                                "description": "Senha de rede AD",
                                "type": "string"
                            },
                            "login_uau": {
                                "description": "Login do usuário Uau",
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
                    "required": false,
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
            >>> api = Autenticador()
            >>> response = api._autenticar_usuario_corporativo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Autenticador/AutenticarUsuarioCorporativo"
        kwargs = {
            "param": param,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

