from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Autenticador:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def logout_usuario(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Autenticador/LogoutUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Criação: Diogo Rodrigues Gonçalves      Data: 22/01/2018
        
        
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
            >>> api = Autenticador()
            >>> response = api._logout_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Autenticador/LogoutUsuario"
        try:
            response = self.api.post(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def autenticar_usuario(
        self,
        login: Optional[str] = None,
        senha: Optional[str] = None,
        usuariouau_site: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Autenticador/AutenticarUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        
        Verifica o método de Login configurado no Sistema Uau https://ajuda.globaltec.com.br/virtuau/configuracao-de-seguranca/ 
        Empresa configurada com Autenticação AD e utilizar este serviço a autenticação será como Cliente/Pessoa.
        Empresa configurada com Autenticação Uau
        Login do usuário maior que 8 caracteres a autenticação será como Cliente/Pessoa.
        Login do usuário menor que 8 caracteres a autenticação será Uau.
        
        
        Para utilizar o recurso de GerarBoleto deve-se informar a propriedade UsuarioUAUSite.
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_Uau
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_via_Active_Directory
        
        Anexos: 
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/774812/
        
        
        
        Args:
            Login (str): The login
            Senha (str): The senha
            UsuarioUAUSite (str): The usuario u a u site
        
        Parameter Structure:
        
            {
                "Login": "string",
                "Senha": "string",
                "UsuarioUAUSite": "string"
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
        path = "Autenticador/AutenticarUsuario"
        try:
            response = self.api.post(
                path,
                json={
                    "Login": login,
                    "Senha": senha,
                    "UsuarioUAUSite": usuariouau_site,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def autenticar_usuario_app(
        self,
        login: Optional[str] = None,
        senha: Optional[str] = None,
        usuariouau_site: Optional[str] = None
    ) -> dict:
        """
          caso contrário será validado como usuário UAU ou Cliente.
          Atualmente utilizado pela API do Mobile.
        
        Endpoint: `Autenticador/AutenticarUsuarioApp`
        HTTP Method: `POST`
        
        Args:
            Login (str): The login
            Senha (str): The senha
            UsuarioUAUSite (str): The usuario u a u site
        
        Parameter Structure:
        
            {
                "Login": "string",
                "Senha": "string",
                "UsuarioUAUSite": "string"
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
        path = "Autenticador/AutenticarUsuarioApp"
        try:
            response = self.api.post(
                path,
                json={
                    "Login": login,
                    "Senha": senha,
                    "UsuarioUAUSite": usuariouau_site,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def verifica_usuario_logado(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Autenticador/VerificaUsuarioLogado`
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
            >>> api = Autenticador()
            >>> response = api._verifica_usuario_logado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Autenticador/VerificaUsuarioLogado"
        try:
            response = self.api.post(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_dados_usr_logado(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
          usuário logado seja do tipo pessoa. Caso contrário uma exceção é lançada informando que
          o usuário logado precisa ser do tipo pessoa para este método.
        
        Endpoint: `Autenticador/ConsultarDadosUsrLogado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Permite consultar os dados do usuário do tipo cliente do Cadastro de Pessoas do Uau.
        
        O usuário cliente deve estar autenticado.
        Retorna as informações do cliente logado, conforme a estrutura abaixo.
        
        Estrutura do Retorno: https://ajuda.globaltec.com.br/download/774818/
        
        Dados Pessoais: 
        codigo = Código do cliente
        nome = Nome completo
        cpf = CPF
        dtnasc = Data de nascimento
        email = E-mail
        login = Login do Cliente no UAU Web
        senha = Senha do cliente
        
        
        Dados do Telefone:
        codigo = Código do cliente
        numero = Número do telefone do cliente
        ddd = DDD do telefone
        ramal = Ramal do telefone do cliente
        tipo = Tipo do telefone (0-residencial;1-comercial;2-celular;3-recado;4-fax;5-bip;6-telex;7-outros;8-fone/fax)
        
        
        Dados do Endereço:
        codPes = Código do cliente
        tipoEndereco = 0-Principal 1-Cobrança 2-Comercial
        endereco = Endereço do cliente
        complemento = Complemento do endereço
        numero = Número do endereço do cliente
        referencia = Referência do endereço
        bairro = Bairro
        cep = CEP
        cidade = Cidade
        uf = UF
        
        
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Consultar_dados_do_Usuario_Logado
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/774809/
        Exemplo Retorno: https://ajuda.globaltec.com.br/download/774818/
        
        
        
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
            >>> api = Autenticador()
            >>> response = api._consultar_dados_usr_logado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Autenticador/ConsultarDadosUsrLogado"
        try:
            response = self.api.post(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def autentificar_usuario_titanium(
        self,
        usuario: Optional[str] = None,
        senha: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Autenticador/AutentificarUsuarioTitanium`
        HTTP Method: `POST`
        
        Args:
            usuario (str): The usuario
            senha (str): The senha
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "senha": "string"
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
        path = "Autenticador/AutentificarUsuarioTitanium"
        try:
            response = self.api.post(
                path,
                json={
                    "usuario": usuario,
                    "senha": senha,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def autenticar_usuario_corporativo(
        self,
        login_ad: Optional[str] = None,
        senha: Optional[str] = None,
        login_uau: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Autenticador/AutenticarUsuarioCorporativo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        
        Verifica o método de Login configurado no Sistema Uau https://ajuda.globaltec.com.br/virtuau/configuracao-de-seguranca/ 
        Empresa configurada para método de Login Uau via banco de dados
        Será realizada a verificação se existe o usuário com a senha informada.
        
        
        Empresa configurada para método de Login via AD
        Será realizada a autenticação validando no Active Directory
        
        
        No parâmetro login_uau do corpo da requisição, deve ser informado o login que é utilizado no uau quando o Active Directory não está habilitado. 
        A informação do login do usuário está no módulo segurança.  
        
        
        
        VirtUau: 
        
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_via_Active_Directory
        
        Anexos: 
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/774812/
        
        
        
        Args:
            login_ad (str): The login_ad
            senha (str): The senha
            login_uau (str): The login_uau
        
        Parameter Structure:
        
            {
                "login_ad": "string",
                "senha": "string",
                "login_uau": "string"
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
        path = "Autenticador/AutenticarUsuarioCorporativo"
        try:
            response = self.api.post(
                path,
                json={
                    "login_ad": login_ad,
                    "senha": senha,
                    "login_uau": login_uau,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

