from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Prospect:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

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
        """
        
        Endpoint: `Prospect/GravarProspect`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Grava as informações do prospect.
        Os dados informados passam por validações.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            permitirResponsavelSemEstrutura (int): The responsavel sem estrutura
            login (str): The login
            prospect (Dict[str, Any]): The prospect
            prospectFis (Dict[str, Any]): The fis
            prospectInteresse (Dict[str, Any]): The interesse
            prospectInteresseProdutos (List[Dict[str, Any]]): The interesse produtos
            prospectInteresseBairros (List[Dict[str, Any]]): The interesse bairros
            prospectTelefones (List[Dict[str, Any]]): The telefones
            prospectEnderecoPrincipal (Dict[str, Any]): The endereco principal
            prospectEnderecoCobranca (Dict[str, Any]): The endereco cobranca
            prospectEnderecoComercial (Dict[str, Any]): The endereco comercial
            prospectDependente (List[Dict[str, Any]]): The dependente
            responsavel (str): The responsavel
            buscouDePessoas (int): The de pessoas
            atualizarPessoas (int): The pessoas
            mensagemRetorno (str): The retorno
            prospectDoc (List[Dict[str, Any]]): The doc
        
        Parameter Structure:
        
            {
                "permitirResponsavelSemEstrutura": true,
                "login": "string",
                "prospect": {
                    "numeroProspect": 0,
                    "nomeProspect": "string",
                    "naturezaJuridica": 0,
                    "cpfCnpj": "string",
                    "dataCadastro": "2025-04-23T13:46:14.303Z",
                    "usuarioCadastro": "string",
                    "dataNascimento": "2025-04-23T13:46:14.303Z",
                    "email": "string",
                    "canalComunicacao": 0,
                    "numeroResponsavel": 0,
                    "numeroCliente": 0,
                    "contato": "string",
                    "anexo": 0,
                    "veiculoDivulgacao": 0,
                    "localAtendimento": 0
                },
                "prospectFis": {
                    "numeroProspect": 0,
                    "sexo": 0,
                    "estadoCivil": 0,
                    "regimeDeBens": 0,
                    "nomeMae": "string",
                    "nomePai": "string",
                    "numeroProfissao": 0,
                    "valorRenda": 0,
                    "moedaRenda": "string",
                    "cargo": "string",
                    "codigoNacionalidade": "string",
                    "referenciaPessoal1": "string",
                    "referenciaPessoal1DDD": "string",
                    "referenciaPessoal1Telefone": "string",
                    "referenciaPessoal2": "string",
                    "referenciaPessoal2DDD": "string",
                    "referenciaPessoal2Telefone": "string",
                    "numeroNaturalidade": 0,
                    "uniaoEstavel": true
                },
                "prospectInteresse": {
                    "numeroInteresse": 0,
                    "numeroProspect": 0,
                    "faixaPrecoInicial": 0,
                    "faixaPrecoFinal": 0,
                    "interessadoEm": 0,
                    "usuarioCadastro": "string",
                    "dataCadastro": "2025-04-23T13:46:14.304Z",
                    "anexos": 0,
                    "observacao": "string",
                    "usuarioQueAlterouStatus": "string",
                    "dataQueAlterouStatus": "2025-04-23T13:46:14.304Z",
                    "status": 0,
                    "qtdeDeQuartos": 0,
                    "qtdeDeSuites": 0,
                    "qtdeDeGaragens": 0
                },
                "prospectInteresseProdutos": [
                    {
                        "numeroProduto": 0,
                        "numeroProspect": 0,
                        "numeroInteresse": 0
                    }
                ],
                "prospectInteresseBairros": [
                    {
                        "numeroProspect": 0,
                        "numeroInteresse": 0,
                        "numeroInteresseBairro": 0,
                        "numeroCidade": 0,
                        "numeroBairro": 0
                    }
                ],
                "prospectTelefones": [
                    {
                        "ddd": "string",
                        "telefone": "string",
                        "complemento": "string",
                        "tipoTelefone": 0
                    }
                ],
                "prospectEnderecoPrincipal": {
                    "numeroProspect": 0,
                    "tipoEndereco": 0,
                    "logradouro": "string",
                    "bairro": "string",
                    "cidade": "string",
                    "uf": "string",
                    "cep": "string",
                    "numero": "string",
                    "complemento": "string",
                    "referencia": "string",
                    "enderecoProprio": 0,
                    "numeroCidade": 0,
                    "numeroBairro": 0,
                    "numeroLogradouro": 0,
                    "codigoEmpresa": 0,
                    "nomeEmpresa": "string",
                    "empresaEstaCadastrada": 0
                },
                "prospectEnderecoCobranca": {
                    "numeroProspect": 0,
                    "tipoEndereco": 0,
                    "logradouro": "string",
                    "bairro": "string",
                    "cidade": "string",
                    "uf": "string",
                    "cep": "string",
                    "numero": "string",
                    "complemento": "string",
                    "referencia": "string",
                    "enderecoProprio": 0,
                    "numeroCidade": 0,
                    "numeroBairro": 0,
                    "numeroLogradouro": 0,
                    "codigoEmpresa": 0,
                    "nomeEmpresa": "string",
                    "empresaEstaCadastrada": 0
                },
                "prospectEnderecoComercial": {
                    "numeroProspect": 0,
                    "tipoEndereco": 0,
                    "logradouro": "string",
                    "bairro": "string",
                    "cidade": "string",
                    "uf": "string",
                    "cep": "string",
                    "numero": "string",
                    "complemento": "string",
                    "referencia": "string",
                    "enderecoProprio": 0,
                    "numeroCidade": 0,
                    "numeroBairro": 0,
                    "numeroLogradouro": 0,
                    "codigoEmpresa": 0,
                    "nomeEmpresa": "string",
                    "empresaEstaCadastrada": 0
                },
                "prospectDependente": [
                    {
                        "numProspect": 0,
                        "numDependente": 0,
                        "dataCasamento": "2025-04-23T13:46:14.304Z",
                        "cartorio": "string",
                        "usuarioCadastrou": "string",
                        "codGrauParentesco": 0,
                        "dataCadastro": "2025-04-23T13:46:14.304Z"
                    }
                ],
                "responsavel": "string",
                "buscouDePessoas": true,
                "atualizarPessoas": true,
                "mensagemRetorno": "string",
                "prospectDoc": [
                    {
                        "tipoProspect": 0,
                        "registro": "string",
                        "orgaoEmissor": "string",
                        "codigoNacao": "string",
                        "UF": "string",
                        "dataCadastro": "2025-04-23T13:46:14.304Z",
                        "dataValidade": "2025-04-23T13:46:14.304Z",
                        "usuarioAlterou": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Prospect()
            >>> response = api._gravar_prospect(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/GravarProspect"
        kwargs = {
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("gravar_prospect::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("gravar_prospect::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def importar_prospect(
        self,
        xml: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Prospect/ImportarProspect`
        HTTP Method: `POST`
        
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
            >>> api = Prospect()
            >>> response = api._importar_prospect(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/ImportarProspect"
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("importar_prospect::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("importar_prospect::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def listar_grau_parentesco(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
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
            >>> api = Prospect()
            >>> response = api._listar_grau_parentesco(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/ListarGrauParentesco"
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("listar_grau_parentesco::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("listar_grau_parentesco::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def migrar_prospect_pessoa(
        self,
        numero_prospect: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Prospect/MigrarProspectPessoa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Migra um prospect para pessoa.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            numeroProspect (int): The prospect
        
        Parameter Structure:
        
            {
                "numeroProspect": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Prospect()
            >>> response = api._migrar_prospect_pessoa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/MigrarProspectPessoa"
        kwargs = {
            "numeroProspect": numero_prospect,
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("migrar_prospect_pessoa::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("migrar_prospect_pessoa::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_todos_prospects(
        self,
        enum_opcao_todos: Optional[int] = None,
        codigo_prospect: Optional[str] = None,
        codigo_vendedor: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Prospect/ConsultarTodosProspects`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta os prospects de acordo com os parâmetros definidos na request.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            enumOpcaoTodos (int): The opcao todos
            codigoProspect (str): The prospect
            codigoVendedor (int): The vendedor
        
        Parameter Structure:
        
            {
                "enumOpcaoTodos": 0,
                "codigoProspect": "string",
                "codigoVendedor": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Prospect()
            >>> response = api._consultar_todos_prospects(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/ConsultarTodosProspects"
        kwargs = {
            "enumOpcaoTodos": enum_opcao_todos,
            "codigoProspect": codigo_prospect,
            "codigoVendedor": codigo_vendedor,
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("consultar_todos_prospects::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_todos_prospects::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_prospect_por_chave(
        self,
        codigo_prospect: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Prospect/ConsultarProspectPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta determinado prospect filtrando pelo número deste prospect.
        
        Informação:
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            codigoProspect (int): The prospect
        
        Parameter Structure:
        
            {
                "codigoProspect": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Prospect()
            >>> response = api._consultar_prospect_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/ConsultarProspectPorChave"
        kwargs = {
            "codigoProspect": codigo_prospect,
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("consultar_prospect_por_chave::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_prospect_por_chave::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def alterar_responsavel_prospect(
        self,
        novo_responsavel: Optional[int] = None,
        cod_empresa: Optional[int] = None,
        num_prospect: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Prospect/AlterarResponsavelProspect`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            novoResponsavel (int): The responsavel
            codEmpresa (int): The empresa
            numProspect (int): The prospect
        
        Parameter Structure:
        
            {
                "novoResponsavel": 0,
                "codEmpresa": 0,
                "numProspect": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Prospect()
            >>> response = api._alterar_responsavel_prospect(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/AlterarResponsavelProspect"
        kwargs = {
            "novoResponsavel": novo_responsavel,
            "codEmpresa": cod_empresa,
            "numProspect": num_prospect,
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("alterar_responsavel_prospect::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("alterar_responsavel_prospect::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        """
        
        Endpoint: `Prospect/ConsultarProspectComFiltro`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta prospect filtrando os parâmentros inseridos da request.
        
        Informação: 
        
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        
        Args:
            numeroOpcao (int): The opcao
            numeroVisao (int): The visao
            prospectSemResponsavel (int): The sem responsavel
            codigoResponsavel (str): The responsavel
            nomePessoa (str): The pessoa
            telefone (str): The telefone
            cpfCnpj (str): The cnpj
            trataSemResponsavel (int): The sem responsavel
            ufProsp (str): The prosp
        
        Parameter Structure:
        
            {
                "numeroOpcao": 0,
                "numeroVisao": 0,
                "prospectSemResponsavel": true,
                "codigoResponsavel": "string",
                "nomePessoa": "string",
                "telefone": "string",
                "cpfCnpj": "string",
                "trataSemResponsavel": true,
                "ufProsp": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Prospect()
            >>> response = api._consultar_prospect_com_filtro(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/ConsultarProspectComFiltro"
        kwargs = {
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("consultar_prospect_com_filtro::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_prospect_com_filtro::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def buscar_grau_parentesco_por_codigo(
        self,
        codigo: Optional[int] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Args:
            Codigo (int): The codigo
        
        Parameter Structure:
        
            {
                "Codigo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Prospect()
            >>> response = api._buscar_grau_parentesco_por_codigo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Prospect/BuscarGrauParentescoPorCodigo"
        kwargs = {
            "Codigo": codigo,
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
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("buscar_grau_parentesco_por_codigo::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("buscar_grau_parentesco_por_codigo::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

