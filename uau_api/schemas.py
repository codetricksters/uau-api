from pydantic import BaseModel, ConfigDict, EmailStr

class ProcessSchema(BaseModel):
    ano: int
    mes: int
    dia: int
    empresa: int
    obra: str
    report_data: list[dict]


class UserSchema(BaseModel):
    login: str
    nome: str
    email: str
    status: int
    report_data: list[dict]