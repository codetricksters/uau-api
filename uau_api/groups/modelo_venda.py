from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class ModeloVenda:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def buscar_plano_indexador(
        self,
        nummodelo_venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ModeloVenda/BuscarPlanoIndexador`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta o plano indexador vinculado ao modelo da venda.
        
        
        
        Args:
            nummodelo_venda (int): The nummodelo_venda
        
        Parameter Structure:
        
            {
                "nummodelo_venda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ModeloVenda()
            >>> response = api._buscar_plano_indexador(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ModeloVenda/BuscarPlanoIndexador"
        try:
            response = self.api.post(
                path,
                json={
                    "nummodelo_venda": nummodelo_venda,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_modelo_venda(
        self,
        cod_modelo_venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ModeloVenda/ConsultarModeloVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta o modelo de vendo filtrando pelo código do modelo.
        
        Tipos de Caps:
        Tipo Parcelamento: 0 - Contrato                  
        
        0 - Principal                                 
        1 - Corr. por atraso                          
        2 - Juros contratual                          
        3 - Correção                                  
        4 - Multa por atraso                          
        5 - Juros por atraso                          
        6 - Acrescimo                                 
        7 - Desconto                                  
        8 - Desconto por antecipação                  
        9 - Taxa de boleto                           
        10 - Desconto custas                         
        11 - Repasse                                 
        12 - Desconto condicional                    
        
        Tipo Parcelamento: 1 - Custas | 3 - Honorário
        
        0 - Principal
        1 - Juros contratual
        2 - Correção
        3 - Multa por atraso
        4 - Juros por atraso
        5 - Corr. por atraso
        6 - Acréscimo
        7 - Desconto
        8 - Desconto por antecipação
        9 - Taxa de boleto
        10 - Desconto custa
        11 - Repasse
        12 - Desconto condicional
        
        
        
        Args:
            codModeloVenda (int): The modelo venda
        
        Parameter Structure:
        
            {
                "codModeloVenda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ModeloVenda()
            >>> response = api._consultar_modelo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ModeloVenda/ConsultarModeloVenda"
        try:
            response = self.api.post(
                path,
                json={
                    "codModeloVenda": cod_modelo_venda,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def gerar_parcelas_proposta(
        self,
        parametromodelovenda: Optional[List[Dict]] = None,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        redistribuir_valor: Optional[bool] = None,
        utilizar_cap: Optional[bool] = None,
        tipo_venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ModeloVenda/GerarParcelasProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Gera parcelas da proposta baseado nos parametros de parcelas informado.
        Valida os campos passados na request.
        
        
        
        Args:
            parametromodelovenda (List[Dict[str, Any]]): The parametromodelovenda
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            redistribuirValor (int): The valor
            utilizarCap (int): The cap
            tipoVenda (int): The venda
        
        Parameter Structure:
        
            {
                "parametromodelovenda": [
                    {
                        "numParametro": 0,
                        "numParcela": 0,
                        "valorParcela": 0,
                        "valorTotalParcela": 0,
                        "percentualParcela": 0,
                        "dataParcela": "2025-04-23T13:46:13.433Z",
                        "dataReajuste": "2025-04-23T13:46:13.433Z",
                        "dataJuros": "2025-04-23T13:46:13.433Z",
                        "juros": 0,
                        "dataSegundoJuros": "2025-04-23T13:46:13.433Z",
                        "percentualSegundoJuros": 0,
                        "tipoParcela": "string",
                        "frequencia": "string",
                        "amortizacao": 0,
                        "beginEnd": 0,
                        "reajuste": "string",
                        "JurosComJuros": 0,
                        "planoIndexParcela": 0,
                        "tipoValor": 0,
                        "carenciaAtraso": 0,
                        "carenciaAtrasoCorrecao": 0,
                        "cobrarJurosProRata": 0,
                        "cobrarJurosProRataPrimeiroMes": 0,
                        "competencia": 0,
                        "numModeloVenda": 0,
                        "tipoContrato": 0,
                        "cap": "string",
                        "capCorrecaoAtraso": "string",
                        "capJuros": "string",
                        "capCorrecao": "string",
                        "capMulta": "string",
                        "capJurosAtraso": "string",
                        "capAcrescimo": "string",
                        "capDesconto": "string",
                        "capDescontoAntecipado": "string",
                        "capTaxaBoleto": "string",
                        "capDescontoCusta": "string",
                        "capRepasse": "string",
                        "capDescontoCondicional": "string",
                        "tipoParcelamento": 0,
                        "NumCtp": 0,
                        "OrigemCusta": 0,
                        "cobrarMulta": 0,
                        "cobrarJurosAtraso": 0,
                        "cobrarImposto": 0,
                        "cobrarCorrecao": 0,
                        "cobrarCPMF": 0,
                        "repassarLocador": 0,
                        "tipoSeguro": 0,
                        "CobrarTaxaAdm": 0
                    }
                ],
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "redistribuirValor": true,
                "utilizarCap": true,
                "tipoVenda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ModeloVenda()
            >>> response = api._gerar_parcelas_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ModeloVenda/GerarParcelasProposta"
        try:
            response = self.api.post(
                path,
                json={
                    "parametromodelovenda": parametromodelovenda,
                    "codigoEmpresa": codigo_empresa,
                    "codigoObra": codigo_obra,
                    "redistribuirValor": redistribuir_valor,
                    "utilizarCap": utilizar_cap,
                    "tipoVenda": tipo_venda,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_modelo_de_venda(
        self,
        obra: Optional[str] = None,
        empresa: Optional[int] = None,
        nummodelo_venda: Optional[int] = None,
        eat_inat: Optional[int] = None,
        campos_retornados: Optional[str] = None,
        tipo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ModeloVenda/ConsultarModeloDeVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta o modelo da venda filtrando os parâmetros informados na request.
        
        
        
        Args:
            obra (str): The obra
            empresa (int): The empresa
            nummodelo_venda (int): The nummodelo_venda
            eat_inat (int): The eat_inat
            campos_retornados (str): The campos_retornados
            tipo (int): The tipo
        
        Parameter Structure:
        
            {
                "obra": "string",
                "empresa": 0,
                "nummodelo_venda": 0,
                "eat_inat": 0,
                "campos_retornados": "string",
                "tipo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ModeloVenda()
            >>> response = api._consultar_modelo_de_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ModeloVenda/ConsultarModeloDeVenda"
        try:
            response = self.api.post(
                path,
                json={
                    "obra": obra,
                    "empresa": empresa,
                    "nummodelo_venda": nummodelo_venda,
                    "eat_inat": eat_inat,
                    "campos_retornados": campos_retornados,
                    "tipo": tipo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def montar_modelo_renegociacao(
        self,
        cod_modelo_venda: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        valor_reneg_contrato: Optional[int] = None,
        valor_reneg_custas: Optional[int] = None,
        valor_reneg_seguromip: Optional[int] = None,
        valor_reneg_segurodfi: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ModeloVenda/MontarModeloRenegociacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite gerar parâmetros do modelo e as parcelas para uma renegociação.
        
        Somente usuários autenticados podem ter acesso a essa rota.
        As informações recebidas no request devem existirem no UAU.
        O modelo de venda deve estar aprovado para ser utilizado.
        O modelo de venda informada está vinculado a empresa/obra informada.
        Os valores de custas, seguros e contratos devem estar configurados para o modelo.
        
        Atenção:
        
        Os campos DtIdxParc e DtJurParc são postos como o dia atual da venda caso o modelo esteja configurada para receber a data da venda.
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777189/
        Exemplo Retorno: https://ajuda.globaltec.com.br/download/777192/
        
        
        
        Args:
            codModeloVenda (int): The modelo venda
            empresa (int): The empresa
            obra (str): The obra
            numVenda (int): The venda
            ValorRenegContrato (int): The valor reneg contrato
            ValorRenegCustas (int): The valor reneg custas
            ValorRenegSeguroMIP (int): The valor reneg seguro m i p
            ValorRenegSeguroDFI (int): The valor reneg seguro d f i
        
        Parameter Structure:
        
            {
                "codModeloVenda": 0,
                "empresa": 0,
                "obra": "string",
                "numVenda": 0,
                "ValorRenegContrato": 0,
                "ValorRenegCustas": 0,
                "ValorRenegSeguroMIP": 0,
                "ValorRenegSeguroDFI": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ModeloVenda()
            >>> response = api._montar_modelo_renegociacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ModeloVenda/MontarModeloRenegociacao"
        try:
            response = self.api.post(
                path,
                json={
                    "codModeloVenda": cod_modelo_venda,
                    "empresa": empresa,
                    "obra": obra,
                    "numVenda": num_venda,
                    "ValorRenegContrato": valor_reneg_contrato,
                    "ValorRenegCustas": valor_reneg_custas,
                    "ValorRenegSeguroMIP": valor_reneg_seguromip,
                    "ValorRenegSeguroDFI": valor_reneg_segurodfi,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_parcelas_modelo_venda(
        self,
        nummodelo_venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ModeloVenda/ConsultarParcelasModeloVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consultar todos os tipo de parcelas do modelo de venda filtrando pela chave/número do modelo.
        
        
        
        Args:
            nummodelo_venda (int): The nummodelo_venda
        
        Parameter Structure:
        
            {
                "nummodelo_venda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ModeloVenda()
            >>> response = api._consultar_parcelas_modelo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ModeloVenda/ConsultarParcelasModeloVenda"
        try:
            response = self.api.post(
                path,
                json={
                    "nummodelo_venda": nummodelo_venda,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_modelo_de_venda_seguro_por_chave(
        self,
        nummodelo_venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ModeloVenda/ConsultarModeloDeVendaSeguroPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta o mo seguro do modelo de venda filtrando pela chave/número do modelo.
        
        
        
        Args:
            nummodelo_venda (int): The nummodelo_venda
        
        Parameter Structure:
        
            {
                "nummodelo_venda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ModeloVenda()
            >>> response = api._consultar_modelo_de_venda_seguro_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ModeloVenda/ConsultarModeloDeVendaSeguroPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "nummodelo_venda": nummodelo_venda,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

