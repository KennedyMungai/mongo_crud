"""Created a model for the events"""
from typing import List, Optional

from sqlmodel import JSON, Column, Field, SQLModel


class Event(SQLModel, table=True):
    """The template for Event data

    Args:
        SQLModel (Class): The parent class of the SQL model
        table (bool, optional): Identifies the type. Defaults to True.
    """
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        """The config subclass"""
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }


class EventUpdate(SQLModel):
    """The Event Update data template

    Args:
        SQLModel (Class): The parent class
    """
    title: Optional[str]
    image: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        """The config subclass"""
        schema_extra = {
            "example": {
                "title": "FastAPI book launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
