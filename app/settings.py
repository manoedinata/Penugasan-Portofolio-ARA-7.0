from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Portofolio ARA 7.0 Backend"
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
