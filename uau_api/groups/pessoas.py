"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Pessoas:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gravar_pessoa(
        self,
        nao_validar_campos_obrigatorios: Optional[bool] = None,
        info_pes: Optional[Dict] = None,
        info_pesfis: Optional[Dict] = None,
        infopes_jur: Optional[Dict] = None,
        dspes_tel_json: Optional[str] = None,
        infopes_doc: Optional[Dict] = None,
        info_pesendereco_principal: Optional[Dict] = None,
        infopesendereco_cobranca: Optional[Dict] = None,
        infopesendereco_comercial: Optional[Dict] = None
    ) -> dict:
        """Insere ou altera Pessoa Física ou Jurídica e seus dados

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite inserir ou alterar pessoa física ou jurídica e seus respectivos dados. Se for uma nova pessoa, informar "0" no parâmetro cod_pes.
  Se for alterar uma pessoa já existente, informar o código no parâmetro cod_pes.

Deve montar uma estrutura com as informações de determinada pessoa.
https://ajuda.globaltec.com.br/download/801043/
Valida a estrutura do e-mail
Valida se o nome de usuário informado para acesso ao uau web existe para outra pessoa
Valida campos obrigatórios
O campo dspes_tel_json espera uma String json no formato abaixo.
  "dspes_tel_json": [ { \"PesTel\": 
  [ { \"ddd_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
     \"fone_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
     \"ram_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
     \"tipo_tel\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
     \"TipoTel_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
     \"ExisteTel_tel\": \"System.Boolean, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
     \"Principal_tel\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"},
  { \"ddd_tel\": \"62\", \"fone_tel\": \"39529100\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
  { \"ddd_tel\": \"62\", \"fone_tel\": \"81129773\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
  { \"ddd_tel\": \"62\", \"fone_tel\": \"3952-9149\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
  { \"ddd_tel\": \"62\", \"fone_tel\": \"984689664\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
  { \"ddd_tel\": \"62\", \"fone_tel\": \"39529136\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ] }]"

Sempre a primeira linha do json é a estrutura do mesmo, então ela sempre irá se repetir, apartir dela, as proximas serão os telefones. No exemplo tempo 5 telefones.
Isto ocorre por ser um método antigo do UAU, que foi migrado para API. Futuramente esse endpoint vai ser descontinuado.


Valida Nação e UF referente aos campos 'codnacao_pf' e 'ufnasc_pf' respectivamente, Ex: Nação: 'BRA' UF: 'GO',ou seja se for informado Nação será obrigado UF ou vice-versa.

https://ajuda.globaltec.com.br/virtuau/cadastro-de-unidade-federativa/


Valida código e descrição do município referente aos campos 'cidadenat_pf' e 'naturalid_pf' respectivamente, Ex: Código: '1' Descrição: 'Goiânia'. 

Se caso for informado cidadenat_pf também será obrigado informar o campo naturalid_pf ou vice-versa. 
https://ajuda.globaltec.com.br/virtuau/virtuau/cadastro-de-municipios/


Validação tamanho do endereço: Essa validação pode ser ativada no cadastro de Pessoas em “Config.” ou seja em configuração de endereço, quando se marca a opção:
    “Limitar o cadastro de endereço de cobrança de pessoas e prospects para o máximo permitido nos boletos”, se essa opção estiver marcada no momento da requisição 
    se tiver utilizando o endereço maior  que o permitido poderá receber a seguinte mensagem” O campo 'Bairro - Endereço de cobrança' está com o tamanho acima do permitido: 15 | atual: 27.", como exemplo.

Verificação para Gravação das informações do documento da Pessoa: Verifica se o campo "info_pesfis" (informações da Pessoa física) foi informado, pois se não foi, o infopes_doc (informações dos documentos da Pessoa) não será considerado. 

Informação: 
  Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


VirtUau:

https://ajuda.globaltec.com.br/virtuau/uau-pessoas/#GravarPessoa

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/774876/
Exemplo Retorno: https://ajuda.globaltec.com.br/download/774882/


        """
        path = "Pessoas/GravarPessoa"
        return self.api.post(
            path,
            json={
                "nao_validar_campos_obrigatorios": nao_validar_campos_obrigatorios,
                "info_pes": info_pes,
                "info_pesfis": info_pesfis,
                "infopes_jur": infopes_jur,
                "dspes_tel_json": dspes_tel_json,
                "infopes_doc": infopes_doc,
                "info_pesendereco_principal": info_pesendereco_principal,
                "infopesendereco_cobranca": infopesendereco_cobranca,
                "infopesendereco_comercial": infopesendereco_comercial,
            }
        )

    def manter_telefone(
        self,
        numero: Optional[int] = None,
        telefones: Optional[List[Dict]] = None
    ) -> dict:
        """Alterar ou inserir telefones ao usuário

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Número de usuário é obrigatório.
Nível de permissão, GETELPES Alteração ou Inclusão

Definição de Negócio:

Quando o telefone não existe, ele é adicionado em relacionamento ao usuário proposto.
Quando o telefone já existe, ele faz a alteração dos dados.
Não se pode ter telefones iguais para a mesma pessoa. Caso tente colocar um telefone que já existe para determinada pessoa, irá retornar uma mensagem de erro.
O mesmo telefone pode ter usuários diferentes, e a alteração é feita somente naquele diretamente relacionado.
  4.Só pode possuir um telefone como principal por pessoa

Informação:
  Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).



        """
        path = "Pessoas/ManterTelefone"
        return self.api.post(
            path,
            json={
                "Numero": numero,
                "Telefones": telefones,
            }
        )

    def excluir_telefone(
        self,
        numero: Optional[int] = None,
        telefones: Optional[List[Dict]] = None
    ) -> dict:
        """Excluir telefones em relação ao usuário

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Número de usuário é obrigatório.
Nível de permissão, GETELPES Exclusão

Definição de Negócio:

A exclusão do telefone é feita somente para o usuário informado.

Informação:

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Pessoas/ExcluirTelefone"
        return self.api.post(
            path,
            json={
                "Numero": numero,
                "Telefones": telefones,
            }
        )

    def consultar_unidades(
        self,
        codigo_pessoa: Optional[int] = None,
        cpf_cnpj: Optional[str] = None
    ) -> dict:
        """Consultar unidades do cliente

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Informar o código da pessoa ou CPF/CNPJ da pessoa para uso do método.

Regras de Negócio:

CPF/CNPJ aceita apenas números.
Valida se encontrou a pessoa.
  VirtUau:
https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes


        """
        path = "Pessoas/ConsultarUnidades"
        return self.api.post(
            path,
            json={
                "CodigoPessoa": codigo_pessoa,
                "CpfCnpj": cpf_cnpj,
            }
        )

    def consultar_telefones(
        self,
        numero: Optional[int] = None
    ) -> dict:
        """Consultar telefones em relação ao usuário

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Número de usuário é obrigatório.
Nível de permissão, GETELPES Consulta

Definição de Negócio:

Listagem dos telefones relacionadas ao usuário.


        """
        path = "Pessoas/ConsultarTelefones"
        return self.api.post(
            path,
            json={
                "Numero": numero,
            }
        )

    def alterar_senha_cliente(
        self,
        codigo_cliente: Optional[int] = None,
        senha: Optional[str] = None
    ) -> dict:
        """Alterar a Senha da Pessoa/Cliente que permite acesso a área de Clientes no Uau Web

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Autenticador/ConsultarDadosUsrLogado
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite alterar a senha do cliente.

Deve informar o código do próprio cliente logado no Uau Web no qual será alterada a senha.
A senha deve conter exatamente 6 caracteres e não poderá estar criptografada.
Realiza validação se o login informado está sendo utilizado por outro cliente.

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Alteracao_de_Senha_do_Usuario_Cliente

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/774830/


        """
        path = "Pessoas/AlterarSenhaCliente"
        return self.api.post(
            path,
            json={
                "codigo_cliente": codigo_cliente,
                "senha": senha,
            }
        )

    def gravar_conta_bancaria(
        self,
        codigo_pessoa: Optional[int] = None,
        banco: Optional[int] = None,
        conta: Optional[str] = None,
        padrao: Optional[bool] = None,
        tipo: Optional[int] = None,
        agencia: Optional[str] = None,
        nome_agencia: Optional[str] = None,
        debito_automatico: Optional[bool] = None
    ) -> dict:
        """Grava banco e conta por pessoa

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
Preencher os parâmetros de request com os dados bancários e o código da pessoa para uso do método.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes


        """
        path = "Pessoas/GravarContaBancaria"
        return self.api.post(
            path,
            json={
                "codigoPessoa": codigo_pessoa,
                "banco": banco,
                "conta": conta,
                "padrao": padrao,
                "tipo": tipo,
                "agencia": agencia,
                "nomeAgencia": nome_agencia,
                "debitoAutomatico": debito_automatico,
            }
        )

    def consultar_tipo_endereco(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """Consultar tipo de endereço da pessoa
        """
        path = "Pessoas/ConsultarTipoEndereco"
        return self.api.post(
            path,
            json={
                "codigoPessoa": codigo_pessoa,
            }
        )

    def criar_credenciais_uauweb(
        self,
        cpf: Optional[str] = None,
        data_nascimento: Optional[datetime] = None,
        login: Optional[str] = None,
        senha: Optional[str] = None,
        email: Optional[str] = None
    ) -> dict:
        """Cria um novo usuário e senha para a pessoa no UAUWeb.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:

É necessário que o usuario forneça o UsuarioUAUSite ao obter o token de autenticação.
O usuário não pode estar duplicado no banco de dados.
O Email não pode estar sendo utilizado por outra pessoa.
O usuário não pode já ter um Login UAUWeb.
O novo login não pode estar sendo utilizado por outra pessoa.


        """
        path = "Pessoas/CriarCredenciaisUAUWeb"
        return self.api.post(
            path,
            json={
                "CPF": cpf,
                "DataNascimento": data_nascimento,
                "Login": login,
                "Senha": senha,
                "Email": email,
            }
        )

    def consultar_pessoa_por_chave(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """Consulta dados primários de uma pessoa

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Cosulta os dados de uma pessoa filtrando pelo código.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Pessoas/ConsultarPessoaPorChave"
        return self.api.post(
            path,
            json={
                "codigo_pessoa": codigo_pessoa,
            }
        )

    def consultar_contas_bancarias(
        self,
        codigo: Optional[str] = None
    ) -> dict:
        """Consultar contas bancárias por código de determinada pessoa

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
Informar o código da pessoa para uso do método.

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes


        """
        path = "Pessoas/ConsultarContasBancarias"
        return self.api.post(
            path,
            json={
                "codigo": codigo,
            }
        )

    def consultar_pessoas_com_venda(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta clientes que são titulares de vendas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Retorna código de nome da pessoa.

Definição de Negócio:

As vendas podem ser quitadas ou não.


        """
        path = "Pessoas/ConsultarPessoasComVenda"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def alterar_pessoa_acesso_portal(
        self,
        codigo_pessoa: Optional[int] = None,
        login: Optional[str] = None,
        senha: Optional[str] = None,
        email: Optional[str] = None
    ) -> dict:
        """Atualiza os dados de acesso ao UAU Web de uma determinada pessoa.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Autenticador/ConsultarDadosUsrLogado
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite alterar os dados de acesso ao Uau Web login, senha e e-mail.

Deve informar o código do próprio cliente logado no Uau Web no qual serão atualizados os dados.
A senha deve conter exatamente 6 caracteres e não poderá estar criptografada.
Realiza validação se o login informado está sendo utilizado por outro cliente.

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Alteracao_dos_Dados_de_Acesso_do_Cliente

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/775432/


        """
        path = "Pessoas/AlterarPessoaAcessoPortal"
        return self.api.post(
            path,
            json={
                "codigo_pessoa": codigo_pessoa,
                "login": login,
                "senha": senha,
                "email": email,
            }
        )

    def consultar_pessoas_por_cpfcnpj(
        self,
        cpf_cnpj: Optional[str] = None,
        status: Optional[int] = None
    ) -> dict:
        """Consulta os dados da pessoa por CPF/CNPJ e Status

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Deve informar o CPF/CNPJ sem formatações e o status.
O status pode ser:
0 = Ativo 
1 = Inativo
2 = Ambos



Definição de Negócio:
  Permite obter os dados de determinada pessoa física ou jurídica.
Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Consultar_dados_da_pessoa_por_CPFCNPJ

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/774849/
Exemplo Retorno: https://ajuda.globaltec.com.br/download/774846/


        """
        path = "Pessoas/ConsultarPessoasPorCPFCNPJ"
        return self.api.post(
            path,
            json={
                "cpf_cnpj": cpf_cnpj,
                "status": status,
            }
        )

    def excluir_banco_econta_por_chave(
        self,
        codigo_pessoa: Optional[int] = None,
        banco: Optional[int] = None,
        conta: Optional[str] = None,
        agencia: Optional[str] = None
    ) -> dict:
        """Exclui banco e conta por pessoa

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
Consultar os dados bancarios da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarContasBancarias.
Preencher os parâmetros de request com os dados bancários e o código da pessoa para uso do método.

Regras de Negócio:

Valida usuário e permissões.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes


        """
        path = "Pessoas/ExcluirBancoEContaPorChave"
        return self.api.post(
            path,
            json={
                "codigoPessoa": codigo_pessoa,
                "banco": banco,
                "conta": conta,
                "agencia": agencia,
            }
        )

    def recuperar_credenciais_uauweb(
        self,
        login: Optional[str] = None,
        email: Optional[str] = None
    ) -> dict:
        """Envia por e-mail a senha de uma pessoa do UAUWeb.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request com o login ou o email do usuário da pessoa para uso do método.

Regras de Negócio:

É necessário que o usuário forneça o UsuarioUAUSite ao obter o token de autenticação.
O usuário logado (informado na rota de autenticação) deverá possuir configuração de email cadastrada. Para verificar, acesse a Tela de Configurações do Usuário - Configurações - Configuração Email.
Deverá estar parametrizado a configuração "Enviar os avisos de pendências também por email externo", na aba Geral da tela de Configurações do Sistema.
O usuário não pode estar duplicado no banco de dados.
O usuário deve já ter um Login UAUWeb.
O usuário deve ter um email cadastrado.
Caso login e email seja enviado, é verificado se o usuário com esse login possui esse email cadastrado.


        """
        path = "Pessoas/RecuperarCredenciaisUAUWeb"
        return self.api.post(
            path,
            json={
                "Login": login,
                "Email": email,
            }
        )

    def consultar_pessoas_por_condicao(
        self,
        condicao_consultar_pessoa: Optional[str] = None
    ) -> dict:
        """Consulta os dados da pessoa de acordo com a condição informanda na busca

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
A condição informada é uma clausula SQL pós WHERE, segue exemplo:
cpf_pes = '12345678910' AND nome_pes LIKE 'GLOBALTEC%'


Devem ser passado as aspas simples para campos string.

Definição de Negócio:

Consulta pessoa por condição informada. 
Valida a condição da consulta, evitando SQL Injection.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Pessoas/ConsultarPessoasPorCondicao"
        return self.api.post(
            path,
            json={
                "condicaoConsultarPessoa": condicao_consultar_pessoa,
            }
        )

    def importar_dados_pessoas_para_uau(
        self,
        xml: Optional[str] = None
    ) -> dict:
        """Importa os dados de pessoas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Deve seguir arquivo XSD com o formato aceito.

Definição de Negócio:

Realiza a importação dos dados de pessoas para o UAU atravéz de arquivo XML.
Será validado o xml deserializado que preenche a classe de importação validando os dados.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:

https://ajuda.globaltec.com.br/virtuau/uau-pessoas-2/

Anexos:

Arquivo XSD do XML: https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2016/06/Pessoasxsd-1.rar
Exemplo XML: https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2016/06/Pessoas-3.rar


        """
        path = "Pessoas/ImportarDadosPessoasParaUau"
        return self.api.post(
            path,
            json={
                "xml": xml,
            }
        )

    def consultar_telefone_pes_por_chave(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """Consulta telefones da pessoa

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
Preencher os parâmetros de request para uso do método.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes


        """
        path = "Pessoas/ConsultarTelefonePesPorChave"
        return self.api.post(
            path,
            json={
                "codigoPessoa": codigo_pessoa,
            }
        )

    def consultar_endereco_pessoas_por_chave(
        self,
        codigo_pessoa: Optional[int] = None,
        tipo_endereco: Optional[int] = None
    ) -> dict:
        """Consultar endereços de pessoa por código da pessoa e tipo de endereço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Pessoas/ConsultarEnderecoPessoasPorChave"
        return self.api.post(
            path,
            json={
                "codigoPessoa": codigo_pessoa,
                "tipoEndereco": tipo_endereco,
            }
        )

    def consultar_pessoas_funcionarios_ativos(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        search_text: Optional[str] = None
    ) -> dict:
        """Consultar funcionários ativos

        Implementation Notes:
        Informação:

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Pessoas/ConsultarPessoasFuncionariosAtivos"
        return self.api.post(
            path,
            json={
                "Page": page,
                "PageSize": page_size,
                "SearchText": search_text,
            }
        )

    def consultar_dados_pessoa_fisica_por_codigo(
        self,
        codigopessoa_fis: Optional[int] = None
    ) -> dict:
        """Consultar dados de pessoa física

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta dados de pessoa física filtrando pelo código da pessoa.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Pessoas/ConsultarDadosPessoaFisicaPorCodigo"
        return self.api.post(
            path,
            json={
                "codigopessoa_fis": codigopessoa_fis,
            }
        )

    def consultar_dados_pessoa_por_cpf_cnpj_estatus(
        self,
        cpf_cnpj: Optional[str] = None,
        status: Optional[int] = None
    ) -> dict:
        """Consulta pessoa por CPF/CNPJ e Status

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Informar o CPF/CNPJ e status da pessoa para uso do método.

Regras de Negócio:

CPF/CNPJ aceita apenas números.
Valida se encontrou a pessoa.

Informação:

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:

https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes


        """
        path = "Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus"
        return self.api.post(
            path,
            json={
                "cpf_cnpj": cpf_cnpj,
                "status": status,
            }
        )

    def consultar_dados_adicionais_pessoa_por_chave(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """Consulta dados adicionais de uma pessoa por chave

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Busca por dados adicionais de pessoa filtrando pela chave.

Informação: 

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Pessoas/ConsultarDadosAdicionaisPessoaPorChave"
        return self.api.post(
            path,
            json={
                "codigo_pessoa": codigo_pessoa,
            }
        )

