from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Medicao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def manter_medicao(
        self,
        empresa: Optional[int] = None,
        numero_contrato: Optional[int] = None,
        numero_medicao: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cnpj_fornecedor: Optional[str] = None,
        num_cidade_prestacao_serv: Optional[int] = None,
        observacao: Optional[str] = None,
        ultima_medicao: Optional[int] = None,
        data_base: Optional[datetime] = None,
        usr_cadastro: Optional[str] = None,
        descontos_medicao: Optional[List[Dict]] = None,
        itens: Optional[List[Dict]] = None,
        adiantamentos: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ManterMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        
        É possível inserir ou atualizar uma medição de contrato de material e/ou serviço.
          1.2. Se o número da medição for informado e essa medição existir, então ela será atualzada, caso contrário será inserida.
        Só poderão ser atualizadas as medições que estiverem em aberto, ou seja, sem nenhuma confirmação de aprovação.
        Os adiantamentos de contratos podem ser informados de duas formas, dependendo do tipo de vínculo de planejamento do contrato, se for vinculado por item, pode ser informado diretamente no item específico, 
          ou de forma geral, onde nesse caso será feito o cálculo proporcional, se o vínculo do planejamento for somente por contrato ou não possuir vínculo algum, só pode ser informado o adiantamento geral.
        
        
        
        Args:
            Empresa (int): The empresa
            NumeroContrato (int): The numero contrato
            NumeroMedicao (int): The numero medicao
            CodigoFornecedor (int): The codigo fornecedor
            CNPJFornecedor (str): The c n p j fornecedor
            NumCidadePrestacaoServ (int): The num cidade prestacao serv
            Observacao (str): The observacao
            UltimaMedicao (int): The ultima medicao
            DataBase (datetime): The data base
            UsrCadastro (str): The usr cadastro
            DescontosMedicao (List[Dict[str, Any]]): The descontos medicao
            Itens (List[Dict[str, Any]]): The itens
            Adiantamentos (List[Dict[str, Any]]): The adiantamentos
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "NumeroContrato": 0,
                "NumeroMedicao": 0,
                "CodigoFornecedor": 0,
                "CNPJFornecedor": "string",
                "NumCidadePrestacaoServ": 0,
                "Observacao": "string",
                "UltimaMedicao": 0,
                "DataBase": "2025-04-23T13:46:13.309Z",
                "UsrCadastro": "string",
                "DescontosMedicao": [
                    {
                        "Valor": 0,
                        "Tipo": 0,
                        "Observacao": "string"
                    }
                ],
                "Itens": [
                    {
                        "Item": 0,
                        "CodigoAcompanhamento": 0,
                        "DescontosAdiantamentos": [
                            {
                                "NumeroProcesso": 0,
                                "Valor": 0,
                                "Tipo": 0
                            }
                        ]
                    }
                ],
                "Adiantamentos": [
                    {
                        "NumeroProcesso": 0,
                        "Valor": 0,
                        "Tipo": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._manter_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ManterMedicao"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "NumeroContrato": numero_contrato,
                    "NumeroMedicao": numero_medicao,
                    "CodigoFornecedor": codigo_fornecedor,
                    "CNPJFornecedor": cnpj_fornecedor,
                    "NumCidadePrestacaoServ": num_cidade_prestacao_serv,
                    "Observacao": observacao,
                    "UltimaMedicao": ultima_medicao,
                    "DataBase": data_base,
                    "UsrCadastro": usr_cadastro,
                    "DescontosMedicao": descontos_medicao,
                    "Itens": itens,
                    "Adiantamentos": adiantamentos,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def excluir_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        numero_medicao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ExcluirMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        
        Somente medições que estiverem abertas e sem nenhuma aprovação poderão ser excluídas.
        Nenhum processo de pagamento poderá estar vinculado à medição.
        Nâo pode haver vínculos dependentes entre os itens da medição (vínculo de item do tipo material com item de serviço).
        Não pode excluir medição que contenha itens que tenham gerado valores excedentes para itens de outras medições.
        
        
        
        Args:
            Empresa (int): The empresa
            Contrato (int): The contrato
            NumeroMedicao (int): The numero medicao
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Contrato": 0,
                "NumeroMedicao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._excluir_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ExcluirMedicao"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Contrato": contrato,
                    "NumeroMedicao": numero_medicao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            contrato (int): The contrato
            medicao (int): The medicao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato": 0,
                "medicao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarMedicao"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato": contrato,
                    "medicao": medicao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_itens_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarItensMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Retorna uma lista de itens da medição por empresa, contrato e medição.
        
        
        
        Args:
            empresa (int): The empresa
            contrato (int): The contrato
            medicao (int): The medicao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato": 0,
                "medicao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarItensMedicao"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato": contrato,
                    "medicao": medicao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def aprovar_medicoes_contrato(
        self,
        medicoes: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/AprovarMedicoesContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        
        O contrato precisa estar com status aprovado.
        É necessário permissão de aprovação para o programa OBMEDCONT
        
        
        
        Args:
            Medicoes (List[Dict[str, Any]]): The medicoes
        
        Parameter Structure:
        
            {
                "Medicoes": [
                    {
                        "empresa": 0,
                        "contrato": "string",
                        "medicao": "string",
                        "Codigojustificativa": 0,
                        "Observacaojustificativa": "string",
                        "departamento": "string",
                        "cargo": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._aprovar_medicoes_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/AprovarMedicoesContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "Medicoes": medicoes,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_boletim_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        avanco_fisico: Optional[bool] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarBoletimMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta boletim de medição dentro do sistema UAU.
        
        
        
        Args:
            empresa (int): The empresa
            contrato (int): The contrato
            avancoFisico (int): The fisico
            medicao (int): The medicao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato": 0,
                "avancoFisico": true,
                "medicao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_boletim_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarBoletimMedicao"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato": contrato,
                    "avancoFisico": avanco_fisico,
                    "medicao": medicao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_medicao_completa(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None,
        cnpj_contratado: Optional[str] = None,
        cnpj_fornecedor: Optional[str] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarMedicaoCompleta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Para retornar as medições, podem ser feitas as seguintes combinações:
        1. Código da empresa e código do contrato
          2. Código da empresa, código do contrato e código da medição
          3. Código da empresa e CNPJ do contrato ou CNPJ do fornecedor (informado na medição)
          4. Código da empresa e período de geração da medição (data inicial e data final)
          
        
        Args:
            Empresa (int): The empresa
            Contrato (int): The contrato
            Medicao (int): The medicao
            CNPJContratado (str): The c n p j contratado
            CNPJFornecedor (str): The c n p j fornecedor
            DataInicial (datetime): The data inicial
            DataFinal (datetime): The data final
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Contrato": 0,
                "Medicao": 0,
                "CNPJContratado": "string",
                "CNPJFornecedor": "string",
                "DataInicial": "2025-04-23T13:46:13.347Z",
                "DataFinal": "2025-04-23T13:46:13.347Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_medicao_completa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarMedicaoCompleta"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Contrato": contrato,
                    "Medicao": medicao,
                    "CNPJContratado": cnpj_contratado,
                    "CNPJFornecedor": cnpj_fornecedor,
                    "DataInicial": data_inicial,
                    "DataFinal": data_final,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_medicao_por_serv_mat(
        self,
        empresa: Optional[int] = None,
        serv_mat: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarMedicaoPorServMat`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            servMat (str): The mat
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "servMat": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_medicao_por_serv_mat(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarMedicaoPorServMat"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "servMat": serv_mat,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_medicoes_por_status(
        self,
        status_med: Optional[int] = None,
        login_usu: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarMedicoesPorStatus`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Retorna uma lista de medições por status e usuário.
        Os possíveis status de uma medição são: 
          0 - Aberta;
          1 - Aprovada;
          2 - Medida;
          3 - Proc. Serviço Gerado.
        O usuário é para indicar quais são as obras que ele possui permissão para retornar as medições pertinentes.
        
        
        
        Args:
            status_med (int): The status_med
            login_usu (str): The login_usu
        
        Parameter Structure:
        
            {
                "status_med": 0,
                "login_usu": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_medicoes_por_status(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarMedicoesPorStatus"
        try:
            response = self.api.post(
                path,
                json={
                    "status_med": status_med,
                    "login_usu": login_usu,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def validar_cnpjao_gravar_medicao(
        self,
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._validarcnpj_ao_gravar_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Medicao/ValidarCNPJAoGravarMedicao"
        try:
            response = self.api.post(
                path,
                json={
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_medicao_por_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarMedicaoPorContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            contrato (int): The contrato
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_medicao_por_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarMedicaoPorContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato": contrato,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_itens_medicao_por_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarItensMedicaoPorMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            contrato (int): The contrato
            medicao (int): The medicao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato": 0,
                "medicao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarItensMedicaoPorMedicao"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato": contrato,
                    "medicao": medicao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_itens_medicao_por_serv_mat(
        self,
        empresa: Optional[int] = None,
        serv_mat: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarItensMedicaoPorServMat`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            servMat (str): The mat
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "servMat": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_serv_mat(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarItensMedicaoPorServMat"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "servMat": serv_mat,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_itens_medicao_por_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarItensMedicaoPorContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            contrato (int): The contrato
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarItensMedicaoPorContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato": contrato,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_itens_medicao_por_item_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None,
        item_contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Medicao/ConsultarItensMedicaoPorItemContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            empresa (int): The empresa
            contrato (int): The contrato
            medicao (int): The medicao
            itemContrato (int): The contrato
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato": 0,
                "medicao": 0,
                "itemContrato": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Medicao()
            >>> response = api._consultar_itens_medicao_por_item_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Medicao/ConsultarItensMedicaoPorItemContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato": contrato,
                    "medicao": medicao,
                    "itemContrato": item_contrato,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

