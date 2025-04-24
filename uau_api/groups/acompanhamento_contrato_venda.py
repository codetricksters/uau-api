from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class AcompanhamentoContratoVenda:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gravar_acompanhamento(
        self,
        num_acompanhamento: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_contrato: Optional[str] = None,
        periodo_inicio: Optional[datetime] = None,
        periodo_fim: Optional[datetime] = None,
        lista_de_produtos: Optional[List[Dict]] = None,
        responsavel: Optional[int] = None,
        status: Optional[int] = None,
        observacao_para_entrega: Optional[str] = None,
        motorista: Optional[int] = None,
        caminhao_placa: Optional[str] = None,
        uf_placa: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanhamentoContratoVenda/GravarAcompanhamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Retorna json com as informações de empresa, obra, número do contrato e número do acompanhamento.
        
        Definição de Negócio:
        
        Permite inserir ou alterar um acompanhamento de contrato de venda. 
        O usuário autenticado deve ter permissão de inclusão ou alteração em OBACOMPVENDA, a depender do objetivo (inserir ou editar acompanhamento).
        O sistema identifica que é uma edição no acompanhamento quando a propriedade [NumAcompanhamento] está preenchida. Em caso de não informação deste campo, será gravado um novo acompanhamento.
        O usuário autenticado deve ter permissão de inclusão em OBMEDICAOVENDA.
        Em caso de manutenção de um acompanhamento, as informações serão sobrescritas e as quantidades "Qtde medida" e "Qtde falta medir" calculadas a partir da propriedade [QtdeAMedir] informada.
        
        
        
        Args:
            NumAcompanhamento (int): The num acompanhamento
            Empresa (int): The empresa
            Obra (str): The obra
            NumContrato (str): The num contrato
            PeriodoInicio (datetime): The periodo inicio
            PeriodoFim (datetime): The periodo fim
            ListaDeProdutos (List[Dict[str, Any]]): The lista de produtos
            Responsavel (int): The responsavel
            Status (int): The status
            ObservacaoParaEntrega (str): The observacao para entrega
            Motorista (int): The motorista
            CaminhaoPlaca (str): The caminhao placa
            UFPlaca (str): The u f placa
        
        Parameter Structure:
        
            {
                "NumAcompanhamento": 0,
                "Empresa": 0,
                "Obra": "string",
                "NumContrato": "string",
                "PeriodoInicio": "2025-04-23T13:46:12.405Z",
                "PeriodoFim": "2025-04-23T13:46:12.405Z",
                "ListaDeProdutos": [
                    {
                        "NumeroProduto": "string",
                        "QtdAMedir": 0
                    }
                ],
                "Responsavel": 0,
                "Status": 0,
                "ObservacaoParaEntrega": "string",
                "Motorista": 0,
                "CaminhaoPlaca": "string",
                "UFPlaca": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanhamentoContratoVenda()
            >>> response = api._gravar_acompanhamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanhamentoContratoVenda/GravarAcompanhamento"
        try:
            response = self.api.post(
                path,
                json={
                    "NumAcompanhamento": num_acompanhamento,
                    "Empresa": empresa,
                    "Obra": obra,
                    "NumContrato": num_contrato,
                    "PeriodoInicio": periodo_inicio,
                    "PeriodoFim": periodo_fim,
                    "ListaDeProdutos": lista_de_produtos,
                    "Responsavel": responsavel,
                    "Status": status,
                    "ObservacaoParaEntrega": observacao_para_entrega,
                    "Motorista": motorista,
                    "CaminhaoPlaca": caminhao_placa,
                    "UFPlaca": uf_placa,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

