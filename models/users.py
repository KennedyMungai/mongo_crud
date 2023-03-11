"""The user model"""
from typing import List, Optional

from models.events import Event
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """The template for the user Data

    Args:
        BaseModel (Class): Parent class
    """
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        """The configuration subclass"""
        schema_extra = {
            "example": {
                "email": "fast@api.com",
                "username": "ChickenWingsRUs",
                "events": []
            }
        }


class UserSignIn(BaseModel):
    """The template for teh User Sign in data

    Args:
        BaseModel (Class): Parent class
    """
    email: EmailStr
    password: str

    class Config:
        """The configuration subclass"""
        schema_extra = {
            "example": {
                "email": "fast@api.com",
                "password": "ChickenW1ngsRUs",
                "events": []
            }
        }
