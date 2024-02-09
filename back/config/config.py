from pydantic import BaseConfig


class Settings(BaseConfig):
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str

    ACCESS_TOKEN_EXPIRES_IN: int
    REFRESH_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    CLIENT_ORIGIN: str

    JWT_PRIVATE_KEY: str
    JWT_PUBLIC_KEY: str

    class Config:
        env_file = "./env"


settings = Settings()
