from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class InsumosGeral:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def inserir_insumos_geral(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        unidades_insumo: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        status: Optional[int] = None,
        confirmado: Optional[int] = None,
        controlar_preco_meta: Optional[bool] = None,
        dias_de_compra: Optional[int] = None,
        dias_utilizacao: Optional[int] = None,
        numero_de_compras: Optional[int] = None,
        dias_entrega: Optional[int] = None,
        numero_pagamentos: Optional[int] = None,
        tipo_pagamento: Optional[int] = None,
        controle: Optional[int] = None,
        controla_estoque: Optional[int] = None,
        pagamento_sobre: Optional[int] = None,
        preco: Optional[str] = None,
        data_cotacao: Optional[datetime] = None,
        frequencia_compra: Optional[str] = None,
        como_pagar: Optional[str] = None,
        cap: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap_aplicacao_material: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        categoria_do_insumo: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        grupo: Optional[int] = None,
        calc_encargo: Optional[int] = None,
        controlafvm: Optional[bool] = None,
        patrimonio: Optional[int] = None,
        depreciacao: Optional[str] = None,
        grupo_de_insumos: Optional[str] = None,
        rateio_para_mecanicos: Optional[int] = None,
        indicador_util_bem: Optional[int] = None,
        capacidade_diaria_trabalho: Optional[str] = None,
        marca_modelo: Optional[str] = None,
        subgrupo: Optional[int] = None,
        item_manutencao: Optional[bool] = None
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
            unidadesInsumo (List[Dict[str, Any]]): The insumo
            usuario (str): The usuario
            status (int): The status
            confirmado (int): The confirmado
            controlarPrecoMeta (int): The preco meta
            diasDeCompra (int): The de compra
            diasUtilizacao (int): The utilizacao
            numeroDeCompras (int): The de compras
            diasEntrega (int): The entrega
            numeroPagamentos (int): The pagamentos
            tipoPagamento (int): The pagamento
            controle (int): The controle
            controlaEstoque (int): The estoque
            pagamentoSobre (int): The sobre
            preco (str): The preco
            dataCotacao (datetime): The cotacao
            frequenciaCompra (str): The compra
            comoPagar (str): The pagar
            CAP (str): The c a p
            categoriaMovFin (str): The mov fin
            CAPAplicacaoMaterial (str): The c a p aplicacao material
            CAPEstorno (str): The c a p estorno
            CAPTransacaoFinanceira (str): The c a p transacao financeira
            CategoriaDoInsumo (str): The categoria do insumo
            NCM (str): The n c m
            CEST (str): The c e s t
            Aplicacao (str): The aplicacao
            grupo (int): The grupo
            calcEncargo (int): The encargo
            controlaFVM (int): The f v m
            patrimonio (int): The patrimonio
            depreciacao (str): The depreciacao
            grupoDeInsumos (str): The de insumos
            rateioParaMecanicos (int): The para mecanicos
            indicadorUtilBem (int): The util bem
            capacidadeDiariaTrabalho (str): The diaria trabalho
            marcaModelo (str): The modelo
            subgrupo (int): The subgrupo
            itemManutencao (int): The manutencao
        
        Parameter Structure:
        
            {
                "codigo": "string",
                "descricao": "string",
                "unidade": "string",
                "unidadesInsumo": [
                    {
                        "unidade": "string",
                        "unidadePadrao": 0,
                        "unidadeAtiva": 0
                    }
                ],
                "usuario": "string",
                "status": 0,
                "confirmado": 0,
                "controlarPrecoMeta": true,
                "diasDeCompra": 0,
                "diasUtilizacao": 0,
                "numeroDeCompras": 0,
                "diasEntrega": 0,
                "numeroPagamentos": 0,
                "tipoPagamento": 0,
                "controle": 0,
                "controlaEstoque": 0,
                "pagamentoSobre": 0,
                "preco": "string",
                "dataCotacao": "2025-04-23T13:46:13.244Z",
                "frequenciaCompra": "string",
                "comoPagar": "string",
                "CAP": "string",
                "categoriaMovFin": "string",
                "CAPAplicacaoMaterial": "string",
                "CAPEstorno": "string",
                "CAPTransacaoFinanceira": "string",
                "CategoriaDoInsumo": "string",
                "NCM": "string",
                "CEST": "string",
                "Aplicacao": "string",
                "grupo": 0,
                "calcEncargo": 0,
                "controlaFVM": true,
                "patrimonio": 0,
                "depreciacao": "string",
                "grupoDeInsumos": "string",
                "rateioParaMecanicos": 0,
                "indicadorUtilBem": 0,
                "capacidadeDiariaTrabalho": "string",
                "marcaModelo": "string",
                "subgrupo": 0,
                "itemManutencao": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = InsumosGeral()
            >>> response = api._inserir_insumos_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "InsumosGeral/InserirInsumosGeral"
        kwargs = {
            "codigo": codigo,
            "descricao": descricao,
            "unidade": unidade,
            "unidadesInsumo": unidades_insumo,
            "usuario": usuario,
            "status": status,
            "confirmado": confirmado,
            "controlarPrecoMeta": controlar_preco_meta,
            "diasDeCompra": dias_de_compra,
            "diasUtilizacao": dias_utilizacao,
            "numeroDeCompras": numero_de_compras,
            "diasEntrega": dias_entrega,
            "numeroPagamentos": numero_pagamentos,
            "tipoPagamento": tipo_pagamento,
            "controle": controle,
            "controlaEstoque": controla_estoque,
            "pagamentoSobre": pagamento_sobre,
            "preco": preco,
            "dataCotacao": data_cotacao,
            "frequenciaCompra": frequencia_compra,
            "comoPagar": como_pagar,
            "CAP": cap,
            "categoriaMovFin": categoria_mov_fin,
            "CAPAplicacaoMaterial": cap_aplicacao_material,
            "CAPEstorno": cap_estorno,
            "CAPTransacaoFinanceira": cap_transacao_financeira,
            "CategoriaDoInsumo": categoria_do_insumo,
            "NCM": ncm,
            "CEST": cest,
            "Aplicacao": aplicacao,
            "grupo": grupo,
            "calcEncargo": calc_encargo,
            "controlaFVM": controlafvm,
            "patrimonio": patrimonio,
            "depreciacao": depreciacao,
            "grupoDeInsumos": grupo_de_insumos,
            "rateioParaMecanicos": rateio_para_mecanicos,
            "indicadorUtilBem": indicador_util_bem,
            "capacidadeDiariaTrabalho": capacidade_diaria_trabalho,
            "marcaModelo": marca_modelo,
            "subgrupo": subgrupo,
            "itemManutencao": item_manutencao,
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
                        print("inserir_insumos_geral::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("inserir_insumos_geral::Server returned an error")
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
                print("inserir_insumos_geral::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def atualizar_insumos_geral(
        self,
        lista_insumos_atualizar: Optional[List[Dict]] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite realizar manutenção em massa no cadastro dos insumos gerais.
        Utilize "" caso queira limpar os campos do cadastro sendo que, código, descrição e unidade padrão, não podem ficar vazios.
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/parametrizacao-de-insumos-gerais/
        
        
        Args:
            listaInsumosAtualizar (List[Dict[str, Any]]): The insumos atualizar
        
        Parameter Structure:
        
            {
                "listaInsumosAtualizar": [
                    {
                        "codigo": "string",
                        "descricao": "string",
                        "unidadesInsumo": [
                            {
                                "unidade": "string",
                                "unidadePadrao": 0,
                                "unidadeAtiva": 0
                            }
                        ],
                        "preco": "string",
                        "inativarVincUnidPadraoSubstituida": true,
                        "CategoriaDoInsumo": "string",
                        "grupo": "string",
                        "status": 0,
                        "codigoInsumoSubstituirNasComposicoes": "string",
                        "ComposicoesSubstituir": [
                            {
                                "codigoComposicao": "string"
                            }
                        ],
                        "NCM": "string",
                        "CEST": "string",
                        "aplicacao": "string",
                        "controlarPrecoMeta": true,
                        "CAP": "string",
                        "CAPAplicacaoMaterial": "string",
                        "CAPEstorno": "string",
                        "CAPTransacaoFinanceira": "string",
                        "categoriaMovFin": "string",
                        "confirmado": 0,
                        "diasDeCompra": "string",
                        "diasUtilizacao": "string",
                        "numeroDeCompras": "string",
                        "diasEntrega": "string",
                        "numeroPagamentos": "string",
                        "tipoPagamento": "string",
                        "controle": "string",
                        "controlaEstoque": 0,
                        "pagamentoSobre": 0,
                        "dataCotacao": "2025-04-23T13:46:13.252Z",
                        "frequenciaCompra": "string",
                        "comoPagar": "string",
                        "calcEncargo": 0,
                        "controlaFVM": true,
                        "patrimonio": 0,
                        "depreciacao": "string",
                        "grupoDeInsumos": "string",
                        "rateioParaMecanicos": 0,
                        "indicadorUtilBem": 0,
                        "capacidadeDiariaTrabalho": "string",
                        "marcaModelo": "string",
                        "subgrupo": 0,
                        "itemManutencao": true,
                        "porcQtdeExcedidaEntrega": "string",
                        "porcPrecoExcedidoEntrega": "string",
                        "porcPrecoReduzidoEntrega": "string",
                        "verificacaoSGQ": 0,
                        "criterioVerificacaoSGQ": "string",
                        "especificacaoSGQ": "string",
                        "identificacaoSGQ": "string",
                        "orientacaoSGQ": "string",
                        "observacaoSGQ": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = InsumosGeral()
            >>> response = api._atualizar_insumos_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "InsumosGeral/AtualizarInsumosGeral"
        kwargs = {
            "listaInsumosAtualizar": lista_insumos_atualizar,
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
                        print("atualizar_insumos_geral::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("atualizar_insumos_geral::Server returned an error")
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
                print("atualizar_insumos_geral::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_insumos_geral(
        self,
        codigo_insumo: Optional[str] = None,
        descricao_insumo: Optional[str] = None,
        codigosub_grupo: Optional[int] = None,
        item_manutencao: Optional[int] = None,
        patrimonio: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `InsumosGeral/ConsultarInsumosGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Nenhum parâmetro é obrigatório e os dados são retornados utilizando o LIKE para encontrar as informações.
        
        
        
        Args:
            codigo_insumo (str): The codigo_insumo
            descricao_insumo (str): The descricao_insumo
            codigosub_grupo (int): The codigosub_grupo
            item_manutencao (int): The item_manutencao
            patrimonio (int): The patrimonio
        
        Parameter Structure:
        
            {
                "codigo_insumo": "string",
                "descricao_insumo": "string",
                "codigosub_grupo": 0,
                "item_manutencao": 0,
                "patrimonio": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = InsumosGeral()
            >>> response = api._consultar_insumos_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "InsumosGeral/ConsultarInsumosGeral"
        kwargs = {
            "codigo_insumo": codigo_insumo,
            "descricao_insumo": descricao_insumo,
            "codigosub_grupo": codigosub_grupo,
            "item_manutencao": item_manutencao,
            "patrimonio": patrimonio,
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
                        print("consultar_insumos_geral::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_insumos_geral::Server returned an error")
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
                print("consultar_insumos_geral::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_insumos_geral_por_chave(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        unidades_insumo: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        status: Optional[int] = None,
        confirmado: Optional[int] = None,
        controlar_preco_meta: Optional[bool] = None,
        dias_de_compra: Optional[int] = None,
        dias_utilizacao: Optional[int] = None,
        numero_de_compras: Optional[int] = None,
        dias_entrega: Optional[int] = None,
        numero_pagamentos: Optional[int] = None,
        tipo_pagamento: Optional[int] = None,
        controle: Optional[int] = None,
        controla_estoque: Optional[int] = None,
        pagamento_sobre: Optional[int] = None,
        preco: Optional[str] = None,
        data_cotacao: Optional[datetime] = None,
        frequencia_compra: Optional[str] = None,
        como_pagar: Optional[str] = None,
        cap: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap_aplicacao_material: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        categoria_do_insumo: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        grupo: Optional[int] = None,
        calc_encargo: Optional[int] = None,
        controlafvm: Optional[bool] = None,
        patrimonio: Optional[int] = None,
        depreciacao: Optional[str] = None,
        grupo_de_insumos: Optional[str] = None,
        rateio_para_mecanicos: Optional[int] = None,
        indicador_util_bem: Optional[int] = None,
        capacidade_diaria_trabalho: Optional[str] = None,
        marca_modelo: Optional[str] = None,
        subgrupo: Optional[int] = None,
        item_manutencao: Optional[bool] = None
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
            unidadesInsumo (List[Dict[str, Any]]): The insumo
            usuario (str): The usuario
            status (int): The status
            confirmado (int): The confirmado
            controlarPrecoMeta (int): The preco meta
            diasDeCompra (int): The de compra
            diasUtilizacao (int): The utilizacao
            numeroDeCompras (int): The de compras
            diasEntrega (int): The entrega
            numeroPagamentos (int): The pagamentos
            tipoPagamento (int): The pagamento
            controle (int): The controle
            controlaEstoque (int): The estoque
            pagamentoSobre (int): The sobre
            preco (str): The preco
            dataCotacao (datetime): The cotacao
            frequenciaCompra (str): The compra
            comoPagar (str): The pagar
            CAP (str): The c a p
            categoriaMovFin (str): The mov fin
            CAPAplicacaoMaterial (str): The c a p aplicacao material
            CAPEstorno (str): The c a p estorno
            CAPTransacaoFinanceira (str): The c a p transacao financeira
            CategoriaDoInsumo (str): The categoria do insumo
            NCM (str): The n c m
            CEST (str): The c e s t
            Aplicacao (str): The aplicacao
            grupo (int): The grupo
            calcEncargo (int): The encargo
            controlaFVM (int): The f v m
            patrimonio (int): The patrimonio
            depreciacao (str): The depreciacao
            grupoDeInsumos (str): The de insumos
            rateioParaMecanicos (int): The para mecanicos
            indicadorUtilBem (int): The util bem
            capacidadeDiariaTrabalho (str): The diaria trabalho
            marcaModelo (str): The modelo
            subgrupo (int): The subgrupo
            itemManutencao (int): The manutencao
        
        Parameter Structure:
        
            {
                "codigo": "string",
                "descricao": "string",
                "unidade": "string",
                "unidadesInsumo": [
                    {
                        "unidade": "string",
                        "unidadePadrao": 0,
                        "unidadeAtiva": 0
                    }
                ],
                "usuario": "string",
                "status": 0,
                "confirmado": 0,
                "controlarPrecoMeta": true,
                "diasDeCompra": 0,
                "diasUtilizacao": 0,
                "numeroDeCompras": 0,
                "diasEntrega": 0,
                "numeroPagamentos": 0,
                "tipoPagamento": 0,
                "controle": 0,
                "controlaEstoque": 0,
                "pagamentoSobre": 0,
                "preco": "string",
                "dataCotacao": "2025-04-23T13:46:13.264Z",
                "frequenciaCompra": "string",
                "comoPagar": "string",
                "CAP": "string",
                "categoriaMovFin": "string",
                "CAPAplicacaoMaterial": "string",
                "CAPEstorno": "string",
                "CAPTransacaoFinanceira": "string",
                "CategoriaDoInsumo": "string",
                "NCM": "string",
                "CEST": "string",
                "Aplicacao": "string",
                "grupo": 0,
                "calcEncargo": 0,
                "controlaFVM": true,
                "patrimonio": 0,
                "depreciacao": "string",
                "grupoDeInsumos": "string",
                "rateioParaMecanicos": 0,
                "indicadorUtilBem": 0,
                "capacidadeDiariaTrabalho": "string",
                "marcaModelo": "string",
                "subgrupo": 0,
                "itemManutencao": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = InsumosGeral()
            >>> response = api._consultar_insumos_geral_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "InsumosGeral/ConsultarInsumosGeralPorChave"
        kwargs = {
            "codigo": codigo,
            "descricao": descricao,
            "unidade": unidade,
            "unidadesInsumo": unidades_insumo,
            "usuario": usuario,
            "status": status,
            "confirmado": confirmado,
            "controlarPrecoMeta": controlar_preco_meta,
            "diasDeCompra": dias_de_compra,
            "diasUtilizacao": dias_utilizacao,
            "numeroDeCompras": numero_de_compras,
            "diasEntrega": dias_entrega,
            "numeroPagamentos": numero_pagamentos,
            "tipoPagamento": tipo_pagamento,
            "controle": controle,
            "controlaEstoque": controla_estoque,
            "pagamentoSobre": pagamento_sobre,
            "preco": preco,
            "dataCotacao": data_cotacao,
            "frequenciaCompra": frequencia_compra,
            "comoPagar": como_pagar,
            "CAP": cap,
            "categoriaMovFin": categoria_mov_fin,
            "CAPAplicacaoMaterial": cap_aplicacao_material,
            "CAPEstorno": cap_estorno,
            "CAPTransacaoFinanceira": cap_transacao_financeira,
            "CategoriaDoInsumo": categoria_do_insumo,
            "NCM": ncm,
            "CEST": cest,
            "Aplicacao": aplicacao,
            "grupo": grupo,
            "calcEncargo": calc_encargo,
            "controlaFVM": controlafvm,
            "patrimonio": patrimonio,
            "depreciacao": depreciacao,
            "grupoDeInsumos": grupo_de_insumos,
            "rateioParaMecanicos": rateio_para_mecanicos,
            "indicadorUtilBem": indicador_util_bem,
            "capacidadeDiariaTrabalho": capacidade_diaria_trabalho,
            "marcaModelo": marca_modelo,
            "subgrupo": subgrupo,
            "itemManutencao": item_manutencao,
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
                        print("consultar_insumos_geral_por_chave::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_insumos_geral_por_chave::Server returned an error")
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
                print("consultar_insumos_geral_por_chave::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_insumos_geral_por_descricao(
        self,
        descricao: Optional[str] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = InsumosGeral()
            >>> response = api._consultar_insumos_geral_por_descricao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "InsumosGeral/ConsultarInsumosGeralPorDescricao"
        kwargs = {
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
                        print("consultar_insumos_geral_por_descricao::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_insumos_geral_por_descricao::Server returned an error")
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
                print("consultar_insumos_geral_por_descricao::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

