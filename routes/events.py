"""The events route logic"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status, Depends

from database.connection import Database
from models.events import Event, EventUpdate
from auth.authenticate import authenticate


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

    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The Event with the supplied Id does not exist")

    return event


@event_router.post("/new")
async def create_event(body: Event, user: str = Depends(authenticate)) -> dict:
    """The create Event endpoint

    Args:
        body (Event): The data of teh new event

    Returns:
        dict: A message to show successful execution
    """
    await event_database.save(body)

    return {"Message": "Event created successfully"}


@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate, user: str = Depends(authenticate)) -> Event:
    """The update event endpoint

    Args:
        id (PydanticObjectId): The type of data for the Id
        body (EventUpdate): The body of the updating event

    Raises:
        HTTPException: The error type for HTTPs

    Returns:
        Event: The data after the update
    """
    updated_event = await event_database.update(id, body)

    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The event with the supplied Id does not exist")

    return updated_event


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId, user: str = Depends(authenticate)) -> dict:
    """The delete event endpoint

    Args:
        id (PydanticObjectId): The event Id

    Raises:
        HTTPException: Raising exceptions incase of a HTTP error

    Returns:
        dict: A message to show successful execution of the logic
    """
    event = await event_database.delete(id)

    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The Event with the supplied ID does not exist")

    return {"Message": : "Event deleted successfully"}
