from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str = "mongodb+srv://vpatel179:LqpC2zz4rO7pmtkR@cluster0.ejksq.mongodb.net/"
    db_name: str = "WriteDB"

    class Config:
        env_file = ".env"

settings = Settings()