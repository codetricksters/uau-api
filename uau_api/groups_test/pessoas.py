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
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite inserir ou alterar pessoa física ou jurídica e seus respectivos dados. Se for uma nova pessoa, informar "0" no parâmetro cod_pes.
        Se for alterar uma pessoa já existente, informar o código no parâmetro cod_pes.
        1. Deve montar uma estrutura com as informações de determinada pessoa.
        - https://ajuda.globaltec.com.br/download/801043/
        2. Valida a estrutura do e-mail
        3. Valida se o nome de usuário informado para acesso ao uau web existe para outra pessoa
        4. Valida campos obrigatórios
        5. O campo *dspes_tel_json* espera uma String json no formato abaixo.
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
        
            - Sempre a primeira linha do json é a estrutura do mesmo, então ela sempre irá se repetir, apartir dela, as proximas serão os telefones. No exemplo tempo 5 telefones.
            - Isto ocorre por ser um método antigo do UAU, que foi migrado para API. Futuramente esse endpoint vai ser descontinuado.
        6. Valida Nação e UF referente aos campos 'codnacao_pf' e 'ufnasc_pf' respectivamente, Ex: Nação: 'BRA' UF: 'GO',ou seja se for informado Nação será obrigado UF ou vice-versa.
            - https://ajuda.globaltec.com.br/virtuau/cadastro-de-unidade-federativa/
            
        7. Valida código e descrição do município referente aos campos 'cidadenat_pf' e 'naturalid_pf' respectivamente, Ex: Código: '1' Descrição: 'Goiânia'. 
            - Se caso for informado cidadenat_pf também será obrigado informar o campo naturalid_pf ou vice-versa. 
            - https://ajuda.globaltec.com.br/virtuau/virtuau/cadastro-de-municipios/
             
        8. Validação tamanho do endereço: Essa validação pode ser ativada no cadastro de Pessoas em “Config.” ou seja em configuração de endereço, quando se marca a opção:
             “Limitar o cadastro de endereço de cobrança de pessoas e prospects para o máximo permitido nos boletos”, se essa opção estiver marcada no momento da requisição 
             se tiver utilizando o endereço maior  que o permitido poderá receber a seguinte mensagem” O campo 'Bairro - Endereço de cobrança' está com o tamanho acima do permitido: 15 | atual: 27.", como exemplo.
            
        9.  Verificação para Gravação das informações do documento da Pessoa: Verifica se o campo "info_pesfis" (informações da Pessoa física) foi informado, pois se não foi, o infopes_doc (informações dos documentos da Pessoa) não será considerado. 
        
        10. Informação: 
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
            
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/uau-pessoas/#GravarPessoa
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/774876/
        - Exemplo Retorno: https://ajuda.globaltec.com.br/download/774882/
        
        Endpoint: `/api/v{version}/Pessoas/GravarPessoa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Insere ou altera Pessoa Física ou Jurídica e seus dados
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "info_pes"
                        ],
                        "type": "object",
                        "properties": {
                            "nao_validar_campos_obrigatorios": {
                                "description": "Indica se está utilizando campos obrigatórios",
                                "type": "boolean"
                            },
                            "info_pes": {
                                "$ref": "#/definitions/UAUApi.Models.Pessoas.Pessoas",
                                "description": "Contém informações da Pessoa(física ou jurídica)"
                            },
                            "info_pesfis": {
                                "$ref": "#/definitions/UAUApi.Models.Pessoas.PesFis",
                                "description": "Contém informações da Pessoa física"
                            },
                            "infopes_jur": {
                                "$ref": "#/definitions/UAUApi.Models.Pessoas.PesJur",
                                "description": "Contém informações da Pessoa jurídica"
                            },
                            "dspes_tel_json": {
                                "description": "Contém os telefones da Pessoa(física ou jurídica)",
                                "type": "string"
                            },
                            "infopes_doc": {
                                "$ref": "#/definitions/UAUApi.Models.Pessoas.PessoasDoc",
                                "description": "Contém as informações dos documentos da Pessoa"
                            },
                            "info_pesendereco_principal": {
                                "$ref": "#/definitions/UAUApi.Models.Pessoas.PesEndereco",
                                "description": "Contém os endereço principal da pessoa"
                            },
                            "infopesendereco_cobranca": {
                                "$ref": "#/definitions/UAUApi.Models.Pessoas.PesEndereco",
                                "description": "Contém o endereço de cobrança da pessoa"
                            },
                            "infopesendereco_comercial": {
                                "$ref": "#/definitions/UAUApi.Models.Pessoas.PesEndereco",
                                "description": "Contém o endereço comercial da pessoa"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
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
        path = f"/api/v{version}/Pessoas/GravarPessoa"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def manter_telefone(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Número de usuário é obrigatório.
        4. Nível de permissão, GETELPES Alteração ou Inclusão
        
        Definição de Negócio:
        1. Quando o telefone não existe, ele é adicionado em relacionamento ao usuário proposto.
        2. Quando o telefone já existe, ele faz a alteração dos dados.
        3. Não se pode ter telefones iguais para a mesma pessoa. Caso tente colocar um telefone que já existe para determinada pessoa, irá retornar uma mensagem de erro.
        4. O mesmo telefone pode ter usuários diferentes, e a alteração é feita somente naquele diretamente relacionado.
        4.Só pode possuir um telefone como principal por pessoa
        
        4. Informação:
        Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ManterTelefone`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar ou inserir telefones ao usuário
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "Numero",
                            "Telefones"
                        ],
                        "type": "object",
                        "properties": {
                            "Numero": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "Telefones": {
                                "description": "Lista de telefones",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Pessoa.ManterTelefone"
                                }
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ManterTelefone"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def excluir_telefone(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Número de usuário é obrigatório.
        4. Nível de permissão, GETELPES Exclusão
        
        Definição de Negócio:
        1. A exclusão do telefone é feita somente para o usuário informado.
        
        Informação:
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ExcluirTelefone`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir telefones em relação ao usuário
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "Numero",
                            "Telefones"
                        ],
                        "type": "object",
                        "properties": {
                            "Numero": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "Telefones": {
                                "description": "Lista de telefones",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Pessoa.ExcluirTelefone"
                                }
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ExcluirTelefone"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_unidades(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Informar o código da pessoa ou CPF/CNPJ da pessoa para uso do método.
        
        Regras de Negócio:
        1. CPF/CNPJ aceita apenas números.
        2. Valida se encontrou a pessoa.
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarUnidades`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar unidades do cliente
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "CodigoPessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "CpfCnpj": {
                                "description": "CPF ou CNPJ da pessoa",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarUnidades"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def alterar_conta_padrao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Parâmetros da request
        1. codigoPessoa: Código da Pessoa.
        2. codigoBanco: Código do Banco.
        3. agencia: Número da Agência.
        4. conta: Conta.
        
        Endpoint: `/api/v{version}/Pessoas/AlterarContaPadrao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Altera a conta corrente padrão de uma pessoa.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "CodigoPessoa",
                            "CodigoBanco",
                            "Agencia",
                            "Conta"
                        ],
                        "type": "object",
                        "properties": {
                            "CodigoPessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "CodigoBanco": {
                                "format": "int32",
                                "description": "Código do banco",
                                "type": "integer"
                            },
                            "Agencia": {
                                "description": "Numero da agência",
                                "type": "string"
                            },
                            "Conta": {
                                "description": "Conta",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Pessoas()
            >>> response = api._alterar_conta_padrao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Pessoas/AlterarContaPadrao"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_telefones(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Número de usuário é obrigatório.
        4. Nível de permissão, GETELPES Consulta
        
        Definição de Negócio:
        1. Listagem dos telefones relacionadas ao usuário.
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarTelefones`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar telefones em relação ao usuário
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "Numero"
                        ],
                        "type": "object",
                        "properties": {
                            "Numero": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarTelefones"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def alterar_senha_cliente(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Autenticador/ConsultarDadosUsrLogado
        3. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite alterar a senha do cliente.
        1. Deve informar o código do próprio cliente logado no Uau Web no qual será alterada a senha.
        2. A senha deve conter exatamente 6 caracteres e não poderá estar criptografada.
        3. Realiza validação se o login informado está sendo utilizado por outro cliente.
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Alteracao_de_Senha_do_Usuario_Cliente
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/774830/
        
        Endpoint: `/api/v{version}/Pessoas/AlterarSenhaCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar a Senha da Pessoa/Cliente que permite acesso a área de Clientes no Uau Web
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigo_cliente",
                            "senha"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo_cliente": {
                                "format": "int32",
                                "description": "Código do cliente",
                                "type": "integer"
                            },
                            "senha": {
                                "description": "Senha do cliente",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/AlterarSenhaCliente"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def gravar_conta_bancaria(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
        3. Preencher os parâmetros de request com os dados bancários e o código da pessoa para uso do método.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        Endpoint: `/api/v{version}/Pessoas/GravarContaBancaria`
        HTTP Method: `POST`
        
        Implementation Notes:
        Grava banco e conta por pessoa
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigoPessoa",
                            "banco",
                            "conta",
                            "tipo",
                            "agencia"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoPessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "banco": {
                                "format": "int32",
                                "description": "Banco",
                                "type": "integer"
                            },
                            "conta": {
                                "description": "Conta (Ex. 10200-3)",
                                "type": "string"
                            },
                            "padrao": {
                                "description": "Conta padrão (true para sim e false para não)",
                                "type": "boolean"
                            },
                            "tipo": {
                                "format": "int32",
                                "description": "Tipo da conta (0 - Conta Corrente, 1 - Conta Poupança, 2 - Conta FGTS ou 3 - Conta Salário)",
                                "type": "integer"
                            },
                            "agencia": {
                                "description": "Agência",
                                "type": "string"
                            },
                            "nomeAgencia": {
                                "description": "Nome da agência",
                                "type": "string"
                            },
                            "debitoAutomatico": {
                                "description": "Débito automático (true para sim e false para não)",
                                "type": "boolean"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/GravarContaBancaria"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_tipo_endereco(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarTipoEndereco`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar tipo de endereço da pessoa
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigoPessoa"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoPessoa": {
                                "format": "int32",
                                "description": "Número do código da pessoa",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarTipoEndereco"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def criar_credenciais_uauweb(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        1. É necessário que o usuario forneça o UsuarioUAUSite ao obter o token de autenticação.
        2. O usuário não pode estar duplicado no banco de dados.
        3. O Email não pode estar sendo utilizado por outra pessoa.
        4. O usuário não pode já ter um Login UAUWeb.
        5. O novo login não pode estar sendo utilizado por outra pessoa.
        
        Endpoint: `/api/v{version}/Pessoas/CriarCredenciaisUAUWeb`
        HTTP Method: `POST`
        
        Implementation Notes:
        Cria um novo usuário e senha para a pessoa no UAUWeb.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "CPF",
                            "DataNascimento",
                            "Login",
                            "Senha",
                            "Email"
                        ],
                        "type": "object",
                        "properties": {
                            "CPF": {
                                "description": "Contém o CPF ou o CNPJ da pessoa. Deve ser informado sem pontuação",
                                "type": "string"
                            },
                            "DataNascimento": {
                                "format": "date-time",
                                "description": "Contém a data de nascimento da pessoa caso seja um CPF na propriedade CPF_CNPJ\r\nou contém a data de fundação caso seja um CNPJ",
                                "type": "string"
                            },
                            "Login": {
                                "description": "Contém o Login do UAUWeb",
                                "type": "string"
                            },
                            "Senha": {
                                "description": "Contém a nova senha no UAUWeb",
                                "type": "string"
                            },
                            "Email": {
                                "description": "Contém o email da pessoa",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/CriarCredenciaisUAUWeb"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_pessoa_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Cosulta os dados de uma pessoa filtrando pelo código.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarPessoaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta dados primários de uma pessoa
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "codigo_pessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarPessoaPorChave"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_contas_bancarias(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
        3. Informar o código da pessoa para uso do método.
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarContasBancarias`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar contas bancárias por código de determinada pessoa
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigo"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo": {
                                "description": "Código da pessoa",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarContasBancarias"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_pessoas_com_venda(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Retorna código de nome da pessoa.
        
        Definição de Negócio:
        1. As vendas podem ser quitadas ou não.
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarPessoasComVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta clientes que são titulares de vendas
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarPessoasComVenda"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def alterar_pessoa_acesso_portal(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Autenticador/ConsultarDadosUsrLogado
        3. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite alterar os dados de acesso ao Uau Web login, senha e e-mail.
        1. Deve informar o código do próprio cliente logado no Uau Web no qual serão atualizados os dados.
        2. A senha deve conter exatamente 6 caracteres e não poderá estar criptografada.
        3. Realiza validação se o login informado está sendo utilizado por outro cliente.
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Alteracao_dos_Dados_de_Acesso_do_Cliente
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/775432/
        
        Endpoint: `/api/v{version}/Pessoas/AlterarPessoaAcessoPortal`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualiza os dados de acesso ao UAU Web de uma determinada pessoa.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigo_pessoa"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo_pessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "login": {
                                "description": "Login de acesso ao Uau Web",
                                "type": "string"
                            },
                            "senha": {
                                "description": "Senha de acesso",
                                "type": "string"
                            },
                            "email": {
                                "description": "Endereço de email",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/AlterarPessoaAcessoPortal"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_pessoas_por_cpfcnpj(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Deve informar o CPF/CNPJ sem formatações e o status.
        4. O status pode ser:
            - 0 = Ativo 
            - 1 = Inativo
            - 2 = Ambos
        
        Definição de Negócio:
        Permite obter os dados de determinada pessoa física ou jurídica.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Consultar_dados_da_pessoa_por_CPFCNPJ
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/774849/
        - Exemplo Retorno: https://ajuda.globaltec.com.br/download/774846/
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarPessoasPorCPFCNPJ`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os dados da pessoa por CPF/CNPJ e Status
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "cpf_cnpj",
                            "status"
                        ],
                        "type": "object",
                        "properties": {
                            "cpf_cnpj": {
                                "description": "Número do CPF/CNPJ - SOMENTE NÚMEROS",
                                "type": "string"
                            },
                            "status": {
                                "format": "int32",
                                "description": "Status 0-Ativos 1-Inativos 2-Ambos",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarPessoasPorCPFCNPJ"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def excluir_banco_econta_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
        3. Consultar os dados bancarios da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarContasBancarias.
        4. Preencher os parâmetros de request com os dados bancários e o código da pessoa para uso do método.
        
        Regras de Negócio:
        1. Valida usuário e permissões.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        Endpoint: `/api/v{version}/Pessoas/ExcluirBancoEContaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Exclui banco e conta por pessoa
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigoPessoa",
                            "banco",
                            "conta",
                            "agencia"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoPessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            },
                            "banco": {
                                "format": "int32",
                                "description": "Banco",
                                "type": "integer"
                            },
                            "conta": {
                                "description": "Conta (Ex. 10200-3)",
                                "type": "string"
                            },
                            "agencia": {
                                "description": "Agência",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ExcluirBancoEContaPorChave"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def recuperar_credenciais_uauweb(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com o login ou o email do usuário da pessoa para uso do método.
        
        Regras de Negócio:
        
        1. É necessário que o usuário forneça o UsuarioUAUSite ao obter o token de autenticação.
        2. O usuário logado (informado na rota de autenticação) deverá possuir configuração de email cadastrada. Para verificar, acesse a Tela de Configurações do Usuário - Configurações - Configuração Email.
        3. Deverá estar parametrizado a configuração "Enviar os avisos de pendências também por email externo", na aba Geral da tela de Configurações do Sistema.
        4. O usuário não pode estar duplicado no banco de dados.
        5. O usuário deve já ter um Login UAUWeb.
        6. O usuário deve ter um email cadastrado.
        7. Caso login e email seja enviado, é verificado se o usuário com esse login possui esse email cadastrado.
        
        Endpoint: `/api/v{version}/Pessoas/RecuperarCredenciaisUAUWeb`
        HTTP Method: `POST`
        
        Implementation Notes:
        Envia por e-mail a senha de uma pessoa do UAUWeb.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Login": {
                                "description": "Contém o login da pessoa",
                                "type": "string"
                            },
                            "Email": {
                                "description": "Contém o email da pessoa",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/RecuperarCredenciaisUAUWeb"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_pessoas_por_condicao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. A condição informada é uma clausula SQL pós WHERE, segue exemplo:
            - cpf_pes = '12345678910' AND nome_pes LIKE 'GLOBALTEC%'
        4. Devem ser passado as aspas simples para campos string.
        
        Definição de Negócio:
        1. Consulta pessoa por condição informada. 
        2. Valida a condição da consulta, evitando SQL Injection.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarPessoasPorCondicao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os dados da pessoa de acordo com a condição informanda na busca
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "condicaoConsultarPessoa": {
                                "description": "Condição WHERE que será usada para consultar pessoas \r\nEx: cod_pes = 1855\r\n    cpf_pes = '13113131313331' AND nome_pes LIKE 'GLOBALTEC%'\r\nobs.: Devem ser passado as aspas simples para campos string.",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarPessoasPorCondicao"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def importar_dados_pessoas_para_uau(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Deve seguir arquivo XSD com o formato aceito.
        
        Definição de Negócio:
        1. Realiza a importação dos dados de pessoas para o UAU atravéz de arquivo XML.
        2. Será validado o xml deserializado que preenche a classe de importação validando os dados.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/uau-pessoas-2/
        
        Anexos:
        1. Arquivo XSD do XML: https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2016/06/Pessoasxsd-1.rar
        2. Exemplo XML: https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2016/06/Pessoas-3.rar
        
        Endpoint: `/api/v{version}/Pessoas/ImportarDadosPessoasParaUau`
        HTTP Method: `POST`
        
        Implementation Notes:
        Importa os dados de pessoas
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "xml"
                        ],
                        "type": "object",
                        "properties": {
                            "xml": {
                                "description": "Xml montado conforme o arquivo XSD de Pessoas",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ImportarDadosPessoasParaUau"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_telefone_pes_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
        3. Preencher os parâmetros de request para uso do método.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarTelefonePesPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta telefones da pessoa
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "codigoPessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarTelefonePesPorChave"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_endereco_pessoas_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarEnderecoPessoasPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar endereços de pessoa por código da pessoa e tipo de endereço
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigoPessoa",
                            "tipoEndereco"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoPessoa": {
                                "format": "int32",
                                "description": "Número do código da pessoa",
                                "type": "integer"
                            },
                            "tipoEndereco": {
                                "format": "int32",
                                "description": "Tipo de endereço: 0 - Endereço Principal, 1 - Endereço Cobrança, 2 - Endereço Comercial",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarEnderecoPessoasPorChave"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_pessoas_funcionarios_ativos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarPessoasFuncionariosAtivos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar funcionários ativos
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Page": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "PageSize": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "SearchText": {
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarPessoasFuncionariosAtivos"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_dados_pessoa_fisica_por_codigo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Consulta dados de pessoa física filtrando pelo código da pessoa.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarDadosPessoaFisicaPorCodigo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar dados de pessoa física
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "codigopessoa_fis": {
                                "format": "int32",
                                "description": "Código da pessoa física",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarDadosPessoaFisicaPorCodigo"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_dados_pessoa_por_cpf_cnpj_estatus(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Informar o CPF/CNPJ e status da pessoa para uso do método.
        
        Regras de Negócio:
        1. CPF/CNPJ aceita apenas números.
        2. Valida se encontrou a pessoa.
        
        Informação:
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        VirtUau:
        - https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta pessoa por CPF/CNPJ e Status
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "cpf_cnpj",
                            "status"
                        ],
                        "type": "object",
                        "properties": {
                            "cpf_cnpj": {
                                "description": "Número do CPF/CNPJ - SOMENTE NÚMEROS",
                                "type": "string"
                            },
                            "status": {
                                "format": "int32",
                                "description": "Status 0-Ativos 1-Inativos 2-Ambos",
                                "enum": [
                                    0,
                                    1,
                                    2
                                ],
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_dados_adicionais_pessoa_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        1. Busca por dados adicionais de pessoa filtrando pela chave.
        
        Informação: 
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Pessoas/ConsultarDadosAdicionaisPessoaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta dados adicionais de uma pessoa por chave
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "codigo_pessoa"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo_pessoa": {
                                "format": "int32",
                                "description": "Código da pessoa",
                                "type": "integer"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Pessoas/ConsultarDadosAdicionaisPessoaPorChave"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

