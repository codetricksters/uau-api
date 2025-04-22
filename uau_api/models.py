from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.dialects.postgresql import JSONB
from typing import Any, Dict

class Base(DeclarativeBase):
    type_annotation_map = {Dict[str, Any]: JSONB}

class Process(Base):
    __tablename__ = 'processos'
    id: Mapped[int] = mapped_column(primary_key=True)
    ano: Mapped[int]
    mes: Mapped[int]
    dia: Mapped[int]
    empresa: Mapped[int]
    obra: Mapped[str]
    report_data: Mapped[Dict[str, Any]]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

class User(Base):
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    nome: Mapped[str]
    email: Mapped[str]
    status: Mapped[str]
    report_data: Mapped[Dict[str, Any]]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())