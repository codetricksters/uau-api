from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Pessoas:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

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
        """
        
        Endpoint: `Pessoas/GravarPessoa`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            nao_validar_campos_obrigatorios (int): The nao_validar_campos_obrigatorios
            info_pes (Dict[str, Any]): The info_pes
            info_pesfis (Dict[str, Any]): The info_pesfis
            infopes_jur (Dict[str, Any]): The infopes_jur
            dspes_tel_json (str): The dspes_tel_json
            infopes_doc (Dict[str, Any]): The infopes_doc
            info_pesendereco_principal (Dict[str, Any]): The info_pesendereco_principal
            infopesendereco_cobranca (Dict[str, Any]): The infopesendereco_cobranca
            infopesendereco_comercial (Dict[str, Any]): The infopesendereco_comercial
        
        Parameter Structure:
        
            {
                "nao_validar_campos_obrigatorios": true,
                "info_pes": {
                    "cod_pes": 0,
                    "nome_pes": "string",
                    "tipo_pes": 0,
                    "cpf_pes": "string",
                    "dtcad_pes": "2025-04-23T13:46:13.714Z",
                    "dtnasc_pes": "2025-04-23T13:46:13.714Z",
                    "intext_pes": 0,
                    "usrcad_pes": "string",
                    "usralt_pes": "string",
                    "status_pes": 0,
                    "tratamento_pes": "string",
                    "siglaobr_pes": "string",
                    "email_pes": "string",
                    "endwww_pes": "string",
                    "matricula_pes": "string",
                    "atinat_pes": 0,
                    "dataalt_pes": "2025-04-23T13:46:13.714Z",
                    "nomefant_pes": "string",
                    "anexos_pes": 0,
                    "inscrmunic_pes": "string",
                    "inscrest_pes": "string",
                    "siglaemp_pes": 0,
                    "login_pes": "string",
                    "senha_pes": "string",
                    "cnae_pes": "string",
                    "datacadportal_pes": "2025-04-23T13:46:13.714Z",
                    "cadastradoprefeituragyn_pes": true,
                    "habilitadoriscosacado_pes": true,
                    "cei_pes": "string"
                },
                "info_pesfis": {
                    "cod_pf": 0,
                    "lotacao_pf": "string",
                    "cargo_pf": "string",
                    "dtadm_pf": "2025-04-23T13:46:13.714Z",
                    "corresp_pf": 0,
                    "estciv_pf": 0,
                    "doc_pf": "string",
                    "tdoc_pf": "string",
                    "dtdoc_pf": "2025-04-23T13:46:13.714Z",
                    "sexo_pf": 0,
                    "nacion_pf": "string",
                    "numdep_pf": 0,
                    "pai_pf": "string",
                    "dtpai_pf": "2025-04-23T13:46:13.715Z",
                    "mae_pf": "string",
                    "dtmae_pf": "2025-04-23T13:46:13.715Z",
                    "naturalid_pf": "string",
                    "codnacao_pf": "string",
                    "codgrau_pf": "string",
                    "codraca_pf": "string",
                    "codsmil_pf": "string",
                    "ufnasc_pf": "string",
                    "cidadenat_pf": 0,
                    "fatorrh_pf": "string",
                    "regcasamento_pf": 0,
                    "cdi_pf": "string",
                    "numpro_pf": 0,
                    "uniaoestavel_pf": true,
                    "detalhanacao_pf": 0,
                    "codnacaoorigem_pf": "string",
                    "codmunicnasc_pf": 0,
                    "indicativofiscal_pf": 0,
                    "formatributacao_pf": "string"
                },
                "infopes_jur": {
                    "cod_pj": 0,
                    "contato_pj": "string",
                    "contato2_pj": "string",
                    "inssuframa_pj": "string",
                    "natureza_pj": 0,
                    "optantesimples_pj": true,
                    "ans_pj": "string"
                },
                "dspes_tel_json": "string",
                "infopes_doc": {
                    "codpes_doc": 0,
                    "tipo_doc": 0,
                    "registro_doc": "string",
                    "orgaoemissor_doc": "string",
                    "codnacao_doc": "string",
                    "uf_doc": "string",
                    "dataemissao_doc": "2025-04-23T13:46:13.715Z",
                    "datavalidade_doc": "2025-04-23T13:46:13.715Z",
                    "categoria_doc": "string",
                    "zonaeleit_doc": "string",
                    "secao_doc": "string",
                    "tipoentclasse_doc": 0,
                    "seqconselho_doc": "string",
                    "dataalt_doc": "2025-04-23T13:46:13.715Z",
                    "usralt_doc": "string"
                },
                "info_pesendereco_principal": {
                    "CodPes_pend": 0,
                    "Tipo_pend": 0,
                    "Endereco_pend": "string",
                    "Bairro_pend": "string",
                    "Cidade_pend": "string",
                    "UF_pend": "string",
                    "CEP_pend": "string",
                    "NumEnd_pend": "string",
                    "ComplEndereco_pend": "string",
                    "ReferEnd_pend": "string",
                    "Proprio_pend": 0,
                    "NumCid_pend": 0,
                    "NumBrr_pend": 0,
                    "NumLogr_pend": 0,
                    "CodEmp_pend": 0,
                    "NomeEmp_pend": "string",
                    "TipoEndEmp_pend": 0
                },
                "infopesendereco_cobranca": {
                    "CodPes_pend": 0,
                    "Tipo_pend": 0,
                    "Endereco_pend": "string",
                    "Bairro_pend": "string",
                    "Cidade_pend": "string",
                    "UF_pend": "string",
                    "CEP_pend": "string",
                    "NumEnd_pend": "string",
                    "ComplEndereco_pend": "string",
                    "ReferEnd_pend": "string",
                    "Proprio_pend": 0,
                    "NumCid_pend": 0,
                    "NumBrr_pend": 0,
                    "NumLogr_pend": 0,
                    "CodEmp_pend": 0,
                    "NomeEmp_pend": "string",
                    "TipoEndEmp_pend": 0
                },
                "infopesendereco_comercial": {
                    "CodPes_pend": 0,
                    "Tipo_pend": 0,
                    "Endereco_pend": "string",
                    "Bairro_pend": "string",
                    "Cidade_pend": "string",
                    "UF_pend": "string",
                    "CEP_pend": "string",
                    "NumEnd_pend": "string",
                    "ComplEndereco_pend": "string",
                    "ReferEnd_pend": "string",
                    "Proprio_pend": 0,
                    "NumCid_pend": 0,
                    "NumBrr_pend": 0,
                    "NumLogr_pend": 0,
                    "CodEmp_pend": 0,
                    "NomeEmp_pend": "string",
                    "TipoEndEmp_pend": 0
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._gravar_pessoa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/GravarPessoa"
        kwargs = {
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
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def manter_telefone(
        self,
        numero: Optional[int] = None,
        telefones: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ManterTelefone`
        HTTP Method: `POST`
        
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
        
        
        
        
        Args:
            Numero (int): The numero
            Telefones (List[Dict[str, Any]]): The telefones
        
        Parameter Structure:
        
            {
                "Numero": 0,
                "Telefones": [
                    {
                        "Telefone": "string",
                        "DDD": "string",
                        "Complemento": "string",
                        "Tipo": 0,
                        "Principal": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._manter_telefone(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ManterTelefone"
        kwargs = {
            "Numero": numero,
            "Telefones": telefones,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def excluir_telefone(
        self,
        numero: Optional[int] = None,
        telefones: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ExcluirTelefone`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            Numero (int): The numero
            Telefones (List[Dict[str, Any]]): The telefones
        
        Parameter Structure:
        
            {
                "Numero": 0,
                "Telefones": [
                    {
                        "Telefone": "string",
                        "DDD": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._excluir_telefone(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ExcluirTelefone"
        kwargs = {
            "Numero": numero,
            "Telefones": telefones,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_unidades(
        self,
        codigo_pessoa: Optional[int] = None,
        cpf_cnpj: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarUnidades`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Informar o código da pessoa ou CPF/CNPJ da pessoa para uso do método.
        
        Regras de Negócio:
        
        CPF/CNPJ aceita apenas números.
        Valida se encontrou a pessoa.
          VirtUau:
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        
        
        Args:
            CodigoPessoa (int): The codigo pessoa
            CpfCnpj (str): The cpf cnpj
        
        Parameter Structure:
        
            {
                "CodigoPessoa": 0,
                "CpfCnpj": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_unidades(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarUnidades"
        kwargs = {
            "CodigoPessoa": codigo_pessoa,
            "CpfCnpj": cpf_cnpj,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_telefones(
        self,
        numero: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarTelefones`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Número de usuário é obrigatório.
        Nível de permissão, GETELPES Consulta
        
        Definição de Negócio:
        
        Listagem dos telefones relacionadas ao usuário.
        
        
        
        Args:
            Numero (int): The numero
        
        Parameter Structure:
        
            {
                "Numero": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_telefones(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarTelefones"
        kwargs = {
            "Numero": numero,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def alterar_senha_cliente(
        self,
        codigo_cliente: Optional[int] = None,
        senha: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/AlterarSenhaCliente`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            codigo_cliente (int): The codigo_cliente
            senha (str): The senha
        
        Parameter Structure:
        
            {
                "codigo_cliente": 0,
                "senha": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._alterar_senha_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/AlterarSenhaCliente"
        kwargs = {
            "codigo_cliente": codigo_cliente,
            "senha": senha,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        """
        
        Endpoint: `Pessoas/GravarContaBancaria`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
        Preencher os parâmetros de request com os dados bancários e o código da pessoa para uso do método.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        
        
        Args:
            codigoPessoa (int): The pessoa
            banco (int): The banco
            conta (str): The conta
            padrao (int): The padrao
            tipo (int): The tipo
            agencia (str): The agencia
            nomeAgencia (str): The agencia
            debitoAutomatico (int): The automatico
        
        Parameter Structure:
        
            {
                "codigoPessoa": 0,
                "banco": 0,
                "conta": "string",
                "padrao": true,
                "tipo": 0,
                "agencia": "string",
                "nomeAgencia": "string",
                "debitoAutomatico": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._gravar_conta_bancaria(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/GravarContaBancaria"
        kwargs = {
            "codigoPessoa": codigo_pessoa,
            "banco": banco,
            "conta": conta,
            "padrao": padrao,
            "tipo": tipo,
            "agencia": agencia,
            "nomeAgencia": nome_agencia,
            "debitoAutomatico": debito_automatico,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_tipo_endereco(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarTipoEndereco`
        HTTP Method: `POST`
        
        Args:
            codigoPessoa (int): The pessoa
        
        Parameter Structure:
        
            {
                "codigoPessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_tipo_endereco(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarTipoEndereco"
        kwargs = {
            "codigoPessoa": codigo_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def criar_credenciais_uauweb(
        self,
        cpf: Optional[str] = None,
        data_nascimento: Optional[datetime] = None,
        login: Optional[str] = None,
        senha: Optional[str] = None,
        email: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/CriarCredenciaisUAUWeb`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            CPF (str): The c p f
            DataNascimento (datetime): The data nascimento
            Login (str): The login
            Senha (str): The senha
            Email (str): The email
        
        Parameter Structure:
        
            {
                "CPF": "string",
                "DataNascimento": "2025-04-23T13:46:13.758Z",
                "Login": "string",
                "Senha": "string",
                "Email": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._criar_credenciaisuau_web(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/CriarCredenciaisUAUWeb"
        kwargs = {
            "CPF": cpf,
            "DataNascimento": data_nascimento,
            "Login": login,
            "Senha": senha,
            "Email": email,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_pessoa_por_chave(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarPessoaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Cosulta os dados de uma pessoa filtrando pelo código.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            codigo_pessoa (int): The codigo_pessoa
        
        Parameter Structure:
        
            {
                "codigo_pessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_pessoa_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarPessoaPorChave"
        kwargs = {
            "codigo_pessoa": codigo_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_contas_bancarias(
        self,
        codigo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarContasBancarias`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
        Informar o código da pessoa para uso do método.
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        
        
        Args:
            codigo (str): The codigo
        
        Parameter Structure:
        
            {
                "codigo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_contas_bancarias(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarContasBancarias"
        kwargs = {
            "codigo": codigo,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_pessoas_com_venda(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarPessoasComVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Retorna código de nome da pessoa.
        
        Definição de Negócio:
        
        As vendas podem ser quitadas ou não.
        
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_pessoas_com_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarPessoasComVenda"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def alterar_pessoa_acesso_portal(
        self,
        codigo_pessoa: Optional[int] = None,
        login: Optional[str] = None,
        senha: Optional[str] = None,
        email: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/AlterarPessoaAcessoPortal`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            codigo_pessoa (int): The codigo_pessoa
            login (str): The login
            senha (str): The senha
            email (str): The email
        
        Parameter Structure:
        
            {
                "codigo_pessoa": 0,
                "login": "string",
                "senha": "string",
                "email": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._alterar_pessoa_acesso_portal(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/AlterarPessoaAcessoPortal"
        kwargs = {
            "codigo_pessoa": codigo_pessoa,
            "login": login,
            "senha": senha,
            "email": email,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_pessoas_por_cpfcnpj(
        self,
        cpf_cnpj: Optional[str] = None,
        status: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarPessoasPorCPFCNPJ`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            cpf_cnpj (str): The cpf_cnpj
            status (int): The status
        
        Parameter Structure:
        
            {
                "cpf_cnpj": "string",
                "status": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_pessoas_porcpfcnpj(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarPessoasPorCPFCNPJ"
        kwargs = {
            "cpf_cnpj": cpf_cnpj,
            "status": status,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def excluir_banco_econta_por_chave(
        self,
        codigo_pessoa: Optional[int] = None,
        banco: Optional[int] = None,
        conta: Optional[str] = None,
        agencia: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ExcluirBancoEContaPorChave`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            codigoPessoa (int): The pessoa
            banco (int): The banco
            conta (str): The conta
            agencia (str): The agencia
        
        Parameter Structure:
        
            {
                "codigoPessoa": 0,
                "banco": 0,
                "conta": "string",
                "agencia": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._excluir_bancoe_conta_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ExcluirBancoEContaPorChave"
        kwargs = {
            "codigoPessoa": codigo_pessoa,
            "banco": banco,
            "conta": conta,
            "agencia": agencia,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def recuperar_credenciais_uauweb(
        self,
        login: Optional[str] = None,
        email: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/RecuperarCredenciaisUAUWeb`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            Login (str): The login
            Email (str): The email
        
        Parameter Structure:
        
            {
                "Login": "string",
                "Email": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._recuperar_credenciaisuau_web(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/RecuperarCredenciaisUAUWeb"
        kwargs = {
            "Login": login,
            "Email": email,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_pessoas_por_condicao(
        self,
        condicao_consultar_pessoa: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarPessoasPorCondicao`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            condicaoConsultarPessoa (str): The consultar pessoa
        
        Parameter Structure:
        
            {
                "condicaoConsultarPessoa": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_pessoas_por_condicao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarPessoasPorCondicao"
        kwargs = {
            "condicaoConsultarPessoa": condicao_consultar_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def importar_dados_pessoas_para_uau(
        self,
        xml: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ImportarDadosPessoasParaUau`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            xml (str): The xml
        
        Parameter Structure:
        
            {
                "xml": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._importar_dados_pessoas_para_uau(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ImportarDadosPessoasParaUau"
        kwargs = {
            "xml": xml,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_telefone_pes_por_chave(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarTelefonePesPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
        Preencher os parâmetros de request para uso do método.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        VirtUau:
        
        https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        
        
        Args:
            codigoPessoa (int): The pessoa
        
        Parameter Structure:
        
            {
                "codigoPessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_telefone_pes_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarTelefonePesPorChave"
        kwargs = {
            "codigoPessoa": codigo_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_endereco_pessoas_por_chave(
        self,
        codigo_pessoa: Optional[int] = None,
        tipo_endereco: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarEnderecoPessoasPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            codigoPessoa (int): The pessoa
            tipoEndereco (int): The endereco
        
        Parameter Structure:
        
            {
                "codigoPessoa": 0,
                "tipoEndereco": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_endereco_pessoas_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarEnderecoPessoasPorChave"
        kwargs = {
            "codigoPessoa": codigo_pessoa,
            "tipoEndereco": tipo_endereco,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_pessoas_funcionarios_ativos(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        search_text: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarPessoasFuncionariosAtivos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Informação:
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            Page (int): The page
            PageSize (int): The page size
            SearchText (str): The search text
        
        Parameter Structure:
        
            {
                "Page": 0,
                "PageSize": 0,
                "SearchText": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_pessoas_funcionarios_ativos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarPessoasFuncionariosAtivos"
        kwargs = {
            "Page": page,
            "PageSize": page_size,
            "SearchText": search_text,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_dados_pessoa_fisica_por_codigo(
        self,
        codigopessoa_fis: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarDadosPessoaFisicaPorCodigo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta dados de pessoa física filtrando pelo código da pessoa.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            codigopessoa_fis (int): The codigopessoa_fis
        
        Parameter Structure:
        
            {
                "codigopessoa_fis": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_dados_pessoa_fisica_por_codigo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarDadosPessoaFisicaPorCodigo"
        kwargs = {
            "codigopessoa_fis": codigopessoa_fis,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_dados_pessoa_por_cpf_cnpj_estatus(
        self,
        cpf_cnpj: Optional[str] = None,
        status: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            cpf_cnpj (str): The cpf_cnpj
            status (int): The status
        
        Parameter Structure:
        
            {
                "cpf_cnpj": "string",
                "status": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_dados_pessoa_por_cpf_cnpje_status(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus"
        kwargs = {
            "cpf_cnpj": cpf_cnpj,
            "status": status,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_dados_adicionais_pessoa_por_chave(
        self,
        codigo_pessoa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Pessoas/ConsultarDadosAdicionaisPessoaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Busca por dados adicionais de pessoa filtrando pela chave.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            codigo_pessoa (int): The codigo_pessoa
        
        Parameter Structure:
        
            {
                "codigo_pessoa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._consultar_dados_adicionais_pessoa_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pessoas/ConsultarDadosAdicionaisPessoaPorChave"
        kwargs = {
            "codigo_pessoa": codigo_pessoa,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
                        print(f"  Detalhe: {detalhe}")
                        print(f"  Mensagem: {mensagem}")
                        print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

