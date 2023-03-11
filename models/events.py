"""Created a model for the events"""
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


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
