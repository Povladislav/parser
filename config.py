from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_ROOT_USERNAME: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    GRANT_TYPE: str

    class Config:
        env_file = ".env"


settings = Settings()
