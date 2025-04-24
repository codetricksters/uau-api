"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Anexo:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def anexar_arquivo(
        self,
        arquivo: Optional[str] = None,
        nome: Optional[str] = None,
        caminho: Optional[str] = None,
        identificador: Optional[str] = None,
        usuario: Optional[str] = None,
        caminho_exclusivo: Optional[str] = None,
        controla_anexouau_web: Optional[bool] = None
    ) -> dict:
        """Anexa um arquivo

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Anexa arquivo dentro do UAU, utilizando a chave identificadora para fazer o vinculo desse arquivo com algum parametro dentro do sistema. 

Parâmetros da request

arquivo: Conteúdo do arquivo em base 64
nome:  Chave identificadora Do arquivo no formato "STRING STRING"
caminho: Caminho do arquivo
identificador: Nome Identificador do arquivo
usuario: Login do usuário
caminhoExclusivo: String correspondente a configuração em configGerais do caminho exclusivo


        """
        path = "Anexo/AnexarArquivo"
        return self.api.post(
            path,
            json={
                "arquivo": arquivo,
                "nome": nome,
                "caminho": caminho,
                "identificador": identificador,
                "usuario": usuario,
                "caminhoExclusivo": caminho_exclusivo,
                "controlaAnexoUAUWeb": controla_anexouau_web,
            }
        )

    def excluir_anexos(
        self,
        identificador: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        origem: Optional[int] = None
    ) -> dict:
        """Exclui o vinculo do anexo ao arquivo.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.       

Parâmetros da request

identificador: Chave identificadora do arquivo no formato "STRING STRING".
nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
origem: Indica o tipo de armazenamento será utilizado para excluir o vinculo ao arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.


        """
        path = "Anexo/ExcluirAnexos"
        return self.api.post(
            path,
            json={
                "identificador": identificador,
                "nome_arquivo": nome_arquivo,
                "origem": origem,
            }
        )

    def listar_diretorios(
        self,
        caminho: Optional[str] = None,
        origem: Optional[int] = None
    ) -> dict:
        path = "Anexo/ListarDiretorios"
        return self.api.post(
            path,
            json={
                "Caminho": caminho,
                "Origem": origem,
            }
        )

    def anexar_base64_imagem(
        self,
        arquivo: Optional[str] = None,
        nome: Optional[str] = None,
        caminho: Optional[str] = None,
        identificador: Optional[str] = None,
        usuario: Optional[str] = None,
        extensao_imagem: Optional[str] = None,
        caminho_exclusivo: Optional[str] = None,
        controla_anexouau_web: Optional[bool] = None,
        origem: Optional[int] = None
    ) -> dict:
        """Anexa uma imagem na base64

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Possibilita anexar imagem no formato Base64

        """
        path = "Anexo/AnexarBase64Imagem"
        return self.api.post(
            path,
            json={
                "arquivo": arquivo,
                "nome": nome,
                "caminho": caminho,
                "identificador": identificador,
                "usuario": usuario,
                "extensaoImagem": extensao_imagem,
                "caminhoExclusivo": caminho_exclusivo,
                "controlaAnexoUAUWeb": controla_anexouau_web,
                "origem": origem,
            }
        )

    def listar_armazenamentos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retorna a lista de armazenamentos ativos
        """
        path = "Anexo/ListarArmazenamentos"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def gravar_comentario_anexo(
        self,
        chave: Optional[str] = None,
        campos: Optional[str] = None,
        usuario: Optional[str] = None,
        comentario: Optional[str] = None,
        tipo_comentario: Optional[str] = None,
        usuario_privado: Optional[List[Dict]] = None,
        grupo_privado: Optional[List[Dict]] = None
    ) -> dict:
        """Anexar um comentario

        Implementation Notes:
        Definição técnica:

Adiciona comentário anexo de acordo com os parâmetros passados na requisição.

Pré requisito:

Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
URL + /api/v{version}/Anexo/ConsultarChavesComentario



Parâmetros da request

Chave: Chave para consulta.
Campos: Campos obrigatórios para a chave="Venda" (empresa, obra, venda). Campos obrigatórios para a chave="Contrato" (Empresa, Contrato) Deve ser inserido juntos, separados por virgula.
Usuario: Usuário logado.
Comentario: Comentário a ser anexado.
TipoComentario: Armazena o tipo do comentário ( 0-Publico, 1-Privado, 2-Interna).
UsuarioPrivado: Armazena a lista de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -> /Usuarios/ConsultarUsuariosAtivos ).
GrupoPrivado: Armazena a lista de grupos de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -> /Usuarios/ConsultarGruposDeUsuario ).


        """
        path = "Anexo/GravarComentarioAnexo"
        return self.api.post(
            path,
            json={
                "Chave": chave,
                "Campos": campos,
                "Usuario": usuario,
                "Comentario": comentario,
                "TipoComentario": tipo_comentario,
                "UsuarioPrivado": usuario_privado,
                "GrupoPrivado": grupo_privado,
            }
        )

    def retorna_arquivo_em_bytes(
        self,
        nome_arquivo: Optional[str] = None,
        origem: Optional[int] = None
    ) -> dict:
        """Retorna um determinado arquivo em base64.

        Implementation Notes:
        Em Modulo UAU >> Utilitários >> Configurações do sistema >> ( Em "Arquivo" >> Arquivos(Anexos): ) Esse e o caminho padrão que a rota usar na consulta para retorna o arquivo em base64.
Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Parâmetros da request

nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
origem: Indica o tipo de armazenamento será utilizado para buscar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.


        """
        path = "Anexo/RetornaArquivoEmBytes"
        return self.api.post(
            path,
            json={
                "nome_arquivo": nome_arquivo,
                "origem": origem,
            }
        )

    def consultar_chaves_comentario(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retorna as chaves, seus campos e exemplo, que podem ser utilizadas para gravação de comentario em anexo.

        Implementation Notes:
        Definição técnica:

Este endpoint oferece suporte para o seguinte endpoint: [URI + /api/v{version}/Anexo/GravarComentarioAnexo]
Retorna objetos com:
Possíveis chaves que podem ser utilizadas.
Ordem dos parâmetros aceitos.
Exemplo de utilização e formatação dos parâmetros.
  Anexos:


Exemplo Postman: https://ajuda.globaltec.com.br/download/777152/


        """
        path = "Anexo/ConsultarChavesComentario"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def anexar_arquivos_base64_request(
        self,
        lista_arquivos: Optional[List[Dict]] = None,
        empresa: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Anexa um arquivo

        Implementation Notes:
        Criação   : Diogo Rodrigues Gonçalves             Data: 11/12/2018
  Projeto   : FVS Mobile

        """
        path = "Anexo/AnexarArquivosBase64Request"
        return self.api.post(
            path,
            json={
                "lista_arquivos": lista_arquivos,
                "empresa": empresa,
                "usuario": usuario,
            }
        )

    def retornar_arquivos_em_lista_bytes(
        self,
        empresa: Optional[str] = None,
        identificador: Optional[str] = None,
        listanomes_arquivos: Optional[List[Dict]] = None
    ) -> dict:
        """Retorna uma lista com os dados dos arquivos e o conteúdo do mesmo em base64.

        Implementation Notes:
        Baseado no ‘’código identificador do documento’’ passado ele já retorna os arquivos tanto disponível localmente e na nuvem, sem a necessidade de passar o parâmetro “origem” no body do request.
Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.       

Parâmetros da request

empresa: Número da empresa.
identificador: Chave identificadora do arquivo no formato "STRING STRING".
listanomes_arquivos:  Lista de 'string' com o nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )


        """
        path = "Anexo/RetornarArquivosEmListaBytes"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "identificador": identificador,
                "listanomes_arquivos": listanomes_arquivos,
            }
        )

