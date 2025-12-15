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
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/InsumosGeral/InserirInsumosGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de inserir dados em InsumosGeral.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigo",
                            "descricao",
                            "usuario"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo": {
                                "description": "Código do insumo",
                                "type": "string"
                            },
                            "descricao": {
                                "description": "Descrição do insumo",
                                "type": "string"
                            },
                            "unidade": {
                                "description": "Unidade do insumo. Somente será considerado se não for informado a property unidadesInsumo.",
                                "type": "string"
                            },
                            "unidadesInsumo": {
                                "description": "Unidades do insumo - Lista de unidades do insumo, onde podem ser atualizados/inseridos o código da unidade, status de ativa ou inativa e determinar a unidade padrão.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.InsumosGeral.UnidadeInsumo"
                                }
                            },
                            "usuario": {
                                "description": "Usuário que está realizando o cadastro",
                                "type": "string"
                            },
                            "status": {
                                "format": "int32",
                                "description": "Status do insumo, onde: 0 - Ativo; 1 - Inativo",
                                "type": "integer"
                            },
                            "confirmado": {
                                "format": "int32",
                                "description": "Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado",
                                "type": "integer"
                            },
                            "controlarPrecoMeta": {
                                "description": "Se controla ou não o preço meta, onde: 0 - Não controla; 1 - Controla",
                                "type": "boolean"
                            },
                            "diasDeCompra": {
                                "format": "int32",
                                "description": "Número de dias para realizar a compra",
                                "type": "integer"
                            },
                            "diasUtilizacao": {
                                "format": "int32",
                                "description": "Número de dias que insumo deve estar na obra antes de sua utilização",
                                "type": "integer"
                            },
                            "numeroDeCompras": {
                                "format": "int32",
                                "description": "Número de compras a serem feitas no mês",
                                "type": "integer"
                            },
                            "diasEntrega": {
                                "format": "int32",
                                "description": "Número de dias para a entrega",
                                "type": "integer"
                            },
                            "numeroPagamentos": {
                                "format": "int32",
                                "description": "Número de pagamentos a serem feitos",
                                "type": "integer"
                            },
                            "tipoPagamento": {
                                "format": "int32",
                                "description": "Tipo de utilização do insumo, sendo: 0 -  Cotação; 1 - Medição; 2 - Solicitação de pagamento",
                                "type": "integer"
                            },
                            "controle": {
                                "format": "int32",
                                "description": "Tipo de controle do insumo (G1G2), onde: 1 - Controle por quantidade; 2 - Controle por verba",
                                "type": "integer"
                            },
                            "controlaEstoque": {
                                "format": "int32",
                                "description": "Indica se controla ou não o estoque, onde: 0 - Não controla; 1 - Controla",
                                "type": "integer"
                            },
                            "pagamentoSobre": {
                                "format": "int32",
                                "description": "Pagamento sobre, onde: 1 - Entrega; 2 - Pedido",
                                "type": "integer"
                            },
                            "preco": {
                                "description": "Preço do insumo",
                                "type": "string"
                            },
                            "dataCotacao": {
                                "format": "date-time",
                                "description": "Refere-se a data da última atualização do preço",
                                "type": "string"
                            },
                            "frequenciaCompra": {
                                "description": "Freqüência em que as compras serão realizadas",
                                "type": "string"
                            },
                            "comoPagar": {
                                "description": "Freqüência em que os pagamentos serão efetivados",
                                "type": "string"
                            },
                            "CAP": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal)",
                                "type": "string"
                            },
                            "categoriaMovFin": {
                                "description": "Categoria de movimentação financeira.",
                                "type": "string"
                            },
                            "CAPAplicacaoMaterial": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para aplicação de material)",
                                "type": "string"
                            },
                            "CAPEstorno": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para estorno)",
                                "type": "string"
                            },
                            "CAPTransacaoFinanceira": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para transacao financeira)",
                                "type": "string"
                            },
                            "CategoriaDoInsumo": {
                                "description": "Categoria do insumo",
                                "type": "string"
                            },
                            "NCM": {
                                "description": "Nomenclatura comum do MERCOSUL",
                                "type": "string"
                            },
                            "CEST": {
                                "description": "Código Especificador da Substituição Tributária",
                                "type": "string"
                            },
                            "Aplicacao": {
                                "description": "Código da aplicação fiscal",
                                "type": "string"
                            },
                            "grupo": {
                                "format": "int32",
                                "description": "Grupo do insumo, onde: 1 - Mão de obra; 2 - Equipamentos; 3 -Materiais; 4 - Serviços; 5 - Transporte",
                                "type": "integer"
                            },
                            "calcEncargo": {
                                "format": "int32",
                                "description": "Indica se o insumo é ou não para cálculo de encargo, onde:  0 - Não; 1 - Sim",
                                "type": "integer"
                            },
                            "controlaFVM": {
                                "description": "Indica se controla ou não a FVM, onde: 0 - Não controla; 1 - Controla\r\n- Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE.",
                                "type": "boolean"
                            },
                            "patrimonio": {
                                "format": "int32",
                                "description": "Indica se o insumo é ou não de patrimônio, onde: 0 - Não patrimônio; 1 - Patrimônio",
                                "type": "integer"
                            },
                            "depreciacao": {
                                "description": "Código de depreciação do patrimônio, fornecido atravez de uma tabela receita federal.",
                                "type": "string"
                            },
                            "grupoDeInsumos": {
                                "description": "Define se é um insumo de patrimônio, caso seja, possibilita informar o grupo de insumos e a depreciação.",
                                "type": "string"
                            },
                            "rateioParaMecanicos": {
                                "format": "double",
                                "description": "porcentagem que será distribuido do valor total deste insumo para uma futura manutenção de patrimônio interna.",
                                "type": "number"
                            },
                            "indicadorUtilBem": {
                                "format": "int32",
                                "description": "Indicador de utilização do bem incorporado ao ativo imobilizado, sendo: 1 - Produção de bens destinados a venda; 2 - Prestação de serviço; 3 - Locação a terceiros; 4 - Outros",
                                "type": "integer"
                            },
                            "capacidadeDiariaTrabalho": {
                                "description": "Capacidade diária de trabalho. Formato: HH:MM",
                                "type": "string"
                            },
                            "marcaModelo": {
                                "description": "Marca/Modelo",
                                "type": "string"
                            },
                            "subgrupo": {
                                "format": "int32",
                                "description": "Subgrupo",
                                "type": "integer"
                            },
                            "itemManutencao": {
                                "description": "Indica se o insumo é um item de manutenção, sendo: 0 (ou false) - Não; 1 (ou true) - Sim\r\n- Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE.",
                                "type": "boolean"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/InsumosGeral/InserirInsumosGeral"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def atualizar_insumos_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        Permite realizar manutenção em massa no cadastro dos insumos gerais.
        
        Utilize "" caso queira limpar os campos do cadastro sendo que, código, descrição e unidade padrão, não podem ficar vazios.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/parametrizacao-de-insumos-gerais/
        
        Endpoint: `/api/v{version}/InsumosGeral/AtualizarInsumosGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de realizar manutenção em massa no cadastro dos insumos gerais.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "listaInsumosAtualizar": {
                                "description": "Lista dos insumos gerais para atualização dos dados.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.InsumosGeral.InsumosGeralAtualizacao"
                                }
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/InsumosGeral/AtualizarInsumosGeral"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_insumos_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Nenhum parâmetro é obrigatório e os dados são retornados utilizando o LIKE para encontrar as informações.
        
        Endpoint: `/api/v{version}/InsumosGeral/ConsultarInsumosGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os itens de determinada revisão de um veículo ou equipamento.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "codigo_insumo": {
                                "description": "Codigo do insumo",
                                "type": "string"
                            },
                            "descricao_insumo": {
                                "description": "Descrição do insumo",
                                "type": "string"
                            },
                            "codigosub_grupo": {
                                "format": "int32",
                                "description": "Codigo do sub grupo do insumo",
                                "type": "integer"
                            },
                            "item_manutencao": {
                                "format": "int32",
                                "description": "Define o tipo de filtro por item da manutenção\r\nNão, Sim, Não Filtrar",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
                                "type": "integer"
                            },
                            "patrimonio": {
                                "format": "int32",
                                "description": "Define o tipo de filtro por patrimônio\r\nNão, Sim, Não Filtrar",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/InsumosGeral/ConsultarInsumosGeral"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_insumos_geral_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/InsumosGeral/ConsultarInsumosGeralPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de consultar dados do insumo geral por chave.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigo",
                            "descricao",
                            "usuario"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo": {
                                "description": "Código do insumo",
                                "type": "string"
                            },
                            "descricao": {
                                "description": "Descrição do insumo",
                                "type": "string"
                            },
                            "unidade": {
                                "description": "Unidade do insumo. Somente será considerado se não for informado a property unidadesInsumo.",
                                "type": "string"
                            },
                            "unidadesInsumo": {
                                "description": "Unidades do insumo - Lista de unidades do insumo, onde podem ser atualizados/inseridos o código da unidade, status de ativa ou inativa e determinar a unidade padrão.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.InsumosGeral.UnidadeInsumo"
                                }
                            },
                            "usuario": {
                                "description": "Usuário que está realizando o cadastro",
                                "type": "string"
                            },
                            "status": {
                                "format": "int32",
                                "description": "Status do insumo, onde: 0 - Ativo; 1 - Inativo",
                                "type": "integer"
                            },
                            "confirmado": {
                                "format": "int32",
                                "description": "Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado",
                                "type": "integer"
                            },
                            "controlarPrecoMeta": {
                                "description": "Se controla ou não o preço meta, onde: 0 - Não controla; 1 - Controla",
                                "type": "boolean"
                            },
                            "diasDeCompra": {
                                "format": "int32",
                                "description": "Número de dias para realizar a compra",
                                "type": "integer"
                            },
                            "diasUtilizacao": {
                                "format": "int32",
                                "description": "Número de dias que insumo deve estar na obra antes de sua utilização",
                                "type": "integer"
                            },
                            "numeroDeCompras": {
                                "format": "int32",
                                "description": "Número de compras a serem feitas no mês",
                                "type": "integer"
                            },
                            "diasEntrega": {
                                "format": "int32",
                                "description": "Número de dias para a entrega",
                                "type": "integer"
                            },
                            "numeroPagamentos": {
                                "format": "int32",
                                "description": "Número de pagamentos a serem feitos",
                                "type": "integer"
                            },
                            "tipoPagamento": {
                                "format": "int32",
                                "description": "Tipo de utilização do insumo, sendo: 0 -  Cotação; 1 - Medição; 2 - Solicitação de pagamento",
                                "type": "integer"
                            },
                            "controle": {
                                "format": "int32",
                                "description": "Tipo de controle do insumo (G1G2), onde: 1 - Controle por quantidade; 2 - Controle por verba",
                                "type": "integer"
                            },
                            "controlaEstoque": {
                                "format": "int32",
                                "description": "Indica se controla ou não o estoque, onde: 0 - Não controla; 1 - Controla",
                                "type": "integer"
                            },
                            "pagamentoSobre": {
                                "format": "int32",
                                "description": "Pagamento sobre, onde: 1 - Entrega; 2 - Pedido",
                                "type": "integer"
                            },
                            "preco": {
                                "description": "Preço do insumo",
                                "type": "string"
                            },
                            "dataCotacao": {
                                "format": "date-time",
                                "description": "Refere-se a data da última atualização do preço",
                                "type": "string"
                            },
                            "frequenciaCompra": {
                                "description": "Freqüência em que as compras serão realizadas",
                                "type": "string"
                            },
                            "comoPagar": {
                                "description": "Freqüência em que os pagamentos serão efetivados",
                                "type": "string"
                            },
                            "CAP": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal)",
                                "type": "string"
                            },
                            "categoriaMovFin": {
                                "description": "Categoria de movimentação financeira.",
                                "type": "string"
                            },
                            "CAPAplicacaoMaterial": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para aplicação de material)",
                                "type": "string"
                            },
                            "CAPEstorno": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para estorno)",
                                "type": "string"
                            },
                            "CAPTransacaoFinanceira": {
                                "description": "O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para transacao financeira)",
                                "type": "string"
                            },
                            "CategoriaDoInsumo": {
                                "description": "Categoria do insumo",
                                "type": "string"
                            },
                            "NCM": {
                                "description": "Nomenclatura comum do MERCOSUL",
                                "type": "string"
                            },
                            "CEST": {
                                "description": "Código Especificador da Substituição Tributária",
                                "type": "string"
                            },
                            "Aplicacao": {
                                "description": "Código da aplicação fiscal",
                                "type": "string"
                            },
                            "grupo": {
                                "format": "int32",
                                "description": "Grupo do insumo, onde: 1 - Mão de obra; 2 - Equipamentos; 3 -Materiais; 4 - Serviços; 5 - Transporte",
                                "type": "integer"
                            },
                            "calcEncargo": {
                                "format": "int32",
                                "description": "Indica se o insumo é ou não para cálculo de encargo, onde:  0 - Não; 1 - Sim",
                                "type": "integer"
                            },
                            "controlaFVM": {
                                "description": "Indica se controla ou não a FVM, onde: 0 - Não controla; 1 - Controla\r\n- Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE.",
                                "type": "boolean"
                            },
                            "patrimonio": {
                                "format": "int32",
                                "description": "Indica se o insumo é ou não de patrimônio, onde: 0 - Não patrimônio; 1 - Patrimônio",
                                "type": "integer"
                            },
                            "depreciacao": {
                                "description": "Código de depreciação do patrimônio, fornecido atravez de uma tabela receita federal.",
                                "type": "string"
                            },
                            "grupoDeInsumos": {
                                "description": "Define se é um insumo de patrimônio, caso seja, possibilita informar o grupo de insumos e a depreciação.",
                                "type": "string"
                            },
                            "rateioParaMecanicos": {
                                "format": "double",
                                "description": "porcentagem que será distribuido do valor total deste insumo para uma futura manutenção de patrimônio interna.",
                                "type": "number"
                            },
                            "indicadorUtilBem": {
                                "format": "int32",
                                "description": "Indicador de utilização do bem incorporado ao ativo imobilizado, sendo: 1 - Produção de bens destinados a venda; 2 - Prestação de serviço; 3 - Locação a terceiros; 4 - Outros",
                                "type": "integer"
                            },
                            "capacidadeDiariaTrabalho": {
                                "description": "Capacidade diária de trabalho. Formato: HH:MM",
                                "type": "string"
                            },
                            "marcaModelo": {
                                "description": "Marca/Modelo",
                                "type": "string"
                            },
                            "subgrupo": {
                                "format": "int32",
                                "description": "Subgrupo",
                                "type": "integer"
                            },
                            "itemManutencao": {
                                "description": "Indica se o insumo é um item de manutenção, sendo: 0 (ou false) - Não; 1 (ou true) - Sim\r\n- Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE.",
                                "type": "boolean"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/InsumosGeral/ConsultarInsumosGeralPorChave"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_insumos_geral_por_descricao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/InsumosGeral/ConsultarInsumosGeralPorDescricao`
        HTTP Method: `POST`
        
        Implementation Notes:
        - Método com finalidade de consultar dados de insumo geral por descrição, considerando o LIKE.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Descricao": {
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/InsumosGeral/ConsultarInsumosGeralPorDescricao"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

