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


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    """Rewrote the retrieve_event function

    Args:
        id (int): The id of the event 
        session (Session, optional): The sb session. Defaults to Depends(get_session).

    Raises:
        HTTPException: If the event does not exist, a 404 error is raised

    Returns:
        Event: The returned event
    """
    event = session.get(Event, id)

    if event:
        return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The event with the supplied ID does not exist"
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


@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    """Rewrote the delete single id endpoint

    Args:
        id (int): The id of the event
        session (_type_, optional): The db session. Defaults to Depends(get_session).

    Raises:
        HTTPException: A 404 error is raised if the event id is not found

    Returns:
        dict: A message to show successful execution
    """
    event = session.get(Events, id)

    if event:
        session.delete(event)
        session.commit()

        return {
            "Message": "Event deleted successfully"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The event with the supplied ID does not exist"
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


@event_router.put("/edit/{id}", response_model=Event):
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)

    if event:
        event_data = new_data.dict(exclude_unset=True)

        for key, value in event_data.items():
            setattr(event, key, value)

        session.add(event)
        session.commit()
        session.refresh(event)

        return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="The event with the supplied ID does not exist"
    )
