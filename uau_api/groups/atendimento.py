"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Atendimento:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gerar_pendencia(
        self,
        usuariouau_destino: Optional[str] = None,
        data_prevista: Optional[datetime] = None,
        data_aviso: Optional[datetime] = None,
        hora_aviso: Optional[datetime] = None,
        mensagem: Optional[str] = None,
        geraremail_interno: Optional[bool] = None,
        gerar_email_externo: Optional[bool] = None,
        gerar_aviso: Optional[bool] = None,
        categoria: Optional[str] = None
    ) -> dict:
        """Criar uma pendência do UAU com as informações informada

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/GerarPendencia"
        return self.api.post(
            path,
            json={
                "usuariouau_destino": usuariouau_destino,
                "data_prevista": data_prevista,
                "data_aviso": data_aviso,
                "hora_aviso": hora_aviso,
                "mensagem": mensagem,
                "geraremail_interno": geraremail_interno,
                "gerar_email_externo": gerar_email_externo,
                "gerar_aviso": gerar_aviso,
                "categoria": categoria,
            }
        )

    def gravar_atendimento(
        self,
        atendimento: Optional[Dict] = None
    ) -> dict:
        """Gravar atendimento no Uau.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Atendimento/GravarAtendimento
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite Gravar o Atendimento.

Deve montar uma estrutura com as informações do Atendimento verificando os parâmetros obrigatórios.
Será apenas registrado Atendimentos com o status [0 - Em Aberto].
Caso não seja informado: usrrespon_atd, numccm_atd e usrcad_atd, será obrigatório ter configurado o serviço atendimento uauweb no CRM. CRM - Utilitários - Configurações de serviço
Para informar a unidade do atendimento é obrigatório informar a empresa, obra e produto. Caso não informe a empresa, vamos desconsiderar essa informação e gravar o atendimento.

VirtUau:

https://ajuda.globaltec.com.br/virtuau/configuracao-de-atendimento-do-uau-web/


        """
        path = "Atendimento/GravarAtendimento"
        return self.api.post(
            path,
            json={
                "atendimento": atendimento,
            }
        )

    def consultar_pendencia(
        self,
        numero: Optional[int] = None,
        data_lancamento: Optional[datetime] = None,
        responsavel_resolucao: Optional[str] = None
    ) -> dict:
        """Consulta as pendências

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarPendencia"
        return self.api.post(
            path,
            json={
                "numero": numero,
                "data_lancamento": data_lancamento,
                "responsavel_resolucao": responsavel_resolucao,
            }
        )

    def consultar_atendimento(
        self,
        codigo_atendimento: Optional[int] = None
    ) -> dict:
        """Método que consulta atendimento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarAtendimento"
        return self.api.post(
            path,
            json={
                "codigo_atendimento": codigo_atendimento,
            }
        )

    def consultar_categ_de_coment_ativas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta as categorias de comentários ativas.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarCategDeComentAtivas"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_pendencia_observacao(
        self,
        numero_pendencia: Optional[int] = None,
        dataquando_lancou: Optional[datetime] = None,
        usuario_resolve: Optional[str] = None
    ) -> dict:
        """Consulta as etapas (pendências).

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarPendenciaObservacao"
        return self.api.post(
            path,
            json={
                "numero_pendencia": numero_pendencia,
                "dataquando_lancou": dataquando_lancou,
                "usuario_resolve": usuario_resolve,
            }
        )

    def vincular_arquivo_ao_atendimento(
        self,
        arquivo: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        num_atendimento: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Vincular arquivo ao atendimento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/VincularArquivoAoAtendimento"
        return self.api.post(
            path,
            json={
                "arquivo": arquivo,
                "nome_arquivo": nome_arquivo,
                "num_atendimento": num_atendimento,
                "usuario": usuario,
            }
        )

    def consultar_atendimento_por_pessoa(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """Realiza consulta de atendimentos do cliente independente de categorias configuradas para o Uau Web.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarAtendimentoPorPessoa"
        return self.api.post(
            path,
            json={
                "codigo_pessoa": codigo_pessoa,
            }
        )

    def consultar_empreendimentos_cliente(
        self,
        cod_pessoa: Optional[int] = None
    ) -> dict:
        """Consultar todos os empreendimentos do cliente do qual ele é titular da venda.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarEmpreendimentosCliente"
        return self.api.post(
            path,
            json={
                "cod_pessoa": cod_pessoa,
            }
        )

    def consultar_categoria_atendimento_web(
        self,
        tipo_atend: Optional[str] = None
    ) -> dict:
        """Consulta as categorias de atendimento web.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarCategoriaAtendimentoWeb"
        return self.api.post(
            path,
            json={
                "tipo_atend": tipo_atend,
            }
        )

    def consultar_numero_work_flow_vinculado(
        self,
        numerovinculo_workflow: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """Consulta o número do workflow vinculado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarNumeroWorkFlowVinculado"
        return self.api.post(
            path,
            json={
                "numerovinculo_workflow": numerovinculo_workflow,
                "empresa": empresa,
                "obra": obra,
            }
        )

    def consultar_pendencias_por_numero_vinculo(
        self,
        numero_vinculo: Optional[int] = None
    ) -> dict:
        """Consulta as etapas(pendências) de um atendimento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarPendenciasPorNumeroVinculo"
        return self.api.post(
            path,
            json={
                "numero_vinculo": numero_vinculo,
            }
        )

    def gerar_atendimento_por_chat_online_cliente(
        self,
        dados_atendimento: Optional[Dict] = None
    ) -> dict:
        """Gerar o atendimento para um cliente do atendimento online do cliente.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/GerarAtendimentoPorChatOnlineCliente"
        return self.api.post(
            path,
            json={
                "dados_atendimento": dados_atendimento,
            }
        )

    def consultar_atendimento_detalhado_por_chave(
        self,
        codigo_atendimento: Optional[int] = None
    ) -> dict:
        """Consulta atendimento detalhado por código do atendimento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarAtendimentoDetalhadoPorChave"
        return self.api.post(
            path,
            json={
                "codigo_atendimento": codigo_atendimento,
            }
        )

    def consultar_configuracao_atendimento_uauweb(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Método que consulta as configurações do uauweb.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarConfiguracaoAtendimentoUAUWEB"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_atendimento_por_categorias_uau_web(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """Realiza consulta de atendimentos do cliente por categorias de comentários configuradas para o Uau Web.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarAtendimentoPorCategoriasUauWeb"
        return self.api.post(
            path,
            json={
                "codigo_pessoa": codigo_pessoa,
            }
        )

    def consultar_atendimento_por_pessoa_comentario(
        self,
        codigo_pessoa: Optional[int] = None,
        lista_categoria: Optional[List[Dict]] = None,
        periodo_incio: Optional[datetime] = None,
        periodo_fim: Optional[datetime] = None
    ) -> dict:
        """Consulta atendimento pelo pessoa e código da categoria de comentário

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarAtendimentoPorPessoaComentario"
        return self.api.post(
            path,
            json={
                "codigo_pessoa": codigo_pessoa,
                "lista_categoria": lista_categoria,
                "periodo_incio": periodo_incio,
                "periodo_fim": periodo_fim,
            }
        )

    def consultar_unidades_do_empreendimento_cliente(
        self,
        obra: Optional[str] = None,
        empresa: Optional[int] = None,
        cod_pessoa: Optional[int] = None
    ) -> dict:
        """Método que consulta a data prevista para término do atendimento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarUnidadesDoEmpreendimentoCliente"
        return self.api.post(
            path,
            json={
                "obra": obra,
                "empresa": empresa,
                "cod_pessoa": cod_pessoa,
            }
        )

    def consultar_data_prevista_de_termino_atendimento(
        self,
        numerovinculo_workflow: Optional[int] = None,
        numero_workflow: Optional[int] = None
    ) -> dict:
        """Método que consulta a data prevista para término do atendimento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarDataPrevistaDeTerminoAtendimento"
        return self.api.post(
            path,
            json={
                "numerovinculo_workflow": numerovinculo_workflow,
                "numero_workflow": numero_workflow,
            }
        )

    def consultar_numero_vinculo_categoria_de_comentario_com_work_flow(
        self,
        codigo_categoria: Optional[str] = None
    ) -> dict:
        """Método que consulta o número do vinculo da categoria de comentário com o workflow.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Atendimento/ConsultarNumeroVinculoCategoriaDeComentarioComWorkFlow"
        return self.api.post(
            path,
            json={
                "codigo_categoria": codigo_categoria,
            }
        )

