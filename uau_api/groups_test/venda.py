from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Venda:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def renegociar_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método
        
        Definição de Negócio:
        Permite renegociar parcelas de uma venda
        1. O usuário deverá estar autenticado e validado
        2. Informar os dados da venda
        3. Informar as parcelas a serem geradas
        4. Informar as parcelas escolhidas para renegociação
        5. Informar o plano de indexação
        6. Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
           retorna mensagem informando a inconsistência encontrada para que seja analisada
        7. Após as validações realiza a renegociação das parcelas
        8. Será registrado comentário na venda sobre a renegociação realizada
        9. Lista de planos indexadores
            - Caso não informe a lista de planos indexadores, serão considerados os planos que já existem na venda. 
            - Caso informe a lista de planos indexadores, a lista informada será considerada.
                - Caso um grupo informado de plano indexador já exista na venda, ele não será inserido novamente.
                - Para verificar se os planos já existem, serão considerados os grupos. Se para um grupo informado, já existir os mesmos indíces e datas na venda, ele não será adicionado.
        10. Padrão de Cobrança
            - Padrão de Cobrança Informado no JSON. (Se o tipo de parcela tiver um padrão de cobrança vinculado, esse padrão será priorizado.)
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
        - https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
        
         Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
        - Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso
        
        Endpoint: `/api/v{version}/Venda/RenegociarVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a renegociação de parcelas de uma venda realizando as validações necessárias.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Dados da venda renegociados pela API",
                        "required": [
                            "Empresa",
                            "Obra",
                            "Venda",
                            "Parc_Geradas",
                            "ParcSel_Reneg"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "Venda": {
                                "format": "int32",
                                "description": "Número do contrato a ser renegociado (Venda, aluguel, aluguel shopping, etc)",
                                "type": "integer"
                            },
                            "Parc_Geradas": {
                                "description": "Novas parcelas geradas após realizar a renegociação",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.RenegociarVenda.ParcelaRenegociacaoRequest"
                                }
                            },
                            "ParcSel_Reneg": {
                                "description": "Tabela com as parcelas originais, selecionadas para ser renegociada (somente chave)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.RenegociarVenda.ParcelaSelRenegociacaoRequest"
                                }
                            },
                            "ValDesc_reneg": {
                                "format": "double",
                                "description": "Valor de desconto utilizado na renegociação",
                                "type": "number"
                            },
                            "ValAcresc_reneg": {
                                "format": "double",
                                "description": "Valor de acréscimo utilizado na renegociação",
                                "type": "number"
                            },
                            "Valor_Reajustado": {
                                "format": "int32",
                                "description": "Renegociação será feita com  [1]-valores reajustado ou [0]-valores dos principais",
                                "type": "integer"
                            },
                            "NumeroPadraoCobranca": {
                                "format": "int32",
                                "description": "Número do padrão de cobrança as ser usado nas novas parcelas geradas após renegociação",
                                "type": "integer"
                            },
                            "Tabelaplano_idx": {
                                "description": "Plano indexador novo a ser utilizado pela venda renegociada",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.RenegociarVenda.PlanoIndexadorRenegociacaoRequest"
                                }
                            },
                            "DataCalculo": {
                                "description": "Data de cálculo das parcelas a serem renegociada",
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
            >>> api = Venda()
            >>> response = api._renegociar_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/RenegociarVenda"
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

    def busca_parc_reneg_web(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Possibilita buscar parcelas calculadas para a data atual (dia da requisição).
        
        Endpoint: `/api/v{version}/Venda/BuscaParcRenegWeb`
        HTTP Method: `POST`
        
        Implementation Notes:
        Buscar parcelas calculadas na data atual
        
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
                            "empresa",
                            "obra",
                            "num_ven",
                            "exibirparcenv_cob",
                            "somenteparc_atraso",
                            "parcelasenviadas_banco"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "num_ven": {
                                "format": "int32",
                                "description": "Código da venda",
                                "type": "integer"
                            },
                            "exibirparcenv_cob": {
                                "description": "Retornar somente parcelas enviadas a cobrança: TRUE = sim, FALSE = não",
                                "type": "boolean"
                            },
                            "somenteparc_atraso": {
                                "description": "Retornar somente parcelas em atraso: TRUE = sim, FALSE = não",
                                "type": "boolean"
                            },
                            "parcelasenviadas_banco": {
                                "description": "Retornar parcelas enviadas ao banco: TRUE = sim, FALSE = não",
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
            >>> api = Venda()
            >>> response = api._busca_parc_reneg_web(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscaParcRenegWeb"
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

    def exclusao_de_boletos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Possibilita excluir boletos que estão com o status de normal.
        2. Será permitido a exclusão de no máximo 20 boletos por requisição.
        
        Endpoint: `/api/v{version}/Venda/ExclusaoDeBoletos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Faz a exclusão dos boletos informados
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Lista com todos os boletos que serão excluídos",
                        "required": [
                            "listaBoletosExcluir"
                        ],
                        "type": "object",
                        "properties": {
                            "listaBoletosExcluir": {
                                "description": "Lista de custas.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ExclusaoDeBoletos"
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
            >>> api = Venda()
            >>> response = api._exclusao_de_boletos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ExclusaoDeBoletos"
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

    def exportar_vendas_xml(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar os dados das contas contábeis com a URI + /api/v{version}/Venda/ExportarVendasXml
        3. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite exportar os registros de uma ou mais vendas do UAU para um arquivo XML no formato esperado para realização de importação de vendas.
        1. Deve informar a venda ou o período para que seja realizada a consulta.
        2. Pode informar as chaves de Venda que são [Empresa, Obra, Venda].
        3. Valida as datas e campos inseridos.
        4. O perído informado buscará vendas considerando a data de cadastro, a data de manutenção e a data de quitação.
        5. O item "listaVendas" permite informar empresa, obra e venda que serão adicionados ao retorno da consulta. 
        Não será filtrado exclusivamente por esta lista de vendas, mas serão acrescidas ao resultado do período informado.
        
        VirtUau:
        - http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Venda/Venda_ExportarVendasXml
        
         Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777060/ 
        - Arquivo de Retorno: https://ajuda.globaltec.com.br/download/777060/
        
        Endpoint: `/api/v{version}/Venda/ExportarVendasXml`
        HTTP Method: `POST`
        
        Implementation Notes:
        Busca as vendas informadas ou as vendas inseridas/alteradas no periodo informado.
        
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
                            "dados_vendas"
                        ],
                        "type": "object",
                        "properties": {
                            "dados_vendas": {
                                "$ref": "#/definitions/UAUApi.Models.Venda.ExportaVendas",
                                "description": "Objeto com os dados das vendas"
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
            >>> api = Venda()
            >>> response = api._exportar_vendas_xml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ExportarVendasXml"
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

    def importacao_de_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Número máximo de importações por vez: 50.
        4. Para obter retorno de sucesso ou falha na importação consulte o endpoint:
            - URI + /api/v1.0/Venda/ImportacaoVendaComRetorno
        
        Validação:
        1. Arquivo XSD: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Manual-de-integracao-de-Vendas_versao1006_2.zip
        
        2. Dicionário de dados: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Venda.zip
        
        Definição de Negócio:
        
        Permite importar vendas para o UAU via XML.
        1. Valida quantidade de importações por requisição.
        2. Caso ocorra erro em uma venda, todas as outras importações são canceladas.
        
        Endpoint: `/api/v{version}/Venda/ImportacaoDeVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Importar vendas para o UAU via XML
        
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
                            "xml_vendas",
                            "alterarnumerodas_vendas"
                        ],
                        "type": "object",
                        "properties": {
                            "xml_vendas": {
                                "description": "XML de importação das vendas",
                                "type": "string"
                            },
                            "alterarnumerodas_vendas": {
                                "description": "Gerar novo número para as vendas importadas.\r\nTrue\r\nFalse",
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
            >>> api = Venda()
            >>> response = api._importacao_de_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ImportacaoDeVenda"
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

    def aprov_desaprov_reneg(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de negócio
        - A rota aprova ou desaprova uma renegociação de venda.
        - É realizada uma validação da Alçada.
        - Os anexos são atualizados conforme a operação solicitada.
        
        Pré requisito:
        - É necessário ter permissão de aprovação em FIMNTVENRENCON
        
        - Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
            - URL + /api/v{version}/Venda/AprovDesaprovReneg
        
        Endpoint: `/api/v{version}/Venda/AprovDesaprovReneg`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar ou desaprovar renegociações
        
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
                            "codEmpresa",
                            "codObra",
                            "numVenda",
                            "aprovDesaprov"
                        ],
                        "type": "object",
                        "properties": {
                            "codEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "codObra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "numVenda": {
                                "format": "int32",
                                "description": "Código da venda",
                                "type": "integer"
                            },
                            "aprovDesaprov": {
                                "description": "Aprovar ou desaprovar",
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
            >>> api = Venda()
            >>> response = api._aprov_desaprov_reneg(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/AprovDesaprovReneg"
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

    def buscar_tipos_de_custas(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Busca a lista de status de cobrança ativos do sistema:
         - URI + /api/v{version}/Venda/BuscarTiposDeCustas
        
        1. Formato dos dados retornados:
         - Codigo(String):Código do tipo de custa
         - Descricao(String):Descrição do status de cobrança
        
        Endpoint: `/api/v{version}/Venda/BuscarTiposDeCustas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista de tipos de custas ativos.
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
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
            >>> api = Venda()
            >>> response = api._buscar_tipos_de_custas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarTiposDeCustas"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_historicos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. O preenchimento da lista de vendas, devem ser preenchidos de forma padronizada, ou preenche todas as vendas com o número da venda, ou todas com apenas empresa e obra.
        4. Para o preenchimento dos tipos de manutenção, o valor de tipo de manutenção deve ser numérico e caso tenha mais de um, devem ser separados por vírgula. Exemplo: 1,2,4.
        5. Recomendável buscar períodos curtos ou uma venda específica para evitar timeout.
        
        Definição de Negócio:
        Consultar os históricos de uma ou mais vendas selecionadas.
        Para buscar os históricos das vendas um dos parâmetros devem estar preenchidos, ou a lista de vendas ou o período da manutenção.
        1. As classes abaixo não serão preenchidas no objeto de retorno porque essas informações não possuem histórico:
            - Comissoes
            - Comentarios
            - AluguelShopping
            - VendaVinculada
            - DescontosDeCusta
            - Recebimentos
            - Prorrogacoes
        
        Endpoint: `/api/v{version}/Venda/ConsultarHistoricos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar os históricos de uma ou mais vendas
        
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
                            "Vendas": {
                                "description": "Lista de objeto (VendasComManutencao) com as vendas selecionadas para visualizar a manutenção se existir",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.VendasComManutencao"
                                }
                            },
                            "DataInicio": {
                                "format": "date-time",
                                "description": "Data inicial da manutenção",
                                "type": "string"
                            },
                            "DataFim": {
                                "format": "date-time",
                                "description": "Data final da manutenção",
                                "type": "string"
                            },
                            "TipoManutencao": {
                                "description": "Tipo de manutenção\r\n    0. Cancelar venda\r\n    1. Renegociar contrato\r\n    2. Cessão de direito\r\n    3. Simulação de distrato\r\n    4. Alterar parâmetros da venda\r\n    5. Alterar juros em parcelas price\r\n    6. Acerto final\r\n    7. Renegociação pendente\r\n    8. Cessão de direito pendente\r\n    9. Renegociação pendente com emissão de boleto\r\n    10. Renegociação de parcelas pendente\r\n    11. Renegociação de parcelas pendente com emissão de boleto\r\n    12. Renegociação de parcelas \r\n    13. Recebimento Parcial\r\n    14. Devolução de recebimento parcial\r\n    15. Devolução de recebimento parcial com estorno\r\n    16. Cancelamento de Aluguéis",
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
            >>> api = Venda()
            >>> response = api._consultar_historicos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarHistoricos"
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

    def excluir_parcela_custa(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Venda/ExcluirParcelaCusta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Reliza a exclusão de Parcela de Custa.
        
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
                            "ExcluirParcelaNoBanco",
                            "Lista"
                        ],
                        "type": "object",
                        "properties": {
                            "ExcluirParcelaNoBanco": {
                                "description": "Parâmetro para identificar se e para excluir a parcela ou não, se ela estiver no banco.",
                                "type": "boolean"
                            },
                            "Lista": {
                                "description": "Lista dos campos",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ExcluirParcelaCustaCampos"
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
            >>> api = Venda()
            >>> response = api._excluir_parcela_custa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ExcluirParcelaCusta"
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

    def gerar_boleto_bancario(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Permite gerar o boleto bancário ou carnê.
        2. O usuário autenticado deve ter permissão de inclusão no programa de permissão VEBOLETOAVULSO.
        3. Para gerar boleto parcial é necessário informar a propriedade ValorBoleto.
            - Não pode ser um valor negativo nem inferior a 0,01 centavo.
            - Se informar um valor igual ao valor total das parcelas enviadas, será gerado um boleto normal.
            - Se informar um valor menor que o valor total das parcelas enviadas, será gerado um boleto parcial.
                - Apenas uma parcela das enviadas deverá ser parcial
                - Não será gerado boleto caso informe um valor que não cubra todas as parcelas enviadas
                - A ordem de envio das parcelas deve ser a mesma ordem de seleção das parcelas ao gerar o boleto pela tela de recebimento avulso.
                Exemplo: Na tela de recebimento avulso, selecionei as parcelas 360, 359 e 358. Ao gerar pela API, as parcelas devem ser enviadas
                na mesma sequência selecionada.
                - Irá validar se as parcelas enviadas podem gerar o boleto parcial de acordo com a regra de dias para vencimento.
            - Será possível gerar boleto parcial somente para parcelas de uma única empresa, obra e venda.
            - Só é possível gerar boleto parcial para mais de uma parcela quando for antecipação.
            - É obrigatório reajustar ao gerar o boleto parcial.
        4. Padrão de cobrança    
            - Não é obrigatório informá-lo.
            - Caso informado, o sistema irá desconsiderar a configuração do parâmetro usarpadraoboleto_avulso e irá gerar o boleto pelo padrão informado.
            - Caso informado, será desconsiderado o padrão de cobrança de todas as parcelas, incluindo custas administrativas, e boleto será gerado com o padrão de cobrança informado.
            - Apenas os padrões de cobrança ativos serão aceitos.
            - Será possivel gerar boleto com o padrão de cobrança informado, somente para parcelas de uma única empresa.
            - Obs.: Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão AVULSO informado no grupo, o sistema irá desconsiderar o padrão informado no JSON e manter o padrão de cobrança da configuração de grupo de cobrança.
        5. Excluir Boletos Existentes
            - Não é obrigatório informar o parâmetro ExcluirBoletosExistentes.
            - Caso não seja informado será mantido a opção padrão de não excluir.
            - Caso informado, irá executar as mesmas ações que a configuração 'Excluir boletos já emitidos ao gerar um novo boleto para a parcela' no cadastro de empresas &gt; config. vendas.
        6. Reaproveitar boleto
            - Não é obrigatório informar o parâmetro ReaproveitarBoleto
            - Caso não seja informado será mantida a opção padrão de não reaproveitar o boleto,
            - Caso informado, irá tentar reaproveitar algum boleto que já exista para uma das parcelas enviadas.
                - Somente válido para bancos e/ou tipos de cobrança que permitem a manutenção do boleto.
                - Somente para parcelas de uma única empresa, obra e venda. Caso envie parcelas de vendas diferentes, a opção de reaproveitar boleto será desconsiderada e irá gerar um novo boleto.
                - Será gerado arquivo de alteração de vencimento ou valor do boleto.
                - Não será possivel reaproveitar caso não exista boleto gerado ou o agrupamento das parcelas gere mais de um boleto.
            - Sempre homologue junto ao banco antes de usar!
        7. Valor taxa boleto
            - Não é obrigatório informar o parâmetro ValorTaxaBoleto
            - Essa taxa será utilizada independente do parâmetro de reaproveitar boleto for true e a venda cobrar taxa de boleto.
            - Caso informado, irá desconsiderar o valor da taxa cadastrado na empresa e aplicar o valor informado.
            - Caso não seja informado ou seja informado zero, irá aplicar o valor da taxa cadastrado na empresa do boleto reaproveitado.
        
        Endpoint: `/api/v{version}/Venda/GerarBoletoBancario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gravar o arquivo de remessa para geração do boleto bancario ou carne
        
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
                            "parcelas",
                            "data_calculo"
                        ],
                        "type": "object",
                        "properties": {
                            "parcelas": {
                                "description": "Lista de objeto (ParcelasBoleto) com as parcelas geradas do tipo boleto ou carne e se existir, o valor do desconto",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ParcelasBoleto"
                                }
                            },
                            "data_calculo": {
                                "format": "date-time",
                                "description": "Data de cálculo",
                                "type": "string"
                            },
                            "antecipar": {
                                "description": "Se o cálculo será antecipado\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "reajustar": {
                                "description": "Se é para reajustar os valores\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "excluirboleto_expirado": {
                                "description": "Se é para excluir os boletos expirados\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "formaarquivo_cobranca": {
                                "format": "int32",
                                "description": "Forma da cobrança\r\nBoleto = 0\r\nCarnê = 1",
                                "enum": [
                                    0,
                                    1
                                ],
                                "type": "integer"
                            },
                            "boletosacado_detalhado": {
                                "description": "Se o sacado será detalhado\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "carnetres_vias": {
                                "description": "Se o carnê será em três vias\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "naovalidardados_pendentes": {
                                "description": "Se não deve validar os dados pendentes da parcela\r\nTRUE - Não validar\r\nFALSE - Validar",
                                "type": "boolean"
                            },
                            "acrescentar_residuo": {
                                "description": "Se vai acrescentar o valor de resíduo\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "usarpadraoboleto_avulso": {
                                "description": "Indica qual o padrão de cobrança será utilizado\r\nTRUE - Irá usar o padrão de cobrança para boleto avulso cadastrado na obra\r\nFALSE - Irá usar o padrão de cobrança das parcelas\r\n<list type=\"bullet\"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão AVULSO informado, \r\nesse padrão irá sobrepor o padrão da obra, mantendo a configuração de grupo de cobrança.</item></list>",
                                "type": "boolean"
                            },
                            "agrupar_parcelas": {
                                "description": "Se deve agrupar as parcelas informadas\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "formaagruparpor_vendas": {
                                "description": "Forma de agrupamento do boleto\r\nTRUE  - Realiza o agrupamento das parcelas por venda\r\nFALSE - Realiza o agrupamento das parcelas por pessoa",
                                "type": "boolean"
                            },
                            "ValorBoleto": {
                                "format": "double",
                                "description": "Valor do boleto, utilizado para geração de boletos parciais.",
                                "type": "number"
                            },
                            "PadraoCobranca": {
                                "format": "int32",
                                "description": "Nr. do padrão para cobrança\r\n<list type=\"bullet\"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão AVULSO informado, \r\nesse padrão irá sobrepor o padrão informado no JSON, mantendo a configuração de grupo de cobrança.</item></list>",
                                "type": "integer"
                            },
                            "ExcluirBoletosExistentes": {
                                "description": "Se irá excluir boletos já emitidos ao gerar um novo boleto para a parcela",
                                "type": "boolean"
                            },
                            "ReaproveitarBoleto": {
                                "description": "Se irá reaproveitar o boleto já gerado para alguma das parcelas enviadas",
                                "type": "boolean"
                            },
                            "ValorTaxaBoleto": {
                                "format": "double",
                                "description": "Valor de taxa do boleto que será utilizada ao reaproveitar um boleto",
                                "type": "number"
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
            >>> api = Venda()
            >>> response = api._gerar_boleto_bancario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GerarBoletoBancario"
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

    def gerar_pdfresumo_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.
        
        Definição de Negócio:
        Gera boleto PDF do resumo da venda em formato Base64.
        1. Validações a nível de usuário.
        
        Endpoint: `/api/v{version}/Venda/GerarPDFResumoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar PDF do relatório do resumo da venda
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "numeroVenda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data do cálculo",
                                "type": "string"
                            },
                            "dataCorrecao": {
                                "format": "date-time",
                                "description": "Data da correção",
                                "type": "string"
                            },
                            "antecipar": {
                                "description": "Antecipar parcelas",
                                "type": "boolean"
                            },
                            "parcelas": {
                                "description": "Lista de parcelas para antecipação do resumo de venda",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ParcelasResumoVendaRequest"
                                }
                            },
                            "aplicarDescontoGeral": {
                                "description": "Aplicar desconto geral",
                                "type": "boolean"
                            },
                            "percentualDescontoGeral": {
                                "format": "double",
                                "description": "Percentual de desconto geral a ser aplicado",
                                "type": "number"
                            },
                            "aplicarDescontoAntecipacao": {
                                "description": "Aplicar desconto de antecipação",
                                "type": "boolean"
                            },
                            "descontoAntecipacao": {
                                "$ref": "#/definitions/UAUApi.Models.Venda.DescontoAntecipacaoResumoVendaRequest",
                                "description": "Dados do desconto de antecipação"
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
            >>> api = Venda()
            >>> response = api._gerarpdf_resumo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GerarPDFResumoVenda"
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

    def buscar_status_cobranca(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Busca a lista de status de cobrança ativos do sistema:
         - URI + /api/v{version}/Venda/BuscarStatusCobranca
        
        1. Formato dos dados retornados:
         - Codigo(Integer):Código do status de cobrança
         - Descricao(String):Descrição do status de cobrança
        
        Endpoint: `/api/v{version}/Venda/BuscarStatusCobranca`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista de status de cobrança ativos.
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
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
            >>> api = Venda()
            >>> response = api._buscar_status_cobranca(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarStatusCobranca"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_resumo_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Obtêm informações referentes a venda consultada.
        
        Endpoint: `/api/v{version}/Venda/ConsultarResumoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar resumo da venda
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "numeroVenda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data do cálculo",
                                "type": "string"
                            },
                            "dataCorrecao": {
                                "format": "date-time",
                                "description": "Data da correção",
                                "type": "string"
                            },
                            "antecipar": {
                                "description": "Antecipar parcelas",
                                "type": "boolean"
                            },
                            "parcelas": {
                                "description": "Lista de parcelas para antecipação do resumo de venda",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ParcelasResumoVendaRequest"
                                }
                            },
                            "aplicarDescontoGeral": {
                                "description": "Aplicar desconto geral",
                                "type": "boolean"
                            },
                            "percentualDescontoGeral": {
                                "format": "double",
                                "description": "Percentual de desconto geral a ser aplicado",
                                "type": "number"
                            },
                            "aplicarDescontoAntecipacao": {
                                "description": "Aplicar desconto de antecipação",
                                "type": "boolean"
                            },
                            "descontoAntecipacao": {
                                "$ref": "#/definitions/UAUApi.Models.Venda.DescontoAntecipacaoResumoVendaRequest",
                                "description": "Dados do desconto de antecipação"
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
            >>> api = Venda()
            >>> response = api._consultar_resumo_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarResumoVenda"
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

    def gerar_venda_de_proposta(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Realiza venda de acordo com a proposta informada.
        1. Validações serão realizadas para efetuar a operação.
        2. Todas alterações informadas no request apenas afetarão a venda gerada.
        3. A opção de desconsiderar não titulares avalistas, serve para o caso onde queriam gravar uma venda sem titular avalista, que possa está configurado na proposta.
        4. Se informar o lista de não titulares, o sistema vai desconsiderar os da proposta e utilizar os informados no request.
        5. A lista de não titulares deve conter o código das pessoas no UAU.
        
        Endpoint: `/api/v{version}/Venda/GerarVendaDeProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Efetua a venda da proposta informada e retorna o Objeto Venda da mesma
        
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
                            "numeroProposta",
                            "atualizaDatasDaVenda"
                        ],
                        "type": "object",
                        "properties": {
                            "numeroProposta": {
                                "format": "int32",
                                "description": "Número da proposta que será transformada em venda",
                                "type": "integer"
                            },
                            "atualizaDatasDaVenda": {
                                "description": "Identifica se irá atualizar as datas da venda caso a proposta esteja com datas desatualizadas.\r\nTRUE - Irá atualizar as datas da venda\r\nFALSE - Não irá atualizar as datas da venda.",
                                "type": "boolean"
                            },
                            "dataVenda": {
                                "format": "date-time",
                                "description": "Indica para qual data irá atualizar as datas da venda caso a proposta esteja com datas desatualizadas MM-dd-yyyy.",
                                "type": "string"
                            },
                            "atualizaInicioPrimeiroJuros": {
                                "description": "Indica se a data de início do primeiro juros será alterada.",
                                "type": "boolean"
                            },
                            "atualizaInicioReajuste": {
                                "description": "Indica se a data de início do reajuste será alterada.",
                                "type": "boolean"
                            },
                            "atualizaInicioSegundoJuros": {
                                "description": "Indica se a data de início do segundo juros será alterada",
                                "type": "boolean"
                            },
                            "atualizaBaseResiduo": {
                                "description": "Indica se a data da base resíduo será alterada",
                                "type": "boolean"
                            },
                            "atualizaPlanoIndexador": {
                                "description": "Indica se a data dos planos indexadores serão alteradas",
                                "type": "boolean"
                            },
                            "dataPrimeiroJuros": {
                                "format": "date-time",
                                "description": "Indica para qual data irá atualizar a data de 1º Juros. yyyy-MM-dd",
                                "type": "string"
                            },
                            "dataSegundoJuros": {
                                "format": "date-time",
                                "description": "Indica para qual data irá atualizar a data de 2º Juros",
                                "type": "string"
                            },
                            "dataReajuste": {
                                "format": "date-time",
                                "description": "Indica para qual data irá atualizar a data de início de reajuste",
                                "type": "string"
                            },
                            "dataBaseResiduo": {
                                "format": "date-time",
                                "description": "Indica para qual data irá atualizar a data base de resíduo",
                                "type": "string"
                            },
                            "listaPlanoIndexador": {
                                "description": "Indicam quais planos indexadores terão as datas alteradas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.PlanoIndexadorRequest"
                                }
                            },
                            "desconsiderarNaoTitularesAvalista": {
                                "description": "Indica que sistema vai desconsiderar todos os não titulares avalistas da proposta para geração da venda, ou seja, vai deixar apenas os titulares.\r\nSe informar a lista de NãoTitulares essa opção se torna nula, visto que o sistema irá utilizar os não titulares da lista.",
                                "type": "boolean"
                            },
                            "diasProrrogacaoParcVencidas": {
                                "format": "int32",
                                "description": "Quantidade de dias que será adicionado a nova data de vencimento das parcelas vencidas.",
                                "type": "integer"
                            },
                            "usuarioCadVenda": {
                                "description": "Usuário que está tranformado a proposta de venda em venda.",
                                "type": "string"
                            },
                            "listaNaoTitularAvalista": {
                                "description": "Lista com os não titulares e avalista da venda, caso seja preenchida o sistema irá desconsiderar os cadastrados na proposta e colocar as pessoas informadas \r\ndessa lista na venda.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.NaoTitularAvalistaRequest"
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
            >>> api = Venda()
            >>> response = api._gerar_venda_de_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GerarVendaDeProposta"
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

    def buscar_tipos_de_parcelas(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Busca a lista de status de cobrança ativos do sistema:
         - URI + /api/v{version}/Venda/BuscarTiposDeParcelas
        
        1. Formato dos dados retornados:
         - Tipo(String):Código do tipo de parcela
         - Descricao(String):Descrição do tipo de parcela
        
        Endpoint: `/api/v{version}/Venda/BuscarTiposDeParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista de tipos de parcelas ativos
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
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
            >>> api = Venda()
            >>> response = api._buscar_tipos_de_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarTiposDeParcelas"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def finalizar_renegociacao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Possibilita finalizar determinada negociação.
        
        Endpoint: `/api/v{version}/Venda/FinalizarRenegociacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Finalizar uma negociação
        
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
                            "usuario_logado": {
                                "description": "Usuário que está realizando a ação",
                                "type": "string"
                            },
                            "parc_geradas_json": {
                                "description": "Tabela com as parcelas geradas na renegociação",
                                "type": "string"
                            },
                            "parcsel_reneg_json": {
                                "description": "Tabela com as parcelas selecionadas para a renegociação",
                                "type": "string"
                            },
                            "grupo_parcelas_json": {
                                "description": "Parametros dos grupos de parcelas utilizados(LogParc)",
                                "type": "string"
                            },
                            "valdesc_reneg": {
                                "format": "double",
                                "description": "Valor de desconto utilizado na renegociação",
                                "type": "number"
                            },
                            "valacresc_reneg": {
                                "format": "double",
                                "description": "Valor de acrescimo utilizado na renegociação",
                                "type": "number"
                            },
                            "val_reneg": {
                                "format": "double",
                                "description": "Valor renegociado",
                                "type": "number"
                            },
                            "pendentevalidar_alcada": {
                                "description": "Se está pendente a validação de alçada de desconto",
                                "type": "boolean"
                            },
                            "venda": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "obra": {
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "tabelaplano_idx_json": {
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
            >>> api = Venda()
            >>> response = api._finalizar_renegociacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/FinalizarRenegociacao"
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

    def gravar_ocorrencia_anexo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - Adiciona uma ou várias ocorrências vinculada de anexo de acordo com os parâmetros passados na requisição.
        
        Parâmetros da request
        1. Chave: Chave para consulta.
        2. Campos: 
            - Campos obrigatórios para a chave="Venda" (empresa, obra, venda, codigo ocorrencia, usuario). 
            - Campos obrigatórios para a chave="Parcela" (empresa, obra, venda, número parcela, número geral da parcela, tipo da parcela, codigo ocorrência, usuario)
        
        Endpoint: `/api/v{version}/Venda/GravarOcorrenciaAnexo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Anexar uma ocorrência
        
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
                            "Ocorrencias"
                        ],
                        "type": "object",
                        "properties": {
                            "Ocorrencias": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.DadosAnexarOcorrencia"
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
            >>> api = Venda()
            >>> response = api._gravar_ocorrencia_anexo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GravarOcorrenciaAnexo"
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

    def alterar_data_prorrogacao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
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
                            "dados_prorrogacao"
                        ],
                        "type": "object",
                        "properties": {
                            "dados_prorrogacao": {
                                "$ref": "#/definitions/UAUApi.Models.Venda.DadosProrrogacao",
                                "description": "Dados da prorrogação"
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
            >>> api = Venda()
            >>> response = api._alterar_data_prorrogacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/AlterarDataProrrogacao"
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

    def buscar_parcelas_areceber(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Possibilita a busca de parcelas a receber na data atual.
        
        Endpoint: `/api/v{version}/Venda/BuscarParcelasAReceber`
        HTTP Method: `POST`
        
        Implementation Notes:
        Buscar parcelas a receber calculadas para a data atual
        
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
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra da venda",
                                "type": "string"
                            },
                            "num_ven": {
                                "format": "int32",
                                "description": "Nº da venda",
                                "type": "integer"
                            },
                            "data_calculo": {
                                "format": "date-time",
                                "description": "Data para calcular o valor das parcelas a receber",
                                "type": "string"
                            },
                            "valor_presente": {
                                "description": "Indica se irá calcular o valor das parcelas a receber a valor presente",
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
            >>> api = Venda()
            >>> response = api._buscar_parcelasa_receber(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarParcelasAReceber"
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

    def buscar_parametro_cobranca(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Busca a lista de parâmetros de cobrança ativos do sistema:
         - URI + /api/v{version}/Venda/BuscarParametroCobranca
        
        2. Formato dos dados retornados:
         - Banco     (String) : Número do banco
         - NomeBanco (String) : Nome do banco
         - Conta     (String) : Número da conta
         - Agencia   (String) : Código da agência do banco
         - Carteira  (String) : Código da carteira do convênio com banco
         - Codigo    (String) : Código do parâmetro de cobrança no sistema
         - Descricao (String) : Descrição do parâmetro de cobrança no sistema
         - Empresa   (String) : Código da empresa
         - Cedente   (String) : Código do cedente da remessa de cobrança
         
        Definição de negócio:
        1. Para buscar todos os padrões de cobrança ativos, usar null nos parâmetros da requisição ou não enviar os campos.
        
        Endpoint: `/api/v{version}/Venda/BuscarParametroCobranca`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista com parâmetros de cobranças
        
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
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa para filtrar parâmetros de cobrança (Não obrigatório)",
                                "type": "integer"
                            },
                            "banco": {
                                "format": "int32",
                                "description": "Número do banco para filtrar parâmetros de cobrança (Não obrigatório)",
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
            >>> api = Venda()
            >>> response = api._buscar_parametro_cobranca(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarParametroCobranca"
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

    def buscar_parcelas_recebidas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Possibilita buscar parcelas que foram recebidas.
        
        Endpoint: `/api/v{version}/Venda/BuscarParcelasRecebidas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Buscar parcelas recebidas da venda
        
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
                            "empresa",
                            "obra",
                            "num_ven"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra da venda",
                                "type": "string"
                            },
                            "num_ven": {
                                "format": "int32",
                                "description": "Nº da venda",
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
            >>> api = Venda()
            >>> response = api._buscar_parcelas_recebidas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarParcelasRecebidas"
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

    def buscar_status_de_escritura(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Busca a lista de Status de escritura ativos do sistema:
         - URI + /api/v{version}/Venda/BuscarStatusDeEscritura
        
        1. Formato dos dados retornados:
         - Codigo(Integer):Código de Status de escritura
         - Descricao(String):Descrição do Status de escritura
        
        Endpoint: `/api/v{version}/Venda/BuscarStatusDeEscritura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista de Status de escritura ativos.
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
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
            >>> api = Venda()
            >>> response = api._buscar_status_de_escritura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarStatusDeEscritura"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_parcelas_da_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite consultar as parcelas de uma venda.
        1. Ao enviar somenteParcelasAptasBoleto como TRUE, irá validar se a venda possui bloqueio ou manutenção pendente e se a empresa está configurada
        para "Não permitir enviar para banco parcelas com status [em banco]"
            - Caso a venda possua bloqueio ou esteja em manutenção, não irá retornar nenhuma parcela da venda.
            - Caso esteja configurado para não enviar parcelas com status em banco, não irá retornar as parcelas que já tenham boletos gerados.
        
        Endpoint: `/api/v{version}/Venda/ConsultarParcelasDaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar parcelas da venda calculadas para a data informada
        
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
                            "empresa",
                            "obra",
                            "num_venda",
                            "data_calculo",
                            "boleto_antecipado"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "num_venda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "data_calculo": {
                                "format": "date-time",
                                "description": "Data de cálculo",
                                "type": "string"
                            },
                            "boleto_antecipado": {
                                "description": "Indica se irá realizar cálculo de antecipação nas parcelas",
                                "type": "boolean"
                            },
                            "somenteParcelasAptasBoleto": {
                                "description": "Retornar somente parcelas aptas para gerar boleto.",
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
            >>> api = Venda()
            >>> response = api._consultar_parcelas_da_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarParcelasDaVenda"
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

    def gerar_pdfevolucao_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.
        
        Definição de Negócio:
        Gera PDF da evolução do contrato em string do tipo Base64.
        1. Validações a nível de usuário.
        
        Endpoint: `/api/v{version}/Venda/GerarPDFEvolucaoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar PDF do relatório da evolução do contrato
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Codigo da empresa da venda",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Codigo da obra da venda",
                                "type": "string"
                            },
                            "numeroVenda": {
                                "format": "int32",
                                "description": "Numero da venda",
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
            >>> api = Venda()
            >>> response = api._gerarpdf_evolucao_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GerarPDFEvolucaoContrato"
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

    def buscar_recebimentos_da_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Permite consultar os reecebimentos de uma venda, ou seja, o que já foi recebido.
        2. Caso o campo "parcelasnao_conciliadas" esteja marcado como "true" as parcelas não conciliadas também serão retornadas.
        
        Endpoint: `/api/v{version}/Venda/BuscarRecebimentosDaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os recebimentos de uma venda
        
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
                            "empresa",
                            "obra",
                            "venda"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "venda": {
                                "format": "int32",
                                "description": "Código da venda",
                                "type": "integer"
                            },
                            "parcelasnao_conciliadas": {
                                "description": "Parcelas NÃO conciliadas: (\"true\": aceita, \"false\": recusa)",
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
            >>> api = Venda()
            >>> response = api._buscar_recebimentos_da_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarRecebimentosDaVenda"
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

    def exportar_pessoas_da_venda_xml(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Possibilita acesso às pessoas que estão relacionadas com a venda informada.
        1. Valida a existência da venda.
        
        Endpoint: `/api/v{version}/Venda/ExportarPessoasDaVendaXml`
        HTTP Method: `POST`
        
        Implementation Notes:
        Busca as pessoas vinculadas às vendas informadas
        
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
                            "lista_vendas": {
                                "description": "Lista com as vendas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ChavesVendas"
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
            >>> api = Venda()
            >>> response = api._exportar_pessoas_da_venda_xml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ExportarPessoasDaVendaXml"
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

    def gravar_pedido_de_recebimento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. É obrigatório ter o ambiente de integração com a PAYGO configurado, só após o registro junto a eles que o registro será gerado no UAU.
        2. É necessário ter permissão de inclusão no programa VEPEDIDORECEBIMENTO
        
        Endpoint: `/api/v{version}/Venda/GravarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gravar pedido de recebimento junto a NTK
        
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
                            "Empresa",
                            "Obra",
                            "NumContrato",
                            "Estabelecimento",
                            "FormaPgto",
                            "QtdeParcelas",
                            "DataCalculo",
                            "TipoRecebimento",
                            "Antecipacao",
                            "Parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empesa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "NumContrato": {
                                "format": "int32",
                                "description": "Número da venda ou da proposta de venda",
                                "type": "integer"
                            },
                            "Estabelecimento": {
                                "description": "Número do estabelecimento",
                                "type": "string"
                            },
                            "FormaPgto": {
                                "format": "int32",
                                "description": "Forma de pagamento (0 - Débito, 1 - Crédito a vista, 2 - Crédito sem juros)",
                                "type": "integer"
                            },
                            "QtdeParcelas": {
                                "format": "int32",
                                "description": "Quantidade de parcelas que será realizado o recebimento. Para forma de pagamento\r\nDébito e Crédito a vista, a quantidade de parcelas dever ser = 1.",
                                "type": "integer"
                            },
                            "DataCalculo": {
                                "format": "date-time",
                                "description": "Data de cálculo para reajuste das parcelas",
                                "type": "string"
                            },
                            "ValorLiquido": {
                                "format": "double",
                                "description": "Valor total do pedido. Deverá ser informado somente quando o tipo de recebimento for\r\n1 - Parte das parcelas",
                                "type": "number"
                            },
                            "TipoRecebimento": {
                                "format": "int32",
                                "description": "Tipo de recebimento: todas as parcelas, parte das parcelas,\r\n0 - Realizar o pedido de recebimento total das parcelas\r\n1 - Realizar o pedido de recebimento de parte das parcelas",
                                "type": "integer"
                            },
                            "Antecipacao": {
                                "description": "Indica se está antecipando as parcelas\r\nTrue - Está antecipando\r\nFalse - Não está antecipando",
                                "type": "boolean"
                            },
                            "Parcelas": {
                                "description": "Lista de objeto (Parcelas) com as parcelas que será realizada o inserção do pedido de recebimento junto a NTK.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ParcelasPedido"
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
            >>> api = Venda()
            >>> response = api._gravar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GravarPedidoDeRecebimento"
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

    def importacao_venda_com_retorno(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Número máximo de importações por vez: 50.
        
        Definição de Negócio:
        Possibilita importa vendas via XML para o UAU e receber como retorno as vendas importadas.
        1. Valida quantidade de importações por requisição.
        2. Caso ocorra erro em uma venda, todas as outras importações são canceladas e terá um retorno com informações da venda que falhou.
        
        Endpoint: `/api/v{version}/Venda/ImportacaoVendaComRetorno`
        HTTP Method: `POST`
        
        Implementation Notes:
        Importar vendas para o UAU via XML com retorno de venda importada
        
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
                            "xml_vendas",
                            "alterarnumerodas_vendas"
                        ],
                        "type": "object",
                        "properties": {
                            "xml_vendas": {
                                "description": "XML de importação das vendas",
                                "type": "string"
                            },
                            "alterarnumerodas_vendas": {
                                "description": "Gerar novo número para as vendas importadas.\r\nTrue\r\nFalse",
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
            >>> api = Venda()
            >>> response = api._importacao_venda_com_retorno(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ImportacaoVendaComRetorno"
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

    def manter_status_cobranca_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Possibilita alterar o status de cobrança referentes a determinada venda.
        Validações serão realizadas para efetuar a operação:
        1. Se os parâmetros forem da parcela, o ocorrência será gravada na parcela correspondente.
        2. Se os parâmetros forem da venda, o ocorrência será gravada na venda correspondente.
        3. Caso seja informado o parâmetro numeroParcela, numeroParcelaGeral ou tipoParcela, os três serão obrigatórios.
        4. O parâmetro 'código' deverá ser do tipo numérico.
        5. Os status de cobrança da venda ou parcela, serão substituídos pelos status informados.
        
        Endpoint: `/api/v{version}/Venda/ManterStatusCobrancaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar status de cobrança da venda
        
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
                            "empresa",
                            "obra",
                            "venda"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "venda": {
                                "format": "int32",
                                "description": "Número da venda.",
                                "type": "integer"
                            },
                            "numeroParcela": {
                                "format": "int32",
                                "description": "Número da parcela da venda.",
                                "type": "integer"
                            },
                            "numeroParcelaGeral": {
                                "format": "int32",
                                "description": "Número da parcela geral.",
                                "type": "integer"
                            },
                            "tipoParcela": {
                                "description": "Tipo da parcela.",
                                "type": "string"
                            },
                            "statusCobranca": {
                                "description": "Código de status de cobrança da venda. (Lista de objeto de códigos)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.CodigoStatus"
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
            >>> api = Venda()
            >>> response = api._manter_status_cobranca_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ManterStatusCobrancaVenda"
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

    def venda_valida_para_manutencao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Valida a possibilidade de realizar a renegociação da venda, para tal tarefa a venda não pode ter restrições.
        1. Os campos inseridos na request serão utilizado para buscar e verificar disponibilidade de renegociação.
        
        Endpoint: `/api/v{version}/Venda/VendaValidaParaManutencao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Valida se a venda pode ser renegociada pela tela de renegociação na Web.
        
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
                            "empresa",
                            "obra",
                            "venda",
                            "usr_logado"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "venda": {
                                "format": "int32",
                                "description": "Código da venda",
                                "type": "integer"
                            },
                            "usr_logado": {
                                "description": "Usuário logado",
                                "type": "string"
                            },
                            "mensagem_securitizacao": {
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
            >>> api = Venda()
            >>> response = api._venda_valida_para_manutencao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/VendaValidaParaManutencao"
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

    def consultar_contas_receber_calc(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Possibilita Consultar as parcelas de contas a receber já calculadas com retorno a lista de parcelas.
        2. Nenhuma propriedade é obrigatória, porém é obrigatório ser enviado pelo menos um tipo de filtro para consultar os dados.
        3. Na propriedade vendas, é obrigatório apenas o parâmetro empresa.
        4. É indispensável que o PROUAU esteja rodando diariamente o cálculo de parcelas para que os resultados estejam sempre corretos.
        5. O Filtro de período filtrará pela data de vencimento da parcela.
        6. O filtro por tipo de parcelas pode aceitar mais de um tipo, é obrigatório colocar entre aspas simples cada código de parcela e separadas por virgula. Ex.: 'P', 'M'
        
        Endpoint: `/api/v{version}/Venda/ConsultarContasReceberCalc`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta de parcelas de contas a receber já calculadas
        
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
                            "DataInicio": {
                                "format": "date-time",
                                "description": "Data de Inicio - Para filtrar por data de vencimento.",
                                "type": "string"
                            },
                            "DataFim": {
                                "format": "date-time",
                                "description": "Data Final - Para filtrar por data de vencimento.",
                                "type": "string"
                            },
                            "TiposParcela": {
                                "description": "Código do tipo da parcela. Ex.: 'P', 'M'",
                                "type": "string"
                            },
                            "Vendas": {
                                "description": "Lista com as chaves das vendas (Venda, Obra, Empresa)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.VendasContasReceberCalcRequest"
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
            >>> api = Venda()
            >>> response = api._consultar_contas_receber_calc(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarContasReceberCalc"
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

    def importacao_parcelas_de_custas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Importação de parcelas do tipo Custas:
         - URI + /api/v{version}/Venda/ImportacaoParcelasDeCustas
        
        Definição de Negócio:
        1. Permite importar parcelas do tipo Custas com as seguintes regras:
         - Os campos: Observacao, CobrarJurosAtraso, CobrarMulta, CobrarCorrecao, CobrarImposto, CobrarTxAdm, CobrarRepasseLocador, Competencia, NUMEROPARCELA e MeioPreferencialDeRecebimento são opcionais.
        
        1. Referente a propriedade de CAPs:
          - Caso não sejam informados os CAPs para uma ou mais parcelas de custas, para essas parcelas, será utilizada a configuração padrão de CAPs da empresa;
          - Será possível utilizar em uma mesma requisição parcelas com CAPs definidos no JSON e parcelas com CAPs padrão da empresa (não informado no JSON);
          - Será validada a existência dos CAPs informado e só será possível utilizar CAPs ativos;
          - Caso seja informado um CAP para uma determinada parcela, todos os demais CAPs daquela parcela, serão obrigatórios;
          
        Anexos:
        1. Link para download de exemplos:
        - Exemplo de parcela tipo Custa: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcelas-de-Custas.postman_collection.zip
        
        Endpoint: `/api/v{version}/Venda/ImportacaoParcelasDeCustas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Importar parcelas do tipo Custa
        
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
                            "custas"
                        ],
                        "type": "object",
                        "properties": {
                            "custas": {
                                "description": "Lista de custas.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.CustaRequest"
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
            >>> api = Venda()
            >>> response = api._importacao_parcelas_de_custas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ImportacaoParcelasDeCustas"
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

    def buscar_campanha_desconto_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método
        
        Definição de Negócio:
        Permite renegociar parcelas de uma venda
        1. O usuário deverá estar autenticado e validado
        2. Informar os dados da venda
        3. Informar as parcelas a serem geradas
        4. Informar as parcelas escolhidas para renegociação
        5. Informar o plano de indexação
        6. Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
           retorna mensagem informando a inconsistência encontrada para que seja analisada
        7. Após as validações realiza a renegociação das parcelas
        8. Será registrado comentário na venda sobre a renegociação realizada
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
        
         Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
        - Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso
        
        Endpoint: `/api/v{version}/Venda/BuscarCampanhaDescontoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Buscar a campanha de desconto disponível para uma campanha
        
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
                            "Empresa",
                            "Obra",
                            "Venda",
                            "DataCalculo"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Venda": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "DataCalculo": {
                                "format": "date-time",
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
            >>> api = Venda()
            >>> response = api._buscar_campanha_desconto_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/BuscarCampanhaDescontoVenda"
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

    def cancelar_pedido_de_recebimento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Pedidos que já tiveram um recebimento parcial junto a NTK, não são cancelados. (trava na NTK).
        2. É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO
        
        Endpoint: `/api/v{version}/Venda/CancelarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Cancelar o pedido de recebimento junto a NTK
        
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
                            "Empresa",
                            "Obra",
                            "Pedido"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empesa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "Pedido": {
                                "format": "int32",
                                "description": "Número do pedido da NTK",
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
            >>> api = Venda()
            >>> response = api._cancelar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/CancelarPedidoDeRecebimento"
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

    def atualizar_pedido_de_recebimento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
        2. Valida usuário e permissões
        3. Valida outras informações passadas no request
        
        Endpoint: `/api/v{version}/Venda/AtualizarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar o(s) pedido(s) de recebimento junto a NTK
        
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
                            "Empresa",
                            "Obra",
                            "Pedido"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empesa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "Pedido": {
                                "format": "int32",
                                "description": "Número do pedido da NTK",
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
            >>> api = Venda()
            >>> response = api._atualizar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/AtualizarPedidoDeRecebimento"
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

    def consultar_pedido_de_recebimento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Possibilita consultar pedido de recebimento junto a NTK
        2. As informações retornadas serão informações do pedido na NTK.
        3. É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO
        
        Endpoint: `/api/v{version}/Venda/ConsultarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar o pedido de recebimento junto a NTK
        
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
                            "Empresa",
                            "Obra",
                            "Pedido"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empesa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "Pedido": {
                                "format": "int32",
                                "description": "Número do pedido da NTK",
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
            >>> api = Venda()
            >>> response = api._consultar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarPedidoDeRecebimento"
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

    def processar_recebimento_parcelas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Responsável por processar recebimentos de parcelas com os dados de recebimento e forma de pagamento.
        1. A origem do recebimento das parcelas DEVE sempre ser 0.
        2. Serão realizadas várias validações para realização da requisição.
        3. O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.
        
        Endpoint: `/api/v{version}/Venda/ProcessarRecebimentoParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Processa o recebimento de parcelas realizados por outros sistemas
        
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
                            "recebimento",
                            "formaPagamento"
                        ],
                        "type": "object",
                        "properties": {
                            "recebimento": {
                                "$ref": "#/definitions/UAUApi.Models.Venda.DTORecebimentoSimplificado",
                                "description": "Dados do recebimento"
                            },
                            "formaPagamento": {
                                "$ref": "#/definitions/UAUApi.Models.Venda.DTOFormaPagamento",
                                "description": "Dados do pagamento"
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
            >>> api = Venda()
            >>> response = api._processar_recebimento_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ProcessarRecebimentoParcelas"
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

    def manter_status_escrituracao_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Valida usuário e suas permissões
        
        Endpoint: `/api/v{version}/Venda/ManterStatusEscrituracaoVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar status da escrituração da venda
        
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
                            "empresa",
                            "obra",
                            "venda"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "venda": {
                                "format": "int32",
                                "description": "Número da venda.",
                                "type": "integer"
                            },
                            "statusEscrituracao": {
                                "description": "Código de status de escrituração da venda. (Lista de objeto de códigos)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.CodigoStatus"
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
            >>> api = Venda()
            >>> response = api._manter_status_escrituracao_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ManterStatusEscrituracaoVenda"
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

    def retorna_chaves_vendas_por_periodo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.   
        3. Formatação das chaves de resposta:
                "Empresa-Obra/Venda, Empresa-Obra/Venda, Empresa-Obra/Venda"
                "01705-B1705/00159,01705-B1705/00160,01705-B1705/00161"
        
        Definição de Negócio:
        1. Permite consultar as chaves das vendas que foram inseridas, tiveram manutenção ou foram quitadas no período informado.
        2. Se o campo "status_escrituracao" do request for marcado como "true" serão retonadas as chaves que tiveram alterações no status de escrituração.
        3. Parâmetro opcional para request: statusVenda.  0 - Normal, 1 - Cancelada, 3 - Quitado, 4 - Em acerto, 5 Aluguel antecipado.
        4. Parâmetros opcionais para request: codigoEmpresa e codigoObra.
        
        Endpoint: `/api/v{version}/Venda/RetornaChavesVendasPorPeriodo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta as chaves das vendas e comentários de status de escrituração de acordo com o período informado
        
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
                            "data_inicio": {
                                "format": "date-time",
                                "description": "Data inicial",
                                "type": "string"
                            },
                            "data_fim": {
                                "format": "date-time",
                                "description": "Data final",
                                "type": "string"
                            },
                            "status_escrituracao": {
                                "description": "Status escrituração com alterações (\"true\": aceita, \"false\": rejeita)",
                                "type": "boolean"
                            },
                            "statusVenda": {
                                "description": "Status da venda  0 - Normal, 1 - Cancelada, 3 - Quitado, 4 - Em acerto, 5 Aluguel antecipado.",
                                "type": "string"
                            },
                            "listaEmpresaObra": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.EmpresaObra"
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
            >>> api = Venda()
            >>> response = api._retorna_chaves_vendas_por_periodo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/RetornaChavesVendasPorPeriodo"
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

    def consultar_demonstrativo_correcao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite consultar demonstrativo de correção da parcela da venda.
        1. Valida usuário e suas permissões.
        2. Valida existência da venda.
        3. Valida existência das parcelas.
        
        Endpoint: `/api/v{version}/Venda/ConsultarDemonstrativoCorrecao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar demonstrativo de correção da parcela da venda
        
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
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra",
                                "type": "string"
                            },
                            "venda": {
                                "format": "int32",
                                "description": "Numero da venda",
                                "type": "integer"
                            },
                            "numeroParcela": {
                                "format": "int32",
                                "description": "Numero da parcela",
                                "type": "integer"
                            },
                            "numeroParcelaGeral": {
                                "format": "int32",
                                "description": "Numero geral da parcela",
                                "type": "integer"
                            },
                            "tipoParcela": {
                                "description": "Tipo da parcela",
                                "type": "string"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data de calculo do resumo de venda",
                                "type": "string"
                            },
                            "dataCorrecao": {
                                "format": "date-time",
                                "description": "Data da correção do resumo de venda",
                                "type": "string"
                            },
                            "valorAntecipado": {
                                "description": "Calcular com valor antecipado\r\nTrue - Sim\r\nFalse - Não",
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
            >>> api = Venda()
            >>> response = api._consultar_demonstrativo_correcao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarDemonstrativoCorrecao"
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

    def consultar_plano_indexadores_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Retorna informações pertinentes ao plano indexador da venda.
        
        Endpoint: `/api/v{version}/Venda/ConsultarPlanoIndexadoresVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta o plano indexador da venda
        
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
                            "empresa",
                            "obra",
                            "venda"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "venda": {
                                "format": "int32",
                                "description": "Número da venda",
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
            >>> api = Venda()
            >>> response = api._consultar_plano_indexadores_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarPlanoIndexadoresVenda"
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

    def gravar_num_contrato_financiamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - Altera número de contrato para uma venda.
        
        Pré requisito:
        - Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
            - URL + /api/v{version}/Venda/GravarNumContratoFinanciamento 
        Anexos:
        - Exemplo Postman: [ALTERAR EXEMPLO]
        
        Endpoint: `/api/v{version}/Venda/GravarNumContratoFinanciamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Altera numero de contrato da venda
        
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
                            "codgEmpresa",
                            "codgObra",
                            "numVenda",
                            "codgUsuario",
                            "numContrato"
                        ],
                        "type": "object",
                        "properties": {
                            "codgEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "codgObra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "numVenda": {
                                "format": "double",
                                "description": "Código da venda",
                                "type": "number"
                            },
                            "codgUsuario": {
                                "description": "Usuário do sistema",
                                "type": "string"
                            },
                            "numContrato": {
                                "description": "Número do contrato",
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
            >>> api = Venda()
            >>> response = api._gravar_num_contrato_financiamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GravarNumContratoFinanciamento"
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

    def consultar_empreendimentos_cliente(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Consulta os empreendimento que o cliente possui e está com situação em aberto.
        
        Endpoint: `/api/v{version}/Venda/ConsultarEmpreendimentosCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os empreendimentos que o cliente possui contrato em aberto
        
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
                            "codigo_usuario": {
                                "format": "int32",
                                "description": "Código do cliente do cadastro de pessoas",
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
            >>> api = Venda()
            >>> response = api._consultar_empreendimentos_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarEmpreendimentosCliente"
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

    def consultar_pedido_de_recebimento_uau(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        1. Possibilita consultar pedido de recebimento registrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
        2. As informações retornadas são referentes a como o UAU registrou o pedido internamente.
        3. É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO
        
        Endpoint: `/api/v{version}/Venda/ConsultarPedidoDeRecebimentoUAU`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar o pedido de recebimento no UAU
        
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
                            "NumeroNTK": {
                                "format": "int32",
                                "description": "Número do pedido na NTK",
                                "type": "integer"
                            },
                            "NumeroPedido": {
                                "format": "int32",
                                "description": "Número do pedido UAU",
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
            >>> api = Venda()
            >>> response = api._consultar_pedido_de_recebimentouau(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarPedidoDeRecebimentoUAU"
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

    def consultar_unidades_compradas_por_cpf(
        self,
        version: str,
        dados: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ
        1. Valida se o usuário está autenticado (logado) no sitema.
        2. Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.
        
        Endpoint: `/api/v{version}/Venda/ConsultarUnidadesCompradasPorCPF`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta unidades compradas pelo número de CPF
        
        Args:
            dados (Dict[str, Any]): The dados
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "dados": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "CpfCnpj": {
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
            >>> api = Venda()
            >>> response = api._consultar_unidades_compradas_porcpf(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarUnidadesCompradasPorCPF"
        kwargs = {
            "dados": dados,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_status_cobranca_ativa(
        self,
        codigo: Optional[str] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            codigo (Dict[str, Any]): The codigo
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "codigo": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "api-version": {
                    "type": "string",
                    "in": "query",
                    "required": false,
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
            >>> api = Venda()
            >>> response = api._consultar_status_cobranca_ativa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Venda/ConsultarStatusCobrancaAtiva"
        kwargs = {
            "codigo": codigo,
            "api-version": api_version,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def calcular_desconto_campanha_antecipacao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método
        
        Definição de Negócio:
        Permite renegociar parcelas de uma venda
        1. O usuário deverá estar autenticado e validado
        2. Informar os dados da venda
        3. Informar as parcelas a serem geradas
        4. Informar as parcelas escolhidas para renegociação
        5. Informar o plano de indexação
        6. Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
           retorna mensagem informando a inconsistência encontrada para que seja analisada
        7. Após as validações realiza a renegociação das parcelas
        8. Será registrado comentário na venda sobre a renegociação realizada
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
        
         Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
        - Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso
        
        Endpoint: `/api/v{version}/Venda/CalcularDescontoCampanhaAntecipacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Buscar a campanha de desconto disponível para uma campanha
        
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
                            "CampanhaDeDesconto": {
                                "$ref": "#/definitions/UAUApi.Models.CalcularDesconto.CampanhaVenda"
                            },
                            "ParcelasCalculadas": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.CalcularDesconto.ParcelaCalculadaCampanha"
                                }
                            },
                            "DataCalculo": {
                                "format": "date-time",
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
            >>> api = Venda()
            >>> response = api._calcular_desconto_campanha_antecipacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/CalcularDescontoCampanhaAntecipacao"
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

    def consultar_campanha_desconto_disponivel(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Consulta a campanha de desconto disponível para utilização.
        1. Valida usuário logado e permissões
        
        Endpoint: `/api/v{version}/Venda/ConsultarCampanhaDescontoDisponivel`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar campanha de desconto disponível para a venda
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa da venda",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da obra da venda",
                                "type": "string"
                            },
                            "numeroVenda": {
                                "format": "int32",
                                "description": "Numero da venda",
                                "type": "integer"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data do calculo da campanha da venda",
                                "type": "string"
                            },
                            "dataCorrecao": {
                                "format": "date-time",
                                "description": "Data de correção das parcelas",
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
            >>> api = Venda()
            >>> response = api._consultar_campanha_desconto_disponivel(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarCampanhaDescontoDisponivel"
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

    def consultar_desconto_antecipacao_parcela(
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
        Consulta o valor do desconto caso a parcela seja paga antecipadamente.
        
        Endpoint: `/api/v{version}/Venda/ConsultarDescontoAntecipacaoParcela`
        HTTP Method: `POST`
        
        Implementation Notes:
        Calcular desconto por antecipação da parcela
        
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
                            "empresa",
                            "obra",
                            "num_venda"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "num_venda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "num_parc": {
                                "format": "int32",
                                "description": "Número da parcela",
                                "type": "integer"
                            },
                            "numparc_ger": {
                                "format": "int32",
                                "description": "Número geral da parcela",
                                "type": "integer"
                            },
                            "tipo_parc": {
                                "description": "Tipo da parcela",
                                "type": "string"
                            },
                            "data_calculo": {
                                "format": "date-time",
                                "description": "Data de cálculo",
                                "type": "string"
                            },
                            "valor_parcela": {
                                "format": "double",
                                "description": "Valor da parcela corrigido",
                                "type": "number"
                            },
                            "data_vencimento": {
                                "format": "date-time",
                                "description": "Data de vencimento da parcela",
                                "type": "string"
                            },
                            "data_prorrogacao": {
                                "format": "date-time",
                                "description": "Data de prorrogação da parcela",
                                "type": "string"
                            },
                            "totalparcelas_sel": {
                                "format": "int32",
                                "description": "Total de parcelas selecionadas",
                                "type": "integer"
                            },
                            "antecipado": {
                                "description": "Se o campo for verdadeiro (true), a data de cálculo informada na requisição será considerada para calcular o desconto. Caso contrário (false), será considerada a data de prorrogação.",
                                "type": "boolean"
                            },
                            "totalpara_quitacao": {
                                "format": "int32",
                                "description": "Total de parcelas para quitação",
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
            >>> api = Venda()
            >>> response = api._consultar_desconto_antecipacao_parcela(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarDescontoAntecipacaoParcela"
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

    def consultar_unidades_compradas_usr_logado(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Possibilita consultar unidades que foram compradas por determinado usuário.
        1. Valida se o usuário está autenticado (logado) no sitema.
        2. Usuário só pode ser do tipo pessoa.
        3. Valida se o usuário está cadastrado para acesso no UAUWeb.
        
        Endpoint: `/api/v{version}/Venda/ConsultarUnidadesCompradasUsrLogado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta unidades compradas pelo usuário que está logado
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
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
            >>> api = Venda()
            >>> response = api._consultar_unidades_compradas_usr_logado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarUnidadesCompradasUsrLogado"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_unidades_compradas_por_cpfcnpj(
        self,
        version: str,
        dados: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ
        1. Valida se o usuário está autenticado (logado) no sitema.
        2. Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.
        
        Endpoint: `/api/v{version}/Venda/ConsultarUnidadesCompradasPorCPFCNPJ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta unidades compradas pelo número de CPF ou CNPJ
        
        Args:
            dados (Dict[str, Any]): The dados
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "dados": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "CpfCnpj": {
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
            >>> api = Venda()
            >>> response = api._consultar_unidades_compradas_porcpfcnpj(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/ConsultarUnidadesCompradasPorCPFCNPJ"
        kwargs = {
            "dados": dados,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def gerar_pdfevolucao_saldo_devedor_financiamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.
        
        Definição de Negócio:
        Gerar PDF do relatório de evolução do saldo devedor do financiamento imobiliário da venda em formato Base64.
        
        Endpoint: `/api/v{version}/Venda/GerarPDFEvolucaoSaldoDevedorFinanciamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar PDF do relatório de evolução do saldo devedor do financiamento imobiliário
        
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
                            "codigoEmpresa",
                            "codigoObra",
                            "numeroVenda",
                            "tipoRelatorio"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa da venda",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da obra da venda",
                                "type": "string"
                            },
                            "numeroVenda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "tipoRelatorio": {
                                "format": "int32",
                                "description": "Tipo do relatório a ser gerado.<br />\r\n0 - Relatório Detalhado.<br />\r\n1 - Relatório Simplificado. <br />",
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
            >>> api = Venda()
            >>> response = api._gerarpdf_evolucao_saldo_devedor_financiamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Venda/GerarPDFEvolucaoSaldoDevedorFinanciamento"
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

