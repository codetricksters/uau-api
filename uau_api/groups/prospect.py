"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Prospect:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gravar_prospect(
        self,
        permitir_responsavel_sem_estrutura: Optional[bool] = None,
        login: Optional[str] = None,
        prospect: Optional[Dict] = None,
        prospect_fis: Optional[Dict] = None,
        prospect_interesse: Optional[Dict] = None,
        prospect_interesse_produtos: Optional[List[Dict]] = None,
        prospect_interesse_bairros: Optional[List[Dict]] = None,
        prospect_telefones: Optional[List[Dict]] = None,
        prospect_endereco_principal: Optional[Dict] = None,
        prospect_endereco_cobranca: Optional[Dict] = None,
        prospect_endereco_comercial: Optional[Dict] = None,
        prospect_dependente: Optional[List[Dict]] = None,
        responsavel: Optional[str] = None,
        buscou_de_pessoas: Optional[bool] = None,
        atualizar_pessoas: Optional[bool] = None,
        mensagem_retorno: Optional[str] = None,
        prospect_doc: Optional[List[Dict]] = None
    ) -> dict:
        """Grava as informações do prospect

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Grava as informações do prospect.
Os dados informados passam por validações.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Prospect/GravarProspect"
        return self.api.post(
            path,
            json={
                "permitirResponsavelSemEstrutura": permitir_responsavel_sem_estrutura,
                "login": login,
                "prospect": prospect,
                "prospectFis": prospect_fis,
                "prospectInteresse": prospect_interesse,
                "prospectInteresseProdutos": prospect_interesse_produtos,
                "prospectInteresseBairros": prospect_interesse_bairros,
                "prospectTelefones": prospect_telefones,
                "prospectEnderecoPrincipal": prospect_endereco_principal,
                "prospectEnderecoCobranca": prospect_endereco_cobranca,
                "prospectEnderecoComercial": prospect_endereco_comercial,
                "prospectDependente": prospect_dependente,
                "responsavel": responsavel,
                "buscouDePessoas": buscou_de_pessoas,
                "atualizarPessoas": atualizar_pessoas,
                "mensagemRetorno": mensagem_retorno,
                "prospectDoc": prospect_doc,
            }
        )

    def importar_prospect(
        self,
        xml: Optional[str] = None
    ) -> dict:
        """Realiza a importação de prospects para o UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Importa prospects para dentro do UAU.
Valida usuário e permissões.
Valida arquivo XML.

Informação:

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Prospect/ImportarProspect"
        return self.api.post(
            path,
            json={
                "xml": xml,
            }
        )

    def listar_grau_parentesco(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        path = "Prospect/ListarGrauParentesco"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def migrar_prospect_pessoa(
        self,
        numero_prospect: Optional[int] = None
    ) -> dict:
        """Realiza a migração dos dados do prospect para pessoa

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Migra um prospect para pessoa.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Prospect/MigrarProspectPessoa"
        return self.api.post(
            path,
            json={
                "numeroProspect": numero_prospect,
            }
        )

    def consultar_todos_prospects(
        self,
        enum_opcao_todos: Optional[int] = None,
        codigo_prospect: Optional[str] = None,
        codigo_vendedor: Optional[int] = None
    ) -> dict:
        """Consultar todos os prospects

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta os prospects de acordo com os parâmetros definidos na request.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Prospect/ConsultarTodosProspects"
        return self.api.post(
            path,
            json={
                "enumOpcaoTodos": enum_opcao_todos,
                "codigoProspect": codigo_prospect,
                "codigoVendedor": codigo_vendedor,
            }
        )

    def consultar_prospect_por_chave(
        self,
        codigo_prospect: Optional[int] = None
    ) -> dict:
        """Consultar prospect por código

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta determinado prospect filtrando pelo número deste prospect.

Informação:

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Prospect/ConsultarProspectPorChave"
        return self.api.post(
            path,
            json={
                "codigoProspect": codigo_prospect,
            }
        )

    def alterar_responsavel_prospect(
        self,
        novo_responsavel: Optional[int] = None,
        cod_empresa: Optional[int] = None,
        num_prospect: Optional[int] = None
    ) -> dict:
        """Alterar responsável do prospect

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Alterar responsável do prospect.
Os dados informados passam por validações.
O campo codEmpresa não é obrigatório, porém, se informado será validado se na configuração da empresa está marcado para 
  "Realizar venda somente se o vendedor estiver em uma estrutura de comissão", e caso o novo responsável não esteja em nenhuma
  estrutura de comissão, não será possível incluir. Caso não esteja marcado a configuração ou o codEmpresa não for informado,
  será possível alterar para qualquer novo responsável, desde que esteja ativo.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Prospect/AlterarResponsavelProspect"
        return self.api.post(
            path,
            json={
                "novoResponsavel": novo_responsavel,
                "codEmpresa": cod_empresa,
                "numProspect": num_prospect,
            }
        )

    def consultar_prospect_com_filtro(
        self,
        numero_opcao: Optional[int] = None,
        numero_visao: Optional[int] = None,
        prospect_sem_responsavel: Optional[bool] = None,
        codigo_responsavel: Optional[str] = None,
        nome_pessoa: Optional[str] = None,
        telefone: Optional[str] = None,
        cpf_cnpj: Optional[str] = None,
        trata_sem_responsavel: Optional[bool] = None,
        uf_prosp: Optional[str] = None
    ) -> dict:
        """Consulta prospect de acordo com as informações do request

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta prospect filtrando os parâmentros inseridos da request.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Prospect/ConsultarProspectComFiltro"
        return self.api.post(
            path,
            json={
                "numeroOpcao": numero_opcao,
                "numeroVisao": numero_visao,
                "prospectSemResponsavel": prospect_sem_responsavel,
                "codigoResponsavel": codigo_responsavel,
                "nomePessoa": nome_pessoa,
                "telefone": telefone,
                "cpfCnpj": cpf_cnpj,
                "trataSemResponsavel": trata_sem_responsavel,
                "ufProsp": uf_prosp,
            }
        )

    def buscar_grau_parentesco_por_codigo(
        self,
        codigo: Optional[int] = None
    ) -> dict:
        path = "Prospect/BuscarGrauParentescoPorCodigo"
        return self.api.post(
            path,
            json={
                "Codigo": codigo,
            }
        )

