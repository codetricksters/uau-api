"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class ChavePix:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def by_cpfcnpj(
        self,
        cpf_cnpj: str,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retorna as chaves pix cadastradas ao CPF/CNPJ informado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:

É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.


        """
        path = f"ChavePix/Pessoas/Consultar/{cpfcnpj}"
        return self.api.get(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def deletar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None
    ) -> dict:
        """Remove uma chave pix de pessoa.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:

É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
A chave pix deve ter no máximo 77 caracteres.


        """
        path = "ChavePix/Pessoas/Deletar"
        return self.api.post(
            path,
            json={
                "cpfCnpj": cpf_cnpj,
                "chavePix": chave_pix,
                "tipoChavePix": tipo_chave_pix,
            }
        )

    def atualizar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None,
        chave_pix_padrao: Optional[int] = None,
        ativo_inativo: Optional[int] = None
    ) -> dict:
        """Atualiza a chave pix de uma pessoa.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:

É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
A chave pix deve ter no máximo 77 caracteres.
A chave padrão deve ser: 0 - NÃO, 1 - SIM.
O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.


        """
        path = "ChavePix/Pessoas/Atualizar"
        return self.api.post(
            path,
            json={
                "cpfCnpj": cpf_cnpj,
                "chavePix": chave_pix,
                "tipoChavePix": tipo_chave_pix,
                "chavePixPadrao": chave_pix_padrao,
                "ativoInativo": ativo_inativo,
            }
        )

    def cadastrar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None,
        chave_pix_padrao: Optional[int] = None,
        ativo_inativo: Optional[int] = None
    ) -> dict:
        """Cadastra uma nova chave pix para a pessoa.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:

É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
A chave pix deve ter no máximo 77 caracteres.
A chave padrão deve ser: 0 - NÃO, 1 - SIM.
O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.


        """
        path = "ChavePix/Pessoas/Cadastrar"
        return self.api.post(
            path,
            json={
                "cpfCnpj": cpf_cnpj,
                "chavePix": chave_pix,
                "tipoChavePix": tipo_chave_pix,
                "chavePixPadrao": chave_pix_padrao,
                "ativoInativo": ativo_inativo,
            }
        )

