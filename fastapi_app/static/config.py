from pydantic import BaseSettings


class Settings(BaseSettings):
    # Add your config here, this will be override by whatever values is added for that key in .env file
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
