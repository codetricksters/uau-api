from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Atendimento:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pendencia(
        self,
        usuariouau_destino: Optional[str] = None,
        data_prevista: Optional[datetime] = None,
        data_aviso: Optional[datetime] = None,
        hora_aviso: Optional[datetime] = None,
        mensagem: Optional[str] = None,
        geraremail_interno: Optional[bool] = None,
        gerar_email_externo: Optional[bool] = None,
        gerar_aviso: Optional[bool] = None,
        categoria: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/GerarPendencia`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuariouau_destino (str): The usuariouau_destino
            data_prevista (datetime): The data_prevista
            data_aviso (datetime): The data_aviso
            hora_aviso (datetime): The hora_aviso
            mensagem (str): The mensagem
            geraremail_interno (int): The geraremail_interno
            gerar_email_externo (int): The gerar_email_externo
            gerar_aviso (int): The gerar_aviso
            categoria (str): The categoria
        
        Parameter Structure:
        
            {
                "usuariouau_destino": "string",
                "data_prevista": "2025-04-23T13:46:12.537Z",
                "data_aviso": "2025-04-23T13:46:12.537Z",
                "hora_aviso": "2025-04-23T13:46:12.537Z",
                "mensagem": "string",
                "geraremail_interno": true,
                "gerar_email_externo": true,
                "gerar_aviso": true,
                "categoria": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._gerar_pendencia(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/GerarPendencia"
        kwargs = {
            "usuariouau_destino": usuariouau_destino,
            "data_prevista": data_prevista,
            "data_aviso": data_aviso,
            "hora_aviso": hora_aviso,
            "mensagem": mensagem,
            "geraremail_interno": geraremail_interno,
            "gerar_email_externo": gerar_email_externo,
            "gerar_aviso": gerar_aviso,
            "categoria": categoria,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def gravar_atendimento(
        self,
        atendimento: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/GravarAtendimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Atendimento/GravarAtendimento
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite Gravar o Atendimento.
        
        Deve montar uma estrutura com as informações do Atendimento verificando os parâmetros obrigatórios.
        Será apenas registrado Atendimentos com o status [0 - Em Aberto].
        Caso não seja informado: usrrespon_atd, numccm_atd e usrcad_atd, será obrigatório ter configurado o serviço atendimento uauweb no CRM. CRM - Utilitários - Configurações de serviço
        Para informar a unidade do atendimento é obrigatório informar a empresa, obra e produto. Caso não informe a empresa, vamos desconsiderar essa informação e gravar o atendimento.
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/configuracao-de-atendimento-do-uau-web/
        
        
        
        Args:
            atendimento (Dict[str, Any]): The atendimento
        
        Parameter Structure:
        
            {
                "atendimento": {
                    "codcateg_atd": "string",
                    "descr_atd": "string",
                    "usrrespon_atd": "string",
                    "usrcad_atd": "string",
                    "numccm_atd": 0,
                    "codpes_atd": 0,
                    "retoraten_atd": 0,
                    "empresa_atd": 0,
                    "obra_atd": "string",
                    "produnid_atd": 0,
                    "numper_atd": 0,
                    "datacad_atd": "2025-04-23T13:46:12.540Z",
                    "reincidente_atd": true,
                    "vlrmaoobra_atd": 0,
                    "tipo_atd": 0
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._gravar_atendimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/GravarAtendimento"
        kwargs = {
            "atendimento": atendimento,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_pendencia(
        self,
        numero: Optional[int] = None,
        data_lancamento: Optional[datetime] = None,
        responsavel_resolucao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarPendencia`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            numero (int): The numero
            data_lancamento (datetime): The data_lancamento
            responsavel_resolucao (str): The responsavel_resolucao
        
        Parameter Structure:
        
            {
                "numero": 0,
                "data_lancamento": "2025-04-23T13:46:12.545Z",
                "responsavel_resolucao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_pendencia(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarPendencia"
        kwargs = {
            "numero": numero,
            "data_lancamento": data_lancamento,
            "responsavel_resolucao": responsavel_resolucao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_atendimento(
        self,
        codigo_atendimento: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarAtendimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo_atendimento (int): The codigo_atendimento
        
        Parameter Structure:
        
            {
                "codigo_atendimento": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_atendimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarAtendimento"
        kwargs = {
            "codigo_atendimento": codigo_atendimento,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_categ_de_coment_ativas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarCategDeComentAtivas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
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
            >>> api = Atendimento()
            >>> response = api._consultar_categ_de_coment_ativas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarCategDeComentAtivas"
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
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_pendencia_observacao(
        self,
        numero_pendencia: Optional[int] = None,
        dataquando_lancou: Optional[datetime] = None,
        usuario_resolve: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarPendenciaObservacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            numero_pendencia (int): The numero_pendencia
            dataquando_lancou (datetime): The dataquando_lancou
            usuario_resolve (str): The usuario_resolve
        
        Parameter Structure:
        
            {
                "numero_pendencia": 0,
                "dataquando_lancou": "2025-04-23T13:46:12.564Z",
                "usuario_resolve": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_pendencia_observacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarPendenciaObservacao"
        kwargs = {
            "numero_pendencia": numero_pendencia,
            "dataquando_lancou": dataquando_lancou,
            "usuario_resolve": usuario_resolve,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def vincular_arquivo_ao_atendimento(
        self,
        arquivo: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        num_atendimento: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/VincularArquivoAoAtendimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            arquivo (str): The arquivo
            nome_arquivo (str): The nome_arquivo
            num_atendimento (int): The num_atendimento
            usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "arquivo": "string",
                "nome_arquivo": "string",
                "num_atendimento": 0,
                "usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._vincular_arquivo_ao_atendimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/VincularArquivoAoAtendimento"
        kwargs = {
            "arquivo": arquivo,
            "nome_arquivo": nome_arquivo,
            "num_atendimento": num_atendimento,
            "usuario": usuario,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_atendimento_por_pessoa(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarAtendimentoPorPessoa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo_pessoa (int): The codigo_pessoa
        
        Parameter Structure:
        
            {
                "codigo_pessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_atendimento_por_pessoa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarAtendimentoPorPessoa"
        kwargs = {
            "codigo_pessoa": codigo_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_empreendimentos_cliente(
        self,
        cod_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarEmpreendimentosCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            cod_pessoa (int): The cod_pessoa
        
        Parameter Structure:
        
            {
                "cod_pessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_empreendimentos_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarEmpreendimentosCliente"
        kwargs = {
            "cod_pessoa": cod_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_categoria_atendimento_web(
        self,
        tipo_atend: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarCategoriaAtendimentoWeb`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            tipo_atend (str): The tipo_atend
        
        Parameter Structure:
        
            {
                "tipo_atend": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_categoria_atendimento_web(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarCategoriaAtendimentoWeb"
        kwargs = {
            "tipo_atend": tipo_atend,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_numero_work_flow_vinculado(
        self,
        numerovinculo_workflow: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarNumeroWorkFlowVinculado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            numerovinculo_workflow (int): The numerovinculo_workflow
            empresa (int): The empresa
            obra (str): The obra
        
        Parameter Structure:
        
            {
                "numerovinculo_workflow": 0,
                "empresa": 0,
                "obra": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_numero_work_flow_vinculado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarNumeroWorkFlowVinculado"
        kwargs = {
            "numerovinculo_workflow": numerovinculo_workflow,
            "empresa": empresa,
            "obra": obra,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_pendencias_por_numero_vinculo(
        self,
        numero_vinculo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarPendenciasPorNumeroVinculo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            numero_vinculo (int): The numero_vinculo
        
        Parameter Structure:
        
            {
                "numero_vinculo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_pendencias_por_numero_vinculo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarPendenciasPorNumeroVinculo"
        kwargs = {
            "numero_vinculo": numero_vinculo,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def gerar_atendimento_por_chat_online_cliente(
        self,
        dados_atendimento: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/GerarAtendimentoPorChatOnlineCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            dados_atendimento (Dict[str, Any]): The dados_atendimento
        
        Parameter Structure:
        
            {
                "dados_atendimento": {
                    "CPF": "string",
                    "NomeCliente": "string",
                    "CodCategoria": "string",
                    "DescAtendimento": "string",
                    "DescChat": "string",
                    "UsrAtendente": "string",
                    "CanalComunicacao": "string",
                    "Email": "string",
                    "CodAtd": "string"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._gerar_atendimento_por_chat_online_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/GerarAtendimentoPorChatOnlineCliente"
        kwargs = {
            "dados_atendimento": dados_atendimento,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_atendimento_detalhado_por_chave(
        self,
        codigo_atendimento: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarAtendimentoDetalhadoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo_atendimento (int): The codigo_atendimento
        
        Parameter Structure:
        
            {
                "codigo_atendimento": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_atendimento_detalhado_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarAtendimentoDetalhadoPorChave"
        kwargs = {
            "codigo_atendimento": codigo_atendimento,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_configuracao_atendimento_uauweb(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarConfiguracaoAtendimentoUAUWEB`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
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
            >>> api = Atendimento()
            >>> response = api._consultar_configuracao_atendimentouauweb(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarConfiguracaoAtendimentoUAUWEB"
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
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_atendimento_por_categorias_uau_web(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarAtendimentoPorCategoriasUauWeb`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo_pessoa (int): The codigo_pessoa
        
        Parameter Structure:
        
            {
                "codigo_pessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_atendimento_por_categorias_uau_web(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarAtendimentoPorCategoriasUauWeb"
        kwargs = {
            "codigo_pessoa": codigo_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_atendimento_por_pessoa_comentario(
        self,
        codigo_pessoa: Optional[int] = None,
        lista_categoria: Optional[List[Dict]] = None,
        periodo_incio: Optional[datetime] = None,
        periodo_fim: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarAtendimentoPorPessoaComentario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo_pessoa (int): The codigo_pessoa
            lista_categoria (List[Dict[str, Any]]): The lista_categoria
            periodo_incio (datetime): The periodo_incio
            periodo_fim (datetime): The periodo_fim
        
        Parameter Structure:
        
            {
                "codigo_pessoa": 0,
                "lista_categoria": [
                    "string"
                ],
                "periodo_incio": "2025-04-23T13:46:12.606Z",
                "periodo_fim": "2025-04-23T13:46:12.606Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_atendimento_por_pessoa_comentario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarAtendimentoPorPessoaComentario"
        kwargs = {
            "codigo_pessoa": codigo_pessoa,
            "lista_categoria": lista_categoria,
            "periodo_incio": periodo_incio,
            "periodo_fim": periodo_fim,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_unidades_do_empreendimento_cliente(
        self,
        obra: Optional[str] = None,
        empresa: Optional[int] = None,
        cod_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarUnidadesDoEmpreendimentoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            obra (str): The obra
            empresa (int): The empresa
            cod_pessoa (int): The cod_pessoa
        
        Parameter Structure:
        
            {
                "obra": "string",
                "empresa": 0,
                "cod_pessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_unidades_do_empreendimento_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarUnidadesDoEmpreendimentoCliente"
        kwargs = {
            "obra": obra,
            "empresa": empresa,
            "cod_pessoa": cod_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_data_prevista_de_termino_atendimento(
        self,
        numerovinculo_workflow: Optional[int] = None,
        numero_workflow: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarDataPrevistaDeTerminoAtendimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            numerovinculo_workflow (int): The numerovinculo_workflow
            numero_workflow (int): The numero_workflow
        
        Parameter Structure:
        
            {
                "numerovinculo_workflow": 0,
                "numero_workflow": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_data_prevista_de_termino_atendimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarDataPrevistaDeTerminoAtendimento"
        kwargs = {
            "numerovinculo_workflow": numerovinculo_workflow,
            "numero_workflow": numero_workflow,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_numero_vinculo_categoria_de_comentario_com_work_flow(
        self,
        codigo_categoria: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Atendimento/ConsultarNumeroVinculoCategoriaDeComentarioComWorkFlow`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo_categoria (str): The codigo_categoria
        
        Parameter Structure:
        
            {
                "codigo_categoria": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Atendimento()
            >>> response = api._consultar_numero_vinculo_categoria_de_comentario_com_work_flow(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Atendimento/ConsultarNumeroVinculoCategoriaDeComentarioComWorkFlow"
        kwargs = {
            "codigo_categoria": codigo_categoria,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

