from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class Venda:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def renegociar_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        parc_geradas: Optional[List[Dict]] = None,
        parc_sel_reneg: Optional[List[Dict]] = None,
        val_desc_reneg: Optional[int] = None,
        val_acresc_reneg: Optional[int] = None,
        valor_reajustado: Optional[int] = None,
        numero_padrao_cobranca: Optional[int] = None,
        tabelaplano_idx: Optional[List[Dict]] = None,
        data_calculo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/RenegociarVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método
        
        Definição de Negócio:
          Permite renegociar parcelas de uma venda
        
        O usuário deverá estar autenticado e validado
        Informar os dados da venda
        Informar as parcelas a serem geradas
        Informar as parcelas escolhidas para renegociação
        Informar o plano de indexação
        Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
          retorna mensagem informando a inconsistência encontrada para que seja analisada
        Após as validações realiza a renegociação das parcelas
        Será registrado comentário na venda sobre a renegociação realizada
        Lista de planos indexadores
        Caso não informe a lista de planos indexadores, serão considerados os planos que já existem na venda. 
        Caso informe a lista de planos indexadores, a lista informada será considerada.
        Caso um grupo informado de plano indexador já exista na venda, ele não será inserido novamente.
        Para verificar se os planos já existem, serão considerados os grupos. Se para um grupo informado, já existir os mesmos indíces e datas na venda, ele não será adicionado.
        
        
        
        
        Padrão de Cobrança
        
        Padrão de Cobrança Informado no JSON. (Se o tipo de parcela tiver um padrão de cobrança vinculado, esse padrão será priorizado.)
            Exemplo:
            Padrão de cobrança informado: 4
            Parcela: P, Padrão de cobrança: 2
            Parcela: J, Não possui padrão de cobrança
            Parcelas geradas:
            Parcela: P, Padrão de cobrança: 2
            Parcela: J, Padrão de cobrança: 4
        
        -Padrão de Cobrança Não Informado no JSON:
        - Se o padrão de cobrança não for informado no JSON, ele será consultado pela obra.
          
          - Se o número do padrão de cobrança não for informado no JSON e na obra não estiver cadastrado, será utilizado o padrão de cobrança da primeira parcela
          que foi selecionada para renegociação. Esse padrão de cobrança será então preenchido em todas as parcelas.
          
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
        Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Venda (int): The venda
            Parc_Geradas (List[Dict[str, Any]]): The parc_ geradas
            ParcSel_Reneg (List[Dict[str, Any]]): The parc sel_ reneg
            ValDesc_reneg (int): The val desc_reneg
            ValAcresc_reneg (int): The val acresc_reneg
            Valor_Reajustado (int): The valor_ reajustado
            NumeroPadraoCobranca (int): The numero padrao cobranca
            Tabelaplano_idx (List[Dict[str, Any]]): The tabelaplano_idx
            DataCalculo (str): The data calculo
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Venda": 0,
                "Parc_Geradas": [
                    {
                        "NumParc_pg": 0,
                        "NumParcGer_pg": 0,
                        "Tipo_pg": "string",
                        "Valor_pg": 0,
                        "Data_pg": "2025-04-23T13:46:14.526Z",
                        "DtParc_pg": "2025-04-23T13:46:14.526Z",
                        "AmortParc_pg": 0,
                        "BeginEndParc_pg": 0,
                        "GrupoParc_pg": 0,
                        "TotParcGrupo_pg": 0,
                        "ComoParc_pg": "string",
                        "DtJurParc_pg": "2025-04-23T13:46:14.526Z",
                        "JurosParc_pg": 0,
                        "DataSegJuros_pg": "2025-04-23T13:46:14.526Z",
                        "PorcSegJuros_pg": 0,
                        "DtIdxParc_pg": "2025-04-23T13:46:14.526Z",
                        "IdxReaj_pg": "string",
                        "GrupoIdx_pg": 0,
                        "DtJurosComJuros_pg": 0,
                        "CobrarJurosProRata_pg": 0,
                        "CobrarJurosProRataPrimeiroMes_pg": 0,
                        "CarenciaAtraso_pg": 0,
                        "CarenciaAtrasoCorrecao_pg": 0,
                        "DataCompetencia_pg": "2025-04-23T13:46:14.526Z",
                        "CobrarMulta_pg": 0,
                        "CobrarJurosAtr_pg": 0,
                        "CobrarCorrecao_pg": 0,
                        "CobrarTxAdm_pg": 0,
                        "CobrarImposto_pg": 0,
                        "CobrarCPMF_pg": 0,
                        "OrigemCusta_pg": 0,
                        "RepassarLocador_pg": 0,
                        "NumCtp_pg": 0,
                        "TipoSeguro_pg": 0,
                        "TotParc_pg": 0,
                        "Cap_pg": "string",
                        "CapAcrescimo_pg": "string",
                        "CapDesconto_pg": "string",
                        "CapDescontoCusta_pg": "string",
                        "CapDescontoAntec_pg": "string",
                        "CapCorrecao_pg": "string",
                        "CapCorrecaoAtr_pg": "string",
                        "CapDescontoCondicional_pg": "string",
                        "CapJuros_pg": "string",
                        "CapJurosAtr_pg": "string",
                        "CapMulta_pg": "string",
                        "CapRepasse_pg": "string",
                        "CapTaxaBol_pg": "string"
                    }
                ],
                "ParcSel_Reneg": [
                    {
                        "NumParc_pg": 0,
                        "NumParcGer_pg": 0,
                        "Tipo_pg": "string"
                    }
                ],
                "ValDesc_reneg": 0,
                "ValAcresc_reneg": 0,
                "Valor_Reajustado": 0,
                "NumeroPadraoCobranca": 0,
                "Tabelaplano_idx": [
                    {
                        "NumPlano_pip": 0,
                        "CodigoIdx_pip": "string",
                        "Data_pidx": "2025-04-23T13:46:14.527Z"
                    }
                ],
                "DataCalculo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._renegociar_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/RenegociarVenda"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Venda": venda,
            "Parc_Geradas": parc_geradas,
            "ParcSel_Reneg": parc_sel_reneg,
            "ValDesc_reneg": val_desc_reneg,
            "ValAcresc_reneg": val_acresc_reneg,
            "Valor_Reajustado": valor_reajustado,
            "NumeroPadraoCobranca": numero_padrao_cobranca,
            "Tabelaplano_idx": tabelaplano_idx,
            "DataCalculo": data_calculo,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def busca_parc_reneg_web(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_ven: Optional[int] = None,
        exibirparcenv_cob: Optional[bool] = None,
        somenteparc_atraso: Optional[bool] = None,
        parcelasenviadas_banco: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscaParcRenegWeb`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Possibilita buscar parcelas calculadas para a data atual (dia da requisição).
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_ven (int): The num_ven
            exibirparcenv_cob (int): The exibirparcenv_cob
            somenteparc_atraso (int): The somenteparc_atraso
            parcelasenviadas_banco (int): The parcelasenviadas_banco
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_ven": 0,
                "exibirparcenv_cob": true,
                "somenteparc_atraso": true,
                "parcelasenviadas_banco": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._busca_parc_reneg_web(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscaParcRenegWeb"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_ven": num_ven,
            "exibirparcenv_cob": exibirparcenv_cob,
            "somenteparc_atraso": somenteparc_atraso,
            "parcelasenviadas_banco": parcelasenviadas_banco,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def exclusao_de_boletos(
        self,
        lista_boletos_excluir: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ExclusaoDeBoletos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Possibilita excluir boletos que estão com o status de normal.
        Será permitido a exclusão de no máximo 20 boletos por requisição.
        
        
        
        Args:
            listaBoletosExcluir (List[Dict[str, Any]]): The boletos excluir
        
        Parameter Structure:
        
            {
                "listaBoletosExcluir": [
                    {
                        "seuNumero": 0,
                        "numeroBanco": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._exclusao_de_boletos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ExclusaoDeBoletos"
        kwargs = {
            "listaBoletosExcluir": lista_boletos_excluir,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def exportar_vendas_xml(
        self,
        dados_vendas: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ExportarVendasXml`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os dados das contas contábeis com a URI + /api/v{version}/Venda/ExportarVendasXml
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite exportar os registros de uma ou mais vendas do UAU para um arquivo XML no formato esperado para realização de importação de vendas.
        
        Deve informar a venda ou o período para que seja realizada a consulta.
        Pode informar as chaves de Venda que são [Empresa, Obra, Venda].
        Valida as datas e campos inseridos.
        O perído informado buscará vendas considerando a data de cadastro, a data de manutenção e a data de quitação.
        O item "listaVendas" permite informar empresa, obra e venda que serão adicionados ao retorno da consulta. 
          Não será filtrado exclusivamente por esta lista de vendas, mas serão acrescidas ao resultado do período informado.
        
        VirtUau:
        
        http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Venda/Venda_ExportarVendasXml
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777060/ 
        Arquivo de Retorno: https://ajuda.globaltec.com.br/download/777060/
        
        
        
        Args:
            dados_vendas (Dict[str, Any]): The dados_vendas
        
        Parameter Structure:
        
            {
                "dados_vendas": {
                    "dataInicio": "2025-04-23T13:46:14.544Z",
                    "dataFim": "2025-04-23T13:46:14.544Z",
                    "statusEscrituracao": true,
                    "listaVendas": [
                        {
                            "Empresa": 0,
                            "Obra": "string",
                            "Venda": 0
                        }
                    ]
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._exportar_vendas_xml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ExportarVendasXml"
        kwargs = {
            "dados_vendas": dados_vendas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def importacao_de_venda(
        self,
        xml_vendas: Optional[str] = None,
        alterarnumerodas_vendas: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ImportacaoDeVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Número máximo de importações por vez: 50.
        Para obter retorno de sucesso ou falha na importação consulte o endpoint:
        URI + /api/v1.0/Venda/ImportacaoVendaComRetorno
        
        
        
        Validação:
        
        Arquivo XSD: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Manual-de-integracao-de-Vendas_versao1006_2.zip
        
        Dicionário de dados: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Venda.zip
        
        
        Definição de Negócio:
        Permite importar vendas para o UAU via XML.
        
        Valida quantidade de importações por requisição.
        Caso ocorra erro em uma venda, todas as outras importações são canceladas.
        
        
        
        Args:
            xml_vendas (str): The xml_vendas
            alterarnumerodas_vendas (int): The alterarnumerodas_vendas
        
        Parameter Structure:
        
            {
                "xml_vendas": "string",
                "alterarnumerodas_vendas": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._importacao_de_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ImportacaoDeVenda"
        kwargs = {
            "xml_vendas": xml_vendas,
            "alterarnumerodas_vendas": alterarnumerodas_vendas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def aprov_desaprov_reneg(
        self,
        cod_empresa: Optional[int] = None,
        cod_obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        aprov_desaprov: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/AprovDesaprovReneg`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de negócio
        
        A rota aprova ou desaprova uma renegociação de venda.
        É realizada uma validação da Alçada.
        Os anexos são atualizados conforme a operação solicitada.
        
        Pré requisito:
        
        É necessário ter permissão de aprovação em FIMNTVENRENCON
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        
        URL + /api/v{version}/Venda/AprovDesaprovReneg
        
        
        
        
        
        Args:
            codEmpresa (int): The empresa
            codObra (str): The obra
            numVenda (int): The venda
            aprovDesaprov (int): The desaprov
        
        Parameter Structure:
        
            {
                "codEmpresa": 0,
                "codObra": "string",
                "numVenda": 0,
                "aprovDesaprov": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._aprov_desaprov_reneg(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/AprovDesaprovReneg"
        kwargs = {
            "codEmpresa": cod_empresa,
            "codObra": cod_obra,
            "numVenda": num_venda,
            "aprovDesaprov": aprov_desaprov,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_tipos_de_custas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarTiposDeCustas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Busca a lista de status de cobrança ativos do sistema:
        
        URI + /api/v{version}/Venda/BuscarTiposDeCustas
        
        
        Formato dos dados retornados:
        
        Codigo(String):Código do tipo de custa
        Descricao(String):Descrição do status de cobrança
        
        
        
        
        
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
            >>> api = Venda()
            >>> response = api._buscar_tipos_de_custas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarTiposDeCustas"
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_historicos(
        self,
        vendas: Optional[List[Dict]] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        tipo_manutencao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarHistoricos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        O preenchimento da lista de vendas, devem ser preenchidos de forma padronizada, ou preenche todas as vendas com o número da venda, ou todas com apenas empresa e obra.
        Para o preenchimento dos tipos de manutenção, o valor de tipo de manutenção deve ser numérico e caso tenha mais de um, devem ser separados por vírgula. Exemplo: 1,2,4.
        Recomendável buscar períodos curtos ou uma venda específica para evitar timeout.
        
        Definição de Negócio:
          Consultar os históricos de uma ou mais vendas selecionadas.
          Para buscar os históricos das vendas um dos parâmetros devem estar preenchidos, ou a lista de vendas ou o período da manutenção.
        
        As classes abaixo não serão preenchidas no objeto de retorno porque essas informações não possuem histórico:
        Comissoes
        Comentarios
        AluguelShopping
        VendaVinculada
        DescontosDeCusta
        Recebimentos
        Prorrogacoes
        
        
        
        
        
        Args:
            Vendas (List[Dict[str, Any]]): The vendas
            DataInicio (datetime): The data inicio
            DataFim (datetime): The data fim
            TipoManutencao (str): The tipo manutencao
        
        Parameter Structure:
        
            {
                "Vendas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "Venda": 0
                    }
                ],
                "DataInicio": "2025-04-23T13:46:14.594Z",
                "DataFim": "2025-04-23T13:46:14.594Z",
                "TipoManutencao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_historicos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarHistoricos"
        kwargs = {
            "Vendas": vendas,
            "DataInicio": data_inicio,
            "DataFim": data_fim,
            "TipoManutencao": tipo_manutencao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def excluir_parcela_custa(
        self,
        excluir_parcela_no_banco: Optional[bool] = None,
        lista: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ExcluirParcelaCusta`
        HTTP Method: `POST`
        
        Args:
            ExcluirParcelaNoBanco (int): The excluir parcela no banco
            Lista (List[Dict[str, Any]]): The lista
        
        Parameter Structure:
        
            {
                "ExcluirParcelaNoBanco": true,
                "Lista": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "Venda": 0,
                        "NumeroParcela": 0,
                        "TipoParcela": "string",
                        "NumeroGeralParcela": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._excluir_parcela_custa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ExcluirParcelaCusta"
        kwargs = {
            "ExcluirParcelaNoBanco": excluir_parcela_no_banco,
            "Lista": lista,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_boleto_bancario(
        self,
        parcelas: Optional[List[Dict]] = None,
        data_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        reajustar: Optional[bool] = None,
        excluirboleto_expirado: Optional[bool] = None,
        formaarquivo_cobranca: Optional[int] = None,
        boletosacado_detalhado: Optional[bool] = None,
        carnetres_vias: Optional[bool] = None,
        naovalidardados_pendentes: Optional[bool] = None,
        acrescentar_residuo: Optional[bool] = None,
        usarpadraoboleto_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        formaagruparpor_vendas: Optional[bool] = None,
        valor_boleto: Optional[int] = None,
        padrao_cobranca: Optional[int] = None,
        excluir_boletos_existentes: Optional[bool] = None,
        reaproveitar_boleto: Optional[bool] = None,
        valor_taxa_boleto: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GerarBoletoBancario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Permite gerar o boleto bancário ou carnê.
        O usuário autenticado deve ter permissão de inclusão no programa de permissão VEBOLETOAVULSO.
        Para gerar boleto parcial é necessário informar a propriedade ValorBoleto.
        Não pode ser um valor negativo nem inferior a 0,01 centavo.
        Se informar um valor igual ao valor total das parcelas enviadas, será gerado um boleto normal.
        Se informar um valor menor que o valor total das parcelas enviadas, será gerado um boleto parcial.
        Apenas uma parcela das enviadas deverá ser parcial
        Não será gerado boleto caso informe um valor que não cubra todas as parcelas enviadas
        A ordem de envio das parcelas deve ser a mesma ordem de seleção das parcelas ao gerar o boleto pela tela de recebimento avulso.
          Exemplo: Na tela de recebimento avulso, selecionei as parcelas 360, 359 e 358. Ao gerar pela API, as parcelas devem ser enviadas
          na mesma sequência selecionada.
        Irá validar se as parcelas enviadas podem gerar o boleto parcial de acordo com a regra de dias para vencimento.
        
        
        Será possível gerar boleto parcial somente para parcelas de uma única empresa, obra e venda.
        Só é possível gerar boleto parcial para mais de uma parcela quando for antecipação.
        É obrigatório reajustar ao gerar o boleto parcial.
        
        
        Padrão de cobrança    
        Não é obrigatório informá-lo.
        Caso informado, o sistema irá desconsiderar a configuração do parâmetro usarpadraoboleto_avulso e irá gerar o boleto pelo padrão informado.
        Caso informado, será desconsiderado o padrão de cobrança de todas as parcelas, incluindo custas administrativas, e boleto será gerado com o padrão de cobrança informado.
        Apenas os padrões de cobrança ativos serão aceitos.
        Será possivel gerar boleto com o padrão de informado somente para parcelas de uma única empresa.
        
        
        Excluir Boletos Existentes
        Não é obrigatório informar o parâmetro ExcluirBoletosExistentes.
        Caso não seja informado será mantido a opção padrão de não excluir.
        Caso informado, irá executar as mesmas ações que a configuração 'Excluir boletos já emitidos ao gerar um novo boleto para a parcela' no cadastro de empresas > config. vendas.
        
        
        Reaproveitar boleto
        Não é obrigatório informar o parâmetro ReaproveitarBoleto
        Caso não seja informado será mantida a opção padrão de não reaproveitar o boleto,
        Caso informado, irá tentar reaproveitar algum boleto que já exista para uma das parcelas enviadas.
        Somente válido para bancos e/ou tipos de cobrança que permitem a manutenção do boleto.
        Somente para parcelas de uma única empresa, obra e venda. Caso envie parcelas de vendas diferentes, a opção de reaproveitar boleto será desconsiderada e irá gerar um novo boleto.
        Será gerado arquivo de alteração de vencimento ou valor do boleto.
        Não será possivel reaproveitar caso não exista boleto gerado ou o agrupamento das parcelas gere mais de um boleto.
        
        
        Sempre homologue junto ao banco antes de usar!
        
        
        Valor taxa boleto
        Não é obrigatório informar o parâmetro ValorTaxaBoleto
        Essa taxa será utilizada independente do parâmetro de reaproveitar boleto for true e a venda cobrar taxa de boleto.
        Caso informado, irá desconsiderar o valor da taxa cadastrado na empresa e aplicar o valor informado.
        Caso não seja informado ou seja informado zero, irá aplicar o valor da taxa cadastrado na empresa do boleto reaproveitado.
        
        
        
        
        
        Args:
            parcelas (List[Dict[str, Any]]): The parcelas
            data_calculo (datetime): The data_calculo
            antecipar (int): The antecipar
            reajustar (int): The reajustar
            excluirboleto_expirado (int): The excluirboleto_expirado
            formaarquivo_cobranca (int): The formaarquivo_cobranca
            boletosacado_detalhado (int): The boletosacado_detalhado
            carnetres_vias (int): The carnetres_vias
            naovalidardados_pendentes (int): The naovalidardados_pendentes
            acrescentar_residuo (int): The acrescentar_residuo
            usarpadraoboleto_avulso (int): The usarpadraoboleto_avulso
            agrupar_parcelas (int): The agrupar_parcelas
            formaagruparpor_vendas (int): The formaagruparpor_vendas
            ValorBoleto (int): The valor boleto
            PadraoCobranca (int): The padrao cobranca
            ExcluirBoletosExistentes (int): The excluir boletos existentes
            ReaproveitarBoleto (int): The reaproveitar boleto
            ValorTaxaBoleto (int): The valor taxa boleto
        
        Parameter Structure:
        
            {
                "parcelas": [
                    {
                        "Empresa_reaj": 0,
                        "Obra_reaj": "string",
                        "NumVenda_reaj": 0,
                        "NumParc_reaj": 0,
                        "Tipo_reaj": "string",
                        "NumParcGer_reaj": 0,
                        "ValorDescAnt_reaj": 0
                    }
                ],
                "data_calculo": "2025-04-23T13:46:14.605Z",
                "antecipar": true,
                "reajustar": true,
                "excluirboleto_expirado": true,
                "formaarquivo_cobranca": 0,
                "boletosacado_detalhado": true,
                "carnetres_vias": true,
                "naovalidardados_pendentes": true,
                "acrescentar_residuo": true,
                "usarpadraoboleto_avulso": true,
                "agrupar_parcelas": true,
                "formaagruparpor_vendas": true,
                "ValorBoleto": 0,
                "PadraoCobranca": 0,
                "ExcluirBoletosExistentes": true,
                "ReaproveitarBoleto": true,
                "ValorTaxaBoleto": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._gerar_boleto_bancario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GerarBoletoBancario"
        kwargs = {
            "parcelas": parcelas,
            "data_calculo": data_calculo,
            "antecipar": antecipar,
            "reajustar": reajustar,
            "excluirboleto_expirado": excluirboleto_expirado,
            "formaarquivo_cobranca": formaarquivo_cobranca,
            "boletosacado_detalhado": boletosacado_detalhado,
            "carnetres_vias": carnetres_vias,
            "naovalidardados_pendentes": naovalidardados_pendentes,
            "acrescentar_residuo": acrescentar_residuo,
            "usarpadraoboleto_avulso": usarpadraoboleto_avulso,
            "agrupar_parcelas": agrupar_parcelas,
            "formaagruparpor_vendas": formaagruparpor_vendas,
            "ValorBoleto": valor_boleto,
            "PadraoCobranca": padrao_cobranca,
            "ExcluirBoletosExistentes": excluir_boletos_existentes,
            "ReaproveitarBoleto": reaproveitar_boleto,
            "ValorTaxaBoleto": valor_taxa_boleto,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_pdfresumo_venda(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None,
        aplicar_desconto_geral: Optional[bool] = None,
        percentual_desconto_geral: Optional[int] = None,
        aplicar_desconto_antecipacao: Optional[bool] = None,
        desconto_antecipacao: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GerarPDFResumoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.
        
        Definição de Negócio:
          Gera boleto PDF do resumo da venda em formato Base64.
        
        Validações a nível de usuário.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            numeroVenda (int): The venda
            dataCalculo (datetime): The calculo
            dataCorrecao (datetime): The correcao
            antecipar (int): The antecipar
            parcelas (List[Dict[str, Any]]): The parcelas
            aplicarDescontoGeral (int): The desconto geral
            percentualDescontoGeral (int): The desconto geral
            aplicarDescontoAntecipacao (int): The desconto antecipacao
            descontoAntecipacao (Dict[str, Any]): The antecipacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "numeroVenda": 0,
                "dataCalculo": "2025-04-23T13:46:14.611Z",
                "dataCorrecao": "2025-04-23T13:46:14.611Z",
                "antecipar": true,
                "parcelas": [
                    {
                        "numeroParcela": 0,
                        "numeroParcelaGeral": 0,
                        "tipoParcela": "string"
                    }
                ],
                "aplicarDescontoGeral": true,
                "percentualDescontoGeral": 0,
                "aplicarDescontoAntecipacao": true,
                "descontoAntecipacao": {
                    "percentualDescAntecipacao": 0,
                    "tipoDescAntecipacao": 0,
                    "descontoAteHabitese": true
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._gerarpdf_resumo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GerarPDFResumoVenda"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "numeroVenda": numero_venda,
            "dataCalculo": data_calculo,
            "dataCorrecao": data_correcao,
            "antecipar": antecipar,
            "parcelas": parcelas,
            "aplicarDescontoGeral": aplicar_desconto_geral,
            "percentualDescontoGeral": percentual_desconto_geral,
            "aplicarDescontoAntecipacao": aplicar_desconto_antecipacao,
            "descontoAntecipacao": desconto_antecipacao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_status_cobranca(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarStatusCobranca`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Busca a lista de status de cobrança ativos do sistema:
        
        URI + /api/v{version}/Venda/BuscarStatusCobranca
        
        
        Formato dos dados retornados:
        
        Codigo(Integer):Código do status de cobrança
        Descricao(String):Descrição do status de cobrança
        
        
        
        
        
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
            >>> api = Venda()
            >>> response = api._buscar_status_cobranca(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarStatusCobranca"
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_resumo_venda(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None,
        aplicar_desconto_geral: Optional[bool] = None,
        percentual_desconto_geral: Optional[int] = None,
        aplicar_desconto_antecipacao: Optional[bool] = None,
        desconto_antecipacao: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarResumoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Obtêm informações referentes a venda consultada.
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            numeroVenda (int): The venda
            dataCalculo (datetime): The calculo
            dataCorrecao (datetime): The correcao
            antecipar (int): The antecipar
            parcelas (List[Dict[str, Any]]): The parcelas
            aplicarDescontoGeral (int): The desconto geral
            percentualDescontoGeral (int): The desconto geral
            aplicarDescontoAntecipacao (int): The desconto antecipacao
            descontoAntecipacao (Dict[str, Any]): The antecipacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "numeroVenda": 0,
                "dataCalculo": "2025-04-23T13:46:14.624Z",
                "dataCorrecao": "2025-04-23T13:46:14.624Z",
                "antecipar": true,
                "parcelas": [
                    {
                        "numeroParcela": 0,
                        "numeroParcelaGeral": 0,
                        "tipoParcela": "string"
                    }
                ],
                "aplicarDescontoGeral": true,
                "percentualDescontoGeral": 0,
                "aplicarDescontoAntecipacao": true,
                "descontoAntecipacao": {
                    "percentualDescAntecipacao": 0,
                    "tipoDescAntecipacao": 0,
                    "descontoAteHabitese": true
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_resumo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarResumoVenda"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "numeroVenda": numero_venda,
            "dataCalculo": data_calculo,
            "dataCorrecao": data_correcao,
            "antecipar": antecipar,
            "parcelas": parcelas,
            "aplicarDescontoGeral": aplicar_desconto_geral,
            "percentualDescontoGeral": percentual_desconto_geral,
            "aplicarDescontoAntecipacao": aplicar_desconto_antecipacao,
            "descontoAntecipacao": desconto_antecipacao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_venda_de_proposta(
        self,
        numero_proposta: Optional[int] = None,
        atualiza_datas_da_venda: Optional[bool] = None,
        data_venda: Optional[datetime] = None,
        atualiza_inicio_primeiro_juros: Optional[bool] = None,
        atualiza_inicio_reajuste: Optional[bool] = None,
        atualiza_inicio_segundo_juros: Optional[bool] = None,
        atualiza_base_residuo: Optional[bool] = None,
        atualiza_plano_indexador: Optional[bool] = None,
        data_primeiro_juros: Optional[datetime] = None,
        data_segundo_juros: Optional[datetime] = None,
        data_reajuste: Optional[datetime] = None,
        data_base_residuo: Optional[datetime] = None,
        lista_plano_indexador: Optional[List[Dict]] = None,
        desconsiderar_nao_titulares_avalista: Optional[bool] = None,
        dias_prorrogacao_parc_vencidas: Optional[int] = None,
        usuario_cad_venda: Optional[str] = None,
        lista_nao_titular_avalista: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GerarVendaDeProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Realiza venda de acordo com a proposta informada.
        
        Validações serão realizadas para efetuar a operação.
        Todas alterações informadas no request apenas afetarão a venda gerada.
        A opção de desconsiderar não titulares avalistas, serve para o caso onde queriam gravar uma venda sem titular avalista, que possa está configurado na proposta.
        Se informar o lista de não titulares, o sistema vai desconsiderar os da proposta e utilizar os informados no request.
        A lista de não titulares deve conter o código das pessoas no UAU.
        
        
        
        Args:
            numeroProposta (int): The proposta
            atualizaDatasDaVenda (int): The datas da venda
            dataVenda (datetime): The venda
            atualizaInicioPrimeiroJuros (int): The inicio primeiro juros
            atualizaInicioReajuste (int): The inicio reajuste
            atualizaInicioSegundoJuros (int): The inicio segundo juros
            atualizaBaseResiduo (int): The base residuo
            atualizaPlanoIndexador (int): The plano indexador
            dataPrimeiroJuros (datetime): The primeiro juros
            dataSegundoJuros (datetime): The segundo juros
            dataReajuste (datetime): The reajuste
            dataBaseResiduo (datetime): The base residuo
            listaPlanoIndexador (List[Dict[str, Any]]): The plano indexador
            desconsiderarNaoTitularesAvalista (int): The nao titulares avalista
            diasProrrogacaoParcVencidas (int): The prorrogacao parc vencidas
            usuarioCadVenda (str): The cad venda
            listaNaoTitularAvalista (List[Dict[str, Any]]): The nao titular avalista
        
        Parameter Structure:
        
            {
                "numeroProposta": 0,
                "atualizaDatasDaVenda": true,
                "dataVenda": "2025-04-23T13:46:14.663Z",
                "atualizaInicioPrimeiroJuros": true,
                "atualizaInicioReajuste": true,
                "atualizaInicioSegundoJuros": true,
                "atualizaBaseResiduo": true,
                "atualizaPlanoIndexador": true,
                "dataPrimeiroJuros": "2025-04-23T13:46:14.663Z",
                "dataSegundoJuros": "2025-04-23T13:46:14.663Z",
                "dataReajuste": "2025-04-23T13:46:14.663Z",
                "dataBaseResiduo": "2025-04-23T13:46:14.663Z",
                "listaPlanoIndexador": [
                    {
                        "codGrupoPlanoIdx": 0,
                        "indice": "string",
                        "data": "2025-04-23T13:46:14.663Z",
                        "novaData": "2025-04-23T13:46:14.663Z"
                    }
                ],
                "desconsiderarNaoTitularesAvalista": true,
                "diasProrrogacaoParcVencidas": 0,
                "usuarioCadVenda": "string",
                "listaNaoTitularAvalista": [
                    {
                        "codPessoa": 0,
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
            >>> api = Venda()
            >>> response = api._gerar_venda_de_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GerarVendaDeProposta"
        kwargs = {
            "numeroProposta": numero_proposta,
            "atualizaDatasDaVenda": atualiza_datas_da_venda,
            "dataVenda": data_venda,
            "atualizaInicioPrimeiroJuros": atualiza_inicio_primeiro_juros,
            "atualizaInicioReajuste": atualiza_inicio_reajuste,
            "atualizaInicioSegundoJuros": atualiza_inicio_segundo_juros,
            "atualizaBaseResiduo": atualiza_base_residuo,
            "atualizaPlanoIndexador": atualiza_plano_indexador,
            "dataPrimeiroJuros": data_primeiro_juros,
            "dataSegundoJuros": data_segundo_juros,
            "dataReajuste": data_reajuste,
            "dataBaseResiduo": data_base_residuo,
            "listaPlanoIndexador": lista_plano_indexador,
            "desconsiderarNaoTitularesAvalista": desconsiderar_nao_titulares_avalista,
            "diasProrrogacaoParcVencidas": dias_prorrogacao_parc_vencidas,
            "usuarioCadVenda": usuario_cad_venda,
            "listaNaoTitularAvalista": lista_nao_titular_avalista,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_tipos_de_parcelas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarTiposDeParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Busca a lista de status de cobrança ativos do sistema:
        
        URI + /api/v{version}/Venda/BuscarTiposDeParcelas
        
        
        Formato dos dados retornados:
        
        Tipo(String):Código do tipo de parcela
        Descricao(String):Descrição do tipo de parcela
        
        
        
        
        
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
            >>> api = Venda()
            >>> response = api._buscar_tipos_de_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarTiposDeParcelas"
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def finalizar_renegociacao(
        self,
        usuario_logado: Optional[str] = None,
        parc_geradas_json: Optional[str] = None,
        parcsel_reneg_json: Optional[str] = None,
        grupo_parcelas_json: Optional[str] = None,
        valdesc_reneg: Optional[int] = None,
        valacresc_reneg: Optional[int] = None,
        val_reneg: Optional[int] = None,
        pendentevalidar_alcada: Optional[bool] = None,
        venda: Optional[int] = None,
        obra: Optional[str] = None,
        empresa: Optional[int] = None,
        tabelaplano_idx_json: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/FinalizarRenegociacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Possibilita finalizar determinada negociação.
        
        
        Args:
            usuario_logado (str): The usuario_logado
            parc_geradas_json (str): The parc_geradas_json
            parcsel_reneg_json (str): The parcsel_reneg_json
            grupo_parcelas_json (str): The grupo_parcelas_json
            valdesc_reneg (int): The valdesc_reneg
            valacresc_reneg (int): The valacresc_reneg
            val_reneg (int): The val_reneg
            pendentevalidar_alcada (int): The pendentevalidar_alcada
            venda (int): The venda
            obra (str): The obra
            empresa (int): The empresa
            tabelaplano_idx_json (str): The tabelaplano_idx_json
        
        Parameter Structure:
        
            {
                "usuario_logado": "string",
                "parc_geradas_json": "string",
                "parcsel_reneg_json": "string",
                "grupo_parcelas_json": "string",
                "valdesc_reneg": 0,
                "valacresc_reneg": 0,
                "val_reneg": 0,
                "pendentevalidar_alcada": true,
                "venda": 0,
                "obra": "string",
                "empresa": 0,
                "tabelaplano_idx_json": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._finalizar_renegociacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/FinalizarRenegociacao"
        kwargs = {
            "usuario_logado": usuario_logado,
            "parc_geradas_json": parc_geradas_json,
            "parcsel_reneg_json": parcsel_reneg_json,
            "grupo_parcelas_json": grupo_parcelas_json,
            "valdesc_reneg": valdesc_reneg,
            "valacresc_reneg": valacresc_reneg,
            "val_reneg": val_reneg,
            "pendentevalidar_alcada": pendentevalidar_alcada,
            "venda": venda,
            "obra": obra,
            "empresa": empresa,
            "tabelaplano_idx_json": tabelaplano_idx_json,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gravar_ocorrencia_anexo(
        self,
        ocorrencias: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GravarOcorrenciaAnexo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Adiciona uma ou várias ocorrências vinculada de anexo de acordo com os parâmetros passados na requisição.
        
        Parâmetros da request
        
        Chave: Chave para consulta.
        Campos: 
        Campos obrigatórios para a chave="Venda" (empresa, obra, venda, codigo ocorrencia, usuario). 
        Campos obrigatórios para a chave="Parcela" (empresa, obra, venda, número parcela, número geral da parcela, tipo da parcela, codigo ocorrência, usuario)
        
        
        
        
        
        Args:
            Ocorrencias (List[Dict[str, Any]]): The ocorrencias
        
        Parameter Structure:
        
            {
                "Ocorrencias": [
                    {
                        "Chave": "string",
                        "Campos": [
                            {
                                "empresa": 0,
                                "obra": "string",
                                "numeroVenda": 0,
                                "numeroParcela": 0,
                                "numeroGeralParcela": 0,
                                "tipoParcela": "string",
                                "codigoOcorrencia": 0,
                                "usuario": "string",
                                "observacao": "string"
                            }
                        ]
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._gravar_ocorrencia_anexo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GravarOcorrenciaAnexo"
        kwargs = {
            "Ocorrencias": ocorrencias,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def alterar_data_prorrogacao(
        self,
        dados_prorrogacao: Optional[Dict] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Args:
            dados_prorrogacao (Dict[str, Any]): The dados_prorrogacao
        
        Parameter Structure:
        
            {
                "dados_prorrogacao": {
                    "Empresa": 0,
                    "Obra": "string",
                    "Venda": 0,
                    "TipoParcela": "string",
                    "Parcela": 0,
                    "ParcelaGeral": 0,
                    "DataAntiga": "2025-04-23T13:46:14.684Z",
                    "DataNova": "2025-04-23T13:46:14.684Z",
                    "Usuario": "string",
                    "UsarDataUtil": 0
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._alterar_data_prorrogacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/AlterarDataProrrogacao"
        kwargs = {
            "dados_prorrogacao": dados_prorrogacao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_parcelas_areceber(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_ven: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        valor_presente: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarParcelasAReceber`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Possibilita a busca de parcelas a receber na data atual.
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_ven (int): The num_ven
            data_calculo (datetime): The data_calculo
            valor_presente (int): The valor_presente
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_ven": 0,
                "data_calculo": "2025-04-23T13:46:14.688Z",
                "valor_presente": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._buscar_parcelasa_receber(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarParcelasAReceber"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_ven": num_ven,
            "data_calculo": data_calculo,
            "valor_presente": valor_presente,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_parametro_cobranca(
        self,
        empresa: Optional[int] = None,
        banco: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarParametroCobranca`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Busca a lista de parâmetros de cobrança ativos do sistema:
        
        URI + /api/v{version}/Venda/BuscarParametroCobranca
        
        
        Formato dos dados retornados:
        
        Banco     (String) : Número do banco
        NomeBanco (String) : Nome do banco
        Conta     (String) : Número da conta
        Agencia   (String) : Código da agência do banco
        Carteira  (String) : Código da carteira do convênio com banco
        Codigo    (String) : Código do parâmetro de cobrança no sistema
        Descricao (String) : Descrição do parâmetro de cobrança no sistema
        Empresa   (String) : Código da empresa
        Cedente   (String) : Código do cedente da remessa de cobrança
        
        
        
        Definição de negócio:
        
        Para buscar todos os padrões de cobrança ativos, usar null nos parâmetros da requisição ou não enviar os campos.
        
        
        
        Args:
            empresa (int): The empresa
            banco (int): The banco
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "banco": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._buscar_parametro_cobranca(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarParametroCobranca"
        kwargs = {
            "empresa": empresa,
            "banco": banco,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_parcelas_recebidas(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_ven: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarParcelasRecebidas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Possibilita buscar parcelas que foram recebidas.
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_ven (int): The num_ven
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_ven": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._buscar_parcelas_recebidas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarParcelasRecebidas"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_ven": num_ven,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_status_de_escritura(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarStatusDeEscritura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Busca a lista de Status de escritura ativos do sistema:
        
        URI + /api/v{version}/Venda/BuscarStatusDeEscritura
        
        
        Formato dos dados retornados:
        
        Codigo(Integer):Código de Status de escritura
        Descricao(String):Descrição do Status de escritura
        
        
        
        
        
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
            >>> api = Venda()
            >>> response = api._buscar_status_de_escritura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarStatusDeEscritura"
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_parcelas_da_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        boleto_antecipado: Optional[bool] = None,
        somente_parcelas_aptas_boleto: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarParcelasDaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite consultar as parcelas de uma venda.
        
        Ao enviar somenteParcelasAptasBoleto como TRUE, irá validar se a venda possui bloqueio ou manutenção pendente e se a empresa está configurada
          para "Não permitir enviar para banco parcelas com status [em banco]"
        Caso a venda possua bloqueio ou esteja em manutenção, não irá retornar nenhuma parcela da venda.
        Caso esteja configurado para não enviar parcelas com status em banco, não irá retornar as parcelas que já tenham boletos gerados.
        
        
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_venda (int): The num_venda
            data_calculo (datetime): The data_calculo
            boleto_antecipado (int): The boleto_antecipado
            somenteParcelasAptasBoleto (int): The parcelas aptas boleto
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_venda": 0,
                "data_calculo": "2025-04-23T13:46:14.708Z",
                "boleto_antecipado": true,
                "somenteParcelasAptasBoleto": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_parcelas_da_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarParcelasDaVenda"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_venda": num_venda,
            "data_calculo": data_calculo,
            "boleto_antecipado": boleto_antecipado,
            "somenteParcelasAptasBoleto": somente_parcelas_aptas_boleto,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_pdfevolucao_contrato(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GerarPDFEvolucaoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.
        
        Definição de Negócio:
          Gera PDF da evolução do contrato em string do tipo Base64.
        
        Validações a nível de usuário.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            numeroVenda (int): The venda
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "numeroVenda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._gerarpdf_evolucao_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GerarPDFEvolucaoContrato"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "numeroVenda": numero_venda,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_recebimentos_da_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        parcelasnao_conciliadas: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarRecebimentosDaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Permite consultar os reecebimentos de uma venda, ou seja, o que já foi recebido.
        Caso o campo "parcelasnao_conciliadas" esteja marcado como "true" as parcelas não conciliadas também serão retornadas.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            venda (int): The venda
            parcelasnao_conciliadas (int): The parcelasnao_conciliadas
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "venda": 0,
                "parcelasnao_conciliadas": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._buscar_recebimentos_da_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarRecebimentosDaVenda"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "venda": venda,
            "parcelasnao_conciliadas": parcelasnao_conciliadas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def exportar_pessoas_da_venda_xml(
        self,
        lista_vendas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ExportarPessoasDaVendaXml`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Possibilita acesso às pessoas que estão relacionadas com a venda informada.
        
        Valida a existência da venda.
        
        
        
        Args:
            lista_vendas (List[Dict[str, Any]]): The lista_vendas
        
        Parameter Structure:
        
            {
                "lista_vendas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "Venda": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._exportar_pessoas_da_venda_xml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ExportarPessoasDaVendaXml"
        kwargs = {
            "lista_vendas": lista_vendas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gravar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_contrato: Optional[int] = None,
        estabelecimento: Optional[str] = None,
        forma_pgto: Optional[int] = None,
        qtde_parcelas: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        valor_liquido: Optional[int] = None,
        tipo_recebimento: Optional[int] = None,
        antecipacao: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GravarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        É obrigatório ter o ambiente de integração com a PAYGO configurado, só após o registro junto a eles que o registro será gerado no UAU.
        É necessário ter permissão de inclusão no programa VEPEDIDORECEBIMENTO
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            NumContrato (int): The num contrato
            Estabelecimento (str): The estabelecimento
            FormaPgto (int): The forma pgto
            QtdeParcelas (int): The qtde parcelas
            DataCalculo (datetime): The data calculo
            ValorLiquido (int): The valor liquido
            TipoRecebimento (int): The tipo recebimento
            Antecipacao (int): The antecipacao
            Parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "NumContrato": 0,
                "Estabelecimento": "string",
                "FormaPgto": 0,
                "QtdeParcelas": 0,
                "DataCalculo": "2025-04-23T13:46:14.733Z",
                "ValorLiquido": 0,
                "TipoRecebimento": 0,
                "Antecipacao": true,
                "Parcelas": [
                    {
                        "NumeroParcela": 0,
                        "NumeroParcelaGeral": 0,
                        "TipoParcela": "string",
                        "ValorDesconto": 0,
                        "ValorDescontoAntecipado": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._gravar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GravarPedidoDeRecebimento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "NumContrato": num_contrato,
            "Estabelecimento": estabelecimento,
            "FormaPgto": forma_pgto,
            "QtdeParcelas": qtde_parcelas,
            "DataCalculo": data_calculo,
            "ValorLiquido": valor_liquido,
            "TipoRecebimento": tipo_recebimento,
            "Antecipacao": antecipacao,
            "Parcelas": parcelas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def importacao_venda_com_retorno(
        self,
        xml_vendas: Optional[str] = None,
        alterarnumerodas_vendas: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ImportacaoVendaComRetorno`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Número máximo de importações por vez: 50.
        
        Definição de Negócio:
          Possibilita importa vendas via XML para o UAU e receber como retorno as vendas importadas.
        
        Valida quantidade de importações por requisição.
        Caso ocorra erro em uma venda, todas as outras importações são canceladas e terá um retorno com informações da venda que falhou.
        
        
        
        Args:
            xml_vendas (str): The xml_vendas
            alterarnumerodas_vendas (int): The alterarnumerodas_vendas
        
        Parameter Structure:
        
            {
                "xml_vendas": "string",
                "alterarnumerodas_vendas": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._importacao_venda_com_retorno(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ImportacaoVendaComRetorno"
        kwargs = {
            "xml_vendas": xml_vendas,
            "alterarnumerodas_vendas": alterarnumerodas_vendas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def manter_status_cobranca_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        numero_parcela: Optional[int] = None,
        numero_parcela_geral: Optional[int] = None,
        tipo_parcela: Optional[str] = None,
        status_cobranca: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ManterStatusCobrancaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Possibilita alterar o status de cobrança referentes a determinada venda.
          Validações serão realizadas para efetuar a operação:
        
        Se os parâmetros forem da parcela, o ocorrência será gravada na parcela correspondente.
        Se os parâmetros forem da venda, o ocorrência será gravada na venda correspondente.
        Caso seja informado o parâmetro numeroParcela, numeroParcelaGeral ou tipoParcela, os três serão obrigatórios.
        O parâmetro 'código' deverá ser do tipo numérico.
        Os status de cobrança da venda ou parcela, serão substituídos pelos status informados.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            venda (int): The venda
            numeroParcela (int): The parcela
            numeroParcelaGeral (int): The parcela geral
            tipoParcela (str): The parcela
            statusCobranca (List[Dict[str, Any]]): The cobranca
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "venda": 0,
                "numeroParcela": 0,
                "numeroParcelaGeral": 0,
                "tipoParcela": "string",
                "statusCobranca": [
                    {
                        "codigo": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._manter_status_cobranca_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ManterStatusCobrancaVenda"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "venda": venda,
            "numeroParcela": numero_parcela,
            "numeroParcelaGeral": numero_parcela_geral,
            "tipoParcela": tipo_parcela,
            "statusCobranca": status_cobranca,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def venda_valida_para_manutencao(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        usr_logado: Optional[str] = None,
        mensagem_securitizacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/VendaValidaParaManutencao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Valida a possibilidade de realizar a renegociação da venda, para tal tarefa a venda não pode ter restrições.
        
        Os campos inseridos na request serão utilizado para buscar e verificar disponibilidade de renegociação.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            venda (int): The venda
            usr_logado (str): The usr_logado
            mensagem_securitizacao (str): The mensagem_securitizacao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "venda": 0,
                "usr_logado": "string",
                "mensagem_securitizacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._venda_valida_para_manutencao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/VendaValidaParaManutencao"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "venda": venda,
            "usr_logado": usr_logado,
            "mensagem_securitizacao": mensagem_securitizacao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_contas_receber_calc(
        self,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        tipos_parcela: Optional[str] = None,
        vendas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarContasReceberCalc`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Possibilita Consultar as parcelas de contas a receber já calculadas com retorno a lista de parcelas.
        Nenhuma propriedade é obrigatória, porém é obrigatório ser enviado pelo menos um tipo de filtro para consultar os dados.
        Na propriedade vendas, é obrigatório apenas o parâmetro empresa.
        É indispensável que o PROUAU esteja rodando diariamente o cálculo de parcelas para que os resultados estejam sempre corretos.
        O Filtro de período filtrará pela data de vencimento da parcela.
        O filtro por tipo de parcelas pode aceitar mais de um tipo, é obrigatório colocar entre aspas simples cada código de parcela e separadas por virgula. Ex.: 'P', 'M'
        
        
        
        Args:
            DataInicio (datetime): The data inicio
            DataFim (datetime): The data fim
            TiposParcela (str): The tipos parcela
            Vendas (List[Dict[str, Any]]): The vendas
        
        Parameter Structure:
        
            {
                "DataInicio": "2025-04-23T13:46:14.790Z",
                "DataFim": "2025-04-23T13:46:14.790Z",
                "TiposParcela": "string",
                "Vendas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "Numero": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_contas_receber_calc(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarContasReceberCalc"
        kwargs = {
            "DataInicio": data_inicio,
            "DataFim": data_fim,
            "TiposParcela": tipos_parcela,
            "Vendas": vendas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def importacao_parcelas_de_custas(
        self,
        custas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ImportacaoParcelasDeCustas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Importação de parcelas do tipo Custas:
        URI + /api/v{version}/Venda/ImportacaoParcelasDeCustas
        
        
        
        Definição de Negócio:
        
        Permite importar parcelas do tipo Custas com as seguintes regras:
        
        Os campos: Observacao, CobrarJurosAtraso, CobrarMulta, CobrarCorrecao, CobrarImposto, CobrarTxAdm, CobrarRepasseLocador, Competencia, NUMEROPARCELA e MeioPreferencialDeRecebimento são opcionais.
        
        
        Referente a propriedade de CAPs:
        
        Caso não sejam informados os CAPs para uma ou mais parcelas de custas, para essas parcelas, será utilizada a configuração padrão de CAPs da empresa;
        Será possível utilizar em uma mesma requisição parcelas com CAPs definidos no JSON e parcelas com CAPs padrão da empresa (não informado no JSON);
        Será validada a existência dos CAPs informado e só será possível utilizar CAPs ativos;
        Caso seja informado um CAP para uma determinada parcela, todos os demais CAPs daquela parcela, serão obrigatórios;
        
        
        
        Anexos:
        
        Link para download de exemplos:
        Exemplo de parcela tipo Custa: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcelas-de-Custas.postman_collection.zip
        
        
        
        Args:
            custas (List[Dict[str, Any]]): The custas
        
        Parameter Structure:
        
            {
                "custas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "Venda": 0,
                        "Valor": 0,
                        "Origem": 0,
                        "PlanoIdx": 0,
                        "Tipo": 0,
                        "Frequencia": "string",
                        "Reajuste": "string",
                        "DtVencimento": "2025-04-23T13:46:14.795Z",
                        "DtReajuste": "2025-04-23T13:46:14.795Z",
                        "PadraoCobranca": 0,
                        "Observacao": "string",
                        "CobrarJurosAtraso": 0,
                        "CobrarMulta": 0,
                        "CobrarCorrecao": 0,
                        "CobrarImposto": 0,
                        "CobrarTxAdm": 0,
                        "CobrarRepasseLocador": 0,
                        "DataDeCompetencia": "2025-04-23T13:46:14.795Z",
                        "NUMEROPARCELA": 0,
                        "MeioPreferencialDeRecebimento": 0,
                        "Cap": {
                            "CapPrincipal": "string",
                            "CapAcrescimo": "string",
                            "CapCorrecao": "string",
                            "CapCorrecaoAtraso": "string",
                            "CapDesconto": "string",
                            "CapDescontoAntecipacao": "string",
                            "CapDescontoCondicional": "string",
                            "CapDescontoCusta": "string",
                            "CapJuros": "string",
                            "CapJurosAtraso": "string",
                            "CapMulta": "string",
                            "CapRepasse": "string",
                            "CapTaxaBoleto": "string"
                        }
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._importacao_parcelas_de_custas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ImportacaoParcelasDeCustas"
        kwargs = {
            "custas": custas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def buscar_campanha_desconto_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/BuscarCampanhaDescontoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método
        
        Definição de Negócio:
          Permite renegociar parcelas de uma venda
        
        O usuário deverá estar autenticado e validado
        Informar os dados da venda
        Informar as parcelas a serem geradas
        Informar as parcelas escolhidas para renegociação
        Informar o plano de indexação
        Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
          retorna mensagem informando a inconsistência encontrada para que seja analisada
        Após as validações realiza a renegociação das parcelas
        Será registrado comentário na venda sobre a renegociação realizada
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
        Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Venda (int): The venda
            DataCalculo (datetime): The data calculo
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Venda": 0,
                "DataCalculo": "2025-04-23T13:46:14.806Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._buscar_campanha_desconto_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/BuscarCampanhaDescontoVenda"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Venda": venda,
            "DataCalculo": data_calculo,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def cancelar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/CancelarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Pedidos que já tiveram um recebimento parcial junto a NTK, não são cancelados. (trava na NTK).
        É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Pedido (int): The pedido
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Pedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._cancelar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/CancelarPedidoDeRecebimento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Pedido": pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def atualizar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/AtualizarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
        Valida usuário e permissões
        Valida outras informações passadas no request
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Pedido (int): The pedido
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Pedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._atualizar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/AtualizarPedidoDeRecebimento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Pedido": pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Possibilita consultar pedido de recebimento junto a NTK
        As informações retornadas serão informações do pedido na NTK.
        É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Pedido (int): The pedido
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Pedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarPedidoDeRecebimento"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Pedido": pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def processar_recebimento_parcelas(
        self,
        recebimento: Optional[Dict] = None,
        forma_pagamento: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ProcessarRecebimentoParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Responsável por processar recebimentos de parcelas com os dados de recebimento e forma de pagamento.
        
        A origem do recebimento das parcelas DEVE sempre ser 0.
        Serão realizadas várias validações para realização da requisição.
        O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.
        
        
        
        Args:
            recebimento (Dict[str, Any]): The recebimento
            formaPagamento (Dict[str, Any]): The pagamento
        
        Parameter Structure:
        
            {
                "recebimento": {
                    "Empresa": 0,
                    "Banco": "string",
                    "Conta": "string",
                    "HistContabil": "string",
                    "UsuarioLogado": "string",
                    "TipoRecebimento": 0,
                    "DataRecebimento": "2025-04-23T13:46:14.872Z",
                    "ValorJurosPreDatado": 0,
                    "DataParcelaPreDatada": "2025-04-23T13:46:14.872Z",
                    "ValorLiquidoRecebido": 0,
                    "ValorDesconto": 0,
                    "ValorAcrescimo": 0,
                    "DataCalculo": "2025-04-23T13:46:14.872Z",
                    "Antecipacao": true,
                    "NovaDataVenc": "2025-04-23T13:46:14.872Z",
                    "ReceberResiduo": true,
                    "OrigemRecebimento": 0,
                    "Parcelas": [
                        {
                            "NumParc": 0,
                            "NumParcGer": 0,
                            "NumeroContrato": 0,
                            "Obra": "string",
                            "TipoParc": "string",
                            "ValorDesconto": 0
                        }
                    ]
                },
                "formaPagamento": {
                    "Cheques": [
                        {
                            "Banco": 0,
                            "Agencia": "string",
                            "Conta": "string",
                            "NumCheque": "string",
                            "DataCadastro": "2025-04-23T13:46:14.872Z",
                            "Valor": 0,
                            "Titular": "string",
                            "QuemRecebeu": "string",
                            "Predatado": "2025-04-23T13:46:14.872Z",
                            "ValorDescontoCedido": 0,
                            "ValorAcrescimoCedido": 0,
                            "NumeroControle": 0,
                            "TipoValorJurosPredatado": 0
                        }
                    ],
                    "Bens": [
                        {
                            "NumBem": 0,
                            "Descricao": "string",
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "QuemRespons": "string",
                            "DataRecebeu": "2025-04-23T13:46:14.872Z"
                        }
                    ],
                    "Dinheiro": [
                        {
                            "NumControle": 0,
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "DataRecebeu": "2025-04-23T13:46:14.872Z"
                        }
                    ],
                    "CredEletro": [
                        {
                            "NumControle": 0,
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "DataRecebimento": "2025-04-23T13:46:14.872Z",
                            "DataDeposito": "2025-04-23T13:46:14.872Z",
                            "DataConciliacao": "2025-04-23T13:46:14.872Z"
                        }
                    ],
                    "Cartao": [
                        {
                            "NumControle": 0,
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "DataRecebimento": "2025-04-23T13:46:14.872Z",
                            "NumTerminal": 0,
                            "NSU": "string",
                            "NumReferencia": "string",
                            "CodAutorizacao": "string",
                            "Modalidade": 0,
                            "TotalParcelas": 0,
                            "Comprovante": "string"
                        }
                    ]
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._processar_recebimento_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ProcessarRecebimentoParcelas"
        kwargs = {
            "recebimento": recebimento,
            "formaPagamento": forma_pagamento,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def manter_status_escrituracao_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        status_escrituracao: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ManterStatusEscrituracaoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Valida usuário e suas permissões
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            venda (int): The venda
            statusEscrituracao (List[Dict[str, Any]]): The escrituracao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "venda": 0,
                "statusEscrituracao": [
                    {
                        "codigo": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._manter_status_escrituracao_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ManterStatusEscrituracaoVenda"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "venda": venda,
            "statusEscrituracao": status_escrituracao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def retorna_chaves_vendas_por_periodo(
        self,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        status_escrituracao: Optional[bool] = None,
        status_venda: Optional[str] = None,
        lista_empresa_obra: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/RetornaChavesVendasPorPeriodo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.   
        Formatação das chaves de resposta: "Empresa-Obra/Venda, Empresa-Obra/Venda, Empresa-Obra/Venda"
           "01705-B1705/00159,01705-B1705/00160,01705-B1705/00161"
          
        
        Definição de Negócio:
        
        Permite consultar as chaves das vendas que foram inseridas, tiveram manutenção ou foram quitadas no período informado.
        Se o campo "status_escrituracao" do request for marcado como "true" serão retonadas as chaves que tiveram alterações no status de escrituração.
        Parâmetro opcional para request: statusVenda.  0 - Normal, 1 - Cancelada, 3 - Quitado, 4 - Em acerto, 5 Aluguel antecipado.
        Parâmetros opcionais para request: codigoEmpresa e codigoObra.
        
        
        
        Args:
            data_inicio (datetime): The data_inicio
            data_fim (datetime): The data_fim
            status_escrituracao (int): The status_escrituracao
            statusVenda (str): The venda
            listaEmpresaObra (List[Dict[str, Any]]): The empresa obra
        
        Parameter Structure:
        
            {
                "data_inicio": "2025-04-23T13:46:14.884Z",
                "data_fim": "2025-04-23T13:46:14.884Z",
                "status_escrituracao": true,
                "statusVenda": "string",
                "listaEmpresaObra": [
                    {
                        "codigoEmpresa": 0,
                        "codigoObra": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._retorna_chaves_vendas_por_periodo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/RetornaChavesVendasPorPeriodo"
        kwargs = {
            "data_inicio": data_inicio,
            "data_fim": data_fim,
            "status_escrituracao": status_escrituracao,
            "statusVenda": status_venda,
            "listaEmpresaObra": lista_empresa_obra,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_demonstrativo_correcao(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        numero_parcela: Optional[int] = None,
        numero_parcela_geral: Optional[int] = None,
        tipo_parcela: Optional[str] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None,
        valor_antecipado: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarDemonstrativoCorrecao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite consultar demonstrativo de correção da parcela da venda.
        
        Valida usuário e suas permissões.
        Valida existência da venda.
        Valida existência das parcelas.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            venda (int): The venda
            numeroParcela (int): The parcela
            numeroParcelaGeral (int): The parcela geral
            tipoParcela (str): The parcela
            dataCalculo (datetime): The calculo
            dataCorrecao (datetime): The correcao
            valorAntecipado (int): The antecipado
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "venda": 0,
                "numeroParcela": 0,
                "numeroParcelaGeral": 0,
                "tipoParcela": "string",
                "dataCalculo": "2025-04-23T13:46:14.890Z",
                "dataCorrecao": "2025-04-23T13:46:14.890Z",
                "valorAntecipado": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_demonstrativo_correcao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarDemonstrativoCorrecao"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "venda": venda,
            "numeroParcela": numero_parcela,
            "numeroParcelaGeral": numero_parcela_geral,
            "tipoParcela": tipo_parcela,
            "dataCalculo": data_calculo,
            "dataCorrecao": data_correcao,
            "valorAntecipado": valor_antecipado,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_plano_indexadores_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarPlanoIndexadoresVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Retorna informações pertinentes ao plano indexador da venda.
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            venda (int): The venda
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "venda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_plano_indexadores_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarPlanoIndexadoresVenda"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "venda": venda,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gravar_num_contrato_financiamento(
        self,
        codg_empresa: Optional[int] = None,
        codg_obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        codg_usuario: Optional[str] = None,
        num_contrato: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GravarNumContratoFinanciamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Altera número de contrato para uma venda.
        
        Pré requisito:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Venda/GravarNumContratoFinanciamento 
          Anexos:
        
        
        Exemplo Postman: [ALTERAR EXEMPLO]
        
        
        
        Args:
            codgEmpresa (int): The empresa
            codgObra (str): The obra
            numVenda (int): The venda
            codgUsuario (str): The usuario
            numContrato (str): The contrato
        
        Parameter Structure:
        
            {
                "codgEmpresa": 0,
                "codgObra": "string",
                "numVenda": 0,
                "codgUsuario": "string",
                "numContrato": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._gravar_num_contrato_financiamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GravarNumContratoFinanciamento"
        kwargs = {
            "codgEmpresa": codg_empresa,
            "codgObra": codg_obra,
            "numVenda": num_venda,
            "codgUsuario": codg_usuario,
            "numContrato": num_contrato,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_empreendimentos_cliente(
        self,
        codigo_usuario: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarEmpreendimentosCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consulta os empreendimento que o cliente possui e está com situação em aberto.
        
        
        Args:
            codigo_usuario (int): The codigo_usuario
        
        Parameter Structure:
        
            {
                "codigo_usuario": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_empreendimentos_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarEmpreendimentosCliente"
        kwargs = {
            "codigo_usuario": codigo_usuario,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_pedido_de_recebimento_uau(
        self,
        numerontk: Optional[int] = None,
        numero_pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarPedidoDeRecebimentoUAU`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        
        Possibilita consultar pedido de recebimento registrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
        As informações retornadas são referentes a como o UAU registrou o pedido internamente.
        É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO
        
        
        
        Args:
            NumeroNTK (int): The numero n t k
            NumeroPedido (int): The numero pedido
        
        Parameter Structure:
        
            {
                "NumeroNTK": 0,
                "NumeroPedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_pedido_de_recebimentouau(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarPedidoDeRecebimentoUAU"
        kwargs = {
            "NumeroNTK": numerontk,
            "NumeroPedido": numero_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_unidades_compradas_por_cpf(
        self,
        cpf_cnpj: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarUnidadesCompradasPorCPF`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ
        
        Valida se o usuário está autenticado (logado) no sitema.
        Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.
        
        
        
        Args:
            CpfCnpj (str): The cpf cnpj
        
        Parameter Structure:
        
            {
                "CpfCnpj": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_unidades_compradas_porcpf(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarUnidadesCompradasPorCPF"
        kwargs = {
            "CpfCnpj": cpf_cnpj,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def calcular_desconto_campanha_antecipacao(
        self,
        campanha_de_desconto: Optional[Dict] = None,
        parcelas_calculadas: Optional[List[Dict]] = None,
        data_calculo: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/CalcularDescontoCampanhaAntecipacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método
        
        Definição de Negócio:
          Permite renegociar parcelas de uma venda
        
        O usuário deverá estar autenticado e validado
        Informar os dados da venda
        Informar as parcelas a serem geradas
        Informar as parcelas escolhidas para renegociação
        Informar o plano de indexação
        Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
          retorna mensagem informando a inconsistência encontrada para que seja analisada
        Após as validações realiza a renegociação das parcelas
        Será registrado comentário na venda sobre a renegociação realizada
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
        Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso
        
        
        
        Args:
            CampanhaDeDesconto (Dict[str, Any]): The campanha de desconto
            ParcelasCalculadas (List[Dict[str, Any]]): The parcelas calculadas
            DataCalculo (datetime): The data calculo
        
        Parameter Structure:
        
            {
                "CampanhaDeDesconto": {
                    "Numero": 0,
                    "Empresa": 0,
                    "Obra": "string",
                    "Venda": 0,
                    "TipoObraVenda": 0,
                    "TotalParaQuitacao": 0,
                    "QuantidadeMinima": 0,
                    "TiposParcelasPermitidos": "string",
                    "ValorMinimo": 0,
                    "TipoFaixa": 0,
                    "Aliquotas": [
                        {
                            "FaixaInicio": 0,
                            "FaixaFinal": 0,
                            "TipoAliquota": 0,
                            "AteHabitese": true,
                            "Porcentagem": 0,
                            "TipoObra": 0,
                            "TipoDesconto": {},
                            "Faixa": 0,
                            "DoMes": 0,
                            "AteMes": 0
                        }
                    ]
                },
                "ParcelasCalculadas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "Venda": 0,
                        "Numero": 0,
                        "NumeroGeral": 0,
                        "Tipo": "string",
                        "DataVencimento": "2025-04-23T13:46:14.931Z",
                        "DataProrrogacao": "2025-04-23T13:46:14.931Z",
                        "ValorCorrigido": 0,
                        "DesconsiderarQuitacao": true,
                        "DataInicioJuros": "2025-04-23T13:46:14.931Z",
                        "ValorDescontoCalculado": 0
                    }
                ],
                "DataCalculo": "2025-04-23T13:46:14.931Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._calcular_desconto_campanha_antecipacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/CalcularDescontoCampanhaAntecipacao"
        kwargs = {
            "CampanhaDeDesconto": campanha_de_desconto,
            "ParcelasCalculadas": parcelas_calculadas,
            "DataCalculo": data_calculo,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_campanha_desconto_disponivel(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarCampanhaDescontoDisponivel`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consulta a campanha de desconto disponível para utilização.
        
        Valida usuário logado e permissões
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            numeroVenda (int): The venda
            dataCalculo (datetime): The calculo
            dataCorrecao (datetime): The correcao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "numeroVenda": 0,
                "dataCalculo": "2025-04-23T13:46:14.940Z",
                "dataCorrecao": "2025-04-23T13:46:14.940Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_campanha_desconto_disponivel(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarCampanhaDescontoDisponivel"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "numeroVenda": numero_venda,
            "dataCalculo": data_calculo,
            "dataCorrecao": data_correcao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_desconto_antecipacao_parcela(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        num_parc: Optional[int] = None,
        numparc_ger: Optional[int] = None,
        tipo_parc: Optional[str] = None,
        data_calculo: Optional[datetime] = None,
        valor_parcela: Optional[int] = None,
        data_vencimento: Optional[datetime] = None,
        data_prorrogacao: Optional[datetime] = None,
        totalparcelas_sel: Optional[int] = None,
        antecipado: Optional[bool] = None,
        totalpara_quitacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarDescontoAntecipacaoParcela`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Consulta o valor do desconto caso a parcela seja paga antecipadamente.
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_venda (int): The num_venda
            num_parc (int): The num_parc
            numparc_ger (int): The numparc_ger
            tipo_parc (str): The tipo_parc
            data_calculo (datetime): The data_calculo
            valor_parcela (int): The valor_parcela
            data_vencimento (datetime): The data_vencimento
            data_prorrogacao (datetime): The data_prorrogacao
            totalparcelas_sel (int): The totalparcelas_sel
            antecipado (int): The antecipado
            totalpara_quitacao (int): The totalpara_quitacao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_venda": 0,
                "num_parc": 0,
                "numparc_ger": 0,
                "tipo_parc": "string",
                "data_calculo": "2025-04-23T13:46:14.944Z",
                "valor_parcela": 0,
                "data_vencimento": "2025-04-23T13:46:14.944Z",
                "data_prorrogacao": "2025-04-23T13:46:14.944Z",
                "totalparcelas_sel": 0,
                "antecipado": true,
                "totalpara_quitacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_desconto_antecipacao_parcela(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarDescontoAntecipacaoParcela"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_venda": num_venda,
            "num_parc": num_parc,
            "numparc_ger": numparc_ger,
            "tipo_parc": tipo_parc,
            "data_calculo": data_calculo,
            "valor_parcela": valor_parcela,
            "data_vencimento": data_vencimento,
            "data_prorrogacao": data_prorrogacao,
            "totalparcelas_sel": totalparcelas_sel,
            "antecipado": antecipado,
            "totalpara_quitacao": totalpara_quitacao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_unidades_compradas_usr_logado(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarUnidadesCompradasUsrLogado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Possibilita consultar unidades que foram compradas por determinado usuário.
        
        Valida se o usuário está autenticado (logado) no sitema.
        Usuário só pode ser do tipo pessoa.
        Valida se o usuário está cadastrado para acesso no UAUWeb.
        
        
        
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
            >>> api = Venda()
            >>> response = api._consultar_unidades_compradas_usr_logado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarUnidadesCompradasUsrLogado"
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_unidades_compradas_por_cpfcnpj(
        self,
        cpf_cnpj: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/ConsultarUnidadesCompradasPorCPFCNPJ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
          Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ
        
        Valida se o usuário está autenticado (logado) no sitema.
        Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.
        
        
        
        Args:
            CpfCnpj (str): The cpf cnpj
        
        Parameter Structure:
        
            {
                "CpfCnpj": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._consultar_unidades_compradas_porcpfcnpj(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/ConsultarUnidadesCompradasPorCPFCNPJ"
        kwargs = {
            "CpfCnpj": cpf_cnpj,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def gerar_pdfevolucao_saldo_devedor_financiamento(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        tipo_relatorio: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Venda/GerarPDFEvolucaoSaldoDevedorFinanciamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.
        
        Definição de Negócio:
          Gerar PDF do relatório de evolução do saldo devedor do financiamento imobiliário da venda em formato Base64.
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            numeroVenda (int): The venda
            tipoRelatorio (int): The relatorio
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "numeroVenda": 0,
                "tipoRelatorio": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Venda()
            >>> response = api._gerarpdf_evolucao_saldo_devedor_financiamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Venda/GerarPDFEvolucaoSaldoDevedorFinanciamento"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "numeroVenda": numero_venda,
            "tipoRelatorio": tipo_relatorio,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

