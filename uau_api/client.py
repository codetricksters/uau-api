"""Main API client module."""
from typing import Dict, Any, Optional
import requests
from .requestsapi import RequestsApi

class UauAPI(RequestsApi):
    """Main API client class that provides access to all API groups."""
    
    def __init__(self, base_url: str, api_key: str, session: Optional[requests.Session] = None):
        """Initialize the API client.
        
        Args:
            base_url: The base URL for the API
            session: Optional session to use for requests
        """
        super().__init__(base_url, api_key, session)
        self.is_authenticated = False
        self._init_api_groups()
        self.session.headers['X-INTEGRATION-Authorization'] = api_key

    def _init_api_groups(self):
        """Initialize API group classes."""
        # Import all group classes
        from .groups.acompanhamento_contrato_venda import AcompanhamentoContratoVenda
        from .groups.acompanhamentos_servicos import AcompanhamentosServicos
        from .groups.acompanhar_entrega import AcompanharEntrega
        from .groups.anexo import Anexo
        from .groups.atendimento import Atendimento
        from .groups.autenticador import Autenticador
        from .groups.banco_horas import BancoHoras
        from .groups.boleto_services import BoletoServices
        from .groups.chave_pix import ChavePix
        from .groups.cobranca_pix import CobrancaPix
        from .groups.comissao import Comissao
        from .groups.composicoes import Composicoes
        from .groups.config_gerais import ConfigGerais
        from .groups.contabil import Contabil
        from .groups.contrato_material_servico import ContratoMaterialServico
        from .groups.correio_eletronico import CorreioEletronico
        from .groups.cotacao import Cotacao
        from .groups.documentos_digitais_integracao import DocumentosDigitaisIntegracao
        from .groups.empresa import Empresa
        from .groups.espelho import Espelho
        from .groups.estrutura import Estrutura
        from .groups.eventos import Eventos
        from .groups.extrato_do_cliente import ExtratoDoCliente
        from .groups.fiscal import Fiscal
        from .groups.folha import Folha
        from .groups.funcionario import Funcionario
        from .groups.insumos_geral import InsumosGeral
        from .groups.lista_preco_referencia import ListaPrecoReferencia
        from .groups.localidade import Localidade
        from .groups.medicao import Medicao
        from .groups.modelo_venda import ModeloVenda
        from .groups.notas_fiscais import NotasFiscais
        from .groups.obras import Obras
        from .groups.orcamento import Orcamento
        from .groups.pedido_compra import PedidoCompra
        from .groups.pessoas import Pessoas
        from .groups.planejamento import Planejamento
        from .groups.processo_pagamento import ProcessoPagamento
        from .groups.proposta import Proposta
        from .groups.prospect import Prospect
        from .groups.recebiveis import Recebiveis
        from .groups.relatorio_irpf import RelatorioIRPF
        from .groups.requisicao_compra import RequisicaoCompra
        from .groups.reserva import Reserva
        from .groups.rotinas_gerais import RotinasGerais
        from .groups.shopping import Shopping
        from .groups.usuarios import Usuarios
        from .groups.venda import Venda
        from .groups.webhook import Webhook
        
        # Initialize group instances
        self.AcompanhamentoContratoVenda = AcompanhamentoContratoVenda(self)
        self.AcompanhamentosServicos = AcompanhamentosServicos(self)
        self.AcompanharEntrega = AcompanharEntrega(self)
        self.Anexo = Anexo(self)
        self.Atendimento = Atendimento(self)
        self.Autenticador = Autenticador(self)
        self.BancoHoras = BancoHoras(self)
        self.BoletoServices = BoletoServices(self)
        self.ChavePix = ChavePix(self)
        self.CobrancaPix = CobrancaPix(self)
        self.Comissao = Comissao(self)
        self.Composicoes = Composicoes(self)
        self.ConfigGerais = ConfigGerais(self)
        self.Contabil = Contabil(self)
        self.ContratoMaterialServico = ContratoMaterialServico(self)
        self.CorreioEletronico = CorreioEletronico(self)
        self.Cotacao = Cotacao(self)
        self.DocumentosDigitaisIntegracao = DocumentosDigitaisIntegracao(self)
        self.Empresa = Empresa(self)
        self.Espelho = Espelho(self)
        self.Estrutura = Estrutura(self)
        self.Eventos = Eventos(self)
        self.ExtratoDoCliente = ExtratoDoCliente(self)
        self.Fiscal = Fiscal(self)
        self.Folha = Folha(self)
        self.Funcionario = Funcionario(self)
        self.InsumosGeral = InsumosGeral(self)
        self.ListaPrecoReferencia = ListaPrecoReferencia(self)
        self.Localidade = Localidade(self)
        self.Medicao = Medicao(self)
        self.ModeloVenda = ModeloVenda(self)
        self.NotasFiscais = NotasFiscais(self)
        self.Obras = Obras(self)
        self.Orcamento = Orcamento(self)
        self.PedidoCompra = PedidoCompra(self)
        self.Pessoas = Pessoas(self)
        self.Planejamento = Planejamento(self)
        self.ProcessoPagamento = ProcessoPagamento(self)
        self.Proposta = Proposta(self)
        self.Prospect = Prospect(self)
        self.Recebiveis = Recebiveis(self)
        self.RelatorioIR_p_f = RelatorioIRPF(self)
        self.RequisicaoCompra = RequisicaoCompra(self)
        self.Reserva = Reserva(self)
        self.RotinasGerais = RotinasGerais(self)
        self.Shopping = Shopping(self)
        self.Usuarios = Usuarios(self)
        self.Venda = Venda(self)
        self.Webhook = Webhook(self)


    def authenticate(self, username: str, password: str) -> Dict[str, Any]:
        """Authenticate with the API.
        
        Args:
            username: API username
            password: API password
        
        Returns:
            Authentication response data
        """
        auth_response = self.post(
            "Autenticador/AutenticarUsuario",
            json={"Login": username, "Senha": password, 'UsuarioUAUSite': username}
        )
        
        if auth_response.status_code == 401:
            # Remove existing Authorization header if present
            self.session.headers.pop('Authorization', None)
            # Try authentication again
            auth_response = self.post(
                "Autenticador/AutenticarUsuario",
                json={"Login": username, "Senha": password}
            )
            
        self.session.headers['Authorization'] = auth_response.json()
        self.is_authenticated = True
        return auth_response
        
    def get_session(self) -> requests.Session:
        """Get the current session.
        
        Returns:
            The requests Session object
        """
        return self.session