from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Proposta:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_boleto(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         3. Retorna string do tipo Base64. Para obter o boleto utilize um conversor: Base64 para PDF.
         
         Definição de Negócio:
         1. Gera boleto com os dados informados na request.
         2. O usuário autenticado deve ter permissão de inclusão no programa de permissão VEBOLETOAVULSO.
         3. Para gerar boleto parcial é necessário informar a propriedade ValorBoleto.
             - Não pode ser um valor negativo nem inferior a 0,01 centavo.
             - Se informar um valor igual ao valor total das parcelas enviadas, será gerado um boleto normal.
             - Se informar um valor menor que o valor total da parcela enviada, será gerado um boleto parcial.
                 - Apenas uma parcela das enviadas deverá ser parcial
                 - Não será gerado boleto caso informe um valor que não cubra todas as parcelas enviadas
                 - Irá validar se as parcelas enviadas podem gerar o boleto parcial de acordo com a regra de dias para vencimento.
             - Será possível gerar boleto parcial somente para parcelas de uma única empresa, obra e proposta.
             - Só é possível gerar boleto parcial para mais de uma parcela quando for antecipação.
             - É obrigatório reajustar ao gerar o boleto parcial.
         4. Padrão de cobrança    
             - Não é obrigatório informá-lo.
             - Caso informado, o sistema irá desconsiderar a configuração do parâmetro usarpadraoboleto_avulso e irá gerar o boleto pelo padrão informado.
             - Caso informado, será desconsiderado o padrão de cobrança de todas as parcelas, incluindo custas administrativas, e boleto será gerado com o padrão de cobrança informado.
             - Apenas os padrões de cobrança ativos serão aceitos.
             - Será possivel gerar boleto com o padrão de informado somente para parcelas de uma única empresa.
         5. Excluir Boletos Existentes
             - Não é obrigatório informar o parâmetro ExcluirBoletosExistentes.
             - Caso não seja informado será mantido a opção padrão de não excluir.
             - Caso informado, irá executar as mesmas ações que a configuração 'Excluir boletos já emitidos ao gerar um novo boleto para a parcela' no cadastro de empresas &gt; config. vendas.
        
        Endpoint: `/api/v{version}/Proposta/GerarBoleto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar boleto
        
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
                            "datacalculo"
                        ],
                        "type": "object",
                        "properties": {
                            "parcelas": {
                                "description": "lista de objeto com as parcelas da proposta que serão geradas o boleto / carne e valor do desconto se existir",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.ParcelasBoleto"
                                }
                            },
                            "datacalculo": {
                                "format": "date-time",
                                "description": "Data para o calculo e vencimento do boleto",
                                "type": "string"
                            },
                            "antecipar": {
                                "description": "Se o cálculo das parcelas será antecipado\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "reajustar": {
                                "description": "Se é para reajustar os valores\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "excluirboletoexpirado": {
                                "description": "Se é para excluir os boletos expirados\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "formacobranca": {
                                "format": "int32",
                                "description": "Tipo de geração: 0 - Boleto, 1 - Carnê",
                                "enum": [
                                    0,
                                    1
                                ],
                                "type": "integer"
                            },
                            "boletosacadodetalhado": {
                                "description": "Se o boleto sacado será detalhado \r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "carnetresvias": {
                                "description": "Se o carne será em três vias\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "validardadospendentes": {
                                "description": "Se não deve validar os dados pendentes de preenchimento do endereço do cliente. \r\nFalse - Não irá travar a geração do boleto, caso os dados do endereço do cliente estejam incompletos.\r\nTrue - Irá travar a geração do boleto, caso os dados do endereço do cliente estejam incompletos.",
                                "type": "boolean"
                            },
                            "acrescentarresiduo": {
                                "description": "Se vai acrescentar o valor de resíduo ou não\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "usarpadraoboletoavulso": {
                                "description": "Indica qual o padrão de cobrança será utilizado    \r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "agruparparcelas": {
                                "description": "Se deve agrupar as parcelas enviadas para gerar o boleto\r\nTRUE - Sim\r\nFALSE - Não",
                                "type": "boolean"
                            },
                            "ValorBoleto": {
                                "format": "double",
                                "description": "Valor do boleto, utilizado para geração de boletos parciais.",
                                "type": "number"
                            },
                            "PadraoCobranca": {
                                "format": "int32",
                                "description": "Nr. do padrão para cobrança",
                                "type": "integer"
                            },
                            "ExcluirBoletosExistentes": {
                                "description": "Se irá excluir boletos já emitidos ao gerar um novo boleto para a parcela",
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
            >>> api = Proposta()
            >>> response = api._gerar_boleto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/GerarBoleto"
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

    def expirar_boletos(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Exclui todos os boletos expirados, propostas e vendas, de acordo com a configuração da empresa.
        
        Endpoint: `/api/v{version}/Proposta/ExpirarBoletos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir boletos expirados de proposta e venda
        
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
            >>> api = Proposta()
            >>> response = api._expirar_boletos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/ExpirarBoletos"
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

    def gravar_proposta(
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
         1. O usuário autenticado deve ter permissão de inclusão e alteração em CRPROPOSTAVENDA.
             - Se não precisar de alterar propostas, basta ter apenas de inclusão.
         2. A alteração de uma proposta é feita respeitando todas informações enviadas, ou seja, deve reeniviar o mesmo objeto da proposta totalmente para alterar apenas 1 campo por exemplo.
             - O sistema identifica que é uma alteração de proposta quando o código da proposta está preenchido [numProposta].
         3. A propriedade de propostaPacelasGeradas, Não precisa ser preenchida pois suas informações serão regeradas pela API.
         4. As validações de propriedades obrigatórias podem validar para o tipo de proposta que está sendo recebido.
             - Os campos marcados como obrigatórios são os campos obrigatórios gerais, para gravar o básico de uma proposta de venda.
                 - Aluguel, aluguel garantido e aluguel shopping, tem mais propriedades obrigatórias ou até mesmo opcionais.
         6. Mais informações sobre as propriedades e como elas devem ser preenchidas estão na documentação dos models.
         7. Tornou-se obsoleto ó código da hierarquia, agora pelo numeroComissao(modelo) nos iremos achar a hierarquia e validar.
         8. O cálculo da comissão é feito da seguinte forma.
         9. Ao informar a propriedade percentualSegundoJuros ou a propriedade dataSegundoJuros, ambas serão obrigatórias em propostaParamParcelas e propostaParamModeloParcelas.
         10. O parâmetro opcional TermoReserva, quando preenchido, precisa ter o valor 0 ou 1. (0-Não, 1-Sim).
         11. Os parâmetros opcionais ValorCurtoPrazo e ValorLongoPrazo, se não preenchidos, serão calculados automaticamente.
             - O valor de provisão de venda curto prazo será a soma das parcelas que irão vencer em ate 12 meses após a data da venda;
             - O valor de provisão de venda longo prazo será a soma das parcelas que irão vencer após 12 meses após a data da venda.
         Obs: Arredondar o valor calculado para duas casas decimais.
         
             Propriedade propostaItens : Valor geral de comissão.
                 - Valor da comissão = (Preço do produto x quantidade x Porcentual da comissão) / 100.
                     - 81831,038 = (492.37 x 2936.17 x 5.660376) / 100.
                     - Após o cálculo o valor da comissão é arredondado considerando duas casas decimais depois da virgula. Valor da comissão = 81831.04.
                     - O Preço do produto, quantidade e Porcentual da comissão são referentes aos seguintes campos respectivamente 'precoProduto', 'qtdeProduto' e 'porcentualComissao'.
                     - Dados referente ao objeto 'propostaItens'.
             Propriedade propostaComissao : Valor da comissão.             
                 - Valor da comissão = (Valor da comissão x Porcentual da comissão)/100.
                     - 27822,5536  = (81831.04 x 34.000000) / 100.
                     - O Valor da comissão e Porcentual da comissão são referentes aos seguintes campos respectivamente 'valorComissao' e 'PorcComissao'.
                     - Dados referente ao objeto 'propostaComissao'.
                 - O resultado do cálculo da comissão é referente ao campo 'valorComissao' e também é o valor que deve ser informado.
         
         Planilha com exemplo do cálculo do valor total e comissão:
         https://drive.google.com/file/d/14IW7aoBkT91FFOJBB5LVth-eerIxnqLP/view
         
         Anexos:
         Exemplo do body json: 
         https://ajuda.globaltec.com.br/wp-content/uploads/2019/12/exemploGravarProposta.txt
        
        Endpoint: `/api/v{version}/Proposta/GravarProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Grava os dados da proposta de venda
        
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
                            "proposta",
                            "propostaParamModeloParcelas",
                            "propostaParamParcelas",
                            "propostaItens",
                            "propostaCliente"
                        ],
                        "type": "object",
                        "properties": {
                            "proposta": {
                                "$ref": "#/definitions/UAUApi.Models.Proposta.Proposta",
                                "description": "Contém todas informações da proposta"
                            },
                            "propostaPacelasGeradas": {
                                "description": "Deve conter as parcelas que foram geradas pela proposta. \r\nAo gravar ou alterar uma proposta o sistema sempre vai gerar essas parcelas novamente, logo elas são descartadas.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ModeloVenda.PropostaParcelasGeradas"
                                }
                            },
                            "propostaParamModeloParcelas": {
                                "description": "Deve conter os parametros de modelo dos grupos de parcela da proposta",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ModeloVenda.PropostaParamModeloVenda"
                                }
                            },
                            "propostaParamParcelas": {
                                "description": "Deve conter os parametros dos grupos de parcela da proposta",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.propostaParametroParcelas"
                                }
                            },
                            "propostaComissao": {
                                "description": "Deve conter as comissões que serão pagas na proposta, caso tenha.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.comissaoProposta"
                                }
                            },
                            "propostaComissaoParc": {
                                "description": "Deve conter o parcelamento da comissão, caso tenha comissão.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.ComissaoParcelamento"
                                }
                            },
                            "propostaItens": {
                                "description": "Deve conter 1 ou mais itens da proposta",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.itensProposta"
                                }
                            },
                            "propostaCliente": {
                                "description": "Deve conter 1 ou mais clientes (prospects) da proposta",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.propostaCliente"
                                }
                            },
                            "propostaPlanoIndex": {
                                "description": "Deve conter os planos indexadores da proposta, caso tenha.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.propostaPlanoIndex"
                                }
                            },
                            "propostaSeguro": {
                                "description": "Deve conter 1 ou mais seguros da proposta, caso tenha.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.propostaSeguro"
                                }
                            },
                            "propostaCustasRetencao": {
                                "$ref": "#/definitions/UAUApi.Models.Proposta.CustasRetencaoProposta",
                                "description": "Válida apenas para propostas de aluguel ou aluguel garantido, armazena as informações do valor de retenção do aluguel."
                            },
                            "propostaCustasRetencaoParcela": {
                                "description": "Válida apenas para propostas de aluguel ou aluguel garantido, armazena o parcelamento das retenções.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.PropostaCustasRetencaoParc"
                                }
                            },
                            "propostaCap": {
                                "description": "Armazena os CAPS padrões da proposta.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.capProposta"
                                }
                            },
                            "propostaShopping": {
                                "$ref": "#/definitions/UAUApi.Models.Proposta.shoppingProposta",
                                "description": "Informações de shopping da proposta, válido apenas para propostas para aluguel shopping."
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
            >>> api = Proposta()
            >>> response = api._gravar_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/GravarProposta"
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

    def cancelar_proposta(
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
        1. É obrigatório informar o código da proposta.
        2. Caso ela esteja vendida, deve informar se é para cancela-la ou não.
        3. A proposta não pode estar cancelada ou expirada
        4. Ao enviar ExcluirBoletos como TRUE, irá excluir os boletos ativos da proposta e permitir o cancelamento.
        
        Endpoint: `/api/v{version}/Proposta/CancelarProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Cancelar determinada proposta
        
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
                            "numeroProposta"
                        ],
                        "type": "object",
                        "properties": {
                            "numeroProposta": {
                                "format": "int32",
                                "description": "Número da proposta a ser cancelada",
                                "type": "integer"
                            },
                            "cancelarVendida": {
                                "description": "Permitir cancelar proposta vendida",
                                "type": "boolean"
                            },
                            "ExcluirBoletos": {
                                "description": "Permitir excluir os boletos ativos da proposta",
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
            >>> api = Proposta()
            >>> response = api._cancelar_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/CancelarProposta"
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

    def renegociar_proposta(
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
        Permite renegociar parcelas de uma proposta
        1. O usuário deverá estar autenticado e validado.
        2. Informar os dados da proposta.
        3. Informar as parcelas a serem geradas.
        4. Informar as parcelas escolhidas para renegociação.
        6. Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
           retorna mensagem informando a inconsistência encontrada para que seja analisada.
        7. Após as validações realiza a renegociação das parcelas.
        8. Será registrado comentário na proposta sobre a renegociação realizada.
        9. O parâmetro opcional TermoReserva, quando preenchido, precisa ter o valor 0 ou 1. (0-Não, 1-Sim).
        10. Os parâmetros opcionais ValorCurtoPrazo e valorLongoPrazo, se não preenchidos, serão calculados automaticamente.
            - O valor de provisão de venda curto prazo será a soma das parcelas que irão vencer em ate 12 meses após a data da venda;
            - O valor de provisão de venda longo prazo será a soma das parcelas que irão vencer após 12 meses após a data da venda.
        
        Endpoint: `/api/v{version}/Proposta/RenegociarProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a renegociação de parcelas de uma proposta de venda com as validações necessárias
        
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
                            "NumProposta",
                            "PropostaParcelasGeradas",
                            "ParcelasSelecionadas"
                        ],
                        "type": "object",
                        "properties": {
                            "NumProposta": {
                                "format": "int64",
                                "description": "Número da proposta",
                                "type": "integer"
                            },
                            "PropostaParcelasGeradas": {
                                "description": "Novas parcelas geradas após realizar a renegociação",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.ParcelaRenegociacaoRequest"
                                }
                            },
                            "ParcelasSelecionadas": {
                                "description": "Tabela com as parcelas originais, selecionadas para serem renegociadas (somente chave)",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.ParcelaSelRenegociacaoRequest"
                                }
                            },
                            "ValorDesconto": {
                                "format": "double",
                                "description": "Valor de desconto utilizado na renegociação",
                                "type": "number"
                            },
                            "ValorAcrescimo": {
                                "format": "double",
                                "description": "Valor de acréscimo utilizado na renegociação",
                                "type": "number"
                            },
                            "valorCurtoPrazo": {
                                "format": "double",
                                "description": "Valor curto prazo",
                                "type": "number"
                            },
                            "valorLongoPrazo": {
                                "format": "double",
                                "description": "Valor longo prazo",
                                "type": "number"
                            },
                            "NumPadraoCobranca": {
                                "format": "int32",
                                "description": "Número do padrão de cobrança as ser usado nas novas parcelas geradas após renegociação",
                                "type": "integer"
                            },
                            "TermoReserva": {
                                "format": "int32",
                                "description": "Define se a proposta é de termo reserva ou não (0 - Não, 1 - Sim)",
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
            >>> api = Proposta()
            >>> response = api._renegociar_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/RenegociarProposta"
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

    def consultar_proposta_por_id(
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
         1. Busca determinada proposta filtrando por ID.
         2. Valida usuário e suas permissões.
         3. O campo valorAntecipado e dataCalculo são opcionais, mas caso informado algum deles, precisa informar valor nos dois campos.
             - valorAntecipado deve ser preenchido com 0 para falso ou 1 para verdadeiro.
        
        Endpoint: `/api/v{version}/Proposta/ConsultarPropostaPorId`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta dados da proposta por ID
        
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
                            "numProposta"
                        ],
                        "type": "object",
                        "properties": {
                            "numProposta": {
                                "format": "int32",
                                "description": "Número da proposta",
                                "type": "integer"
                            },
                            "valorAntecipado": {
                                "format": "int32",
                                "description": "Informar se buscará valor antecipado ou não.",
                                "type": "integer"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data cálculo para obter valores reajustados.",
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
            >>> api = Proposta()
            >>> response = api._consultar_proposta_por_id(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/ConsultarPropostaPorId"
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

    def vincular_arquivo_proposta(
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
        1. Realiza a vinculadção de arquivo com determinada proposta.
        
        Endpoint: `/api/v{version}/Proposta/VincularArquivoProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Vincular arquivo a proposta
        
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
                            "arquivo",
                            "proposta"
                        ],
                        "type": "object",
                        "properties": {
                            "arquivo": {
                                "format": "byte",
                                "description": "Arquivo em bytes",
                                "type": "string"
                            },
                            "nome_arquivo": {
                                "description": "Nome do arquivo",
                                "type": "string"
                            },
                            "proposta": {
                                "format": "int32",
                                "description": "Número da proposta",
                                "type": "integer"
                            },
                            "usuario": {
                                "description": "Usuário que vai anexar o arquivo",
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
            >>> api = Proposta()
            >>> response = api._vincular_arquivo_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/VincularArquivoProposta"
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
        1. É obrigatório ter o ambiente de integração com a NTK configurado, só após o registro junto a eles que o registro será gerado no UAU.
        2. É necessário ter permissão de inclusão no programa VEPEDIDORECEBIMENTO
        3. Não é possível gerar pedido para receber todas as parcelas de uma proposta, o sistema irá validar juntamente com boletos gerados.
        4. Somente propostas com status 2 - confirmadas podem gerar pedido de recebimento.
        5. É necessário que o prospect esteja migrado para geração do pedido.
        
        Endpoint: `/api/v{version}/Proposta/GravarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gravar pedido de recebimento  junto a NTK
        
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
            >>> api = Proposta()
            >>> response = api._gravar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/GravarPedidoDeRecebimento"
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
        
        Definição de Negócio:
        1. Pedidos que já tiveram um recebimento parcial junto a NTK, não são cancelados. (trava na NTK).
        2. É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO
        
        Endpoint: `/api/v{version}/Proposta/CancelarPedidoDeRecebimento`
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
            >>> api = Proposta()
            >>> response = api._cancelar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/CancelarPedidoDeRecebimento"
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

    def consultar_hierarquia_parcelas(
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
        
        Endpoint: `/api/v{version}/Proposta/ConsultarHierarquiaParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta parcelas a desconsiderar que estão vinculadas a hierarquia informada
        
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
                            "codigo"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo": {
                                "format": "int32",
                                "description": "Código da Hierarquia",
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
            >>> api = Proposta()
            >>> response = api._consultar_hierarquia_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/ConsultarHierarquiaParcelas"
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
        
        Definição de Negócio:
        1. Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
        2. É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO
        
        Endpoint: `/api/v{version}/Proposta/AtualizarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar o(s) pedido(s) de recebimento  junto a NTK
        
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
            >>> api = Proposta()
            >>> response = api._atualizar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/AtualizarPedidoDeRecebimento"
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
        
        Definição de Negócio:
        1. Possibilita consultar pedido de recebimento junto a NTK
        2. As informações retornadas serão informações do pedido na NTK.
        
        Endpoint: `/api/v{version}/Proposta/ConsultarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar o pedido de recebimento  junto a NTK
        
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
            >>> api = Proposta()
            >>> response = api._consultar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/ConsultarPedidoDeRecebimento"
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
        1. Processa as parcelas recebidas
        2. O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.
        3. Não é possível realizar recebimento para todas as parcelas da proposta! Ao realizar o recebimento de parcelas o sistema verifica se possui boleto gerado e pedido de recebimento para outra parcelas da proposta.
        
        Endpoint: `/api/v{version}/Proposta/ProcessarRecebimentoParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Processa o recebimento de parcelas referentes a propostas
        
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
            >>> api = Proposta()
            >>> response = api._processar_recebimento_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/ProcessarRecebimentoParcelas"
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
        1. Possibilita consultar pedido de recebimento regisrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
        2. As informações retornadas são referentes a como o UAU registrou o pedido internamente.
        
        Endpoint: `/api/v{version}/Proposta/ConsultarPedidoDeRecebimentoUAU`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar o pedido de recebimento no UAU.
        
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
            >>> api = Proposta()
            >>> response = api._consultar_pedido_de_recebimentouau(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/ConsultarPedidoDeRecebimentoUAU"
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

    def retornar_valores_estrutura_comissao(
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
        1. Realiza cálculos da comissão e retorna os valores
        2. Parâmetros:
            - Grupo de parcelas
            - Estrutura de comissão
        
        Endpoint: `/api/v{version}/Proposta/RetornarValoresEstruturaComissao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna a comissão calculada
        
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
                            "codigoVendedor",
                            "codigoHierarquia",
                            "codigoComissao",
                            "parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da Empresa",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da Obra",
                                "type": "string"
                            },
                            "codigoVendedor": {
                                "format": "int32",
                                "description": "Código do Vendedor",
                                "type": "integer"
                            },
                            "codigoHierarquia": {
                                "format": "int32",
                                "description": "Código da Hierarquia - Estrutura de Comissão",
                                "type": "integer"
                            },
                            "codigoComissao": {
                                "format": "int32",
                                "description": "Código da comissão do modelo da comissão.",
                                "type": "integer"
                            },
                            "valorTotalComissao": {
                                "format": "double",
                                "description": "Valor Total da Comissão",
                                "type": "number"
                            },
                            "valorComissaoDireta": {
                                "format": "double",
                                "description": "Valor Total da Comissão Direta",
                                "type": "number"
                            },
                            "valorCurtoPrazoProposta": {
                                "format": "double",
                                "description": "Valor curto prazo",
                                "type": "number"
                            },
                            "valorLongoPrazoProposta": {
                                "format": "double",
                                "description": "Valor de longo prazo",
                                "type": "number"
                            },
                            "produtos": {
                                "description": "Produtos da proposta",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.itensProposta"
                                }
                            },
                            "parcelas": {
                                "description": "Parcelas do Grupo",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Proposta.ParcelaGeradasDeducao"
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
            >>> api = Proposta()
            >>> response = api._retornar_valores_estrutura_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/RetornarValoresEstruturaComissao"
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

    def retorna_valor_comissao_deducao_parcelas(
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
        Calcula o valor da comissão deduzido.
        
        Endpoint: `/api/v{version}/Proposta/RetornaValorComissaoDeducaoParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna o valor da comissão deduzido
        
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
                            "CodigoHierarquia",
                            "CodigoModeloVenda",
                            "ValorTotalProduto",
                            "ValorTotalComissao",
                            "ValorTotalComissaoDireta",
                            "ParcelasGeradas",
                            "PorcentagemComissao",
                            "ValorItemProposta"
                        ],
                        "type": "object",
                        "properties": {
                            "CodigoHierarquia": {
                                "format": "int32",
                                "description": "Código da hierarquia.",
                                "type": "integer"
                            },
                            "CodigoModeloVenda": {
                                "format": "int32",
                                "description": "Código do modelo da venda.",
                                "type": "integer"
                            },
                            "ValorTotalProduto": {
                                "format": "double",
                                "description": "Valor total do produto.",
                                "type": "number"
                            },
                            "ValorTotalComissao": {
                                "format": "double",
                                "description": "Valor total da comissão.",
                                "type": "number"
                            },
                            "ValorTotalComissaoDireta": {
                                "format": "double",
                                "description": "Valor total da comissão direta.",
                                "type": "number"
                            },
                            "ParcelasGeradas": {
                                "description": "Parcelas geradas.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ComissaoHierarquia.ParcelaGerada"
                                }
                            },
                            "PorcentagemComissao": {
                                "format": "double",
                                "description": "Porcentagem da comissão.",
                                "type": "number"
                            },
                            "ValorItemProposta": {
                                "format": "double",
                                "description": "Valor do item da proposta.",
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
            >>> api = Proposta()
            >>> response = api._retorna_valor_comissao_deducao_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Proposta/RetornaValorComissaoDeducaoParcelas"
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

    def traduzir_request_parcelas_geradas(
        self,
        proposta: Optional[int] = None,
        parcelas: Optional[Dict] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            proposta (Dict[str, Any]): The proposta
            parcelas (Dict[str, Any]): The parcelas
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "proposta": {
                    "type": "integer",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "parcelas": {
                    "definition": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/UAUApi.Models.Proposta.ParcelaRenegociacaoRequest"
                        }
                    },
                    "in": "body",
                    "required": true
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
            >>> api = Proposta()
            >>> response = api._traduzir_request_parcelas_geradas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Proposta/TraduzirRequestParcelasGeradas"
        kwargs = {
            "proposta": proposta,
            "parcelas": parcelas,
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

    def traduzir_request_parcelas_selecionadas(
        self,
        num_proposta: Optional[int] = None,
        parcelas: Optional[Dict] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            numProposta (Dict[str, Any]): The proposta
            parcelas (Dict[str, Any]): The parcelas
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "numProposta": {
                    "type": "integer",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "parcelas": {
                    "definition": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/UAUApi.Models.Proposta.ParcelaSelRenegociacaoRequest"
                        }
                    },
                    "in": "body",
                    "required": true
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
            >>> api = Proposta()
            >>> response = api._traduzir_request_parcelas_selecionadas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Proposta/TraduzirRequestParcelasSelecionadas"
        kwargs = {
            "numProposta": num_proposta,
            "parcelas": parcelas,
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

