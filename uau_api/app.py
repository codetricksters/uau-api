import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import copy

from uau_api.database import get_session
from uau_api.models import Process, User
from uau_api.schemas import ProcessSchema, UserSchema
from uau_api.database import get_session
from uau_api.settings import Settings
from uau_api.operations import *
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from sqlalchemy import text, select
from IPython.display import display, HTML
from requests.compat import urljoin
import pandas as pd
import plotly.express as px

from itertools import groupby

import locale
import logging

pd.options.plotting.backend = 'plotly'

logging.basicConfig(
    filename='uau_processos.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# # Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")


api = Api(url=Settings().API_URL)
api.login(**dict(login='natalias', senha='Nat@amora1'))


def gerar_parcelas(
    data_inicio: str,
    valor: int,
    dia_vencimento: int,
    dados_parcela: dict,
    parcelas: int = 12,
):
    '''
    data_inicio  = '2024-09-05'
    data_termino = '2025-09-05'
    parcela = {
       'Datavencimento': vencimento.strftime('%Y-%m-%d') + 'T00:00:00',
       'Valor': valor_parcela,
       'Banco': '341',
       'Conta': '36887-2',
       'CodigoDeBarras': '',
       'ObservacaoPagamento': url,
       'DataDocumentoFiscal': '2023-03-06T00:00:00'
    }
    '''
    result = []
    valor_parcela = valor / parcelas
    if isinstance(data_inicio, str):
        data_termino = datetime.strptime(data_inicio, '%Y-%m-%d') + relativedelta(
            months=parcelas
        )
    else:
        data_termino = data_inicio + relativedelta(months=parcelas)

    for date in pd.date_range(start=data_inicio, end=data_termino, freq='ME'):
        vencimento = date.replace(day=dia_vencimento)
        dados = copy.deepcopy(dados_parcela)
        dados['Datavencimento'] = vencimento.strftime('%Y-%m-%d') + 'T00:00:00'
        dados['Valor'] = valor_parcela
        result.append(dados)

    return result


def gerar_processo(
    empresa: int,
    obra: str,
    banco: str,
    conta: str,
    codigo_fornecedor: int,
    nome_fornecedor: str,
    data_inicio: str,
    dia_vencimento: int,
    valor: int,
    numero_parcelas: int,
    url: str,
):
    '''
    url = 'https://hybrazil.sharepoint.com/sites/HYBRAZIL_SOLAR/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FHYBRAZIL%5FSOLAR%2FShared%20Documents%2F01%20%2D%20PROSPEC%C3%83O%2DFUNDI%C3%81RIO%2FUFVs%20CEAR%C3%81%2FTERRENOS%20FECHADOS%2FBARRO%201%2D5%2FContratos&viewid=2cd14a51%2D58c2%2D41e0%2D97a6%2Db2cfbd24f3d5'
    empresa=254
    obra='ADM'
    codigo_fornecedor=60562,
    nome_fornecedor='FRANCISCO IVALTER BATISTA ALVES'
    data_inicio = '2024-09-10'
    valor = 26400
    parcelas = 12
    '''
    dados_parcela = dict(
        Banco=banco,
        Conta=conta,
        ObservacaoPagamento=url,
        DataDocumentoFiscal=data_inicio,
    )
    parcelas = gerar_parcelas(
        data_inicio=data_inicio,
        valor=valor,
        dia_vencimento=dia_vencimento,
        dados_parcela=dados_parcela,
        parcelas=numero_parcelas,
    )
    processo = {
        'Empresa': empresa,
        'Obra': obra,
        'CodigoFornecedor': codigo_fornecedor,
        'NomeFornecedor': nome_fornecedor,
        'TipoProcesso': 1,
        'TipoItem': 0,
        'Parcelas': parcelas,
        'Itens': [
            {
                'Item': 'HY0799',
                'Quantidade': 1.0,
                'Preco': valor,
                'Cap': '124',
                'CategoriaMovimentacaoFinanceira': '',
                'Unidade': 'VB',
                'VinculoPL': [
                    {
                        'Item': '01.01',
                        'CodigoProduto': -3,
                        'Contrato': -3,
                        'Servico': '902271',
                        'Insumo': 'HY0799',
                        'MesPlanejamento': '2024-09-01T00:00:00',
                        'Quantidade': 1.0,
                        'Preco': valor,
                    }
                ],
            }
        ],
    }

    # response = api.post('ProcessoPagamento/GerarProcesso', json=processo)
    # return response
    return processo


@st.cache_data
def load_data(nrows): ...


def run():
    # Use the full page instead of a narrow central column
    st.set_page_config(layout="wide")
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            empresa: int = st.number_input(label='Código da empresa', step=(1))
        with col2:
            obra: str = st.text_input('Código da obra')
        with col3:
            banco: str = st.text_input('Número do banco')  # '341'
        with col4:
            conta: str = st.text_input('Número da conta')  # '36887-2'
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            codigo_fornecedor: int = st.number_input(
                label='Código do fornecedor', step=(1)
            )
        with col2:
            nome_fornecedor: str = st.text_input('Nome do fornecedor')
        with col3:
            data_inicio: str = st.date_input(
                label='Data de início do contrato', format='YYYY-MM-DD'
            )
        with col4:
            dia_vencimento: int = st.number_input(label='Dia do vencimento', step=(1))
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            valor: int = st.number_input(label='Valor do contrato', step=(1))
        with col2:
            numero_parcelas: int = st.number_input(label='Número de parcelas', step=(1))
        with col3:
            url: str = st.text_input('URL do contrato')

    if st.button('Gerar processo'):
        response = gerar_processo(
            empresa=empresa,
            obra=obra,
            banco=banco,
            conta=conta,
            codigo_fornecedor=codigo_fornecedor,
            nome_fornecedor=nome_fornecedor,
            data_inicio=data_inicio,
            dia_vencimento=dia_vencimento,
            valor=valor,
            numero_parcelas=numero_parcelas,
            url=url,
        )
        df = pd.json_normalize(response, record_path='Parcelas', meta=['Empresa', 'Obra', 'CodigoFornecedor', 'NomeFornecedor'])
        st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    run()
