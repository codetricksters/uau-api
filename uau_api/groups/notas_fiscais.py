"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class NotasFiscais:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_nfentrada(
        self,
        listanf_entrada: Optional[List[Dict]] = None,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        cnpj_fornecedor: Optional[str] = None,
        codigo_fornecedor: Optional[str] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
        tipo_periodo: Optional[Any] = None
    ) -> dict:
        """Listagem de nota fiscal

        Implementation Notes:
         Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Ao menos uma chave de pesquisa deve ser preenchida sendo elas ([CodigoEmpresa],
  [CnpjFornecedor], [CodigoFornecedor], [DataInicial], [ListaNFEntrada]).
Caso tenha informado a propriedade da Obra, a Empresa torna-se obrigatória.
Preenchimento da [DataInicial] torna [DataFinal] obrigatória.
Preenchimento da [DataFinal] torna [DataInicial] obrigatória.
Obra só vai achar informação se a nota estiver vinculada a um processo.
[ListaNFEntrada] Cada objeto deve ter obrigatoriamente o [CodigoEmpresa] e o [NumeroNotaFiscal ou NumeroNotaFiscalEletronica]
  6.1 NumeroNotaFiscal = Número de controle da nota fiscal (Obs: no retorno dos dados esse valor fica no campo Numero)
  6.2 NumeroNotaFiscalEletronica = Número da nota fiscal eletrônica, informado na DANFE ou NFS-e (Obs: no retorno dos dados esse valor fica no campo NumeroNotaFiscal)


        """
        path = "NotasFiscais/ConsultarNFEntrada"
        return self.api.post(
            path,
            json={
                "ListaNFEntrada": listanf_entrada,
                "CodigoEmpresa": codigo_empresa,
                "CodigoObra": codigo_obra,
                "CnpjFornecedor": cnpj_fornecedor,
                "CodigoFornecedor": codigo_fornecedor,
                "DataInicial": data_inicial,
                "DataFinal": data_final,
                "TipoPeriodo": tipo_periodo,
            }
        )

    def salvar_arquivo_xmlnotafiscal_entrada(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """Salvar o arquivo XML das notas fiscais para importação no sistema.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Poderá ser enviado uma lista de arquivos XML.
Será permitido no máximo uma lista com 20 arquivos.
Tipo do arquivo XML [TipoXML]
   0 para NF-e
   1 para CT-e
   2 para NFS-e,
Arquivo XML da nota fiscal (Texto do arquivo) [ArquivoXML].


        """
        path = "NotasFiscais/SalvarArquivoXMLnotafiscalEntrada"
        return self.api.post(
            path,
            json=parameters if parameters is not None else {}
        )

