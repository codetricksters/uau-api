"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class RotinasGerais:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def busca_campos_person(
        self,
        empresa: Optional[str] = None,
        produto: Optional[str] = None
    ) -> dict:
        """Busca campos personalizados de uma empresa e produto

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta campos personalizados de empresa e produto.
Valida permissão de consulta (2) para o usuário autenticado


        """
        path = "RotinasGerais/BuscaCamposPerson"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "produto": produto,
            }
        )

    def busca_capvenda_empresa(
        self,
        codigo_empresa: Optional[int] = None
    ) -> dict:
        """Consulta e detalha as configurações de CAPs de determinada empresa.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Irá retornar as configurações de CAPs de uma determinada empresa.
Existem dois estados para o request:
Caso o request seja nulo, irá retornar todas as configurações de CAPs existentes no sistema.
Caso seja determinado um número de empresa, irá retornar as configurações de CAPs dessa empresa.




        """
        path = "RotinasGerais/BuscaCAPVendaEmpresa"
        return self.api.post(
            path,
            json={
                "CodigoEmpresa": codigo_empresa,
            }
        )

    def inserir_consulta_geral(
        self,
        clausula_sql: Optional[str] = None,
        descricao: Optional[str] = None,
        codigo_pasta: Optional[str] = None,
        status: Optional[int] = None,
        parametros: Optional[List[Dict]] = None
    ) -> dict:
        """Inserir consulta geral

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

A Globaltec não se responsabiliza:

Pela compatibilidade entre as alterações do banco de dados e as consultas personalizadas efetuadas pelos clientes.
Pelos dados informados nos geradores de resultado que utilizam consultas personalizadas criadas pelos clientes.

Definição de Negócio:

Irá realizar a inserção da consulta geral.
Será necessario permissão de INCLUSÃO no programa GECONSGER.

VirtUau:

https://ajuda.globaltec.com.br/virtuau/como-realizar-o-cadastro-de-consultas-gerais/


        """
        path = "RotinasGerais/InserirConsultaGeral"
        return self.api.post(
            path,
            json={
                "ClausulaSql": clausula_sql,
                "Descricao": descricao,
                "CodigoPasta": codigo_pasta,
                "Status": status,
                "Parametros": parametros,
            }
        )

    def executar_consulta_geral(
        self,
        id: Optional[int] = None,
        personalizado: Optional[int] = None,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """Executa query armazenada

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente

Definição de Negócio:

Consulta campos personalizados de empresa e produto.
Valida permissão de consulta (2) para o usuário autenticado 
Os parâmetros de cada consulta geral podem ser consultados através da rota RotinasGerais/ConsultarParamConsultaGeral
Retorna valores dinâmicos da respectiva query armazenada como ConsultaGeral.

Deve ser enviado o ID da ConsultaGeral e seus respectivos parâmetros, sendo o preenchimento da propriedade Parameters,
  um array de string, e se necessário notações sql que atribuem características de tipagem. Por exemplo, apóstrofo entre uma string, considerando que 
  em situações que usam um inteiro, podem funcionar com apóstrofo ou sem, mas em cláusulas como IN(params), 
  o uso de apóstrofo pode gerar um erro, e ainda para atribuir uma lista de inteiros nesta, deve ser usado a vírgula.
  Seguindo esta padrão comum,   "Parameters":["Nome do parâmetro", "Valor do parâmetro", "Nome do segundo parâmetro", "valor do segundo parâmetro"]
Apóstrofo = '
Datas devem ser acompanhadas de Apóstrofo, exceto em ocasiões especiais que devem ser analisadas na query, sendo
  um destes, o uso da cláusula IN
Exemplo formato json da body
{
  "Id": "1",
  "Personalizado": "0",
  "Parameters":["P01", "1"]
  }
{
   "Id": "2",
   "Personalizado": "0",
   "Parameters":["EmpresaObra", " '1|1' ", "Status", "1"]
  }
"Personalizado": 1 - True / 0 - False
VirtUau:

https://ajuda.globaltec.com.br/virtuau/consultas-gerais/
Anexos:

Exemplo Postman json request:


ExecutarConsultaGeral

        """
        path = "RotinasGerais/ExecutarConsultaGeral"
        return self.api.post(
            path,
            json={
                "Id": id,
                "Personalizado": personalizado,
                "Parameters": parameters,
            }
        )

    def buscar_indices_de_reajuste(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar a lista de índices de reajuste ativos

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Busca a lista de índices de reajuste ativos do sistema


        """
        path = "RotinasGerais/BuscarIndicesDeReajuste"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def buscar_tipos_de_vencimento(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta os tipos de vencimento ativos

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Possibilita consultar os tipo de vencimento que estão ativos.


        """
        path = "RotinasGerais/BuscarTiposDeVencimento"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_padroes_cobranca(
        self,
        empresa: Optional[int] = None,
        status: Optional[int] = None,
        banco: Optional[int] = None
    ) -> dict:
        """Consultar os padrões de cobrança disponíveis

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

O único campo obrigatório do request é o Status.
Irá retornar os padrões de cobrança de acordo com o(s) filtro(s).
As informações personalizadas da cobrança virão como Configuracao_01 até a Configuracao_08.


        """
        path = "RotinasGerais/ConsultarPadroesCobranca"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Status": status,
                "Banco": banco,
            }
        )

    def buscar_categorias_de_produto(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar a lista de categorias de produto ativos

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta a lista de categorias de produtos com status ativos.


        """
        path = "RotinasGerais/BuscarCategoriasDeProduto"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def buscar_finalidades_de_compra(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar com finalidades de compra ativas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Este endpoint não necessita de parâmetros no request.

Definição de Negócio:

Consulta a lista de finalidades para compras com status ativo.


        """
        path = "RotinasGerais/BuscarFinalidadesDeCompra"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def buscar_veiculos_de_divulgacao(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar veículos de divulgação ativos

        Implementation Notes:
        Lista de Veículos de divulgação.
   Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Definição de Negócio:

Consulta veículos de divulgação que estão ativos.


        """
        path = "RotinasGerais/BuscarVeiculosDeDivulgacao"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_param_consulta_geral(
        self,
        id: Optional[int] = None,
        personalizado: Optional[int] = None
    ) -> dict:
        """Consutar parâmetros necessários e seus atributos da ConsultaGeral

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente
Retorna uma lista de parâmetros dinâmicos, apresentando o nome do parâmetro e sua descrição, se ele é restrito, multiseleção e OrigemDados
  com pressuposição do uso dessas informações em "ExecutarConsultaGeral

Definição de Negócio:

Permite visualizar o padrão de parâmetros da ConsultaGeral informada de forma detalhada
Valida permissão de consulta (2) para o usuário autenticado
VirtUau:

https://ajuda.globaltec.com.br/virtuau/consultas-gerais/
Exemplo:

Json request: 


{
  "Id": "1",
  "Personalizado": "0",
  "Parameters":["P01", "1"]
  }
"Personalizado": 1 - True / 0 - False

        """
        path = "RotinasGerais/ConsultarParamConsultaGeral"
        return self.api.post(
            path,
            json={
                "Id": id,
                "Personalizado": personalizado,
            }
        )

