from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from models.users import User
from models.events import Event


class Settings(BaseSettings):
    """The settings for connecting to the Mongo DB

    Args:
        BaseSettings (Class): The parent class
    """
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        """Initialize the database"""
        client = AsyncIOMotorClient(self.DATABASE_URL)

        await init_beanie(
            database=client.get_default_database(),
            document_models=[]
        )

    class Config:
        """The configuration for the settings class"""
        env_file = ".env"
