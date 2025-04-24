from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class AcompanhamentosServicos:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def acompanhar_contrato(
        self,
        empresa: Optional[str] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        descricao_servico: Optional[str] = None,
        mes: Optional[datetime] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        usuario: Optional[str] = None,
        qtde: Optional[int] = None,
        sequencia: Optional[str] = None,
        codigo_estrutura: Optional[str] = None,
        orcamento: Optional[int] = None,
        contrato_vinculado: Optional[int] = None,
        ordem: Optional[int] = None,
        etapa: Optional[str] = None,
        observacao: Optional[str] = None,
        aplicacao_material: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/AcompanharContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Grava o acompanhamento de contrato vinculado a um planejamento ou orçamento
        
        Informar os parâmetros dependendo do vinculo com orçamento ou planejamento
        
        
        
        Args:
            empresa (str): The empresa
            obra (str): The obra
            produto (int): The produto
            contrato (int): The contrato
            item (str): The item
            servico (str): The servico
            descricaoServico (str): The servico
            mes (datetime): The mes
            dataInicio (datetime): The inicio
            dataFim (datetime): The fim
            usuario (str): The usuario
            qtde (int): The qtde
            sequencia (str): The sequencia
            codigoEstrutura (str): The estrutura
            orcamento (int): The orcamento
            contratoVinculado (int): The vinculado
            ordem (int): The ordem
            etapa (str): The etapa
            observacao (str): The observacao
            aplicacaoMaterial (List[Dict[str, Any]]): The material
        
        Parameter Structure:
        
            {
                "empresa": "string",
                "obra": "string",
                "produto": 0,
                "contrato": 0,
                "item": "string",
                "servico": "string",
                "descricaoServico": "string",
                "mes": "2025-04-23T13:46:12.416Z",
                "dataInicio": "2025-04-23T13:46:12.416Z",
                "dataFim": "2025-04-23T13:46:12.416Z",
                "usuario": "string",
                "qtde": 0,
                "sequencia": "string",
                "codigoEstrutura": "string",
                "orcamento": 0,
                "contratoVinculado": 0,
                "ordem": 0,
                "etapa": "string",
                "observacao": "string",
                "aplicacaoMaterial": [
                    {
                        "itemMaterial": 0,
                        "QtdeAplicada": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/AcompanharContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "produto": produto,
                    "contrato": contrato,
                    "item": item,
                    "servico": servico,
                    "descricaoServico": descricao_servico,
                    "mes": mes,
                    "dataInicio": data_inicio,
                    "dataFim": data_fim,
                    "usuario": usuario,
                    "qtde": qtde,
                    "sequencia": sequencia,
                    "codigoEstrutura": codigo_estrutura,
                    "orcamento": orcamento,
                    "contratoVinculado": contrato_vinculado,
                    "ordem": ordem,
                    "etapa": etapa,
                    "observacao": observacao,
                    "aplicacaoMaterial": aplicacao_material,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def acompanhar_servico_pl(
        self,
        empresa: Optional[str] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        usuario: Optional[str] = None,
        qtde: Optional[int] = None,
        sequencia: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None,
        aprova_contrato: Optional[bool] = None,
        contrato_vinculado: Optional[int] = None,
        descricao_servico: Optional[str] = None,
        ordem: Optional[int] = None,
        etapa: Optional[str] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/AcompanharServicoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio: 
          Acompanhar serviço do planejamento solicitado.
        
        Valida se o usuário está cadastrado no sistema e ativo.
        Valida se já existe acompanhamento para o código externo de integração solicitado.
        Verifica se o fechamento do acompanhamento não foi realizado.
        
        
        
        Args:
            empresa (str): The empresa
            obra (str): The obra
            produto (int): The produto
            contrato (int): The contrato
            item (str): The item
            servico (str): The servico
            mes (str): The mes
            usuario (str): The usuario
            qtde (int): The qtde
            sequencia (str): The sequencia
            codExternoIntegracao (str): The externo integracao
            aprovaContrato (int): The contrato
            contratoVinculado (int): The vinculado
            descricaoServico (str): The servico
            ordem (int): The ordem
            etapa (str): The etapa
            observacao (str): The observacao
        
        Parameter Structure:
        
            {
                "empresa": "string",
                "obra": "string",
                "produto": 0,
                "contrato": 0,
                "item": "string",
                "servico": "string",
                "mes": "string",
                "usuario": "string",
                "qtde": 0,
                "sequencia": "string",
                "codExternoIntegracao": "string",
                "aprovaContrato": true,
                "contratoVinculado": 0,
                "descricaoServico": "string",
                "ordem": 0,
                "etapa": "string",
                "observacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servicopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/AcompanharServicoPL"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "produto": produto,
                    "contrato": contrato,
                    "item": item,
                    "servico": servico,
                    "mes": mes,
                    "usuario": usuario,
                    "qtde": qtde,
                    "sequencia": sequencia,
                    "codExternoIntegracao": cod_externo_integracao,
                    "aprovaContrato": aprova_contrato,
                    "contratoVinculado": contrato_vinculado,
                    "descricaoServico": descricao_servico,
                    "ordem": ordem,
                    "etapa": etapa,
                    "observacao": observacao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def acompanhar_servico_orcado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        servico: Optional[str] = None,
        item: Optional[str] = None,
        orcamento: Optional[int] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None,
        usuario_logado: Optional[str] = None,
        sequencia: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None,
        aprova_contrato: Optional[bool] = None,
        contrato_vinculado: Optional[int] = None,
        descricao_servico: Optional[str] = None,
        ordem: Optional[int] = None,
        etapa: Optional[str] = None,
        mes: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/AcompanharServicoOrcado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.
        
        Deve montar uma estrutura seguindo o modelo.
        Valida se o usuário está cadastrado.
        Valida se o serviço não possui estruturas.
        Valida se possui distribuição no periodo acompanhado.
        Valida o saldo do orçamento que será acompanhado.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            servico (str): The servico
            item (str): The item
            orcamento (int): The orcamento
            periodo (str): The periodo
            quantidade (int): The quantidade
            usuario_logado (str): The usuario_logado
            sequencia (str): The sequencia
            codExternoIntegracao (str): The externo integracao
            aprovaContrato (int): The contrato
            contratoVinculado (int): The vinculado
            descricaoServico (str): The servico
            ordem (int): The ordem
            etapa (str): The etapa
            mes (str): The mes
            produto (int): The produto
            contrato (int): The contrato
            observacao (str): The observacao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "servico": "string",
                "item": "string",
                "orcamento": 0,
                "periodo": "string",
                "quantidade": 0,
                "usuario_logado": "string",
                "sequencia": "string",
                "codExternoIntegracao": "string",
                "aprovaContrato": true,
                "contratoVinculado": 0,
                "descricaoServico": "string",
                "ordem": 0,
                "etapa": "string",
                "mes": "string",
                "produto": 0,
                "contrato": 0,
                "observacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servico_orcado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/AcompanharServicoOrcado"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "servico": servico,
                    "item": item,
                    "orcamento": orcamento,
                    "periodo": periodo,
                    "quantidade": quantidade,
                    "usuario_logado": usuario_logado,
                    "sequencia": sequencia,
                    "codExternoIntegracao": cod_externo_integracao,
                    "aprovaContrato": aprova_contrato,
                    "contratoVinculado": contrato_vinculado,
                    "descricaoServico": descricao_servico,
                    "ordem": ordem,
                    "etapa": etapa,
                    "mes": mes,
                    "produto": produto,
                    "contrato": contrato,
                    "observacao": observacao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def acompanhar_servico_contrato(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contrato_servico: Optional[int] = None,
        item_contrato: Optional[int] = None,
        servico: Optional[str] = None,
        data_inicio: Optional[str] = None,
        data_fim: Optional[str] = None,
        mes_pl: Optional[str] = None,
        quantidade: Optional[int] = None,
        porcentagem_acomp: Optional[int] = None,
        observacoes: Optional[str] = None,
        etapa: Optional[str] = None,
        cod_estrutura: Optional[str] = None,
        sequencia: Optional[str] = None,
        usuario_logado: Optional[str] = None,
        cod_acomp: Optional[int] = None,
        orcamento: Optional[int] = None,
        item_orcamento: Optional[str] = None,
        aplicacao_material: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/AcompanharServicoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método do acordo com o modelo.
        
        Definição de Negócio:
          Permite consultar e portanto acompanhar serviços referentes aos contratos.
        
        Valida usuário.
        Valida prazo de validade do contrato.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            contrato_servico (int): The contrato_servico
            item_contrato (int): The item_contrato
            servico (str): The servico
            data_inicio (str): The data_inicio
            data_fim (str): The data_fim
            mes_pl (str): The mes_pl
            quantidade (int): The quantidade
            porcentagem_acomp (int): The porcentagem_acomp
            observacoes (str): The observacoes
            etapa (str): The etapa
            cod_estrutura (str): The cod_estrutura
            sequencia (str): The sequencia
            usuario_logado (str): The usuario_logado
            cod_acomp (int): The cod_acomp
            orcamento (int): The orcamento
            itemOrcamento (str): The orcamento
            aplicacaoMaterial (List[Dict[str, Any]]): The material
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "contrato_servico": 0,
                "item_contrato": 0,
                "servico": "string",
                "data_inicio": "string",
                "data_fim": "string",
                "mes_pl": "string",
                "quantidade": 0,
                "porcentagem_acomp": 0,
                "observacoes": "string",
                "etapa": "string",
                "cod_estrutura": "string",
                "sequencia": "string",
                "usuario_logado": "string",
                "cod_acomp": 0,
                "orcamento": 0,
                "itemOrcamento": "string",
                "aplicacaoMaterial": [
                    {
                        "itemMaterial": 0,
                        "QtdeAplicada": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._acompanhar_servico_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/AcompanharServicoContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "contrato_servico": contrato_servico,
                    "item_contrato": item_contrato,
                    "servico": servico,
                    "data_inicio": data_inicio,
                    "data_fim": data_fim,
                    "mes_pl": mes_pl,
                    "quantidade": quantidade,
                    "porcentagem_acomp": porcentagem_acomp,
                    "observacoes": observacoes,
                    "etapa": etapa,
                    "cod_estrutura": cod_estrutura,
                    "sequencia": sequencia,
                    "usuario_logado": usuario_logado,
                    "cod_acomp": cod_acomp,
                    "orcamento": orcamento,
                    "itemOrcamento": item_orcamento,
                    "aplicacaoMaterial": aplicacao_material,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def excluir_acompanhamento_servico_pl(
        self,
        empresa: Optional[str] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        usuario: Optional[str] = None,
        qtde: Optional[int] = None,
        sequencia: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/ExcluirAcompanhamentoServicoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
          Permite excluir acompanhamento de Serviços do planejamento.
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio: 
          Acompanhar serviço do planejamento solicitado.
        
        Valida se existe acompanhamento para o código informado.
        Valida se existe acompanhamento para o registro informado.
        Valida se o acompanhamento se encontra aberto.
        Valida a quantidade informada para exclusão.
        
        
        
        Args:
            empresa (str): The empresa
            obra (str): The obra
            produto (int): The produto
            contrato (int): The contrato
            item (str): The item
            servico (str): The servico
            mes (str): The mes
            usuario (str): The usuario
            qtde (int): The qtde
            sequencia (str): The sequencia
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "empresa": "string",
                "obra": "string",
                "produto": 0,
                "contrato": 0,
                "item": "string",
                "servico": "string",
                "mes": "string",
                "usuario": "string",
                "qtde": 0,
                "sequencia": "string",
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servicopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoPL"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "produto": produto,
                    "contrato": contrato,
                    "item": item,
                    "servico": servico,
                    "mes": mes,
                    "usuario": usuario,
                    "qtde": qtde,
                    "sequencia": sequencia,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def excluir_acompanhamento_servico_orcado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        servico: Optional[str] = None,
        item: Optional[str] = None,
        orcamento: Optional[int] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None,
        sequencia: Optional[str] = None,
        num_acomp: Optional[int] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Permite excluir acompanhamento de serviço orçado.
        
        Valida se a exclusão pode ser realizada.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            servico (str): The servico
            item (str): The item
            orcamento (int): The orcamento
            periodo (str): The periodo
            quantidade (int): The quantidade
            sequencia (str): The sequencia
            numAcomp (int): The acomp
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "servico": "string",
                "item": "string",
                "orcamento": 0,
                "periodo": "string",
                "quantidade": 0,
                "sequencia": "string",
                "numAcomp": 0,
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_orcado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcado"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "servico": servico,
                    "item": item,
                    "orcamento": orcamento,
                    "periodo": periodo,
                    "quantidade": quantidade,
                    "sequencia": sequencia,
                    "numAcomp": num_acomp,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def alterar_acompanhamento_servico_contrato(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contrato_servico: Optional[int] = None,
        item_contrato: Optional[int] = None,
        servico: Optional[str] = None,
        data_inicio: Optional[str] = None,
        data_fim: Optional[str] = None,
        mes_pl: Optional[str] = None,
        quantidade: Optional[int] = None,
        porcentagem_acomp: Optional[int] = None,
        observacoes: Optional[str] = None,
        etapa: Optional[str] = None,
        cod_estrutura: Optional[str] = None,
        sequencia: Optional[str] = None,
        usuario_logado: Optional[str] = None,
        cod_acomp: Optional[int] = None,
        orcamento: Optional[int] = None,
        item_orcamento: Optional[str] = None,
        aplicacao_material: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/AlterarAcompanhamentoServicoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.
        
        Deve montar uma estrutura seguindo o modelo.
        Valida se o usuário é cadastrado e se tem permissão para realizar a alteração.
        Valida se o serviço é controlado por tipologia de produção.
        Valida se a quantidade a acompanhar excede o saldo a acompanhar.
        Valida se o contrato é valido para aletrações.
        Valida o prazo de validade do contrato.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            contrato_servico (int): The contrato_servico
            item_contrato (int): The item_contrato
            servico (str): The servico
            data_inicio (str): The data_inicio
            data_fim (str): The data_fim
            mes_pl (str): The mes_pl
            quantidade (int): The quantidade
            porcentagem_acomp (int): The porcentagem_acomp
            observacoes (str): The observacoes
            etapa (str): The etapa
            cod_estrutura (str): The cod_estrutura
            sequencia (str): The sequencia
            usuario_logado (str): The usuario_logado
            cod_acomp (int): The cod_acomp
            orcamento (int): The orcamento
            itemOrcamento (str): The orcamento
            aplicacaoMaterial (List[Dict[str, Any]]): The material
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "contrato_servico": 0,
                "item_contrato": 0,
                "servico": "string",
                "data_inicio": "string",
                "data_fim": "string",
                "mes_pl": "string",
                "quantidade": 0,
                "porcentagem_acomp": 0,
                "observacoes": "string",
                "etapa": "string",
                "cod_estrutura": "string",
                "sequencia": "string",
                "usuario_logado": "string",
                "cod_acomp": 0,
                "orcamento": 0,
                "itemOrcamento": "string",
                "aplicacaoMaterial": [
                    {
                        "itemMaterial": 0,
                        "QtdeAplicada": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._alterar_acompanhamento_servico_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/AlterarAcompanhamentoServicoContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "contrato_servico": contrato_servico,
                    "item_contrato": item_contrato,
                    "servico": servico,
                    "data_inicio": data_inicio,
                    "data_fim": data_fim,
                    "mes_pl": mes_pl,
                    "quantidade": quantidade,
                    "porcentagem_acomp": porcentagem_acomp,
                    "observacoes": observacoes,
                    "etapa": etapa,
                    "cod_estrutura": cod_estrutura,
                    "sequencia": sequencia,
                    "usuario_logado": usuario_logado,
                    "cod_acomp": cod_acomp,
                    "orcamento": orcamento,
                    "itemOrcamento": item_orcamento,
                    "aplicacaoMaterial": aplicacao_material,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def excluir_acompanhamento_servico_de_contrato(
        self,
        empresa: Optional[int] = None,
        contrato_servico: Optional[int] = None,
        item_contrato: Optional[int] = None,
        servico: Optional[str] = None,
        quantidade: Optional[int] = None,
        sequencia: Optional[str] = None,
        codigo_estrutura: Optional[str] = None,
        usuario_logado: Optional[str] = None,
        cod_aec: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Exclui o acompanhamento de serviço no contrato.
        
        Valida se o usuário tem permissão para excluir um acompanhamento.
        Valida se possui estrutura e se o status do acompanhamento está como "aberto". Neste caso não será excluido.
        
        
        
        Args:
            empresa (int): The empresa
            contrato_servico (int): The contrato_servico
            item_contrato (int): The item_contrato
            servico (str): The servico
            quantidade (int): The quantidade
            sequencia (str): The sequencia
            codigo_estrutura (str): The codigo_estrutura
            usuario_logado (str): The usuario_logado
            codAec (int): The aec
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "contrato_servico": 0,
                "item_contrato": 0,
                "servico": "string",
                "quantidade": 0,
                "sequencia": "string",
                "codigo_estrutura": "string",
                "usuario_logado": "string",
                "codAec": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_de_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "contrato_servico": contrato_servico,
                    "item_contrato": item_contrato,
                    "servico": servico,
                    "quantidade": quantidade,
                    "sequencia": sequencia,
                    "codigo_estrutura": codigo_estrutura,
                    "usuario_logado": usuario_logado,
                    "codAec": cod_aec,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def excluir_acompanhamento_servico_orcado_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        servico: Optional[str] = None,
        item: Optional[str] = None,
        orcamento: Optional[int] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None,
        sequencia: Optional[str] = None,
        num_acomp: Optional[int] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Exclui o acompanhamento de serviço oraçado de acordo com a chave informada.
        
        Valida se o acompanhamento informado existe.
        Valida se a exclusão pode ser realizada.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            servico (str): The servico
            item (str): The item
            orcamento (int): The orcamento
            periodo (str): The periodo
            quantidade (int): The quantidade
            sequencia (str): The sequencia
            numAcomp (int): The acomp
            codExternoIntegracao (str): The externo integracao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "servico": "string",
                "item": "string",
                "orcamento": 0,
                "periodo": "string",
                "quantidade": 0,
                "sequencia": "string",
                "numAcomp": 0,
                "codExternoIntegracao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._excluir_acompanhamento_servico_orcado_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                    "servico": servico,
                    "item": item,
                    "orcamento": orcamento,
                    "periodo": periodo,
                    "quantidade": quantidade,
                    "sequencia": sequencia,
                    "numAcomp": num_acomp,
                    "codExternoIntegracao": cod_externo_integracao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def consultar_acompanhamento_contrato_servico_por_servico(
        self,
        empresa: Optional[int] = None,
        servico: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consulta acompanhamento de contrato de serviço filtrando por serviço.
        
        
        Args:
            Empresa (int): The empresa
            Servico (str): The servico
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Servico": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._consultar_acompanhamento_contrato_servico_por_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorServico"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Servico": servico,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def consultar_acompanhamento_contrato_servico_por_contrato_eservico(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        servico: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorContratoEServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
          Definição de Negócio:
          Permite acompanhar contratos filtrando por:
        Empresa
        Contrato
        Serviço
        
        
        
        
        
        Args:
            Empresa (int): The empresa
            Contrato (int): The contrato
            Servico (str): The servico
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Contrato": 0,
                "Servico": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentosServicos()
            >>> response = api._consultar_acompanhamento_contrato_servico_por_contratoe_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorContratoEServico"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Contrato": contrato,
                    "Servico": servico,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

