from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Anexo:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def anexar_arquivo(
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
        1. Anexa arquivo dentro do UAU, utilizando a chave identificadora para fazer o vinculo desse arquivo com algum parametro dentro do sistema. 
        
        Parâmetros da request
        1. arquivo: Conteúdo do arquivo em base 64
        2. nome:  Chave identificadora Do arquivo no formato "STRING STRING"
        3. caminho: Caminho do arquivo
        4. identificador: Nome Identificador do arquivo
        5. usuario: Login do usuário
        6. caminhoExclusivo: String correspondente a configuração em configGerais do caminho exclusivo
        
        Endpoint: `/api/v{version}/Anexo/AnexarArquivo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Anexa um arquivo
        
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
                            "arquivo": {
                                "format": "byte",
                                "description": "Conteúdo do arquivo em bytes",
                                "type": "string"
                            },
                            "nome": {
                                "description": "Nome do arquivo",
                                "type": "string"
                            },
                            "caminho": {
                                "description": "Caminho do arquivo",
                                "type": "string"
                            },
                            "identificador": {
                                "description": "Chave identificadora do arquivo no formato \"STRING STRING\"",
                                "type": "string"
                            },
                            "usuario": {
                                "description": "Login do usuário",
                                "type": "string"
                            },
                            "caminhoExclusivo": {
                                "description": "String correspondente a configuração em configGerais do caminho exclusivo",
                                "type": "string"
                            },
                            "controlaAnexoUAUWeb": {
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
            >>> api = Anexo()
            >>> response = api._anexar_arquivo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/AnexarArquivo"
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

    def excluir_anexos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.       
        
        Parâmetros da request
        1. identificador: Chave identificadora do arquivo no formato "STRING STRING".
        2. nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
        3. origem: Indica o tipo de armazenamento será utilizado para excluir o vinculo ao arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.
        
        Endpoint: `/api/v{version}/Anexo/ExcluirAnexos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Exclui o vinculo do anexo ao arquivo.
        
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
                            "identificador"
                        ],
                        "type": "object",
                        "properties": {
                            "identificador": {
                                "description": "Chave identificadora do arquivo no formato \"STRING STRING\"",
                                "type": "string"
                            },
                            "nome_arquivo": {
                                "description": "Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )",
                                "type": "string"
                            },
                            "origem": {
                                "format": "int32",
                                "description": "Indica o tipo de armazenamento será utilizado para excluir o vinculo ao arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.",
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
            >>> api = Anexo()
            >>> response = api._excluir_anexos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/ExcluirAnexos"
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

    def baixar_arquivos(
        self,
        version: str,
        request_arquivos: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <list type="number">
          <item>Autenticar o usuário cliente via URI: /api/v{version}/Autenticador/AutenticarUsuario</item>
          <item>Preencher os parâmetros de request para uso do método.</item>
          <item>Utilizar a rota Anexo/ListaArquivoPorChave para obter os caminhos completos dos arquivos.</item>
        </list>
        <b>Parâmetros do Request:</b>
        <list type="bullet">
          <item>
            CaminhoCompleto: Caminho completo do arquivo que deverá ser compactado para ZIP.</item>
          <item>
            Origem (Obrigatório):
            <list type="bullet">
              <item>
                1 - Caminho local / rede</item>
              <item>
                2 - Caminho AWS.</item>
            </list>
          </item>
        </list>
        
        Endpoint: `/api/v{version}/Anexo/BaixarArquivos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna um arquivo ZIP contendo os arquivos informados por caminho.
        
        Args:
            requestArquivos (Dict[str, Any]): The arquivos
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "requestArquivos": {
                    "definition": {
                        "required": [
                            "Arquivos"
                        ],
                        "type": "object",
                        "properties": {
                            "Arquivos": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Anexo.ArquivoResponse"
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
            >>> api = Anexo()
            >>> response = api._baixar_arquivos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/BaixarArquivos"
        kwargs = {
            "requestArquivos": request_arquivos,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def listar_diretorios(
        self,
        version: str,
        diretorio: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
            * Status 200 - Retorna uma lista de diretórios
        
        Endpoint: `/api/v{version}/Anexo/ListarDiretorios`
        HTTP Method: `POST`
        
        Args:
            diretorio (Dict[str, Any]): The diretorio
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "diretorio": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Caminho": {
                                "type": "string"
                            },
                            "Origem": {
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
            >>> api = Anexo()
            >>> response = api._listar_diretorios(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/ListarDiretorios"
        kwargs = {
            "diretorio": diretorio,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def anexar_base64_imagem(
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
        Possibilita anexar imagem no formato Base64
        
        Endpoint: `/api/v{version}/Anexo/AnexarBase64Imagem`
        HTTP Method: `POST`
        
        Implementation Notes:
        Anexa uma imagem na base64
        
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
                            "arquivo": {
                                "description": "Deve estar no formato Base64 sem os prefixos",
                                "type": "string"
                            },
                            "nome": {
                                "description": "Nome do arquivo",
                                "type": "string"
                            },
                            "caminho": {
                                "description": "Caminho do arquivo",
                                "type": "string"
                            },
                            "identificador": {
                                "description": "Chave identificadora do arquivo no formato \"STRING STRING\"",
                                "type": "string"
                            },
                            "usuario": {
                                "description": "Login do usuário",
                                "type": "string"
                            },
                            "extensaoImagem": {
                                "description": "Extensao da imagem. ex: 'png' ou 'jpeg', etc",
                                "type": "string"
                            },
                            "caminhoExclusivo": {
                                "description": "String correspondente a configuração em configgerais do caminho exclusivo",
                                "type": "string"
                            },
                            "controlaAnexoUAUWeb": {
                                "description": "Indica se deverá gravar os arquivos no caminho de configuração padrão para arquivos do UAUWeb",
                                "type": "boolean"
                            },
                            "origem": {
                                "format": "int32",
                                "description": "Indica o tipo de armazenamento será utilizado para gravar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.",
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
            >>> api = Anexo()
            >>> response = api._anexar_base64_imagem(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/AnexarBase64Imagem"
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

    def lista_arquivo_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <list type="number">
          <item>Autenticar o usuário cliente via URI: /api/v{version}/Autenticador/AutenticarUsuario</item>
          <item>Preencher os parâmetros de request para uso do método.</item>
        </list>
        <b>Parâmetros da Request:</b>
        <list type="bullet">
          <item>
            chave: Identificador do arquivo.</item>
          <item>
            valores: Valores identificadores do arquivo.</item>
        </list>
         
         Para obter as chaves de utilização na requisição, utilize a rota:  
         Anexo/ConsultarChavesComentario
        
        Endpoint: `/api/v{version}/Anexo/ListaArquivoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna todos os arquivos relacionados com a chave, incluindo nome e caminho completo.
        
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
                            "Chave": {
                                "description": "Identificador do arquivo. Exemplo: \"Contrato\"",
                                "type": "string"
                            },
                            "Valores": {
                                "description": "Valores de identificação do arquivo. Exemplo: \"123\", \"1234\"",
                                "type": "array",
                                "items": {
                                    "type": "string"
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
            >>> api = Anexo()
            >>> response = api._lista_arquivo_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/ListaArquivoPorChave"
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

    def listar_armazenamentos(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Anexo/ListarArmazenamentos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna a lista de armazenamentos ativos
        
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
            >>> api = Anexo()
            >>> response = api._listar_armazenamentos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/ListarArmazenamentos"
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

    def gravar_comentario_anexo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - Adiciona comentário anexo de acordo com os parâmetros passados na requisição.
        
        Pré requisito:
        - Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
            - URL + /api/v{version}/Anexo/ConsultarChavesComentario
            
        Parâmetros da request
        1. Chave: Chave para consulta.
        2. Campos: Campos obrigatórios para a chave="Venda" (empresa, obra, venda). Campos obrigatórios para a chave="Contrato" (Empresa, Contrato) Deve ser inserido juntos, separados por virgula.
        3. Usuario: Usuário logado.
        4. Comentario: Comentário a ser anexado.
        5. TipoComentario: Armazena o tipo do comentário ( 0-Publico, 1-Privado, 2-Interna).
        6. UsuarioPrivado: Armazena a lista de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarUsuariosAtivos ).
        7. GrupoPrivado: Armazena a lista de grupos de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarGruposDeUsuario ).
        
        Endpoint: `/api/v{version}/Anexo/GravarComentarioAnexo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Anexar um comentario
        
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
                            "Chave",
                            "Campos",
                            "Usuario",
                            "Comentario"
                        ],
                        "type": "object",
                        "properties": {
                            "Chave": {
                                "description": "Chave para consulta",
                                "type": "string"
                            },
                            "Campos": {
                                "description": "Campos obrigatórios para a chave=\"Venda\" (empresa, obra, venda). Campos obrigatórios para a chave=\"Contrato\" (Empresa, Contrato)\r\nDeve ser inserido juntos, separados por virgula.",
                                "type": "string"
                            },
                            "Usuario": {
                                "description": "Usuário logado",
                                "type": "string"
                            },
                            "Comentario": {
                                "description": "Comentário a ser anexado.",
                                "type": "string"
                            },
                            "TipoComentario": {
                                "description": "Armazena o tipo do comentário ( 0-Publico, 1-Privado, 2-Interna).",
                                "type": "string"
                            },
                            "UsuarioPrivado": {
                                "description": "Armazena a lista de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarUsuariosAtivos )",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Anexo.Usuario"
                                }
                            },
                            "GrupoPrivado": {
                                "description": "Armazena a lista de grupos de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarGruposDeUsuario )",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Anexo.Grupo"
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
            >>> api = Anexo()
            >>> response = api._gravar_comentario_anexo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/GravarComentarioAnexo"
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

    def retorna_arquivo_em_bytes(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        
        Definição Técnica:
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Parâmetros da request
        1. nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
        2. origem: Indica o tipo de armazenamento será utilizado para buscar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.
        
        Endpoint: `/api/v{version}/Anexo/RetornaArquivoEmBytes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna um determinado arquivo em base64.
        
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
                            "nome_arquivo": {
                                "description": "Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )",
                                "type": "string"
                            },
                            "origem": {
                                "format": "int32",
                                "description": "Indica o tipo de armazenamento será utilizado para buscar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.",
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
            >>> api = Anexo()
            >>> response = api._retorna_arquivo_em_bytes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/RetornaArquivoEmBytes"
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

    def consultar_chaves_comentario(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - Este endpoint oferece suporte para o seguinte endpoint: [URI + /api/v{version}/Anexo/GravarComentarioAnexo]
        - Retorna objetos com:
            - Possíveis chaves que podem ser utilizadas.
            - Ordem dos parâmetros aceitos.
            - Exemplo de utilização e formatação dos parâmetros.
         Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777152/
        
        Endpoint: `/api/v{version}/Anexo/ConsultarChavesComentario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna as chaves, seus campos e exemplo, que podem ser utilizadas para gravação de comentario em anexo.
        
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
            >>> api = Anexo()
            >>> response = api._consultar_chaves_comentario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/ConsultarChavesComentario"
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

    def anexar_arquivos_base64_request(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Projeto   : FVS Mobile
        
        Endpoint: `/api/v{version}/Anexo/AnexarArquivosBase64Request`
        HTTP Method: `POST`
        
        Implementation Notes:
        Anexa um arquivo
        
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
                            "lista_arquivos": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Anexo.EstruturaAnexoBase64"
                                }
                            },
                            "empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
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
            >>> api = Anexo()
            >>> response = api._anexar_arquivos_base64_request(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/AnexarArquivosBase64Request"
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

    def retornar_arquivos_em_lista_bytes(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
                
        
        Definição Técnica:
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.       
        
        Parâmetros da request
        1. empresa: Número da empresa.
        2. identificador: Chave identificadora do arquivo no formato "STRING STRING".
        3. listanomes_arquivos:  Lista de 'string' com o nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
        
        Endpoint: `/api/v{version}/Anexo/RetornarArquivosEmListaBytes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna uma lista com os dados dos arquivos e o conteúdo do mesmo em base64.
        
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
                            "identificador"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "description": "Número da empresa",
                                "type": "string"
                            },
                            "identificador": {
                                "description": "Chave identificadora do arquivo no formato \"STRING STRING\"",
                                "type": "string"
                            },
                            "listanomes_arquivos": {
                                "description": "Lista de 'string' com o nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )",
                                "type": "array",
                                "items": {
                                    "type": "string"
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
            >>> api = Anexo()
            >>> response = api._retornar_arquivos_em_lista_bytes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Anexo/RetornarArquivosEmListaBytes"
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

