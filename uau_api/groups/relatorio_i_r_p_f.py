"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class RelatorioIRPF:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gerar_pdfrel_irpf(
        self,
        vendasobras_empresa: Optional[List[Dict]] = None,
        ano_base: Optional[int] = None,
        naomostradados_venda: Optional[bool] = None
    ) -> dict:
        """Método responsável por gerar o PDF do IRPF

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.

A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
Substituir cada parâmetro pelo valor correspondente:

"Venda" - Número da Venda.
"Obra" - Código da Obra.
"Empresa" - Número da Empresa.
"ano_base" - ano base para geração do IRPF.
"naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
  {
        "vendasobras_empresa" [
            [
            "Venda", 
            "Obra", 
            "Empresa"
            ]
        ],
            "ano_base": 2018,
            "naomostradados_venda": true
    }
  


Segue exemplo  após substituição dos parâmetros:
      {
             "vendasobras_empresa" [
               [
               "838",
               "424V",
               "308"
               ]
           ],
             "ano_base": 2021,
             "naomostradados_venda": false
        }
  




        """
        path = "RelatorioIRPF/GerarPDFRelIRPF"
        return self.api.post(
            path,
            json={
                "vendasobras_empresa": vendasobras_empresa,
                "ano_base": ano_base,
                "naomostradados_venda": naomostradados_venda,
            }
        )

    def gerar_pdfrel_irpfv2(
        self,
        vendasobras_empresa: Optional[List[Dict]] = None,
        ano_base: Optional[int] = None,
        naomostradados_venda: Optional[bool] = None
    ) -> dict:
        """Método responsável por gerar o PDF do IRPF

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.

A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
Substituir cada parâmetro pelo valor correspondente:

"Venda" - Número da Venda.
"Obra" - Código da Obra.
"Empresa" - Número da Empresa.
"ano_base" - ano base para geração do IRPF.
"naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
  {
        "vendasobras_empresa" [
            [
            "Venda", 
            "Obra", 
            "Empresa"
            ]
        ],
            "ano_base": 2018,
            "naomostradados_venda": true
    }
  


Segue exemplo  após substituição dos parâmetros:
      {
             "vendasobras_empresa" [
               [
               "838",
               "424V",
               "308"
               ]
           ],
             "ano_base": 2021,
             "naomostradados_venda": false
        }
  




        """
        path = "RelatorioIRPF/GerarPDFRelIRPFV2"
        return self.api.post(
            path,
            json={
                "vendasobras_empresa": vendasobras_empresa,
                "ano_base": ano_base,
                "naomostradados_venda": naomostradados_venda,
            }
        )

