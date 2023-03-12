from typing import List, Optional

from beanie import Document


class Event(Document):
    """The template for the Event document

    Args:
        Document (MongoDB type): A level of data storage in MongoDB
    """
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
