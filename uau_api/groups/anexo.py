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
        arquivo: Optional[str] = None,
        nome: Optional[str] = None,
        caminho: Optional[str] = None,
        identificador: Optional[str] = None,
        usuario: Optional[str] = None,
        caminho_exclusivo: Optional[str] = None,
        controla_anexouau_web: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/AnexarArquivo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Anexa arquivo dentro do UAU, utilizando a chave identificadora para fazer o vinculo desse arquivo com algum parametro dentro do sistema. 
        
        Parâmetros da request
        
        arquivo: Conteúdo do arquivo em base 64
        nome:  Chave identificadora Do arquivo no formato "STRING STRING"
        caminho: Caminho do arquivo
        identificador: Nome Identificador do arquivo
        usuario: Login do usuário
        caminhoExclusivo: String correspondente a configuração em configGerais do caminho exclusivo
        
        
        
        Args:
            arquivo (str): The arquivo
            nome (str): The nome
            caminho (str): The caminho
            identificador (str): The identificador
            usuario (str): The usuario
            caminhoExclusivo (str): The exclusivo
            controlaAnexoUAUWeb (int): The anexo u a u web
        
        Parameter Structure:
        
            {
                "arquivo": "string",
                "nome": "string",
                "caminho": "string",
                "identificador": "string",
                "usuario": "string",
                "caminhoExclusivo": "string",
                "controlaAnexoUAUWeb": true
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
        path = "Anexo/AnexarArquivo"
        kwargs = {
            "arquivo": arquivo,
            "nome": nome,
            "caminho": caminho,
            "identificador": identificador,
            "usuario": usuario,
            "caminhoExclusivo": caminho_exclusivo,
            "controlaAnexoUAUWeb": controla_anexouau_web,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("anexar_arquivo::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("anexar_arquivo::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("anexar_arquivo::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def excluir_anexos(
        self,
        identificador: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        origem: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/ExcluirAnexos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.       
        
        Parâmetros da request
        
        identificador: Chave identificadora do arquivo no formato "STRING STRING".
        nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
        origem: Indica o tipo de armazenamento será utilizado para excluir o vinculo ao arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.
        
        
        
        Args:
            identificador (str): The identificador
            nome_arquivo (str): The nome_arquivo
            origem (int): The origem
        
        Parameter Structure:
        
            {
                "identificador": "string",
                "nome_arquivo": "string",
                "origem": 0
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
        path = "Anexo/ExcluirAnexos"
        kwargs = {
            "identificador": identificador,
            "nome_arquivo": nome_arquivo,
            "origem": origem,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("excluir_anexos::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("excluir_anexos::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("excluir_anexos::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def listar_diretorios(
        self,
        caminho: Optional[str] = None,
        origem: Optional[int] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        DEFINIÇÕES TÉCNICAS
        * Status 200 - Retorna uma lista de diretórios
          
        
        Args:
            Caminho (str): The caminho
            Origem (int): The origem
        
        Parameter Structure:
        
            {
                "Caminho": "string",
                "Origem": 0
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
        path = "Anexo/ListarDiretorios"
        kwargs = {
            "Caminho": caminho,
            "Origem": origem,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("listar_diretorios::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("listar_diretorios::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("listar_diretorios::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def anexar_base64_imagem(
        self,
        arquivo: Optional[str] = None,
        nome: Optional[str] = None,
        caminho: Optional[str] = None,
        identificador: Optional[str] = None,
        usuario: Optional[str] = None,
        extensao_imagem: Optional[str] = None,
        caminho_exclusivo: Optional[str] = None,
        controla_anexouau_web: Optional[bool] = None,
        origem: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/AnexarBase64Imagem`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Possibilita anexar imagem no formato Base64
        
        
        Args:
            arquivo (str): The arquivo
            nome (str): The nome
            caminho (str): The caminho
            identificador (str): The identificador
            usuario (str): The usuario
            extensaoImagem (str): The imagem
            caminhoExclusivo (str): The exclusivo
            controlaAnexoUAUWeb (int): The anexo u a u web
            origem (int): The origem
        
        Parameter Structure:
        
            {
                "arquivo": "string",
                "nome": "string",
                "caminho": "string",
                "identificador": "string",
                "usuario": "string",
                "extensaoImagem": "string",
                "caminhoExclusivo": "string",
                "controlaAnexoUAUWeb": true,
                "origem": 0
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
        path = "Anexo/AnexarBase64Imagem"
        kwargs = {
            "arquivo": arquivo,
            "nome": nome,
            "caminho": caminho,
            "identificador": identificador,
            "usuario": usuario,
            "extensaoImagem": extensao_imagem,
            "caminhoExclusivo": caminho_exclusivo,
            "controlaAnexoUAUWeb": controla_anexouau_web,
            "origem": origem,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("anexar_base64_imagem::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("anexar_base64_imagem::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("anexar_base64_imagem::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def listar_armazenamentos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/ListarArmazenamentos`
        HTTP Method: `POST`
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
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
        path = "Anexo/ListarArmazenamentos"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("listar_armazenamentos::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("listar_armazenamentos::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("listar_armazenamentos::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def gravar_comentario_anexo(
        self,
        chave: Optional[str] = None,
        campos: Optional[str] = None,
        usuario: Optional[str] = None,
        comentario: Optional[str] = None,
        tipo_comentario: Optional[str] = None,
        usuario_privado: Optional[List[Dict]] = None,
        grupo_privado: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/GravarComentarioAnexo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Adiciona comentário anexo de acordo com os parâmetros passados na requisição.
        
        Pré requisito:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Anexo/ConsultarChavesComentario
        
        
        
        Parâmetros da request
        
        Chave: Chave para consulta.
        Campos: Campos obrigatórios para a chave="Venda" (empresa, obra, venda). Campos obrigatórios para a chave="Contrato" (Empresa, Contrato) Deve ser inserido juntos, separados por virgula.
        Usuario: Usuário logado.
        Comentario: Comentário a ser anexado.
        TipoComentario: Armazena o tipo do comentário ( 0-Publico, 1-Privado, 2-Interna).
        UsuarioPrivado: Armazena a lista de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -> /Usuarios/ConsultarUsuariosAtivos ).
        GrupoPrivado: Armazena a lista de grupos de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -> /Usuarios/ConsultarGruposDeUsuario ).
        
        
        
        Args:
            Chave (str): The chave
            Campos (str): The campos
            Usuario (str): The usuario
            Comentario (str): The comentario
            TipoComentario (str): The tipo comentario
            UsuarioPrivado (List[Dict[str, Any]]): The usuario privado
            GrupoPrivado (List[Dict[str, Any]]): The grupo privado
        
        Parameter Structure:
        
            {
                "Chave": "string",
                "Campos": "string",
                "Usuario": "string",
                "Comentario": "string",
                "TipoComentario": "string",
                "UsuarioPrivado": [
                    {
                        "Login_usr": "string"
                    }
                ],
                "GrupoPrivado": [
                    {
                        "Cod_cad": "string"
                    }
                ]
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
        path = "Anexo/GravarComentarioAnexo"
        kwargs = {
            "Chave": chave,
            "Campos": campos,
            "Usuario": usuario,
            "Comentario": comentario,
            "TipoComentario": tipo_comentario,
            "UsuarioPrivado": usuario_privado,
            "GrupoPrivado": grupo_privado,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("gravar_comentario_anexo::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("gravar_comentario_anexo::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("gravar_comentario_anexo::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def retorna_arquivo_em_bytes(
        self,
        nome_arquivo: Optional[str] = None,
        origem: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/RetornaArquivoEmBytes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Em Modulo UAU >> Utilitários >> Configurações do sistema >> ( Em "Arquivo" >> Arquivos(Anexos): ) Esse e o caminho padrão que a rota usar na consulta para retorna o arquivo em base64.
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Parâmetros da request
        
        nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
        origem: Indica o tipo de armazenamento será utilizado para buscar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.
        
        
        
        Args:
            nome_arquivo (str): The nome_arquivo
            origem (int): The origem
        
        Parameter Structure:
        
            {
                "nome_arquivo": "string",
                "origem": 0
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
        path = "Anexo/RetornaArquivoEmBytes"
        kwargs = {
            "nome_arquivo": nome_arquivo,
            "origem": origem,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("retorna_arquivo_em_bytes::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("retorna_arquivo_em_bytes::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("retorna_arquivo_em_bytes::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_chaves_comentario(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/ConsultarChavesComentario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Este endpoint oferece suporte para o seguinte endpoint: [URI + /api/v{version}/Anexo/GravarComentarioAnexo]
        Retorna objetos com:
        Possíveis chaves que podem ser utilizadas.
        Ordem dos parâmetros aceitos.
        Exemplo de utilização e formatação dos parâmetros.
          Anexos:
        
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777152/
        
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
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
        path = "Anexo/ConsultarChavesComentario"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("consultar_chaves_comentario::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_chaves_comentario::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("consultar_chaves_comentario::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def anexar_arquivos_base64_request(
        self,
        lista_arquivos: Optional[List[Dict]] = None,
        empresa: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/AnexarArquivosBase64Request`
        HTTP Method: `POST`
        
        Implementation Notes:
        Criação   : Diogo Rodrigues Gonçalves             Data: 11/12/2018
          Projeto   : FVS Mobile
        
        
        Args:
            lista_arquivos (List[Dict[str, Any]]): The lista_arquivos
            empresa (int): The empresa
            usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "lista_arquivos": [
                    {
                        "ConteudoArquivo": "string",
                        "NomeArquivo": "string",
                        "CaminhoArquivo": "string",
                        "Extension": "string",
                        "Identificador": "string",
                        "Origem": 0,
                        "CaminhoPadrao": "string"
                    }
                ],
                "empresa": 0,
                "usuario": "string"
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
        path = "Anexo/AnexarArquivosBase64Request"
        kwargs = {
            "lista_arquivos": lista_arquivos,
            "empresa": empresa,
            "usuario": usuario,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("anexar_arquivos_base64_request::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("anexar_arquivos_base64_request::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("anexar_arquivos_base64_request::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def retornar_arquivos_em_lista_bytes(
        self,
        empresa: Optional[str] = None,
        identificador: Optional[str] = None,
        listanomes_arquivos: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Anexo/RetornarArquivosEmListaBytes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Baseado no ‘’código identificador do documento’’ passado ele já retorna os arquivos tanto disponível localmente e na nuvem, sem a necessidade de passar o parâmetro “origem” no body do request.
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.       
        
        Parâmetros da request
        
        empresa: Número da empresa.
        identificador: Chave identificadora do arquivo no formato "STRING STRING".
        listanomes_arquivos:  Lista de 'string' com o nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
        
        
        
        Args:
            empresa (str): The empresa
            identificador (str): The identificador
            listanomes_arquivos (List[Dict[str, Any]]): The listanomes_arquivos
        
        Parameter Structure:
        
            {
                "empresa": "string",
                "identificador": "string",
                "listanomes_arquivos": [
                    "string"
                ]
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
        path = "Anexo/RetornarArquivosEmListaBytes"
        kwargs = {
            "empresa": empresa,
            "identificador": identificador,
            "listanomes_arquivos": listanomes_arquivos,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("retornar_arquivos_em_lista_bytes::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("retornar_arquivos_em_lista_bytes::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("retornar_arquivos_em_lista_bytes::Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

