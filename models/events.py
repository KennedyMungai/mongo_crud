from typing import List, Optional

from beanie import Document

from pydantic import BaseModel


class Event(Document):
    """The template for the Event document

    Args:
        Document (MongoDB type): A level of data storage in MongoDB
    """
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        """The Event class config"""
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your  own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

    class Settings:
        """The settings"""
        name = "events"


class EventUpdate(BaseModel):
    """The event update data template

    Args:
        BaseModel (Class): The parent class
    """
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        """Configuration for the EventUpdate class"""
        schema_extra = {
            "example": {
                "title": "FastAPI book launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
