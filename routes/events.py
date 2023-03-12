"""The events routes file"""
from typing import List, select

from fastapi import APIRouter, Body, HTTPException, status, Depends, Request

from database.connection import get_session
from models.events import Event, EventUpdate

event_router = APIRouter(tags=["Events"])

events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    """A rewritten function for retrieving all events from the database

    Args:
        session (Session, optional): The session. Defaults to Depends(get_session).

    Returns:
        List[Event]: All events in a list
    """
    statement = select(Event)
    events = session.exec(statement).all("")
    return events


@event_router.get("/{id}")
async def retrieve_event(_id: int) -> Event:
    """The endpoint to retrieve specific events

    Args:
        id (int): The id of the event

    Raises:
        HTTPException: Raises an 404 error incase the event is not found

    Returns:
        Event: The template for the event data
    """
    for event in events:
        if event.id == _id:
            return event
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The event with supplied ID does not exist"
        )


@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    """A rewritten create_event function that uses the database

    Args:
        new_event (Event): The Event data of type Event
        session (_type_, optional): _description_. Defaults to Depends(get_session).

    Returns:
        dict: _description_
    """
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "Message": "Event created successfully"
    }


@event_router.delete("/{id}")
async def delete_event(_id: int) -> dict:
    """The endpoint to delete an event

    Args:
        _id (int): The id of the event

    Raises:
        HTTPException: Raises a 404 incase the event is missing

    Returns:
        dict: The returned message on successful execution
    """
    for event in events:
        if event.id == _id:
            events.remove(event)

            return {
                "Message": "Event deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied Id does not exist"
    )


@event_router.delete("/")
async def delete_all_events() -> dict:
    """Deletes all events

    Returns:
        dict: The message to show successful execution
    """
    events.clear()

    return {
        "Message": "All events deleted"
    }
