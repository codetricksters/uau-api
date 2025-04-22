from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL

from uau_api.models import Base
from uau_api.settings import Settings

url = URL.create(**Settings().DATABASE_URL.model_dump())

engine = create_engine(url)

Base.metadata.create_all(engine)


def get_session():  # pragma no cover
    with Session(engine) as session:
        yield session