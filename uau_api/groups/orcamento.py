"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Orcamento:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def alterar_insumo_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        composicao: Optional[str] = None,
        insumo: Optional[str] = None,
        usuario: Optional[str] = None,
        quantidade: Optional[int] = None,
        preco: Optional[int] = None,
        tipo_insumo: Optional[int] = None,
        encargo: Optional[int] = None
    ) -> dict:
        """Alterar insumo no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/AlterarInsumoOrcamento"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "orcamento": orcamento,
                "composicao": composicao,
                "insumo": insumo,
                "usuario": usuario,
                "quantidade": quantidade,
                "preco": preco,
                "tipoInsumo": tipo_insumo,
                "encargo": encargo,
            }
        )

    def excluir_insumo_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        composicao: Optional[str] = None,
        insumo: Optional[str] = None,
        usuario: Optional[str] = None,
        quantidade: Optional[int] = None,
        preco: Optional[int] = None,
        tipo_insumo: Optional[int] = None,
        encargo: Optional[int] = None
    ) -> dict:
        """Excluir insumo no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ExcluirInsumoOrcamento"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "orcamento": orcamento,
                "composicao": composicao,
                "insumo": insumo,
                "usuario": usuario,
                "quantidade": quantidade,
                "preco": preco,
                "tipoInsumo": tipo_insumo,
                "encargo": encargo,
            }
        )

    def inserir_insumo_orcamento(
        self,
        insumos_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """Inserir insumos no orçamento. Podem ser informados diversos insumos para que sejam inseridos em lote.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/InserirInsumoOrcamento"
        return self.api.post(
            path,
            json={
                "InsumosOrcamento": insumos_orcamento,
            }
        )

    def alterar_servico_orcamento(
        self,
        usuario: Optional[str] = None,
        quantidade: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Alterar serviço no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/AlterarServicoOrcamento"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "quantidade": quantidade,
                "dataInicio": data_inicio,
                "dataFim": data_fim,
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def excluir_servico_orcamento(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Exclui serviço ou item do orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ExcluirServicoOrcamento"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def inserir_servico_orcamento(
        self,
        servicos_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """Inserir serviços no orçamento. Podem ser informados diversos serviços para que sejam inseridos em lote.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/InserirServicoOrcamento"
        return self.api.post(
            path,
            json={
                "ServicosOrcamento": servicos_orcamento,
            }
        )

    def consultar_insumos_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        composicao: Optional[str] = None
    ) -> dict:
        """Consultar a tabela PlanilhaCronograma pela sua chave

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ConsultarInsumosPorChave"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "orcamento": orcamento,
                "composicao": composicao,
            }
        )

    def alterar_planilha_cronograma(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None
    ) -> dict:
        """Alterar cronograma no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/AlterarPlanilhaCronograma"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "periodo": periodo,
                "quantidade": quantidade,
            }
        )

    def excluir_planilha_cronograma(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None
    ) -> dict:
        """Excluir cronograma no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ExcluirPlanilhaCronograma"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "periodo": periodo,
                "quantidade": quantidade,
            }
        )

    def inserir_planilha_cronograma(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None
    ) -> dict:
        """Inserir cronograma no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/InserirPlanilhaCronograma"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "periodo": periodo,
                "quantidade": quantidade,
            }
        )

    def exportar_orcamento_estrutura(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None
    ) -> dict:
        """Exportar orçamento com suas estruturas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ExportarOrcamentoEstrutura"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "orcamento": orcamento,
            }
        )

    def consultar_estrutura_orca_por_chave(
        self,
        sequencia: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Consultar estrutura de serviço do orçamento de acordo com a chave do orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ConsultarEstruturaOrcaPorChave"
        return self.api.post(
            path,
            json={
                "sequencia": sequencia,
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def consultar_estrutura_orca_por_servico(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Consultar as estruturas do orçamento para um determinado serviço.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ConsultarEstruturaOrcaPorServico"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def consultar_servico_orcamento_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Buscar os serviços do orçamento de acordo com a chave do orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ConsultarServicoOrcamentoPorChave"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def consultar_servico_orcado_desintegrado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None
    ) -> dict:
        """Consultar serviço orçado desintegrado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ConsultarServicoOrcadoDesintegrado"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
            }
        )

    def excluir_estrutura_servico_de_orcamento(
        self,
        estruturas_de_servico_de_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """Excluir uma determinada estrutura de serviço no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite excluir níveis ou itens de estruturas do serviço do orçamento.

Deve preencher os parâmetros de acordo com a estrutura que deseja excluir.
  1.1 Informar se é nível ou item que esta excluindo, a sequencia e os dados do orçamento e serviço.
Valida se a estrutura poderá ser excluída.
Valida campos obrigatórios.
Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem excluídas.

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/776140/


        """
        path = "Orcamento/ExcluirEstruturaServicoDeOrcamento"
        return self.api.post(
            path,
            json={
                "EstruturasDeServicoDeOrcamento": estruturas_de_servico_de_orcamento,
            }
        )

    def inserir_estrutura_servico_de_orcamento(
        self,
        estruturas_de_servico_de_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """Inserir estrutura para um determinado serviço no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite inserir níveis ou itens de estruturas no serviço existente no orçamento.

Deve preencher os parâmetros de acordo com a estrutura que deseja inserir.
  1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
Valida se a estrutura poderá ser inserida.
Valida campos obrigatórios.
Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/776144/


        """
        path = "Orcamento/InserirEstruturaServicoDeOrcamento"
        return self.api.post(
            path,
            json={
                "EstruturasDeServicoDeOrcamento": estruturas_de_servico_de_orcamento,
            }
        )

    def consultar_planilha_cronograma_por_chave(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        periodo: Optional[str] = None
    ) -> dict:
        """Consultar a tabela PlanilhaCronograma pela sua chave

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ConsultarPlanilhaCronogramaPorChave"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "item": item,
                "servico": servico,
                "periodo": periodo,
            }
        )

    def atualizar_estrutura_servico_de_orcamento(
        self,
        estruturas_de_servico_de_orcamento: Optional[List[Dict]] = None
    ) -> dict:
        """Atualizar a quantidade e/ou preço de uma lista de estruturas de serviço no orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite alterar níveis ou itens de uma estrutura do serviço existente no orçamento

Deve preencher os parâmetros de acordo com a estrutura que deseja alterar .
  1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
Valida se a estrutura poderá ser alterada.
Valida campos obrigatórios.
Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/776147/


        """
        path = "Orcamento/AtualizarEstruturaServicoDeOrcamento"
        return self.api.post(
            path,
            json={
                "EstruturasDeServicoDeOrcamento": estruturas_de_servico_de_orcamento,
            }
        )

    def consultar_servico_orcamento_por_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_orcamento: Optional[int] = None,
        tipo_item: Optional[int] = None
    ) -> dict:
        """Buscar os serviços do orçamento de acordo com o código do orçamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Orcamento/ConsultarServicoOrcamentoPorOrcamento"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "numOrcamento": num_orcamento,
                "tipoItem": tipo_item,
            }
        )

