from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ContratoMaterialServico:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_itens_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ContratoMaterialServico/ConsultarItensContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consultar itens presentes em um contrato.
        
        
        
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_itens_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarItensContrato"
        kwargs = {
            "empresa": empresa,
            "contrato": contrato,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_contrato_por_chave(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ContratoMaterialServico/ConsultarContratoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        Retorna os dados do contrato.
        
        Definição de Negócio:
        
        Consulta contrato filtrando pela chave.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        
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
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contrato_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarContratoPorChave"
        kwargs = {
            "empresa": empresa,
            "contrato": contrato,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_contrato_por_fornecedor(
        self,
        fornecedor: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ContratoMaterialServico/ConsultarContratoPorFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consulta os contratos de um fornecedor.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        
        Args:
            fornecedor (int): The fornecedor
        
        Parameter Structure:
        
            {
                "fornecedor": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contrato_por_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarContratoPorFornecedor"
        kwargs = {
            "fornecedor": fornecedor,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_contrato_por_servico_material(
        self,
        empresa: Optional[int] = None,
        servico_material: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ContratoMaterialServico/ConsultarContratoPorServicoMaterial`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consulta contrato filtrando por:
        Empresa;
        Serviço ou material;
        
        
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        
        Args:
            empresa (int): The empresa
            servicoMaterial (str): The material
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "servicoMaterial": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contrato_por_servico_material(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarContratoPorServicoMaterial"
        kwargs = {
            "empresa": empresa,
            "servicoMaterial": servico_material,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_itens_vinculo_orcamento_servico(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        orcamento: Optional[int] = None,
        somente_contratos_aprovados: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ContratoMaterialServico/ConsultarItensVinculoOrcamentoServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.
        
        Definição de Negócio:
        
        Consultar os itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
        Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            item (str): The item
            servico (str): The servico
            orcamento (int): The orcamento
            somenteContratosAprovados (int): The contratos aprovados
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "item": "string",
                "servico": "string",
                "orcamento": 0,
                "somenteContratosAprovados": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_itens_vinculo_orcamento_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarItensVinculoOrcamentoServico"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "item": item,
            "servico": servico,
            "orcamento": orcamento,
            "somenteContratosAprovados": somente_contratos_aprovados,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_saldo_reajustado_por_item_contrato(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contratos: Optional[List[Dict]] = None,
        situacoes: Optional[List[Dict]] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consultar valores aprovados e saldo reajustado de itens do contrato.
        Consulta contrato filtrando por:
        Empresa (obrigatório)
        Obra;
        Situacoes (pode ser informado uma lista de situações): 
        0 - Andamento
        1 - Paralisado
        2 - Cancelado
        3 - Concluído
        4 - Em encerramento
        
        
        Contratos (pode ser informada uma lista de contratos);
        
        
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            contratos (List[Dict[str, Any]]): The contratos
            situacoes (List[Dict[str, Any]]): The situacoes
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "contratos": [
                    0
                ],
                "situacoes": [
                    0
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_saldo_reajustado_por_item_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarSaldoReajustadoPorItemContrato"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "contratos": contratos,
            "situacoes": situacoes,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_itens_vinculo_planejamento_servico(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ContratoMaterialServico/ConsultarItensVinculoPlanejamentoServico`
        HTTP Method: `POST`
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            item (str): The item
            servico (str): The servico
            produto (int): The produto
            contrato (int): The contrato
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "item": "string",
                "servico": "string",
                "produto": 0,
                "contrato": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_itens_vinculo_planejamento_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarItensVinculoPlanejamentoServico"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "item": item,
            "servico": servico,
            "produto": produto,
            "contrato": contrato,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_contratos_itens_vinculado_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        somente_contratos_aprovados: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ContratoMaterialServico/ConsultarContratosItensVinculadoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.
        
        Definição de Negócio:
        
        Consultar os contratos e itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
        Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            orcamento (int): The orcamento
            somenteContratosAprovados (int): The contratos aprovados
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "orcamento": 0,
                "somenteContratosAprovados": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ContratoMaterialServico()
            >>> response = api._consultar_contratos_itens_vinculado_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ContratoMaterialServico/ConsultarContratosItensVinculadoOrcamento"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "orcamento": orcamento,
            "somenteContratosAprovados": somente_contratos_aprovados,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

