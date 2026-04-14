import requests
from .requestsapi import RequestsApi as RequestsApi
from .groups.acompanhamento_contrato_venda import AcompanhamentoContratoVenda as AcompanhamentoContratoVenda
from .groups.acompanhamentos_servicos import AcompanhamentosServicos as AcompanhamentosServicos
from .groups.acompanhar_entrega import AcompanharEntrega as AcompanharEntrega
from .groups.anexo import Anexo as Anexo
from .groups.atendimento import Atendimento as Atendimento
from .groups.autenticador import Autenticador as Autenticador
from .groups.banco_horas import BancoHoras as BancoHoras
from .groups.boleto_services import BoletoServices as BoletoServices
from .groups.chave_pix import ChavePix as ChavePix
from .groups.cobranca_pix import CobrancaPix as CobrancaPix
from .groups.comissao import Comissao as Comissao
from .groups.composicoes import Composicoes as Composicoes
from .groups.config_gerais import ConfigGerais as ConfigGerais
from .groups.contabil import Contabil as Contabil
from .groups.contrato_material_servico import ContratoMaterialServico as ContratoMaterialServico
from .groups.correio_eletronico import CorreioEletronico as CorreioEletronico
from .groups.cotacao import Cotacao as Cotacao
from .groups.documentos_digitais_integracao import DocumentosDigitaisIntegracao as DocumentosDigitaisIntegracao
from .groups.empresa import Empresa as Empresa
from .groups.espelho import Espelho as Espelho
from .groups.estrutura import Estrutura as Estrutura
from .groups.eventos import Eventos as Eventos
from .groups.extrato_do_cliente import ExtratoDoCliente as ExtratoDoCliente
from .groups.fiscal import Fiscal as Fiscal
from .groups.folha import Folha as Folha
from .groups.funcionario import Funcionario as Funcionario
from .groups.insumos_geral import InsumosGeral as InsumosGeral
from .groups.lista_preco_referencia import ListaPrecoReferencia as ListaPrecoReferencia
from .groups.localidade import Localidade as Localidade
from .groups.medicao import Medicao as Medicao
from .groups.modelo_venda import ModeloVenda as ModeloVenda
from .groups.notas_fiscais import NotasFiscais as NotasFiscais
from .groups.obras import Obras as Obras
from .groups.orcamento import Orcamento as Orcamento
from .groups.pedido_compra import PedidoCompra as PedidoCompra
from .groups.pessoas import Pessoas as Pessoas
from .groups.planejamento import Planejamento as Planejamento
from .groups.processo_pagamento import ProcessoPagamento as ProcessoPagamento
from .groups.proposta import Proposta as Proposta
from .groups.prospect import Prospect as Prospect
from .groups.recebiveis import Recebiveis as Recebiveis
from .groups.relatorio_irpf import RelatorioIRPF as RelatorioIRPF
from .groups.requisicao_compra import RequisicaoCompra as RequisicaoCompra
from .groups.reserva import Reserva as Reserva
from .groups.rotinas_gerais import RotinasGerais as RotinasGerais
from .groups.shopping import Shopping as Shopping
from .groups.usuarios import Usuarios as Usuarios
from .groups.venda import Venda as Venda
from .groups.webhook import Webhook as Webhook

class UauAPI(RequestsApi):
    is_authenticated: bool
    AcompanhamentoContratoVenda: AcompanhamentoContratoVenda
    AcompanhamentosServicos: AcompanhamentosServicos
    AcompanharEntrega: AcompanharEntrega
    Anexo: Anexo
    Atendimento: Atendimento
    Autenticador: Autenticador
    BancoHoras: BancoHoras
    BoletoServices: BoletoServices
    ChavePix: ChavePix
    CobrancaPix: CobrancaPix
    Comissao: Comissao
    Composicoes: Composicoes
    ConfigGerais: ConfigGerais
    Contabil: Contabil
    ContratoMaterialServico: ContratoMaterialServico
    CorreioEletronico: CorreioEletronico
    Cotacao: Cotacao
    DocumentosDigitaisIntegracao: DocumentosDigitaisIntegracao
    Empresa: Empresa
    Espelho: Espelho
    Estrutura: Estrutura
    Eventos: Eventos
    ExtratoDoCliente: ExtratoDoCliente
    Fiscal: Fiscal
    Folha: Folha
    Funcionario: Funcionario
    InsumosGeral: InsumosGeral
    ListaPrecoReferencia: ListaPrecoReferencia
    Localidade: Localidade
    Medicao: Medicao
    ModeloVenda: ModeloVenda
    NotasFiscais: NotasFiscais
    Obras: Obras
    Orcamento: Orcamento
    PedidoCompra: PedidoCompra
    Pessoas: Pessoas
    Planejamento: Planejamento
    ProcessoPagamento: ProcessoPagamento
    Proposta: Proposta
    Prospect: Prospect
    Recebiveis: Recebiveis
    RelatorioIR_p_f: RelatorioIRPF
    RequisicaoCompra: RequisicaoCompra
    Reserva: Reserva
    RotinasGerais: RotinasGerais
    Shopping: Shopping
    Usuarios: Usuarios
    Venda: Venda
    Webhook: Webhook
    def __init__(self, base_url: str, api_key: str, session: requests.Session | None = None) -> None: ...
    def authenticate(self, username: str, password: str) -> requests.Response: ...
    def get_session(self) -> requests.Session: ...
