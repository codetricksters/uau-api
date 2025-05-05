from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests


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
        controla_anexouau_web: Optional[bool] = None,
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
        try:
            response = self.api.post(
                path,
                json={
                    "arquivo": arquivo,
                    "nome": nome,
                    "caminho": caminho,
                    "identificador": identificador,
                    "usuario": usuario,
                    "caminhoExclusivo": caminho_exclusivo,
                    "controlaAnexoUAUWeb": controla_anexouau_web,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return None

    def excluir_anexos(
        self,
        identificador: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        origem: Optional[int] = None,
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
        try:
            response = self.api.post(
                path,
                json={
                    "identificador": identificador,
                    "nome_arquivo": nome_arquivo,
                    "origem": origem,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return None

    def listar_diretorios(
        self, caminho: Optional[str] = None, origem: Optional[int] = None
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
        try:
            response = self.api.post(
                path,
                json={
                    "Caminho": caminho,
                    "Origem": origem,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
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
        origem: Optional[int] = None,
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
        try:
            response = self.api.post(
                path,
                json={
                    "arquivo": arquivo,
                    "nome": nome,
                    "caminho": caminho,
                    "identificador": identificador,
                    "usuario": usuario,
                    "extensaoImagem": extensao_imagem,
                    "caminhoExclusivo": caminho_exclusivo,
                    "controlaAnexoUAUWeb": controla_anexouau_web,
                    "origem": origem,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return None

    def listar_armazenamentos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None,
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
        try:
            response = self.api.post(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return None

    def gravar_comentario_anexo(
        self,
        chave: Optional[str] = None,
        campos: Optional[str] = None,
        usuario: Optional[str] = None,
        comentario: Optional[str] = None,
        tipo_comentario: Optional[str] = None,
        usuario_privado: Optional[List[Dict]] = None,
        grupo_privado: Optional[List[Dict]] = None,
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
        try:
            response = self.api.post(
                path,
                json={
                    "Chave": chave,
                    "Campos": campos,
                    "Usuario": usuario,
                    "Comentario": comentario,
                    "TipoComentario": tipo_comentario,
                    "UsuarioPrivado": usuario_privado,
                    "GrupoPrivado": grupo_privado,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return None

    def retorna_arquivo_em_bytes(
        self, nome_arquivo: Optional[str] = None, origem: Optional[int] = None
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
        try:
            response = self.api.post(
                path,
                json={
                    "nome_arquivo": nome_arquivo,
                    "origem": origem,
                },
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return e

    def consultar_chaves_comentario(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None,
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
        try:
            response = self.api.post(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                },
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return None

    def anexar_arquivos_base64_request(
        self,
        lista_arquivos: Optional[List[Dict]] = None,
        empresa: Optional[int] = None,
        usuario: Optional[str] = None,
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
        try:
            response = self.api.post(
                path,
                json={
                    "lista_arquivos": lista_arquivos,
                    "empresa": empresa,
                    "usuario": usuario,
                },
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            return None

    def retornar_arquivos_em_lista_bytes(
        self,
        empresa: Optional[str] = None,
        identificador: Optional[str] = None,
        listanomes_arquivos: Optional[List[Dict]] = None,
    ) -> dict:
        """

        Endpoint: `Anexo/RetornarArquivosEmListaBytes`
        HTTP Method: `POST`

        Implementation Notes:
        Baseado no 'código identificador do documento' passado ele já retorna os arquivos tanto disponível localmente e na nuvem, sem a necessidade de passar o parâmetro “origem” no body do request.
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
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "identificador": identificador,
                    "listanomes_arquivos": listanomes_arquivos,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return None
