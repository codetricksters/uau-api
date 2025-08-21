from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Funcionario:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_funcionario(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        codigo_pessoa: Optional[int] = None,
        codigo_funcionario: Optional[int] = None,
        matricula: Optional[str] = None,
        situacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Funcionario/ConsultarFuncionario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os dados dos funcionários URI + api/v{version:apiVersion}/Funcionario/ConsultarFuncionario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consulta os dados de funcionários do UAU, podendo fazer filtros pela empresa, obra, pessoa, funcionário, matrícula e situação.
        
        Deve informar obrigatoriamente o código da empresa.
        Pode informar opcionalmente o código da obra, pessoa, funcionário, matrícula e situação.
        
        VirtUau:
        
        Link para Virtuau relacionado:https://ajuda.globaltec.com.br/virtuau/cadastro-de-funcionarios/
        
        
        
        Args:
            CodigoEmpresa (int): The codigo empresa
            CodigoObra (str): The codigo obra
            CodigoPessoa (int): The codigo pessoa
            CodigoFuncionario (int): The codigo funcionario
            Matricula (str): The matricula
            Situacao (int): The situacao
        
        Parameter Structure:
        
            {
                "CodigoEmpresa": 0,
                "CodigoObra": "string",
                "CodigoPessoa": 0,
                "CodigoFuncionario": 0,
                "Matricula": "string",
                "Situacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Funcionario()
            >>> response = api._consultar_funcionario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Funcionario/ConsultarFuncionario"
        kwargs = {
            "CodigoEmpresa": codigo_empresa,
            "CodigoObra": codigo_obra,
            "CodigoPessoa": codigo_pessoa,
            "CodigoFuncionario": codigo_funcionario,
            "Matricula": matricula,
            "Situacao": situacao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

