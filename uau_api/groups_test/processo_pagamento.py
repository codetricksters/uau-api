from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ProcessoPagamento:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def aprovar_dvq(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Permite a aprovação DVQ de parcelas específicas.
        1. No request [dvq] deve ser informado qual a letra que será aprovada ou não.
           - Os seguintes parâmetros obrigatórios para aprovação da letra "D":  Confirmação de data
                - usrConfirmou
                - codigoEmpresa
                - codigoObra
                - numeroProcesso
                - numeroParcela 
           - Os seguintes parâmetros obrigatórios para aprovação da letra "V" : Confirmação do valor
                - usrConfirmou
                - codigo_empresa
                - codigo_obra
                - numero_processo
                - codigo_departamento
                - numero_parcela
                - status_processo
                - valor_parcela      
           - Os seguintes parâmetros obrigatórios para aprovação da letra "Q" : Confirmação da quantidade
                - usrConfirmou
                - codigo_empresa
                - codigo_obra
                - numero_processo
                - numero_parcela
                - status_processo
                - tipo_Docprocesso
                - adiantamento_parcela       
        3. Será validado as permissões do usuário informado. Verifique as permissões caso esteja sendo retornado erro na requisição;
            - FID : Permissão para aprovar "D"
            - FIV : Permissão para aprovar "V"
            - FIQ : Permissão para aprovar "Q"
        4. O usuário autenticado precisa ter acesso a empresa e a obra da qual está fazendo a requisição.   
        5. Será apenas validado a aprovação DVQ das parcelas informadas. Recomendado utilizar a API [RetornarParcelasDVQ] para retornar as informações das parcelas.
        
        Endpoint: `/api/v{version}/ProcessoPagamento/AprovarDVQ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a aprovação DVQ de uma ou várias parcelas.
        
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
                            "dvq",
                            "aprovar",
                            "usuario",
                            "sobreporAprovacoesDeOutrosUsuarios",
                            "parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "dvq": {
                                "description": "DVQ (Confirmação de [D]ata, [V]alor e [Q]uantidade da parcela do processo).",
                                "type": "string"
                            },
                            "aprovar": {
                                "description": "Define se irá aprovar a parcela.",
                                "type": "boolean"
                            },
                            "usuario": {
                                "description": "Login do usuário.",
                                "type": "string"
                            },
                            "sobreporAprovacoesDeOutrosUsuarios": {
                                "description": "Define se a aprovação do usuário atual irá sobrepor as outras aprovações existentes.",
                                "type": "boolean"
                            },
                            "parcelas": {
                                "description": "Lista com a confirmação DVQ das parcelas.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.DVQParcelas"
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
            >>> api = ProcessoPagamento()
            >>> response = api._aprovardvq(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/AprovarDVQ"
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

    def gerar_processo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <br>Dados básicos para o funcionamento da API.</br>
        <list type="bullet">
          <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
          <item>2. Preencher os parâmetros de request para uso do método.</item>
          <item>3. <a href="https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2024/11/ProcessoPagamento_GerarProcesso-3.pdf" target="_blank">Documentação API - Gerar Processo (Clique Aqui)</a></item>
        </list>
        <b>Definição de Negócio:</b>
        <br>Gera um processo de pagamento.</br>
        <list type="bullet">
          <item>1. É obrigatório informar os dados básicos do processo de pagamento.</item>
          <item>2. O usuário autenticado precisa ter acesso à empresa e obra que está fazendo a requisição.</item>
          <item>3. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
          <item>4. Só aceita os tipos de processo de pagamento: composições e insumos, insumos planejados, adiantamento de caixa de obra, patrimônio vinculado ao planejamento.</item>
          <item>5. Você pode informar uma parcela ou uma lista de parcelas.</item>
          <item>6. Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de DocumentoFiscal; o documento deve existir.</item>
          <item>7. Você pode aplicar desconto normal à parcela, informe os dados de desconto no objeto Descontos.</item>
          <item>8. Quando o insumo PL for do tipo 1 - quantidade, será considerado o preço do item.</item>
          <item>9. Somente podem ser gerados processos dos tipos: 1 - Processo de Pagamento, 11 - Compra de patrimônio, 13 - Adiantamento de caixa de obra.</item>
          <item>10. Processos de pagamento de serviços gerarão automaticamente os descontos vinculados (impostos) caso estejam configurados.</item>
          <item>11. Categoria de movimentação financeira na propriedade de Item:
         <list type="bullet"><item><description>Deve adicionar a propriedade CategoriaMovimentacaoFinanceira na propriedade de Item, para armazenar o código da categoria de movimentação financeira.</description></item><item><description>Não é obrigatório informar o parâmetro CategoriaMovimentacaoFinanceira.</description></item></list></item>
          <item>12. Caso não seja informado o tipo de pagamento TipoPagamento ou tipo de emissão TipoEmissao, será considerada a configuração padrão do processo de pagamento.</item>
        </list>
        
        Endpoint: `/api/v{version}/ProcessoPagamento/GerarProcesso`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um processo de pagamento.
        
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
                            "CodigoFornecedor",
                            "TipoProcesso",
                            "ControlarEstoque",
                            "AcompanhaEntrega",
                            "TipoItem",
                            "Parametro",
                            "Parcelas",
                            "Itens"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Código da empresa no UAU.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "<list type=\"bullet\">\r\n  <item>Código da obra no UAU.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "CodigoFornecedor": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Código do fornecedor no UAU.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "TipoProcesso": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Tipos de processo de pagamento no UAU.</item>\r\n  <item>\r\n    1 - Processo de Pagamento\r\n  </item>\r\n  <item>\r\n    11 - Compra de patrimônio\r\n  </item>\r\n  <item>\r\n    13 - Adiantamento de caixa de obra\r\n  </item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "ControlarEstoque": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Controlar estoque. Se vai controlar estoque e o tipo de processo for 1 - Processo de pagamento,<br> então o tipo de processo passa a ser 2 - Compra rápida.</br></item>\r\n  <item>\r\n    0 - Não\r\n  </item>\r\n  <item>\r\n    1 - Sim\r\n  </item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "AcompanhaEntrega": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Acompanha entrega. Se vai acompanhar entrega e o tipo de processo for 1 - Processo de pagamento,<br> então o tipo de processo passa a ser 10 - Tipo Solicit. Pagamento c/ Acomp. de Entrega.</br></item>\r\n  <item>\r\n    0 - Não\r\n  </item>\r\n  <item>\r\n    1 - Sim\r\n  </item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "DataPrevisaoEntrega": {
                                "format": "date-time",
                                "description": "<list type=\"bullet\">\r\n  <item>Data de previsão para entrega. Caso o tipo de processo seja igual a 13 - Adiantamento de caixa,<br> a data de previsão para entrega não será considerada.</br></item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "TipoItem": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Tipo do item:</item>\r\n  <item>\r\n    0 - Insumos gerais\r\n  </item>\r\n  <item>\r\n    1 - Insumos planejados\r\n  </item>\r\n  <item>\r\n    2 - Composições gerais\r\n  </item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "HistoricoLancContabil": {
                                "description": "<list type=\"bullet\">\r\n  <item>Histórico de lançamento contábil.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "HistoricoLancContabilPago": {
                                "description": "<list type=\"bullet\">\r\n  <item>Histórico de lançamento contábil pago.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "CategoriaMovimentacaoFinanceira": {
                                "description": "<list type=\"bullet\">\r\n  <item>Código da categoria de movimentação financeira.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "NumeroContrato": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Código do contrato de material e serviço, onde o processo será adicionado como adiantamento de contrato.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "Parametro": {
                                "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ParametroProcesso",
                                "description": "<list type=\"bullet\">\r\n  <item>Parâmetros do processo de pagamento.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>"
                            },
                            "Parcelas": {
                                "description": "<list type=\"bullet\">\r\n  <item>Parcelas do processo de pagamento.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ParcelaProcesso"
                                }
                            },
                            "Itens": {
                                "description": "<list type=\"bullet\">\r\n  <item>Itens do processo de pagamento.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ItensProcesso"
                                }
                            },
                            "DescontoVinculado": {
                                "description": "<list type=\"bullet\">\r\n  <item>Descontos vinculados.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ProcessoVinculado"
                                }
                            },
                            "SolicitacaoCaixaObra": {
                                "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.AprovarSolicitacaoCXO",
                                "description": "<list type=\"bullet\">\r\n  <item>Aprovar Solicitação.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>"
                            },
                            "PermiteBoletoVencido": {
                                "description": "<b>Permite Boleto Vencido</b>\r\n<list type=\"bullet\">\r\n  <item>\r\n    True - Permite alterar o processo se a data de vencimento for menor que a data de prorrogação.</item>\r\n  <item>\r\n    False - Não permite alterar.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
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
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_processo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/GerarProcesso"
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

    def gerar_nota_fiscal(
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
        Gerar nota fiscal de entrada de acordo com os dados do processo
         
        1. É obrigatório informar os dados básicos da nota fiscal.
        2. O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
        3. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção;
        4. Serão utilizadas as informações fiscais de tributo cadastradas no produto ou na empresa.
        5. Especies disponíveis para geração do documento fiscal (NF - Nota fiscal, CT - Conhecimento de transporte, RE - Recibo, OU - Outros, CF - Cupom fiscal)
        
        Endpoint: `/api/v{version}/ProcessoPagamento/GerarNotaFiscal`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar nota fiscal com base nos dados do processo informado. A nota será vinculada ao processo.
        
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
                            "NumeroProcesso",
                            "TipoNF",
                            "Especie",
                            "Serie",
                            "NFEletronica",
                            "NumeroNotaFiscal",
                            "CodigoRemetente",
                            "DataEmissao",
                            "DataDeEmissaoMaiorQueCadastro",
                            "DataEntrada",
                            "DataDeEntradaMaiorQueCadastro"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Número da empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "código da obra",
                                "type": "string"
                            },
                            "NumeroProcesso": {
                                "format": "int32",
                                "description": "Número do processo",
                                "type": "integer"
                            },
                            "Parcela": {
                                "format": "int32",
                                "description": "Número da parcela",
                                "type": "integer"
                            },
                            "TipoNF": {
                                "format": "int32",
                                "description": "Tipo da nota fiscal\r\n0 - Estadual\r\n1 - Municipal",
                                "enum": [
                                    0,
                                    1
                                ],
                                "type": "integer"
                            },
                            "Especie": {
                                "description": "Espécie da nota fiscal (NF - Nota fiscal, CT - Conhecimento de transporte, RE - Recibo, OU - Outros, CF - Cupom fiscal)",
                                "type": "string"
                            },
                            "Serie": {
                                "description": "Série da nota fiscal",
                                "type": "string"
                            },
                            "NFEletronica": {
                                "description": "Indica se a nota fiscal é eletrônica\r\nTRUE - É nota fiscal eletrônica\r\nFALSE - Não é nota fiscal eletrônica",
                                "type": "boolean"
                            },
                            "ChaveNfe": {
                                "description": "Chave da nota fiscal eletrônica",
                                "type": "string"
                            },
                            "NumeroNotaFiscal": {
                                "description": "Número da nota fiscal",
                                "type": "string"
                            },
                            "CodigoRemetente": {
                                "format": "int32",
                                "description": "Código do remetente/destinatário da nota fiscal.",
                                "type": "integer"
                            },
                            "DataEmissao": {
                                "format": "date-time",
                                "description": "Date de emissão da nota fiscal",
                                "type": "string"
                            },
                            "DataDeEmissaoMaiorQueCadastro": {
                                "description": "Permitir que a data de emissão da nota seja maior que a data de cadastro",
                                "type": "boolean"
                            },
                            "DataEntrada": {
                                "format": "date-time",
                                "description": "Data de entrada da nota fiscal",
                                "type": "string"
                            },
                            "DataDeEntradaMaiorQueCadastro": {
                                "description": "Permitir que a data de entrada da nota seja maior que a data de cadastro",
                                "type": "boolean"
                            },
                            "ModeloNF": {
                                "format": "int32",
                                "description": "Modelo da nota fiscal (Código controlado pelo UAU). Obrigatório para espécies NF, CT, CF.",
                                "type": "integer"
                            },
                            "ArqNotaFiscal": {
                                "description": "Arquivo da nota nota fiscal convertido em string base 64 para anexar ao processo de pagamento.\r\nPara conseguir anexar o arquivo informado, deverá informar o nome do arquivo obrigatoriamente. (Propriedade NomeArquivo)",
                                "type": "string"
                            },
                            "CaminhoOrigemArquivoLocal": {
                                "description": "Caminho onde o arquivo se encontra na rede local do cliente.\r\nPara conseguir mover o arquivo da pasta, deverá informar o nome do arquivo obrigatoriamente. (Propriedade NomeArquivo)\r\n(Deverá ser informado o caminho com o dobro de barras para cada barra informada. \r\nEXEMPLO: Caso o caminho do arquivo for \\\\\\\\Servidor\\documentos\\notasFiscais, deverá ser informado \\\\\\\\\\\\\\\\Servidor\\\\\\\\documentos\\\\\\\\notasFiscais ao requisitar o serviço)",
                                "type": "string"
                            },
                            "CaminhoDestinoArquivo": {
                                "description": "Pasta onde o arquivo será salvo. \r\nCaso não informe a pasta, o arquivo será na pasta padrão de arquivos(anexos).\r\nCaso seja informado a pasta, será concatenado a pasta informada à pasta padrão de arquivos(anexos). Exemplo: \\\\\\\\Servidor\\PastaPadrao + \\CaminhoDestinoArquivo\r\n(Deverá ser informado o caminho da pasta com o dobro de barras para cada barra informada. \r\nEXEMPLO: Caso o caminho da pasta do arquivo for \\documentos\\notasFiscais, deverá ser informado \\\\\\\\documentos\\\\\\\\notasFiscais ao requisitar o serviço)",
                                "type": "string"
                            },
                            "NomeArquivo": {
                                "description": "Nome do arquivo que será anexado. Deverá informar o nome e a extensão do arquivo.",
                                "type": "string"
                            },
                            "CopiarArquivo": {
                                "description": "Identifica se irá copiar o arquivo ao invés de mover\r\nTRUE - Irá copiar o arquivo da nota \r\nFALSE - Irá mover o arquivo da nota",
                                "type": "boolean"
                            },
                            "VincularADescontos": {
                                "description": "Indica ser irá vincular a nota fiscal gerada nos processos vinculados\r\nTRUE  - Irá vincular as notas nos demais processos vinculados\r\nFALSE - Não irá vincular as notas nos processos vinculados\r\nObs.: Por padrão o valor sempre será TRUE, assim mesmo que não seja informado será vinculado a nota nos processos vinculados.",
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
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/GerarNotaFiscal"
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

    def aprovar_processos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        2. O Usuário informado precisa ter a permissão [FICHEQUE] para aprovar as parcelas do processo.
        3. A(s) parcela(s) precisam estar no "Emissão de Pagamentos" para serem aprovadas.
        4. Todos os parâmetros são obrigatórios.
        
        Endpoint: `/api/v{version}/ProcessoPagamento/AprovarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a aprovação de parcelas de um processo de pagamento.
        
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
                            "processos"
                        ],
                        "type": "object",
                        "properties": {
                            "processos": {
                                "description": "Lista de processos para serem Aprovados ou Desaprovados.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.AprovarProcessoRequest"
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
            >>> api = ProcessoPagamento()
            >>> response = api._aprovar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/AprovarProcessos"
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

    def emissao_pagamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Rota destinada para emitir processos de pagamento que estão prontos (aprovados) para serem emitidos.
        
        **Definição de negócio:**
        1. Emissão será realizada somente para processos aprovados com Tipo de Emissão "Débito CC";
        2. Validar status da parcela como 2 - Reprovado, não deve enviar;
        3. Verifica se existe alguma restrição(Ocorrência) para o fornecedor/beneficiário;
        4. Valida programa de permissão;
        5. Valida se o processo é vinculado a algum tributo, e se for, valida se o tributo está confirmado;
              - Caso esteja confirmado, atualiza o status do tributo para 2 - Pago; - Ação;
        6. Valida se o processo é de retenção contratual, tipos 16 ou 13, e se for, valida o configuração da empresa, se está para realizar retenção contratual e valida a situação do contrato vinculado;
        
        Endpoint: `/api/v{version}/ProcessoPagamento/EmissaoPagamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Enviar processo de pagamento em emissão para o banco
        
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
                            "parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "parcelas": {
                                "description": "Lista de processos para serem Aprovados ou Desaprovados.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.EmitirParcelaRequest"
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
            >>> api = ProcessoPagamento()
            >>> response = api._emissao_pagamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/EmissaoPagamento"
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

    def acrescimo_desconto(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        **Parâmetros do Request:**
        Empresa, Obra, NumeroDoProcesso e NumeroDaParcela são obrigatórios e identificam o processo;
        Data: Data do acréscimo a ser inserido no processo;
        Valor: Valor do acréscimo ou desconto. Positivo = acréscimo, negativo = desconto. Percentuais não são aceitos;
        Descricao: Texto livre limitado conforme tabela do banco de dados;
        CAP: Código fiscal a ser utilizado no processamento contábil do ajuste;
        HistoricoContabil: Texto opcional que será enviado à contabilidade como histórico da movimentação.
        TipoCalculo: Campo opcional que define entre 0 - Compõe base de cálculo e 1 - Não compõe base de cálculo para o cadastro de desconto
        **Definição Técnica:**
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/ProcessoPagamento/AcrescimoDesconto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aplicar um novo acréscimo ou desconto fixo em um processo de pagamento
        
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
                            "NumeroDoProcesso",
                            "NumeroDaParcela",
                            "Data",
                            "Valor"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Código da empresa no UAU.</item>\r\n  <item>Campo obrigatório.</item>\r\n</list>",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "<list type=\"bullet\">\r\n  <item>Código da obra no UAU.</item>\r\n  <item>Campo obrigatório.</item>\r\n</list>",
                                "type": "string"
                            },
                            "NumeroDoProcesso": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Número do processo de pagamento no UAU.</item>\r\n  <item>Campo obrigatório.</item>\r\n</list>",
                                "type": "integer"
                            },
                            "NumeroDaParcela": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Número da parcela do processo de pagamento no UAU.</item>\r\n  <item>Campo obrigatório.</item>\r\n</list>",
                                "type": "integer"
                            },
                            "Data": {
                                "format": "date-time",
                                "description": "<list type=\"bullet\">\r\n  <item>Data do acréscimo a ser inserido no processo.</item>\r\n  <item>Campo obrigatório.</item>\r\n</list>",
                                "type": "string"
                            },
                            "Valor": {
                                "format": "double",
                                "description": "<list type=\"bullet\">\r\n  <item>Valor do acréscimo ou desconto. Positivo = acréscimo, negativo = desconto. Percentuais não são aceitos.</item>\r\n  <item>Campo obrigatório.</item>\r\n</list>",
                                "type": "number"
                            },
                            "Descricao": {
                                "description": "<list type=\"bullet\">\r\n  <item>Texto livre limitado conforme tabela do banco de dados.</item>\r\n</list>",
                                "type": "string"
                            },
                            "CAP": {
                                "description": "<list type=\"bullet\">\r\n  <item>Código fiscal a ser utilizado no processamento contábil do ajuste.</item>\r\n</list>",
                                "type": "string"
                            },
                            "HistoricoContabil": {
                                "description": "<list type=\"bullet\">\r\n  <item>Texto opcional que será enviado à contabilidade como histórico da movimentação</item>\r\n</list>",
                                "type": "string"
                            },
                            "TipoCalc": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Campo opcional que irá definir se o desconto entra ou não na base de cálculo</item>\r\n</list>",
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
            >>> api = ProcessoPagamento()
            >>> response = api._acrescimo_desconto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/AcrescimoDesconto"
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

    def consultar_processos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Permite que você consulte o(s) processo(s) de pagamento por um número e/ou período específico.
        1. Você pode consultar informando uma lista dos números dos processos de pagamento, código da empresa e código da obra cadastrados no UAU.
        2. Você pode consultar processos de pagamento informado uma lista de código da empresa e código da obra cadastrado no UAU por um determinado período.
        3. Você pode consultar processos de pagamento informado uma lista de fornecedores cadastrado no UAU por um determinado período.
        4. O usuário autenticado precisa ter acesso as empresas e obras das quais ele está fazendo a requisição.   
        5. Caso consulte vários processos ou informe um longo período, sugerimos que consulte o serviço de maneira assíncrona. 
        6. NovoBeneficiario: O campo Parametro/NovoBeneficiario sempre retornará o valor null. A informação é retornada no campo Parcelas/NovoBeneficiario.
        7. Caso passe uma mistura de todos os filtros, o filtro de data que será utilizado será o do busca por cnpj a frente do busca por empresas e obras.
        7.1 Caso queria buscar por períodos diferentes recomendamos utilizar requests separados para respeitar os períodos por grupo separado.
        
        Endpoint: `/api/v{version}/ProcessoPagamento/ConsultarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar processos de pagamento por empresa(s), obra(s) e número(s) do(s) processo(s) e/ou empresa, obra e período(data de cadastro do processo) e/ou CNPJ do fornecedor e período(data de cadastro do processo).
        
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
                            "Processos": {
                                "description": "Lista de processos de pagamento",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.Processo"
                                }
                            },
                            "EmpresaObraPeriodo": {
                                "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.EmpresaObraPeriodo",
                                "description": "Consulta por empresa, obra e período(data de cadastro do processo)"
                            },
                            "FornecedorPeriodo": {
                                "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.FornecedorPeriodo",
                                "description": "Buscar os processos de pagamento específicos de um fornecedor pelo seu CNPJ ou CPF"
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
            >>> api = ProcessoPagamento()
            >>> response = api._consultar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/ConsultarProcessos"
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

    def manutencao_processo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <br>Dados básicos para o funcionamento da API.</br>
        <list type="bullet">
          <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
          <item>2. Consultar os dados de um processo de pagamento: URI + /api/v{version}/ProcessoPagamento/ConsultarProcessos</item>
          <item>3. Preencher os parâmetros de request para uso do método.</item>
          <item>4. <a href="https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2024/11/ProcessoPagamento_ManutencaoProcesso-1.pdf" target="_blank">Documentação API - Manutenção de Processo (Clique Aqui)</a></item>
        </list>
        <b>Definição de Negócio:</b>
        <br>Permite ajustar informações básicas do processo de pagamento, como vencimento, data de prorrogação, novo beneficiário, fornecedor, etc.
         Consulte a documentação do objeto de request.</br>
        <list type="bullet">
          <item>1. É obrigatório informar os dados básicos do processo de pagamento.</item>
          <item>2. Para alterar informações da parcela do processo, preencha o objeto de Parcelas.</item>
          <item>3. Todas as alterações gerarão um comentário de alteração no processo.</item>
          <item>4. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a alteração.</item>
          <item>5. O parâmetro CodigoNovoBeneficiario altera todas as parcelas a pagar do processo informado, independentemente da parcela informada.
         <list type="bullet"><item><description>Ao informar esse valor no processo, na resposta da request o valor será null, mas estará indicado nas parcelas. Isso ocorre porque esse campo pertence à parcela.</description></item></list></item>
          <item>6. O parâmetro NovoBeneficiario altera apenas a parcela informada, se ela estiver a pagar.
         <list type="bullet"><item><description>Se preencher o parâmetro de beneficiário no processo e na parcela, o parâmetro do processo será desconsiderado, alterando apenas os beneficiários das parcelas informadas.</description></item></list></item>
          <item>7. Se preencher o valor zero ou vazio para o novo beneficiário, a alteração não será considerada. A API não limpa valores de novo beneficiário.</item>
        </list>
        
        Endpoint: `/api/v{version}/ProcessoPagamento/ManutencaoProcesso`
        HTTP Method: `POST`
        
        Implementation Notes:
        Executa manutenção básica em uma etapa do processo de pagamento.
        
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
                            "Numero",
                            "Empresa",
                            "Obra"
                        ],
                        "type": "object",
                        "properties": {
                            "Numero": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Número do processo de pagamento.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "Empresa": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Empresa do processo de pagamento.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "<list type=\"bullet\">\r\n  <item>Código da obra que foi gerado o processo a ser pago.</item>\r\n  <item>\r\n    <b>Campo obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "CodigoFornecedor": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Número do código do fornecedor.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "CodigoNovoBeneficiario": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Código do novo beneficiário, dados sobre o cedente responsável pela emissão do título original,<br> sacador avalista.</br></item>\r\n  <item>\r\n    Informar valor \"0\" para limpar o beneficiário existente.\r\n  </item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "Antecipado": {
                                "description": "Define se é antecipado ou não, é utilizado para poder parametrizar um processo como antecipado,<br> ou seja, efetuar a confirmação Q da parcela e pagar sem a necessidade do Acompanhamento de Entrega. </br><list type=\"bullet\"><item><br>True  - Antecipado.</br></item><item><br>False - Não antecipado.</br></item><item><b>Campo não obrigatório.</b></item></list>",
                                "type": "boolean"
                            },
                            "Retroacao": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Número de meses de retroação para o pagamento do processo.</item>\r\n  <item>\r\n    Valor pode ser entre 0 a 999\r\n  </item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "CodigoDepartamento": {
                                "description": "<list type=\"bullet\">\r\n  <item>Código do departamento do processo de pagamento.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "TipoJuros": {
                                "format": "int32",
                                "description": "<list type=\"bullet\">\r\n  <item>Tipo de juros, cobrado por atraso, o sistema já calcula usando os valores digitados nos campos %Multa e %Juros Dia,<br>e pode ser calculado dois tipos de juros: Juros Simples e Juros Composto.</br></item>\r\n  <item>\r\n    0 - Juro simples percentual.\r\n  </item>\r\n  <item>\r\n    1 - Juro composto percentual\r\n  </item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "TaxaJurosAtraso": {
                                "format": "double",
                                "description": "<list type=\"bullet\">\r\n  <item>Percentual de juros a ser aplicado em caso de atraso.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "number"
                            },
                            "TaxaMultaAtraso": {
                                "format": "double",
                                "description": "<list type=\"bullet\">\r\n  <item>Percentual de multa a ser aplicado em caso de atraso.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "number"
                            },
                            "ChaveNfe": {
                                "description": "<list type=\"bullet\">\r\n  <item>Chave da nota fiscal eletrônica.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "string"
                            },
                            "Parcela": {
                                "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ManutencaoProcessoParcela",
                                "description": "<list type=\"bullet\">\r\n  <item>Dados da parcela.</item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>"
                            },
                            "NumeroProtocolo": {
                                "format": "int32",
                                "description": "<b>Número do protocolo</b>\r\n<list type=\"bullet\">\r\n  <item>\r\n    <br>Informe o número do protocolo que deseja atribuir ao processo de pagamento.</br>\r\n  </item>\r\n  <item>\r\n    <br>Se desejar limpar o campo, informe o valor -1 neste parâmetro</br>\r\n  </item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
                                "type": "integer"
                            },
                            "PermiteBoletoVencido": {
                                "description": "<b>Permite Boleto Vencido</b>\r\n<list type=\"bullet\">\r\n  <item>\r\n    <br>\r\n      True  - Permite alterar o processo se a data de vencimento for menor que a data de prorrogação.</br>\r\n  </item>\r\n  <item>\r\n    <br>\r\n      False - Não permite alterar.</br>\r\n  </item>\r\n  <item>\r\n    <b>Campo não obrigatório.</b>\r\n  </item>\r\n</list>",
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
            >>> api = ProcessoPagamento()
            >>> response = api._manutencao_processo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/ManutencaoProcesso"
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

    def retornar_parcelas_dvq(
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
        1. Os campos empresa, obra e usuário são obrigatórios.
        2. É validado se o usuário existe no banco de dados, e se tem permissão na empresa e obra informada.
        3. Data e Fornecedor devem está vazio ou sem o parâmetro informado na requisição para não serem considerados na consulta.
        4. Número processo(numeroproc) e notafiscal devem está como 0 ou sem o parâmetro informado na requisição para não serem considerados na consulta.
        5. O parâmetro nota fiscal é o número de controle interno da nota fiscal.
        6. Status atual da aprovação status_d, status_v e status_q.
            - Valor [A]: aprovado
            - Valor [D]: não aprovado
        
        Endpoint: `/api/v{version}/ProcessoPagamento/RetornarParcelasDVQ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna parcelas com alguma possibilidade de aprovação DVQ.
        
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
                            "Usuario",
                            "Empresa",
                            "Obra"
                        ],
                        "type": "object",
                        "properties": {
                            "Usuario": {
                                "description": "Login do usuário",
                                "type": "string"
                            },
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "numeroproc": {
                                "format": "int32",
                                "description": "Número processo",
                                "type": "integer"
                            },
                            "fornecedor": {
                                "description": "Código da pessoa(Fornecedor)",
                                "type": "string"
                            },
                            "notafiscal": {
                                "format": "int32",
                                "description": "Número nota fiscal",
                                "type": "integer"
                            },
                            "inicial": {
                                "description": "Data inicio",
                                "type": "string"
                            },
                            "final": {
                                "description": "Data final",
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
            >>> api = ProcessoPagamento()
            >>> response = api._retornar_parcelasdvq(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/RetornarParcelasDVQ"
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

    def gerar_processo_medicao(
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
        Gerar processo de pagamento de medição de contrato de material/serviço
         
        1. É obrigatório informar os dados básicos do processo de pagamento;
        2. O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
        3. O usuário autenticado precisa ter acesso a aos programas de permissão necessários para fazer a inserção;
        4. Você pode informar uma parcela ou uma lista de parcelas;
        5. Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de “DocumentoFiscal”, o documento deve existir;
        6. Você pode aplicar desconto normal a parcela, informe os dados de desconto no objeto “Descontos”;
        7. Quando o insumo PL for do tipo 1 - quantidade será considerado o preço do item;
        
        Endpoint: `/api/v{version}/ProcessoPagamento/GerarProcessoMedicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar processo de pagamento de medição de contrato de material/serviço
        
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
                            "Contrato",
                            "Medicao",
                            "MesPlanejamento",
                            "Parametro",
                            "Parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa no UAU",
                                "type": "integer"
                            },
                            "Contrato": {
                                "format": "int32",
                                "description": "Código do contrato de material e serviço",
                                "type": "integer"
                            },
                            "Medicao": {
                                "format": "int32",
                                "description": "Código da medição",
                                "type": "integer"
                            },
                            "MesPlanejamento": {
                                "format": "date-time",
                                "description": "Mês do planejamento",
                                "type": "string"
                            },
                            "ControlarEstoque": {
                                "format": "int32",
                                "description": "Controlar estoque (0 -Não 1-Sim). Se vai ter controle de estoque para os itens de material.",
                                "type": "integer"
                            },
                            "AcompanhaEntrega": {
                                "format": "int32",
                                "description": "Acompanha entrega (0 - Não 1 - Sim). Se vai acompanhar entrega dos itens de material.",
                                "type": "integer"
                            },
                            "DataPrevisaoEntrega": {
                                "format": "date-time",
                                "description": "Data de previsão para entrega do itens de material.",
                                "type": "string"
                            },
                            "HistoricoLancContabilApagar": {
                                "description": "Histórico de lançamento contábil a pagar",
                                "type": "string"
                            },
                            "HistoricoLancContabilPago": {
                                "description": "Histórico de lançamento contábil pago",
                                "type": "string"
                            },
                            "HistoricoLancContabilDescNormalMed": {
                                "description": "Histórico de lançamento contábil do desconto normal já existente na medição",
                                "type": "string"
                            },
                            "CategoriaMovimentacaoFinanceira": {
                                "description": "Código da categoria de movimentação financeira",
                                "type": "string"
                            },
                            "Parametro": {
                                "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ParametroProcesso",
                                "description": "Parametro do processo de pagamento"
                            },
                            "DocumentoFiscal": {
                                "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.DocumentoFiscalMedicao",
                                "description": "Objeto com os dados da nota fiscal para o processo de serviço/material da medição."
                            },
                            "Parcelas": {
                                "description": "Parcelas do processo de pagamento",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ParcelaProcessoMedicao"
                                }
                            },
                            "Itens": {
                                "description": "Itens do processo de pagamento. \r\nÉ obrigatório quando o contrato não possui vínculos por item. \r\nSe informar os itens mesmo o contrato sendo vinculado por item, serão coletadas apenas as informações de Cap e categoria de movimentação financeira.\r\nAs demais informações serão preenchidas com o resultado da consulta dos itens da medição.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ItensProcessoMedicao"
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
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_processo_medicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/GerarProcessoMedicao"
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

    def manutencao_parcelas_processo(
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
        Permite dar manutenção nas parcelas do processo de pagamento. Ao informar os dados para as novas parcelas, será simulado e gerado automaticamente as novas parcelas
        com novas numerações, valores e data de vencimento. Será excluido a(s) parcela(s) informadas no request, pois foram substituídas pelas novas parcelas geradas.
        
        1. É obrigatório informar os dados básicos da parcela e do processo de pagamento;
        2. O usuário autenticado precisa ter acesso aos programas de permissão necessários (FIANALISE) para fazer a alteração.
        
        Endpoint: `/api/v{version}/ProcessoPagamento/ManutencaoParcelasProcesso`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza manutenção em parcelas de processo de pagamento. Será simulado e gerado automaticamente as novas parcelas conforme os parâmetros informados.
        
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
                            "numeroProcesso",
                            "dataVencimento",
                            "qtdeParcelas",
                            "intervaloParcelas",
                            "listaParcelasManutencao"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa do processo de pagamento",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da obra do processo de pagamento",
                                "type": "string"
                            },
                            "numeroProcesso": {
                                "format": "int32",
                                "description": "Número do processo de pagamento",
                                "type": "integer"
                            },
                            "dataVencimento": {
                                "format": "date-time",
                                "description": "Data de vencimento da primeira parcela",
                                "type": "string"
                            },
                            "qtdeParcelas": {
                                "format": "int32",
                                "description": "Quantidade de novas parcelas a serem geradas",
                                "type": "integer"
                            },
                            "intervaloParcelas": {
                                "format": "int32",
                                "description": "Intervalo das parcelas",
                                "type": "integer"
                            },
                            "listaParcelasManutencao": {
                                "description": "Lista de parcelas para manutenção.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ParcelaManutencaoRequest"
                                }
                            },
                            "listaValoresNovasParcelas": {
                                "description": "Lista com Valores das novas parcelas. \r\nA lista de valores das parcelas quando informada, deve ter a quantidade de valores igual a quantidade das novas parcelas a serem geradas.\r\nCaso não seja informada, será calculado o valor das parcelas de forma proporcional.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ValorParcelaManutencaoRequest"
                                }
                            },
                            "listaValoresAcrescimoNovasParcelas": {
                                "description": "Lista com valores de acréscimo das parcelas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.AcrescimoParcelaManutencaoRequest"
                                }
                            },
                            "listaDataVencimentoNovasParcelas": {
                                "description": "Lista com data de vencimento das parcelas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.DataVencimentoParcelaManutencaoRequest"
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
            >>> api = ProcessoPagamento()
            >>> response = api._manutencao_parcelas_processo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/ManutencaoParcelasProcesso"
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

    def confirmar_processo_para_emissao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Valida se foram selecionadas parcelas de processos diferentes com tipos de Internos e Externos, ou seja, só pode confirmar parcelas de processos com mesmo tipo, ou todos internos ou todos externos;
        
        **Definição de negócio:**
        1. Valida se parcela tem confirmação de DVQ;
        2. Valida se a parcela tem banco e conta informado, e Tipo de emissão;
        3. Valida fechamento fiscal de banco e conta para a data de prorrogação;
        5. Valida configuração geral de provisionamento de documento fiscal, onde se a config estiver marcada, só pode confirmar se todas as parcelas forem provisionado ou se as parcelas foram de adiantamento;
        6. Valida se o processo é transação financeira, ou seja, vinculado a alguma venda;
        7. Valida se o processo é transação financeira (Processo de REEMBOLSO), e caso seja, só pode confirmar se o tipo de emissão for Débito Eletrônico;
        8. Valida se a parcela possui chave da Nfe e caso tenha, valida o status da NF, e se estiver pendente não permite gerar;
        9. Validações para tipo de emissão Débito Eletrônico;
            - Valida se tem alguma forma de pagamento informada;
            - Valida se tem algum tipo de pagamento informado;
            - Valida se o banco informado na parcela com emissão débito eletrônico, tem opção de geração de arquivo de pagamento;
            - Valida se a conta informada na parcela com emissão débito eletrônico é do tipo conta corrente e se existe agência cadastrada;
            - Valida se o fornecedor ou beneficiário está cadastrado ou se possui endereço principal;
            - Valida caracteres especiais nos dados do fornecedor ou beneficiário;
            - Validações das formas de pagamento 
                 - CRÉDITO C/C; CRÉDITO C/ POUPANÇA; DOC ; TED (01,03,05,06,07,08,09 e 10);
                     - Caso existe dados bancários para a parcela do processo, valida se existe conta cadastrada como padrão para o beneficiário ou fornecedor da parcela;
                     - Valida se o banco creditado é IGUAL do banco debitado para as formas ((01,06,07 e 09);
                     - Valida se o banco creditado é DIFERENTE do banco debitado para as formas ((03,05,08 e 10);
                     - Para os bancos 341 e 444 e para as formas 06, 08 ou 10, valida se o fornecedor possui CPF ou CPNJ e valida se o CPF/CNPJ do creditado é IGUAL ao debitado;
                 - PAG TÍTULOS; CONCECIONÁRIAS; TRIBUTOS; e PIX; (30, 31, 13, 29, 19, 91, 35, 47)
                     - Valida se o código de barras foi preenchido;
                     - Valida se o Pix copia e cola foi preenchido;
                     - Valida duplicidade de código de barras ou pix copia e cola, caso a configuração geral esteja marcada;
                     - Valida se o valor ou a data no código de barras é diferente do valor ou data do processo;
                     - Para a forma 21, valida se o banco creditado é diferente do banco debitado;
                     - Para os banco 356;291;389 e as formas 29 e 30, valida se o banco creditado é igual ao banco debitado;
                     - Para a forma de pagamento 35 - FGTS, valida o tamanho máximo do campo identificador do FGTS, onde é 20 para o banco 237, e para os bancos 1, 8, 33, 104, 341, 353, 756, 748, 444, o tamanho máximo é 16;
                 - CARTÃO SALÁRIO (14) para o Banco 409
                     - Valida se o fornecedor possui um cartão salário cadastrado;
        10. Validações processo do tipo folha - Tipo processo 18:
            - Caso processo seja gerado na tela de Gerar arquivo de pagamento folha, só pode confirmar como Débito C/C;
            - Valida se o processo folha tem o status do tipo "4 - Gerar arquivo" na tela de Gerar arquivo de pagamento folha, e se tiver mesmo que seja debito eletrônico, permite confirmar sem a forma de pagamento informada na parcela;
            - Caso o projeto esteja com o status do tipo "4 - Gerar arquivo", permite confirmar mesmo sem informar tipo de pagamento;
            - Processos de folha, que estão agrupados e com status "4 - Gerar arquivo", só podem ser confirmados como Débito eletrônico;
            - Valida se os processos do tipo folha tem cálculo gerado para o mesmo, no modulo Folha de pagamento;
        11. Valida se os processos são do tipo tributo, e se estão vinculados a algum tributo;
        12. Valida se o pagamento está DUPLICADO, caso a config geral esteja marcada, onde valida se existem a mesma parcela em emissão ou em contas pagas;
        13. Valida se a parcela já está confirmada, para evitar a concorrência; 
        14. Valida se existem notas fiscais vinculadas ao processo que está com o total menor que o total de todos processos vinculados, caso a config geral esteja marcada;
        15. Valida se a nota fiscal está conferida, caso config geral esteja marcada;
        16. Valida se existe nota fiscal na parcela, caso config geral de provisionamento seja marcada;
        
        Endpoint: `/api/v{version}/ProcessoPagamento/ConfirmarProcessoParaEmissao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Enviar processo de pagamento para emissão de pagamentos
        
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
                            "parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "parcelas": {
                                "description": "Lista de processos para serem Aprovados ou Desaprovados.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ProcessoPagamento.ConfirmaParcelaRequest"
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
            >>> api = ProcessoPagamento()
            >>> response = api._confirmar_processo_para_emissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/ConfirmarProcessoParaEmissao"
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

    def gerar_nota_fiscal_produto_pelo_xml(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Projeto   : 442112
        Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
        Projeto   : 443200
        Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
        
        Alteração  : Augusto Rabelo Barbosa      data: 04/01/2023
        Projeto    : 443200
        Manutenção  : Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais
        
        Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
        Projeto   : 454022
        Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
        
        Alteração : Juliana Oliveira Souza    Data: 19/06/2023
        Projeto   : 467593
        Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
        
        	
        Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
        Projeto   : 442322 - SPT 10-2024 - US 359545
        Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].
        
        Endpoint: `/api/v{version}/ProcessoPagamento/GerarNotaFiscalProdutoPeloXML`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar NF-e com base nos dados informado, xml do diretório.
        
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
                            "Processo",
                            "VincularADescontos"
                        ],
                        "type": "object",
                        "properties": {
                            "ChaveNFe": {
                                "description": "Chave da NFe.\r\nObrigatório apenas quando não for informado o ArquivoXML.",
                                "type": "string"
                            },
                            "ArquivoXML": {
                                "description": "Arquivo xml.\r\nObrigatório apenas quando não for informado o a ChaveNFe.",
                                "type": "string"
                            },
                            "Empresa": {
                                "format": "int32",
                                "description": "Número da empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "Processo": {
                                "format": "int32",
                                "description": "Número do processo",
                                "type": "integer"
                            },
                            "Parcela": {
                                "format": "int32",
                                "description": "Número da parcela",
                                "type": "integer"
                            },
                            "VincularADescontos": {
                                "description": "Vincular a descontos",
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
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal_produto_peloxml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/GerarNotaFiscalProdutoPeloXML"
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

    def gerar_nota_fiscal_servico_pelo_xml(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Projeto   : 442112
        
        Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
        Projeto   : 443200
        Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
        
        Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
        Projeto   : 454022
        Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
        
        
        Alteração : Juliana Oliveira Souza    Data: 19/06/2023
        Projeto   : 467593
        Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
        
        Alteração : Rogério Adriano           Data: 31/07/2023
        Projeto   : 475869
        Manutenção: Foi inserido validação após o preenchimento da classe de nota fiscal
                    para verificar se foi preenchido com sucesso, caso contrario irá retornar o erro.
        
        Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
        Projeto   : 442322 - SPT 10-2024 - US 359545
        Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].
        
        Alteração : Daniel Eugenio Vaz          Data: 11/08/2025
        Projeto   : 381359 - NFse Nacional - Contas a Pagar - US 380751
        Manutenção: Ajuste para consulta do novo padrão NFs-e Nacional
        
        Endpoint: `/api/v{version}/ProcessoPagamento/GerarNotaFiscalServicoPeloXML`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar NFS-e com base nos dados informado, xml do diretório ou arquivo.
        
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
                            "CodigoFornecedor",
                            "Empresa",
                            "Obra",
                            "Processo",
                            "VincularADescontos"
                        ],
                        "type": "object",
                        "properties": {
                            "CodigoFornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor da nota fiscal.",
                                "type": "integer"
                            },
                            "Numero": {
                                "description": "Número da nota fiscal.\r\nObrigatório apenas quando não for informado o ArquivoXML.",
                                "type": "string"
                            },
                            "ChaveNFSe": {
                                "description": "Chave da nota fiscal.\r\nObrigatório apenas quando não for informado o ArquivoXML.",
                                "type": "string"
                            },
                            "ArquivoXML": {
                                "description": "Arquivo xml.\r\nObrigatório apenas quando não for informado o Número.",
                                "type": "string"
                            },
                            "Empresa": {
                                "format": "int32",
                                "description": "Número da empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "Processo": {
                                "format": "int32",
                                "description": "Número do processo",
                                "type": "integer"
                            },
                            "Parcela": {
                                "format": "int32",
                                "description": "Número da parcela",
                                "type": "integer"
                            },
                            "VincularADescontos": {
                                "description": "Vincular a descontos",
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
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal_servico_peloxml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/GerarNotaFiscalServicoPeloXML"
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

    def integrar_processo_pagamento_uauws(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Deve seguir arquivo XSD como formato aceito.
        4. Os campos do tipo data devem obedecer o formato específico (yyyy-MM-dd).
        
        Definição de negócio:
        1. Realiza a importação dos dados de processo de pagamento para o UAU de acordo com o arquivo XML.
        2. Será validado os dados do XML para realizar a importação, bem como tipagem de dados, dados obrigatórios, entre outros. 
        3. Virtuau: https://ajuda.globaltec.com.br/virtuau/como-integrar-meus-processos-de-pagamento/
        
        Anexos:
        1. XML: https://ajuda.globaltec.com.br/download/777734/
        2. XSD: https://ajuda.globaltec.com.br/download/777719/
        3. Postman: https://ajuda.globaltec.com.br/download/777737/
        
        Endpoint: `/api/v{version}/ProcessoPagamento/IntegrarProcessoPagamentoUAUWS`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realizar a integração do processo de pagamento utilizando arquivo XML
        
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
                            "xml_proc"
                        ],
                        "type": "object",
                        "properties": {
                            "xml_proc": {
                                "description": "Arquivo XML com os processos a serem incluidos, de acordo com o XSD",
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
            >>> api = ProcessoPagamento()
            >>> response = api._integrar_processo_pagamentouauws(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/IntegrarProcessoPagamentoUAUWS"
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

    def gerar_nota_fiscal_transporte_pelo_xml(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Projeto   : 442112
        
        Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
        Projeto   : 443200
        Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
        
        Alteração: Augusto Rabelo Barbosa      data: 04/01/2023
        Projeto: 443200
        Manutenção: Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais
        
        Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
        Projeto   : 454022
        Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
        
        Alteração : Juliana Oliveira Souza    Data: 19/06/2023
        Projeto   : 467593
        Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
        
        Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
        Projeto   : 442322 - SPT 10-2024 - US 359545
        Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].
        
        Endpoint: `/api/v{version}/ProcessoPagamento/GerarNotaFiscalTransportePeloXML`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gerar CT-e com base nos dados informado, xml do diretório.
        
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
                            "Processo",
                            "VincularADescontos"
                        ],
                        "type": "object",
                        "properties": {
                            "ChaveCTe": {
                                "description": "Chave da NFe.\r\nObrigatório apenas quando não for informado o ArquivoXML.",
                                "type": "string"
                            },
                            "ArquivoXML": {
                                "description": "Arquivo xml.\r\nObrigatório apenas quando não for informado a ChaveCTe.",
                                "type": "string"
                            },
                            "Empresa": {
                                "format": "int32",
                                "description": "Número da empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "código da obra",
                                "type": "string"
                            },
                            "Processo": {
                                "format": "int32",
                                "description": "Número do processo",
                                "type": "integer"
                            },
                            "Parcela": {
                                "format": "int32",
                                "description": "Número da parcela",
                                "type": "integer"
                            },
                            "VincularADescontos": {
                                "description": "Vincular a descontos",
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
            >>> api = ProcessoPagamento()
            >>> response = api._gerar_nota_fiscal_transporte_peloxml(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ProcessoPagamento/GerarNotaFiscalTransportePeloXML"
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

    def conta_processo_emissao_pagamento_resumido(
        self,
        login_usuario: Optional[str] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Projeto  : 310963 -
        Propósito: Contar os processos de emissão de pagamento
        
        Endpoint: `/api/ProcessoPagamento/ContaProcessoEmissaoPagamentoResumido`
        HTTP Method: `POST`
        
        Implementation Notes:
        Conta os Processo de Emissão de Pagamento
        
        Args:
            login_usuario (Dict[str, Any]): login do usuário.
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "login_usuario": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": "login do usuário."
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
            >>> api = ProcessoPagamento()
            >>> response = api._conta_processo_emissao_pagamento_resumido(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/ProcessoPagamento/ContaProcessoEmissaoPagamentoResumido"
        kwargs = {
            "login_usuario": login_usuario,
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

    def consultar_quantidade_processos_aprovar_dvq(
        self,
        login_usuario: Optional[str] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Projeto  : 310963
        
        Endpoint: `/api/ProcessoPagamento/ConsultarQuantidadeProcessosAprovarDVQ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna a quantidade de processos a ser aprovado do processo DVQ
        
        Args:
            login_usuario (Dict[str, Any]): login do usuário
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "login_usuario": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": "login do usuário"
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
            >>> api = ProcessoPagamento()
            >>> response = api._consultar_quantidade_processos_aprovardvq(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/ProcessoPagamento/ConsultarQuantidadeProcessosAprovarDVQ"
        kwargs = {
            "login_usuario": login_usuario,
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

    def valida_dados_pagamento_para_aceitar_pix_copia_cola(
        self,
        banco: Optional[str] = None,
        conta: Optional[str] = None,
        tipo_emissao: Optional[str] = None,
        forma_pagamento: Optional[str] = None,
        tipo_pagamento: Optional[str] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/ProcessoPagamento/ValidaDadosPagamentoParaAceitarPixCopiaCola`
        HTTP Method: `POST`
        
        Implementation Notes:
        Validações dos dados de pagamento para o aceite da inserção do Pix Copia e Cola no processo de pagamento.
        
        Args:
            banco (Dict[str, Any]): The banco
            conta (Dict[str, Any]): The conta
            tipoEmissao (Dict[str, Any]): The emissao
            formaPagamento (Dict[str, Any]): The pagamento
            tipoPagamento (Dict[str, Any]): The pagamento
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "banco": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "conta": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "tipoEmissao": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "formaPagamento": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "tipoPagamento": {
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
            >>> api = ProcessoPagamento()
            >>> response = api._valida_dados_pagamento_para_aceitar_pix_copia_cola(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/ProcessoPagamento/ValidaDadosPagamentoParaAceitarPixCopiaCola"
        kwargs = {
            "banco": banco,
            "conta": conta,
            "tipoEmissao": tipo_emissao,
            "formaPagamento": forma_pagamento,
            "tipoPagamento": tipo_pagamento,
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

    def valida_dados_pagamento_para_aceitar_codigo_de_barras(
        self,
        banco: Optional[str] = None,
        conta: Optional[str] = None,
        tipo_emissao: Optional[str] = None,
        forma_pagamento: Optional[str] = None,
        tipo_pagamento: Optional[str] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/ProcessoPagamento/ValidaDadosPagamentoParaAceitarCodigoDeBarras`
        HTTP Method: `POST`
        
        Implementation Notes:
        Validações dos dados de pagamento para o aceite da inserção do Código de Barras no processo de pagamento.
        
        Args:
            banco (Dict[str, Any]): The banco
            conta (Dict[str, Any]): The conta
            tipoEmissao (Dict[str, Any]): The emissao
            formaPagamento (Dict[str, Any]): The pagamento
            tipoPagamento (Dict[str, Any]): The pagamento
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "banco": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "conta": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "tipoEmissao": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "formaPagamento": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "tipoPagamento": {
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
            >>> api = ProcessoPagamento()
            >>> response = api._valida_dados_pagamento_para_aceitar_codigo_de_barras(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/ProcessoPagamento/ValidaDadosPagamentoParaAceitarCodigoDeBarras"
        kwargs = {
            "banco": banco,
            "conta": conta,
            "tipoEmissao": tipo_emissao,
            "formaPagamento": forma_pagamento,
            "tipoPagamento": tipo_pagamento,
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

