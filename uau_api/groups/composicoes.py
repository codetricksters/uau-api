from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class Composicoes:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def inserir_composicoes(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        prod_equipe: Optional[int] = None,
        tipo_custo: Optional[str] = None,
        civil_pes: Optional[int] = None,
        status: Optional[int] = None,
        categoria: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        codigo_servico_fiscal: Optional[str] = None,
        controlafvs: Optional[bool] = None,
        confirmado: Optional[int] = None,
        porc_qtde_excedida_entrega: Optional[str] = None,
        porc_preco_excedido_entrega: Optional[str] = None,
        porc_preco_reduzido_entrega: Optional[str] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo (str): The codigo
            descricao (str): The descricao
            unidade (str): The unidade
            prodEquipe (int): The equipe
            tipoCusto (str): The custo
            civilPes (int): The pes
            status (int): The status
            categoria (str): The categoria
            categoriaMovFin (str): The mov fin
            CAP (str): The c a p
            CAPEstorno (str): The c a p estorno
            CAPTransacaoFinanceira (str): The c a p transacao financeira
            NCM (str): The n c m
            CEST (str): The c e s t
            aplicacao (str): The aplicacao
            codigoServicoFiscal (str): The servico fiscal
            controlaFVS (int): The f v s
            confirmado (int): The confirmado
            porcQtdeExcedidaEntrega (str): The qtde excedida entrega
            porcPrecoExcedidoEntrega (str): The preco excedido entrega
            porcPrecoReduzidoEntrega (str): The preco reduzido entrega
        
        Parameter Structure:
        
            {
                "codigo": "string",
                "descricao": "string",
                "unidade": "string",
                "prodEquipe": 0,
                "tipoCusto": "string",
                "civilPes": 0,
                "status": 0,
                "categoria": "string",
                "categoriaMovFin": "string",
                "CAP": "string",
                "CAPEstorno": "string",
                "CAPTransacaoFinanceira": "string",
                "NCM": "string",
                "CEST": "string",
                "aplicacao": "string",
                "codigoServicoFiscal": "string",
                "controlaFVS": true,
                "confirmado": 0,
                "porcQtdeExcedidaEntrega": "string",
                "porcPrecoExcedidoEntrega": "string",
                "porcPrecoReduzidoEntrega": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._inserir_composicoes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/InserirComposicoes"
        kwargs = {
            "codigo": codigo,
            "descricao": descricao,
            "unidade": unidade,
            "prodEquipe": prod_equipe,
            "tipoCusto": tipo_custo,
            "civilPes": civil_pes,
            "status": status,
            "categoria": categoria,
            "categoriaMovFin": categoria_mov_fin,
            "CAP": cap,
            "CAPEstorno": cap_estorno,
            "CAPTransacaoFinanceira": cap_transacao_financeira,
            "NCM": ncm,
            "CEST": cest,
            "aplicacao": aplicacao,
            "codigoServicoFiscal": codigo_servico_fiscal,
            "controlaFVS": controlafvs,
            "confirmado": confirmado,
            "porcQtdeExcedidaEntrega": porc_qtde_excedida_entrega,
            "porcPrecoExcedidoEntrega": porc_preco_excedido_entrega,
            "porcPrecoReduzidoEntrega": porc_preco_reduzido_entrega,
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

    def atualizar_composicoes(
        self,
        lista_composicoes_atualizar: Optional[List[Dict]] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Utilize "" (vazio) caso queira limpar os campos do cadastro sendo que, código, descrição e unidade padrão, não podem ficar vazios.
        
        
        Args:
            listaComposicoesAtualizar (List[Dict[str, Any]]): The composicoes atualizar
        
        Parameter Structure:
        
            {
                "listaComposicoesAtualizar": [
                    {
                        "codigo": "string",
                        "descricao": "string",
                        "unidade": "string",
                        "status": 0,
                        "prodEquipe": 0,
                        "tipoCusto": "string",
                        "civilPes": 0,
                        "categoria": "string",
                        "categoriaMovFin": "string",
                        "CAP": "string",
                        "CAPEstorno": "string",
                        "CAPTransacaoFinanceira": "string",
                        "NCM": "string",
                        "CEST": "string",
                        "aplicacao": "string",
                        "codigoServicoFiscal": "string",
                        "controlaFVS": true,
                        "confirmado": 0,
                        "porcQtdeExcedidaEntrega": "string",
                        "porcPrecoExcedidoEntrega": "string",
                        "porcPrecoReduzidoEntrega": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._atualizar_composicoes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/AtualizarComposicoes"
        kwargs = {
            "listaComposicoesAtualizar": lista_composicoes_atualizar,
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

    def consultar_todas_composicoes(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Composicoes/ConsultarTodasComposicoes`
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
            >>> api = Composicoes()
            >>> response = api._consultar_todas_composicoes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/ConsultarTodasComposicoes"
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

    def consultar_composicoes_por_chave(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        status: Optional[int] = None,
        prod_equipe: Optional[int] = None,
        tipo_custo: Optional[str] = None,
        civil_pes: Optional[int] = None,
        categoria: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        codigo_servico_fiscal: Optional[str] = None,
        controlafvs: Optional[bool] = None,
        confirmado: Optional[int] = None,
        porc_qtde_excedida_entrega: Optional[str] = None,
        porc_preco_excedido_entrega: Optional[str] = None,
        porc_preco_reduzido_entrega: Optional[str] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo (str): The codigo
            descricao (str): The descricao
            unidade (str): The unidade
            status (int): The status
            prodEquipe (int): The equipe
            tipoCusto (str): The custo
            civilPes (int): The pes
            categoria (str): The categoria
            categoriaMovFin (str): The mov fin
            CAP (str): The c a p
            CAPEstorno (str): The c a p estorno
            CAPTransacaoFinanceira (str): The c a p transacao financeira
            NCM (str): The n c m
            CEST (str): The c e s t
            aplicacao (str): The aplicacao
            codigoServicoFiscal (str): The servico fiscal
            controlaFVS (int): The f v s
            confirmado (int): The confirmado
            porcQtdeExcedidaEntrega (str): The qtde excedida entrega
            porcPrecoExcedidoEntrega (str): The preco excedido entrega
            porcPrecoReduzidoEntrega (str): The preco reduzido entrega
        
        Parameter Structure:
        
            {
                "codigo": "string",
                "descricao": "string",
                "unidade": "string",
                "status": 0,
                "prodEquipe": 0,
                "tipoCusto": "string",
                "civilPes": 0,
                "categoria": "string",
                "categoriaMovFin": "string",
                "CAP": "string",
                "CAPEstorno": "string",
                "CAPTransacaoFinanceira": "string",
                "NCM": "string",
                "CEST": "string",
                "aplicacao": "string",
                "codigoServicoFiscal": "string",
                "controlaFVS": true,
                "confirmado": 0,
                "porcQtdeExcedidaEntrega": "string",
                "porcPrecoExcedidoEntrega": "string",
                "porcPrecoReduzidoEntrega": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._consultar_composicoes_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/ConsultarComposicoesPorChave"
        kwargs = {
            "codigo": codigo,
            "descricao": descricao,
            "unidade": unidade,
            "status": status,
            "prodEquipe": prod_equipe,
            "tipoCusto": tipo_custo,
            "civilPes": civil_pes,
            "categoria": categoria,
            "categoriaMovFin": categoria_mov_fin,
            "CAP": cap,
            "CAPEstorno": cap_estorno,
            "CAPTransacaoFinanceira": cap_transacao_financeira,
            "NCM": ncm,
            "CEST": cest,
            "aplicacao": aplicacao,
            "codigoServicoFiscal": codigo_servico_fiscal,
            "controlaFVS": controlafvs,
            "confirmado": confirmado,
            "porcQtdeExcedidaEntrega": porc_qtde_excedida_entrega,
            "porcPrecoExcedidoEntrega": porc_preco_excedido_entrega,
            "porcPrecoReduzidoEntrega": porc_preco_reduzido_entrega,
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

    def consultar_insumos_da_composicao(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        status: Optional[int] = None,
        prod_equipe: Optional[int] = None,
        tipo_custo: Optional[str] = None,
        civil_pes: Optional[int] = None,
        categoria: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        codigo_servico_fiscal: Optional[str] = None,
        controlafvs: Optional[bool] = None,
        confirmado: Optional[int] = None,
        porc_qtde_excedida_entrega: Optional[str] = None,
        porc_preco_excedido_entrega: Optional[str] = None,
        porc_preco_reduzido_entrega: Optional[str] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigo (str): The codigo
            descricao (str): The descricao
            unidade (str): The unidade
            status (int): The status
            prodEquipe (int): The equipe
            tipoCusto (str): The custo
            civilPes (int): The pes
            categoria (str): The categoria
            categoriaMovFin (str): The mov fin
            CAP (str): The c a p
            CAPEstorno (str): The c a p estorno
            CAPTransacaoFinanceira (str): The c a p transacao financeira
            NCM (str): The n c m
            CEST (str): The c e s t
            aplicacao (str): The aplicacao
            codigoServicoFiscal (str): The servico fiscal
            controlaFVS (int): The f v s
            confirmado (int): The confirmado
            porcQtdeExcedidaEntrega (str): The qtde excedida entrega
            porcPrecoExcedidoEntrega (str): The preco excedido entrega
            porcPrecoReduzidoEntrega (str): The preco reduzido entrega
        
        Parameter Structure:
        
            {
                "codigo": "string",
                "descricao": "string",
                "unidade": "string",
                "status": 0,
                "prodEquipe": 0,
                "tipoCusto": "string",
                "civilPes": 0,
                "categoria": "string",
                "categoriaMovFin": "string",
                "CAP": "string",
                "CAPEstorno": "string",
                "CAPTransacaoFinanceira": "string",
                "NCM": "string",
                "CEST": "string",
                "aplicacao": "string",
                "codigoServicoFiscal": "string",
                "controlaFVS": true,
                "confirmado": 0,
                "porcQtdeExcedidaEntrega": "string",
                "porcPrecoExcedidoEntrega": "string",
                "porcPrecoReduzidoEntrega": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._consultar_insumos_da_composicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/ConsultarInsumosDaComposicao"
        kwargs = {
            "codigo": codigo,
            "descricao": descricao,
            "unidade": unidade,
            "status": status,
            "prodEquipe": prod_equipe,
            "tipoCusto": tipo_custo,
            "civilPes": civil_pes,
            "categoria": categoria,
            "categoriaMovFin": categoria_mov_fin,
            "CAP": cap,
            "CAPEstorno": cap_estorno,
            "CAPTransacaoFinanceira": cap_transacao_financeira,
            "NCM": ncm,
            "CEST": cest,
            "aplicacao": aplicacao,
            "codigoServicoFiscal": codigo_servico_fiscal,
            "controlaFVS": controlafvs,
            "confirmado": confirmado,
            "porcQtdeExcedidaEntrega": porc_qtde_excedida_entrega,
            "porcPrecoExcedidoEntrega": porc_preco_excedido_entrega,
            "porcPrecoReduzidoEntrega": porc_preco_reduzido_entrega,
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

    def alterar_insumo_composicoes_geral(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codComposicao (str): The composicao
            codInsumo (str): The insumo
            tipoItem (int): The item
            coeficiente (int): The coeficiente
            preco (int): The preco
        
        Parameter Structure:
        
            {
                "codComposicao": "string",
                "codInsumo": "string",
                "tipoItem": 0,
                "coeficiente": 0,
                "preco": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._alterar_insumo_composicoes_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/AlterarInsumoComposicoesGeral"
        kwargs = {
            "codComposicao": cod_composicao,
            "codInsumo": cod_insumo,
            "tipoItem": tipo_item,
            "coeficiente": coeficiente,
            "preco": preco,
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

    def inserir_insumo_composicoes_geral(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codComposicao (str): The composicao
            codInsumo (str): The insumo
            tipoItem (int): The item
            coeficiente (int): The coeficiente
            preco (int): The preco
        
        Parameter Structure:
        
            {
                "codComposicao": "string",
                "codInsumo": "string",
                "tipoItem": 0,
                "coeficiente": 0,
                "preco": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._inserir_insumo_composicoes_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/InserirInsumoComposicoesGeral"
        kwargs = {
            "codComposicao": cod_composicao,
            "codInsumo": cod_insumo,
            "tipoItem": tipo_item,
            "coeficiente": coeficiente,
            "preco": preco,
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

    def consultar_composicoes_por_descricao(
        self,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Composicoes/ConsultarComposicoesPorDescricao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._consultar_composicoes_por_descricao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/ConsultarComposicoesPorDescricao"
        kwargs = {
            "descricao": descricao,
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

    def consultar_composicoes_com_filtro_livre(
        self,
        filtro: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Composicoes/ConsultarComposicoesComFiltroLivre`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite consultar os registros de composições gerais utilizando um filtro livre com qualquer um dos campos existentes
        Exemplo de filtro a ser utilizado: 
        
        "filtro": "Cod_comp = '10.50'"
        "filtro": "Descr_comp LIKE 'TERRAPLANAGEM%'" 
        "filtro": "Cod_comp = '10.50' AND Descr_comp LIKE 'TERRAPLANAGEM%'" 
        "filtro": "Cod_comp = '10.50' OR Descr_comp LIKE 'TERRAPLANAGEM%'"
        
        
        
        Args:
            filtro (str): The filtro
        
        Parameter Structure:
        
            {
                "filtro": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._consultar_composicoes_com_filtro_livre(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/ConsultarComposicoesComFiltroLivre"
        kwargs = {
            "filtro": filtro,
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

    def alterar_insumo_composicoes_geral_pesada(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None,
        coef_prod: Optional[int] = None,
        coef_im_prod: Optional[int] = None,
        dmt: Optional[int] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codComposicao (str): The composicao
            codInsumo (str): The insumo
            tipoItem (int): The item
            coeficiente (int): The coeficiente
            preco (int): The preco
            coefProd (int): The prod
            coefImProd (int): The im prod
            dMT (int): The m t
        
        Parameter Structure:
        
            {
                "codComposicao": "string",
                "codInsumo": "string",
                "tipoItem": 0,
                "coeficiente": 0,
                "preco": 0,
                "coefProd": 0,
                "coefImProd": 0,
                "dMT": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._alterar_insumo_composicoes_geral_pesada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/AlterarInsumoComposicoesGeralPesada"
        kwargs = {
            "codComposicao": cod_composicao,
            "codInsumo": cod_insumo,
            "tipoItem": tipo_item,
            "coeficiente": coeficiente,
            "preco": preco,
            "coefProd": coef_prod,
            "coefImProd": coef_im_prod,
            "dMT": dmt,
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

    def inserir_insumo_composicoes_geral_pesada(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None,
        coef_prod: Optional[int] = None,
        coef_im_prod: Optional[int] = None,
        dmt: Optional[int] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codComposicao (str): The composicao
            codInsumo (str): The insumo
            tipoItem (int): The item
            coeficiente (int): The coeficiente
            preco (int): The preco
            coefProd (int): The prod
            coefImProd (int): The im prod
            dMT (int): The m t
        
        Parameter Structure:
        
            {
                "codComposicao": "string",
                "codInsumo": "string",
                "tipoItem": 0,
                "coeficiente": 0,
                "preco": 0,
                "coefProd": 0,
                "coefImProd": 0,
                "dMT": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Composicoes()
            >>> response = api._inserir_insumo_composicoes_geral_pesada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Composicoes/InserirInsumoComposicoesGeralPesada"
        kwargs = {
            "codComposicao": cod_composicao,
            "codInsumo": cod_insumo,
            "tipoItem": tipo_item,
            "coeficiente": coeficiente,
            "preco": preco,
            "coefProd": coef_prod,
            "coefImProd": coef_im_prod,
            "dMT": dmt,
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

