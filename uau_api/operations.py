from http import HTTPStatus
from uau_api.requestsapi import RequestsApi
from uau_api.settings import Settings
from datetime import datetime
from typing import List, Dict
import json


from uau_api.models import Process, User
from uau_api.schemas import ProcessSchema, UserSchema
from uau_api.database import get_session
from sqlalchemy import text, select
from sqlalchemy.orm import Session
from requests.exceptions import HTTPError


from datetime import datetime
from http import HTTPStatus
import json
from typing import List, Dict, Optional

# Assuming RequestsApi and Settings are defined elsewhere
class Api(RequestsApi):
    def __init__(self, url):
        super().__init__(url)
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def login(self, login: str, senha: str):
        '''
        'Login': 'str',
        'Senha': 'str',
        'UsuarioUAUSite': 'str'
        '''
        user = {
            'Login': login,
            'Senha': senha,
            'UsuarioUAUSite': login
        }
        api_key = Settings().API_KEY
        self.headers['X-INTEGRATION-Authorization'] = api_key

        response = self.post(
            'Autenticador/AutenticarUsuario',
            headers=self.headers,
            data=json.dumps(user)
        )

        if not response.status_code == HTTPStatus.OK:
            self.session.close()
            
        print('Update headers')
        
        self.headers['Authorization'] = response.json()
        
        self.session.headers.update(self.headers)
        return response

    @staticmethod
    def query_construct(
        empresa_obra: List[Dict],
        data_inicio: datetime,
        data_termino: datetime,
        processos: Optional[List[int]] = None,
        **kwargs
    ):
        '''
        Constructs the query payload.
        '''
        data = {
            'EmpresaObraPeriodo': {
                'EmpresaObra': empresa_obra,
                'PeriodoInicial': data_inicio.isoformat() + 'Z',
                'PeriodoFinal': data_termino.isoformat() + 'Z'
            }
        }
        if processos:
            processos_list = [
                {
                    'NumeroProcesso': processo,
                    'Empresa': empresa['Empresa'],
                    'Obra': empresa['Obra']
                }
                for empresa in empresa_obra
                for processo in processos
            ]
            data['Processos'] = processos_list

        return data
    def gerar_processo(
        self, 
    ):
        '''
        post /api/v{version}/ProcessoPagamento/GerarProcesso
        '''
    
    def get_processos(
        self,
        empresa_obra: List[Dict],
        data_inicio: datetime,
        data_termino: datetime,
        processos: Optional[List[int]] = None):
        
        data = self.query_construct(
            empresa_obra=empresa_obra,
            processos=processos,
            data_inicio=data_inicio,
            data_termino=data_termino
        )
        response = self.post(
            'ProcessoPagamento/ConsultarProcessos',
            json=data
        )
        return response

    def get_users(self, username=None):
        payload = {'login_usuario': username} if username else {}
        response = self.post(
            'Usuarios/ConsultarUsuariosAtivos',
            json=payload
        )
        if response.status_code == HTTPStatus.OK:
            return response
        else:
            response.raise_for_status()

    def inserir_insumo(self, insumo):
        '''
        Inserts an "insumo" into the system.
        '''
        consulta_servico = self.post(
            'Planejamento/ConsultarServicoPlanejamento',
            json=insumo
        ).json()

        servico_existe = len(consulta_servico) > 1

        if not servico_existe:
            return False

        response = self.post(
            'Planejamento/AtualizarInsumosPlanejamento',
            json={'Insumos': [insumo]}
        )

        if response.status_code != HTTPStatus.OK:
            response.raise_for_status()

        return response



def create_process(process: ProcessSchema, session: Session):
    db_process = session.scalar(
        select(Process).where(
            (Process.ano == process.ano) 
            & (Process.mes == process.mes) 
            & (Process.dia == process.dia) 
            & (Process.empresa == process.empresa)
            & (Process.obra == process.obra)
        )
    )

    if db_process:
        if all([db_process.ano == process.ano, db_process.mes == process.mes, db_process.dia == process.dia]):
            session.rollback()
            return 0

    db_process = Process(
        ano=process.ano,
        mes=process.mes,
        dia=process.dia,
        empresa=process.empresa,
        obra=process.obra,
        report_data=process.report_data,
    )

    session.add(db_process)
    session.commit()
    session.refresh(db_process)

    return db_process


def update_process(process: ProcessSchema, session:Session):
    db_process = session.scalar(
        select(Process).where(
            (Process.ano == process.ano) 
            & (Process.mes == process.mes) 
            & (Process.dia == process.dia) 
            & (Process.empresa == process.empresa)
            & (Process.obra == process.obra)
        )
    )
    if not db_process:
        print(f'Processo não encontrado para {process.ano=} {process.mes=} {process.dia=} {process.empresa=} {process.obra=}')
        return

    db_process.ano = process.ano
    db_process.mes = process.mes
    db_process.dia = process.dia
    db_process.empresa = process.empresa
    db_process.obra = process.obra

    session.commit()
    session.refresh(db_process)

    return db_process


def create_user(user: UserSchema, session: Session):
    db_user = session.scalar(
        select(User).where(User.login == user.login)
    )

    if db_user:
        if db_user.login == user.login:
            session.rollback()
            print(f'Processo {db_user} já existe')

    db_user = User(
        login=user.login,
        nome=user.nome,
        email=user.email,
        status=user.status,
        report_data=user.report_data,
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def read_process(process: ProcessSchema, session: Session, limit: int = 10, offset: int = 0):
    process = session.scalars(select(Process).limit(limit).offset(offset)).all()
    return dict(process=process)

