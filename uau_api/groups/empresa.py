"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Empresa:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_empresa(
        self,
        codigo_empresa: Optional[int] = None
    ) -> dict:
        """Consultar os dados da empresa.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Empresa/ConsultarEmpresa"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
            }
        )

    def obter_empresas_ativas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta e retorna uma lista de Empresas cadastradas e ativas na base de dados UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Empresa/ObterEmpresasAtivas"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_dados_basicos_empresas_por_filtro(
        self,
        empresa: Optional[int] = None,
        descricao_empresa: Optional[str] = None,
        cnpj: Optional[str] = None,
        limitar_retorno_em: Optional[int] = None
    ) -> dict:
        """Consultar dados básicos da empresa por filtro, com limite de registros.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Empresa/DadosBasicosEmpresa
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Consultar dados de empresas por meio dos seguintes filtros (empresa, cnpj e descricaoEmpresa), os resultados da busca será de acordo com o limite especificado no parâmetro (limitarRetornoEm).

Se apenas informar o código da empresa parâmetro (empresa) o mesmo deve estar completo.
Os parâmetros (DescricaoEmpresa e Cnpj) devem possuir no mínimo 3 caracteres..
Os parâmetros (DescricaoEmpresa e Cnpj) podem conter o sinal de porcentagem (%), caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.
O campo LimitarRetornoEm é obrigatório.
Caso não informe nenhum dos parâmetros o resultado será os N primeiros registros encontrados, obedecendo o parâmetro LimitarRetornoEm.
O método usa o operador “Or” para montar a consulta de acordo com os parâmetros do request, consultando informações por código ou descrição ou CNPJ da empresa.

VirtUau:

http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Empresa/Empresa_ConsultarDadosBasicosEmpresasPorFiltro

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777099/


        """
        path = "Empresa/ConsultarDadosBasicosEmpresasPorFiltro"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "DescricaoEmpresa": descricao_empresa,
                "Cnpj": cnpj,
                "LimitarRetornoEm": limitar_retorno_em,
            }
        )

