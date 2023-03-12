"""The events route logic"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

from database.connection import Database
from models.events import Event


event_database = Database(Event)

event_router = APIRouter(tags=["Events"])


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    """The endpoint to retrieve all events

    Returns:
        List[Event]: All events output as a List
    """
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    """The endpoint to retrieve a specific event

    Args:
        id (PydanticObjectId): The identifier field for the dta

    Returns:
        Event: The event data itself
    """
    event = await event_database.get(id)
    return event
