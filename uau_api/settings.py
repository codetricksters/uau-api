from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore', env_nested_delimiter='__'
    )

    API_URL: str
    API_KEY: str
    USERNAME: str
    PASSWORD: str