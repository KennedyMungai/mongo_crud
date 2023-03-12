from typing import Optional, List

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings, BaseModel

from models.events import Event
from models.users import User


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
            database=client.get_default_database(), document_models=[Event, User],
            document_models=[]
        )

    class Config:
        """The configuration for the settings class"""
        env_file = ".env"


class Database:
    """The DB class"""

    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        """Function to save any changes in the document

        Args:
            document (MongoDB data type): The base type of MongoDB
        """
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        """The get specific event function

        Args:
            id (PydanticObjectId): The Id type

        Returns:
            Any: Returns a non-specified data type
        """
        doc = await self.model.get(id)

        if doc:
            return doc

        return False

    async def get_all(self) -> List(Any):
        """The function to retrieve all Events

        Args:
            self (_type_): _description_

        Returns:
            _type_: _description_
        """
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        """The data update endpoint

        Args:
            id (PydanticObjectId): Something
            body (BaseModel): The body of the updating model

        Returns:
            Any: Any datatype is valid
        """
        doc_id = id
        des_body = body.dict()
        des_body = {k: v in des_body.items() if v is not None}
        update_query = {
            "$set": {
                field: value for field, value in des_body.items()
            }
        }

        doc = await self.get(doc_id)

        if not doc:
            return False
        await doc.update(update_query)
        return doc
