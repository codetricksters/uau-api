from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class BoletoServices:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pdfcarne(
        self,
        filtro_chaves_boleto: Optional[List[Dict]] = None,
        filtro_venda_remessa: Optional[Dict] = None,
        carne_tres_boletos_pagina_na_vertical: Optional[bool] = None,
        carne_dois_boletos_pagina_na_horizontal: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/GerarPDFCarne`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        O retorno será um base64. Para poder visualizar os carnês, é necessário fazer uma conversão para PDF.
        
        Regras de Negócio:
        
        Para realizar a requisição, informar apenas um filtro. Caso o filtro de chaves do boleto for informado, o filtro de venda remessa, não deve ser informado. O mesmo para o caso contrário.
        CarneTresBoletosPaginaNaVertical, irá gerar três boletos por página
        CarneDoisBoletosPaginaNaHorizontal irá gerar dois boletos por página na horizontal
        Informar apenas um dos parametros de layout de carnê por página como true, caso um seja true, o outro deverá ser informado como false.
        No filtro de venda remessa, caso não deseje passar o numeroRemessa, não o inclua na chave ou passe o valor como 0.
        
        
        
        Args:
            filtroChavesBoleto (List[Dict[str, Any]]): The chaves boleto
            filtroVendaRemessa (Dict[str, Any]): The venda remessa
            CarneTresBoletosPaginaNaVertical (int): The carne tres boletos pagina na vertical
            CarneDoisBoletosPaginaNaHorizontal (int): The carne dois boletos pagina na horizontal
        
        Parameter Structure:
        
            {
                "filtroChavesBoleto": [
                    {
                        "banco": 0,
                        "seuNumero": 0
                    }
                ],
                "filtroVendaRemessa": {
                    "empresa": 0,
                    "numeroRemessa": 0,
                    "obra": "string",
                    "venda": 0
                },
                "CarneTresBoletosPaginaNaVertical": true,
                "CarneDoisBoletosPaginaNaHorizontal": true
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
        path = "BoletoServices/GerarPDFCarne"
        try:
            response = self.api.post(
                path,
                json={
                    "filtroChavesBoleto": filtro_chaves_boleto,
                    "filtroVendaRemessa": filtro_venda_remessa,
                    "CarneTresBoletosPaginaNaVertical": carne_tres_boletos_pagina_na_vertical,
                    "CarneDoisBoletosPaginaNaHorizontal": carne_dois_boletos_pagina_na_horizontal,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gerar_pdfboleto(
        self,
        cod_banco: Optional[int] = None,
        seu_numero: Optional[int] = None,
        ocultar_dados_pessoais: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/GerarPDFBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Utilize em conversor de string Base64 para PDF.
        
        Definição de Negócio:
          Permite gerar boleto.
        
        O parâmetro booleano (true ou false) "ocultar_dados_pessoais" determina se 
          os dados pessoais do cliente (nome completo e endereço) serão exibidos no PDF do boleto gerado.
        O parâmetro inteiro "cod_banco" deve ser informado sem zeros a esquerda por se tratar de um número inteiro 
        
        
        
        Args:
            cod_banco (int): The cod_banco
            seu_numero (int): The seu_numero
            ocultar_dados_pessoais (int): The ocultar_dados_pessoais
        
        Parameter Structure:
        
            {
                "cod_banco": 0,
                "seu_numero": 0,
                "ocultar_dados_pessoais": true
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
        path = "BoletoServices/GerarPDFBoleto"
        try:
            response = self.api.post(
                path,
                json={
                    "cod_banco": cod_banco,
                    "seu_numero": seu_numero,
                    "ocultar_dados_pessoais": ocultar_dados_pessoais,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def obter_codigo_de_barras(
        self,
        cod_banco: Optional[str] = None,
        seu_numero: Optional[str] = None,
        data_venc: Optional[datetime] = None,
        valor_nominal: Optional[int] = None,
        campo_livre: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/ObterCodigoDeBarras`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Busca o número do código de barras do boleto informado.
        Caso boleto que deseja consultar seja gerado via intermediário digital informar: código do banco e seu número
        
        
        
        Args:
            cod_banco (str): The cod_banco
            seu_numero (str): The seu_numero
            data_venc (datetime): The data_venc
            valor_nominal (int): The valor_nominal
            campo_livre (str): The campo_livre
        
        Parameter Structure:
        
            {
                "cod_banco": "string",
                "seu_numero": "string",
                "data_venc": "2025-04-23T13:46:12.668Z",
                "valor_nominal": 0,
                "campo_livre": "string"
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
        path = "BoletoServices/ObterCodigoDeBarras"
        try:
            response = self.api.post(
                path,
                json={
                    "cod_banco": cod_banco,
                    "seu_numero": seu_numero,
                    "data_venc": data_venc,
                    "valor_nominal": valor_nominal,
                    "campo_livre": campo_livre,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def obter_linha_digitavel(
        self,
        codigode_barras: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/ObterLinhaDigitavel`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta a linha digitável do código de barras.
        
        
        
        Args:
            codigode_barras (str): The codigode_barras
        
        Parameter Structure:
        
            {
                "codigode_barras": "string"
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
        path = "BoletoServices/ObterLinhaDigitavel"
        try:
            response = self.api.post(
                path,
                json={
                    "codigode_barras": codigode_barras,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def alterar_data_vencimento(
        self,
        seu_numero: Optional[int] = None,
        cod_banco: Optional[int] = None,
        cod_empresa: Optional[int] = None,
        nova_data_venc: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/AlterarDataVencimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio: Permite alterar a data de vencimento de um boleto cadastrado no UAU.
        
        Não é permitido alterar a data de vencimento para um boleto excluído.
        Não é permitido alterar a data de vencimento para um boleto antecipado.
        Não é permito alterar data de vencimento de um boleto gerado via intermediario digital.
        Para manutenção de boleto, o campo Nosso Número não pode estar vazio.
        A nova data de vencimento do boleto não pode ser menor que a data original.
        Não é permitido alterar a data de vencimento para um boleto dos bancos 246-ABC, 353-SANTANDER e 425-SOCINAL.
        Não é permitido alterar a data de vencimento para um boleto com tipo de cobrança "Débito Automático" nos bancos; 1 (carteira 2), 341 (carteira 2) e 104 (carteira 5).
        Para boletos do banco "341 - Itau", "01 - Banco do Brasil", "425 - Banco Socinal"  ou "104 - Caixa Econômica Federal" débito automático, carteira "00 - Débito automático" só é permitido a ação "1 - Cancelamento".
        Alguns bancos não possuem a opção de alteração de vencimento implementada. A API informará se não puder realizar a alteração.
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/wp-content/uploads/2019/06/BoletoUAU.postman_collection.zip
        Exemplo Retorno: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/AlterarDataVencimento.retorno.zip
        
        
        
        Args:
            seuNumero (int): The numero
            codBanco (int): The banco
            codEmpresa (int): The empresa
            novaDataVenc (datetime): The data venc
        
        Parameter Structure:
        
            {
                "seuNumero": 0,
                "codBanco": 0,
                "codEmpresa": 0,
                "novaDataVenc": "2025-04-23T13:46:12.674Z"
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
        path = "BoletoServices/AlterarDataVencimento"
        try:
            response = self.api.post(
                path,
                json={
                    "seuNumero": seu_numero,
                    "codBanco": cod_banco,
                    "codEmpresa": cod_empresa,
                    "novaDataVenc": nova_data_venc,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_status_boleto(
        self,
        codigo_banco: Optional[int] = None,
        seu_numero: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/ConsultarStatusBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Possibilita consulta status do boleto.
        
        
        
        Args:
            codigoBanco (int): The banco
            seuNumero (int): The numero
        
        Parameter Structure:
        
            {
                "codigoBanco": 0,
                "seuNumero": 0
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
        path = "BoletoServices/ConsultarStatusBoleto"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoBanco": codigo_banco,
                    "seuNumero": seu_numero,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def obter_mensagem_do_boleto(
        self,
        seu_numero: Optional[int] = None,
        cod_banco: Optional[int] = None,
        cod_empresa: Optional[int] = None,
        instrucao: Optional[str] = None,
        carteira: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/ObterMensagemDoBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta a mensagem do boleto informado nos parâmetros da request.
        
        
        
        Args:
            seu_numero (int): The seu_numero
            cod_banco (int): The cod_banco
            cod_empresa (int): The cod_empresa
            instrucao (str): The instrucao
            carteira (str): The carteira
        
        Parameter Structure:
        
            {
                "seu_numero": 0,
                "cod_banco": 0,
                "cod_empresa": 0,
                "instrucao": "string",
                "carteira": "string"
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
        path = "BoletoServices/ObterMensagemDoBoleto"
        try:
            response = self.api.post(
                path,
                json={
                    "seu_numero": seu_numero,
                    "cod_banco": cod_banco,
                    "cod_empresa": cod_empresa,
                    "instrucao": instrucao,
                    "carteira": carteira,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_dados_do_boleto(
        self,
        cod_banco: Optional[str] = None,
        seu_numero: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/ConsultarDadosDoBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta informações contidas no boleto.
        
        
        
        Args:
            cod_banco (str): The cod_banco
            seu_numero (str): The seu_numero
        
        Parameter Structure:
        
            {
                "cod_banco": "string",
                "seu_numero": "string"
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
        path = "BoletoServices/ConsultarDadosDoBoleto"
        try:
            response = self.api.post(
                path,
                json={
                    "cod_banco": cod_banco,
                    "seu_numero": seu_numero,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_boletos_do_cliente(
        self,
        cod_pessoa: Optional[int] = None,
        nao_mostra_boleto_vencido: Optional[bool] = None,
        usuario: Optional[str] = None,
        tipo_usuario: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/ConsultarBoletosDoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Consulta ou não boletos vencidos.
        
        Definição de Negócio:
        Consulta boletos por cliente.
        
        Consulta boletos por cliente.
        Ao definir que não irá mostrar boletos vencidos, serão retornados apenas os boletos a vencer.
        Ao definir que deve mostrar boletos vencidos, serão retornados boletos vencidos e a vencer.
        Parcelas que possuem mais de um boleto ativo, não terão os boletos trazidos na consulta, 
          devido a quem For obter/utilizar o retorno, não saber qual dos boletos deve ser impresso e pago.
        Parcelas que possuem um único boleto ativo, terão os boletos trazidos na consulta.
        Os boletos serão listados em ordem crescente de vencimento.
        Os boletos que não tiverem o Nosso número banco preenchidos mão serão mostrados.
        Serão mostrados somente os boletos que estiverem com os status a seguir:
        0 - Normal
        1 - Pendente de confirmação de alteração de vencimento
        2 - Pendente de cancelamento de boleto
        3 - Confirmada alteração de vencimento/cancelamento
        4 - Confirmada alteração de vencimento
        6 - Registrado online
        10 - Pendente para confirmação de alteração de valor do boleto
        11 - Confirmada alteração de valor do boleto
        
        
        
        
        
        Args:
            codPessoa (int): The pessoa
            naoMostraBoletoVencido (int): The mostra boleto vencido
            usuario (str): The usuario
            tipo_usuario (int): The tipo_usuario
        
        Parameter Structure:
        
            {
                "codPessoa": 0,
                "naoMostraBoletoVencido": true,
                "usuario": "string",
                "tipo_usuario": 0
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
        path = "BoletoServices/ConsultarBoletosDoCliente"
        try:
            response = self.api.post(
                path,
                json={
                    "codPessoa": cod_pessoa,
                    "naoMostraBoletoVencido": nao_mostra_boleto_vencido,
                    "usuario": usuario,
                    "tipo_usuario": tipo_usuario,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_boletos_reimpressao(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        naomostraboleto_vencido: Optional[bool] = None,
        mostrar_apenas_ultimo_boleto: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `BoletoServices/ConsultarBoletosReimpressao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio: Consultar boletos disponíveis para reimpressão.
        
        Valida usuário logado do tipo (pessoa/cliente).
        Valida código do usuário.
        Parcelas que possuem mais de um boleto ativo, não terão os boletos trazidos na consulta, 
          devido a quem for obter/utilizar o retorno, não saber qual dos boletos deve ser impresso e pago.
        Parcelas que possuem um único boleto ativo, terão os boletos trazidos na consulta.
        Os boletos serão listados em ordem crescente de vencimento'
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_venda (int): The num_venda
            naomostraboleto_vencido (int): The naomostraboleto_vencido
            mostrarApenasUltimoBoleto (int): The apenas ultimo boleto
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_venda": 0,
                "naomostraboleto_vencido": true,
                "mostrarApenasUltimoBoleto": true
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
        path = "BoletoServices/ConsultarBoletosReimpressao"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "num_venda": num_venda,
                    "naomostraboleto_vencido": naomostraboleto_vencido,
                    "mostrarApenasUltimoBoleto": mostrar_apenas_ultimo_boleto,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

