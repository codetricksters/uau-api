"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Medicao:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def manter_medicao(
        self,
        empresa: Optional[int] = None,
        numero_contrato: Optional[int] = None,
        numero_medicao: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cnpj_fornecedor: Optional[str] = None,
        num_cidade_prestacao_serv: Optional[int] = None,
        observacao: Optional[str] = None,
        ultima_medicao: Optional[int] = None,
        data_base: Optional[datetime] = None,
        usr_cadastro: Optional[str] = None,
        descontos_medicao: Optional[List[Dict]] = None,
        itens: Optional[List[Dict]] = None,
        adiantamentos: Optional[List[Dict]] = None
    ) -> dict:
        """Método com finalidade de inserir ou atualizar uma determinada medição de contrato de material e serviço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras básicas:

É possível inserir ou atualizar uma medição de contrato de material e/ou serviço.
  1.2. Se o número da medição for informado e essa medição existir, então ela será atualzada, caso contrário será inserida.
Só poderão ser atualizadas as medições que estiverem em aberto, ou seja, sem nenhuma confirmação de aprovação.
Os adiantamentos de contratos podem ser informados de duas formas, dependendo do tipo de vínculo de planejamento do contrato, se for vinculado por item, pode ser informado diretamente no item específico, 
  ou de forma geral, onde nesse caso será feito o cálculo proporcional, se o vínculo do planejamento for somente por contrato ou não possuir vínculo algum, só pode ser informado o adiantamento geral.


        """
        path = "Medicao/ManterMedicao"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "NumeroContrato": numero_contrato,
                "NumeroMedicao": numero_medicao,
                "CodigoFornecedor": codigo_fornecedor,
                "CNPJFornecedor": cnpj_fornecedor,
                "NumCidadePrestacaoServ": num_cidade_prestacao_serv,
                "Observacao": observacao,
                "UltimaMedicao": ultima_medicao,
                "DataBase": data_base,
                "UsrCadastro": usr_cadastro,
                "DescontosMedicao": descontos_medicao,
                "Itens": itens,
                "Adiantamentos": adiantamentos,
            }
        )

    def excluir_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        numero_medicao: Optional[int] = None
    ) -> dict:
        """Método com finalidade de excluir uma determinada medição de contrato de material e serviço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras básicas:

Somente medições que estiverem abertas e sem nenhuma aprovação poderão ser excluídas.
Nenhum processo de pagamento poderá estar vinculado à medição.
Nâo pode haver vínculos dependentes entre os itens da medição (vínculo de item do tipo material com item de serviço).
Não pode excluir medição que contenha itens que tenham gerado valores excedentes para itens de outras medições.


        """
        path = "Medicao/ExcluirMedicao"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Contrato": contrato,
                "NumeroMedicao": numero_medicao,
            }
        )

    def consultar_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """Consultar medição por empresa, contrato e código da medição.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Medicao/ConsultarMedicao"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
                "medicao": medicao,
            }
        )

    def consultar_itens_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """Consultar itens de medição por empresa, contrato e medição.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Retorna uma lista de itens da medição por empresa, contrato e medição.


        """
        path = "Medicao/ConsultarItensMedicao"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
                "medicao": medicao,
            }
        )

    def aprovar_medicoes_contrato(
        self,
        medicoes: Optional[List[Dict]] = None
    ) -> dict:
        """Método com finalidade de aprovar medições de contrato de material e serviço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras básicas:

O contrato precisa estar com status aprovado.
É necessário permissão de aprovação para o programa OBMEDCONT


        """
        path = "Medicao/AprovarMedicoesContrato"
        return self.api.post(
            path,
            json={
                "Medicoes": medicoes,
            }
        )

    def consultar_boletim_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        avanco_fisico: Optional[bool] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """Consultar boletim de medição.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta boletim de medição dentro do sistema UAU.


        """
        path = "Medicao/ConsultarBoletimMedicao"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
                "avancoFisico": avanco_fisico,
                "medicao": medicao,
            }
        )

    def consultar_medicao_completa(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None,
        cnpj_contratado: Optional[str] = None,
        cnpj_fornecedor: Optional[str] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None
    ) -> dict:
        """Método com finalidade de consultar as medições de contrato de material e serviço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Para retornar as medições, podem ser feitas as seguintes combinações:
1. Código da empresa e código do contrato
  2. Código da empresa, código do contrato e código da medição
  3. Código da empresa e CNPJ do contrato ou CNPJ do fornecedor (informado na medição)
  4. Código da empresa e período de geração da medição (data inicial e data final)
  
        """
        path = "Medicao/ConsultarMedicaoCompleta"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Contrato": contrato,
                "Medicao": medicao,
                "CNPJContratado": cnpj_contratado,
                "CNPJFornecedor": cnpj_fornecedor,
                "DataInicial": data_inicial,
                "DataFinal": data_final,
            }
        )

    def consultar_medicao_por_serv_mat(
        self,
        empresa: Optional[int] = None,
        serv_mat: Optional[str] = None
    ) -> dict:
        """Consultar medição por empresa, contrato e código da medição.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Medicao/ConsultarMedicaoPorServMat"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "servMat": serv_mat,
            }
        )

    def consultar_medicoes_por_status(
        self,
        status_med: Optional[int] = None,
        login_usu: Optional[str] = None
    ) -> dict:
        """Consultar medições por status e usuário.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Retorna uma lista de medições por status e usuário.
Os possíveis status de uma medição são: 
  0 - Aberta;
  1 - Aprovada;
  2 - Medida;
  3 - Proc. Serviço Gerado.
O usuário é para indicar quais são as obras que ele possui permissão para retornar as medições pertinentes.


        """
        path = "Medicao/ConsultarMedicoesPorStatus"
        return self.api.post(
            path,
            json={
                "status_med": status_med,
                "login_usu": login_usu,
            }
        )

    def validar_cnpjao_gravar_medicao(
        self,
    ) -> dict:
        path = "/api/Medicao/ValidarCNPJAoGravarMedicao"
        return self.api.post(
            path,
            json={
            }
        )

    def consultar_medicao_por_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """Consultar medição por contrato.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Medicao/ConsultarMedicaoPorContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
            }
        )

    def consultar_itens_medicao_por_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None
    ) -> dict:
        """Consultar itens de medição por medição.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Medicao/ConsultarItensMedicaoPorMedicao"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
                "medicao": medicao,
            }
        )

    def consultar_itens_medicao_por_serv_mat(
        self,
        empresa: Optional[int] = None,
        serv_mat: Optional[str] = None
    ) -> dict:
        """Consultar itens de medição por empresa e serviço/material.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Medicao/ConsultarItensMedicaoPorServMat"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "servMat": serv_mat,
            }
        )

    def consultar_itens_medicao_por_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """Consultar itens de medição por contrato.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Medicao/ConsultarItensMedicaoPorContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
            }
        )

    def consultar_itens_medicao_por_item_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None,
        item_contrato: Optional[int] = None
    ) -> dict:
        """Consultar itens de medição por item de contrato.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Medicao/ConsultarItensMedicaoPorItemContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
                "medicao": medicao,
                "itemContrato": item_contrato,
            }
        )

