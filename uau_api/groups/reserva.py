"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Reserva:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gravar_reserva(
        self,
        dados_reserva_json: Optional[str] = None
    ) -> dict:
        """Grava ou altera uma reserva

        Implementation Notes:
        Definição técnica:  

Preencher os parâmetros de request para uso do método.
As contrabarras são impotantes para não encerrar a string antes do fim.
As datas devem estar no formato: AAAA-MM-DD.
SE O VALOR A SER PASSADO É NULL OU VAZIO, NÃO O INFORME NO JSON.
Troque apenas os ❌ pelos valores desejados.
o JSON deve ser uma string no seguinte formato:{
    "dados_reserva_json": 
    "[
      {
        \"reserva\": [
          {
            \"Empresa_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumProd_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumPer_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Num_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"CodDvg_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Vendedor_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Login_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Data_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Periodo_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Cliente_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Fone_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"TempoIndet_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Status_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumProposta_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"DataConfir_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"UsrConfir_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"UsrCancel_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"DataCancel_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumConf_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"CodPesConfir_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"GeraTaxaReserva_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"ValReserva_rsv\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"ReservaPaga_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Banco_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Conta_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumEs_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"EntSai_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"DataCad_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
          },
          {
            \"Empresa_rsv\": \"❌\",
            \"NumProd_rsv\": \"❌\",
            \"NumPer_rsv\": \"❌\",
            \"Num_rsv\": \"❌\",
            \"CodDvg_rsv\": \"❌\",
            \"Vendedor_rsv\": \"❌\",
            \"Login_rsv\": \"❌\",
            \"Data_rsv\": \"❌\",
            \"Periodo_rsv\": \"❌\",
            \"Cliente_rsv\": \"❌\",
            \"Fone_rsv\": \"❌\",
            \"TempoIndet_rsv\": \"❌\",
            \"Status_rsv\": \"❌\",
            \"NumProposta_rsv\": \"❌\",
            \"DataConfir_rsv\": \"❌\",
            \"UsrConfir_rsv\": \"❌\",
            \"UsrCancel_rsv\": \"❌\",
            \"DataCancel_rsv\": \"❌\",
            \"NumConf_rsv\": \"❌\",
            \"CodPesConfir_rsv\": \"❌\",
            \"GeraTaxaReserva_rsv\": \"❌\",
            \"ValReserva_rsv\": \"❌\",
            \"ReservaPaga_rsv\": \"❌\",
            \"Banco_rsv\": \"❌\",
            \"Conta_rsv\": \"❌\",
            \"NumEs_rsv\": \"❌\",
            \"EntSai_rsv\": \"❌\",
            \"DataCad_rsv\": \"❌\"
          }
        ]
      },
      {
        \"Taxa\": [
          {
            \"Empresa_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Banco_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Conta_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Num_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"EntSai_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Obra_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Data_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Usuario_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Valor_es\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Natureza_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Cap_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"MesPL_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumDoc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"Emissao_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"HistLanc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"CategMovFin_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumAplic_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"StatusAplic_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"NumSeq_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
            \"DataCad_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
          },
          {
            \"Empresa_es\": \"❌\",
            \"Banco_es\": \"❌\",
            \"Conta_es\": \"❌\",
            \"Num_es\": \"❌\",
            \"EntSai_es\": \"❌\",
            \"Obra_es\": \"❌\",
            \"Data_es\": \"❌\",
            \"Usuario_es\": \"❌\",
            \"Valor_es\": \"❌\",
            \"Natureza_es\": \"❌\",
            \"Cap_es\": \"❌\",
            \"MesPL_es\": \"❌\",
            \"NumDoc_es\": \"❌\",
            \"Emissao_es\": \"❌\",
            \"HistLanc_es\": \"❌\",
            \"CategMovFin_es\": \"❌\",
            \"NumAplic_es\": \"❌\",
            \"StatusAplic_es\": \"❌\",
            \"NumSeq_es\": \"❌\",
            \"DataCad_es\": \"❌\"
          }
        ]
      }
    ]"
  }
  




        """
        path = "Reserva/GravarReserva"
        return self.api.post(
            path,
            json={
                "dados_reserva_json": dados_reserva_json,
            }
        )

    def excluir_reserva(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_proposta: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        cod_reserva: Optional[int] = None
    ) -> dict:
        """Excluir uma reserva

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Valida usuário e permissões


        """
        path = "Reserva/ExcluirReserva"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_proposta": num_proposta,
                "cod_produto": cod_produto,
                "cod_person": cod_person,
                "cod_reserva": cod_reserva,
            }
        )

    def consultar_reservas(
        self,
        empresa: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict:
        """Consulta as reservas da personalização filtrando por status

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta reservas da personalização que possuem o status informado na request.


        """
        path = "Reserva/ConsultarReservas"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "cod_produto": cod_produto,
                "cod_person": cod_person,
                "status": status,
            }
        )

    def consultar_reserva_vendedor(
        self,
        empresa: Optional[int] = None,
        num_prod: Optional[int] = None,
        num_per: Optional[int] = None,
        vendedor: Optional[int] = None
    ) -> dict:
        """Consulta a reserva da personalização filtrando pelo vendedor

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint

Definição de Negócio:

Valida usuário e permissões


        """
        path = "Reserva/ConsultarReservaVendedor"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "num_prod": num_prod,
                "num_per": num_per,
                "vendedor": vendedor,
            }
        )

    def consultar_reserva_por_codigo(
        self,
        empresa: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        cod_reserva: Optional[int] = None
    ) -> dict:
        """Consulta as reservas da personalização filtrando pelo código

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta todas as reservas da personalização que tem o código informado.
Valida usuário e suas permissões.


        """
        path = "Reserva/ConsultarReservaPorCodigo"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "cod_produto": cod_produto,
                "cod_person": cod_person,
                "cod_reserva": cod_reserva,
            }
        )

    def consulta_reserva_por_proposta(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_proposta: Optional[int] = None
    ) -> dict:
        """Consulta as reservas da personalização filtrando po código

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Valida usuário e permissões


        """
        path = "Reserva/ConsultaReservaPorProposta"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_proposta": num_proposta,
            }
        )

    def consultar_dados_controle_reserva(
        self,
        empresa: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_person: Optional[int] = None,
        status: Optional[str] = None
    ) -> dict:
        """Cosulta dados da reserva

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Valida usuário e permissões.


        """
        path = "Reserva/ConsultarDadosControleReserva"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "cod_produto": cod_produto,
                "cod_person": cod_person,
                "status": status,
            }
        )

