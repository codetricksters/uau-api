from _typeshed import Incomplete
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config: Incomplete
    API_URL: str
    API_KEY: str
    USERNAME: str
    PASSWORD: str
