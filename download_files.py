import json
import re
from pathlib import Path
from time import sleep
from typing import Dict, List

import dateutil
import pandas as pd
from requests.compat import urlencode
from rich import print as rprint
from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn, track

from uau_api import UauAPI
from uau_api.settings import Settings
from uau_api.utils import save_base64_to_file, write_jsonl

# Initialize the client
uau = UauAPI(Settings().API_URL, Settings().API_KEY)
wd = Path(Settings().WORKDIR)


uau.authenticate('leonardo', 'hybr01')


def get_file(empresa: int, obra: str, processo: str) -> List[Dict]:
    return uau.Anexo.retornar_arquivos_em_lista_bytes(
        empresa, f'PROCESSO {processo}-{obra}'
    )


def load_jsonl(jsonl: str | Path):
    file_content = []
    with open(jsonl) as fc:
        json_file = [json.loads(line) for line in fc.readlines()]
        file_content.extend(json_file)
    return file_content


def remove_duplicate_dicts(list_of_dicts):
    return [dict(t) for t in {tuple(d.items()) for d in list_of_dicts}]


def url_encode(file: str) -> str:
    base_url = (
        'https://hybrazil.sharepoint.com/sites/DataScience'
        '/Documentos%20Compartilhados/Forms/AllItems.aspx'
    )
    root_dir = ('/sites/DataScience'
                '/Documentos Compartilhados/NotasUAU/')
    params = dict(
        id=f'{root_dir}{file}',
        viewid='5b892423-10db-4b4f-a8f9-f0bdeafd317e',
        parent=root_dir,
    )
    encoded = urlencode(params)
    return f'{base_url}?{encoded}'


def main():
    nfe_entrada_jsonl = []
    for file in track(
        (wd / 'NotasUAU/json_files').glob('*.jsonl'), description='Carregando jsonl'
    ):
        content = load_jsonl(file)
        nfe_entrada_jsonl.extend(content)

    nfe_entrada = pd.json_normalize(nfe_entrada_jsonl)
    nfe_entrada = nfe_entrada.filter(regex='^(?!NotaFiscal).')
    nfe_entrada['to_download'] = nfe_entrada['Processos'].apply(
        lambda x: remove_duplicate_dicts(
            [
                dict(Empresa=p['Empresa'], Obra=p['Obra'], Processo=p['Numero'])
                for p in x
                if isinstance(x, list)
            ]
        )
    )

    downloaded = load_jsonl(wd / 'NotasUAU/downloaded.jsonl')
    downloaded = pd.DataFrame(downloaded)
    if not downloaded.empty:
        cols = [
            'Empresa',
            'Obra',
            'Numero',
            'CodigoFornecedor',
            'NumeroNotaFiscal',
        ]
        indexes_df1 = nfe_entrada.set_index(cols).index
        indexes_df2 = downloaded.set_index(cols).index

        indexes_df1.isin(indexes_df2)
        nfe_entrada = nfe_entrada[~indexes_df1.isin(indexes_df2)]

    columns = nfe_entrada.filter(regex=re.compile('data', re.IGNORECASE)).columns
    nfe_entrada[columns] = nfe_entrada[columns].map(dateutil.parser.parse)
    idx = nfe_entrada['ChaveNotaFiscalEletronica'].replace('', pd.NA).isna()
    nfe_entrada = nfe_entrada[~idx].explode('to_download').dropna(subset='to_download')

    with Progress(
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        '[progress.percentage]{task.percentage:>3.0f}%',
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task('Processing rows...', total=len(nfe_entrada))

        for _, row in nfe_entrada.iterrows():
            empresa = row['Empresa']
            obra = row['Obra']
            processo = row['to_download'].get('Processo')
            data_formatada = row['DataEmissao'].strftime('%Y-%m-%d')
            cpf_cnpj_ornecedor = row['CNPJCPFFornecedor']
            numero_nota_fiscal = row['NumeroNotaFiscal']
            dir_name = (f'{row["DataEmissao"].year}'
                        f'/{row["DataEmissao"].month:02d}'
                        f'/{row["DataEmissao"].day:02d}'
                        f'/{empresa}-{obra}')
            destination = wd / f'NotasUAU/{dir_name}'
            destination.mkdir(parents=True, exist_ok=True)
            response = get_file(*row['to_download'].values())
            if isinstance(response, list):
                rprint(row['to_download'].values())
                for index, item in enumerate(response):
                    conteudo = item['ConteudoArquivo']
                    extensao_arquivo = Path(item['NomeArquivo']).suffix.lower()
                    file_name = (
                        f'{empresa}-'
                        f'{obra}-'
                        f'{processo}-'
                        f'{data_formatada}-'
                        f'{cpf_cnpj_ornecedor}-'
                        f'{numero_nota_fiscal}-'
                        f'{index}'
                        f'{extensao_arquivo}'
                    )
                    file_location = destination / f'{file_name}'
                    save_base64_to_file(
                        base64_string=conteudo, output_filename=file_location
                    )
                    url = url_encode(str(file_location).rsplit('NotasUAU/', maxsplit=1)[-1])
                    rcopy = row.copy()
                    rcopy[columns] = rcopy[columns].apply(
                        lambda x: x.strftime('%Y-%m-%d')
                    )
                    line = rcopy.to_dict() | dict(url=url)
                    write_jsonl(line, wd / 'NotasUAU/downloaded.jsonl', mode='a')
            sleep(2)
            progress.advance(task)


if __name__ == '__main__':
    main()
