from typing import List, Optional

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

from models.events import Event


class User(Document):
    """The template for teh User class

    Args:
        Document (_type_): _description_
    """
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        """The settings subclass for the User class"""
        name = "users"

    class Config:
        """The configuration subclass"""
        schema_extra = {
            "example": {
                "email": "fast@api.com",
                "password": "strong!!!",
                "events": []
            }
        }
