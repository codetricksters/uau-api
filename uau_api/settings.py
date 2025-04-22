from pydantic import BaseModel, SecretStr


from pydantic_settings import BaseSettings, SettingsConfigDict


class UserSettings(BaseModel):
    Login: str
    Senha: str
    UsuarioUAUSite: str


class User(BaseModel):
    name: str
    config: UserSettings

class DatabaseUrl(BaseModel):
    drivername: str
    username: str
    password: str
    host: str
    port: int
    database: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore', env_nested_delimiter='__'
    )

    API_URL: str
    API_KEY: str
    USERS: list[User]
    DATABASE_URL: DatabaseUrl