from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class Recebiveis:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_meios_preferenciais_recebimento(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Recebiveis/ConsultarMeiosPreferenciaisRecebimento`
        HTTP Method: `GET`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Permite consultar os meios preferenciais de recebimento que estão ativos.
        
        
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
            >>> api = Recebiveis()
            >>> response = api._consultar_meios_preferenciais_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Recebiveis/ConsultarMeiosPreferenciaisRecebimento"
        try:
            response = self.api.get(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def by_numpadraocobranca(
        self,
        id_empresa: str,
        num_padrao_cobranca: str,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Recebiveis/PadraoDeCobranca/{IdEmpresa}/{NumPadraoCobranca}`
        HTTP Method: `GET`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma empresa cadastrada.
        Numero do padrão de cobrança 0 busca todos os padrões de cobrança.
        
        
        
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
            >>> api = Recebiveis()
            >>> response = api.{_num_padrao_cobranca}(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"Recebiveis/PadraoDeCobranca/{IdEmpresa}/{NumPadraoCobranca}"
        try:
            response = self.api.get(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def parcelas_ecobrancas_do_cliente(
        self,
        cpf: Optional[str] = None,
        valor_reajustado: Optional[bool] = None,
        qtde_parcelas: Optional[int] = None,
        data_inicio_vencimento: Optional[datetime] = None,
        data_fim_vencimento: Optional[datetime] = None,
        pesquisa_por_nao_titulares: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Recebiveis/ParcelasECobrancasDoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Definição de Negócio:
        
        Busca parcelas e cobranças em aberto do cliente, informando o CPF.
        O parametro PesquisaPorNaoTitulares não é obrigatório, se não informado no request ou informado false, buscará somente dos clientes da venda que possuam o tipo 0 - Titular. Caso informado true buscará de todos os clientes da venda independente do tipo.
        
        
        
        Args:
            Cpf (str): The cpf
            ValorReajustado (int): The valor reajustado
            QtdeParcelas (int): The qtde parcelas
            DataInicioVencimento (datetime): The data inicio vencimento
            DataFimVencimento (datetime): The data fim vencimento
            PesquisaPorNaoTitulares (int): The pesquisa por nao titulares
        
        Parameter Structure:
        
            {
                "Cpf": "string",
                "ValorReajustado": true,
                "QtdeParcelas": 0,
                "DataInicioVencimento": "2025-04-23T13:46:14.396Z",
                "DataFimVencimento": "2025-04-23T13:46:14.396Z",
                "PesquisaPorNaoTitulares": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Recebiveis()
            >>> response = api._parcelase_cobrancas_do_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Recebiveis/ParcelasECobrancasDoCliente"
        try:
            response = self.api.post(
                path,
                json={
                    "Cpf": cpf,
                    "ValorReajustado": valor_reajustado,
                    "QtdeParcelas": qtde_parcelas,
                    "DataInicioVencimento": data_inicio_vencimento,
                    "DataFimVencimento": data_fim_vencimento,
                    "PesquisaPorNaoTitulares": pesquisa_por_nao_titulares,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def alterar_meio_preferencial_de_recebimento_da_parcela(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        numero_parcela: Optional[int] = None,
        tipo_parcela: Optional[str] = None,
        numero_parcela_geral: Optional[int] = None,
        meio_preferencial_recebimento: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Recebiveis/AlterarMeioPreferencialDeRecebimentoDaParcela`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Permite alteração na parcela do meio preferencial de recebimento.
          Permite consultar a alteração realizada na parcela.
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Venda (int): The venda
            NumeroParcela (int): The numero parcela
            TipoParcela (str): The tipo parcela
            NumeroParcelaGeral (int): The numero parcela geral
            MeioPreferencialRecebimento (int): The meio preferencial recebimento
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Venda": 0,
                "NumeroParcela": 0,
                "TipoParcela": "string",
                "NumeroParcelaGeral": 0,
                "MeioPreferencialRecebimento": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Recebiveis()
            >>> response = api._alterar_meio_preferencial_de_recebimento_da_parcela(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Recebiveis/AlterarMeioPreferencialDeRecebimentoDaParcela"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Obra": obra,
                    "Venda": venda,
                    "NumeroParcela": numero_parcela,
                    "TipoParcela": tipo_parcela,
                    "NumeroParcelaGeral": numero_parcela_geral,
                    "MeioPreferencialRecebimento": meio_preferencial_recebimento,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

