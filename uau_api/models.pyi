from _typeshed import Incomplete
from datetime import datetime as datetime
from sqlalchemy.orm import DeclarativeBase, Mapped as Mapped
from typing import Any

class Base(DeclarativeBase):
    type_annotation_map: Incomplete

class Process(Base):
    __tablename__: str
    id: Mapped[int]
    ano: Mapped[int]
    mes: Mapped[int]
    dia: Mapped[int]
    empresa: Mapped[int]
    obra: Mapped[str]
    report_data: Mapped[dict[str, Any]]
    created_at: Mapped[datetime]

class User(Base):
    __tablename__: str
    id: Mapped[int]
    login: Mapped[str]
    nome: Mapped[str]
    email: Mapped[str]
    status: Mapped[str]
    report_data: Mapped[dict[str, Any]]
    created_at: Mapped[datetime]
