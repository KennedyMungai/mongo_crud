"""The events routes file"""
from typing import List

from fastapi import APIRouter, Body, HTTPException, status

from models.events import Event

event_router = APIRouter(tags=["Events"])

events = []


@event_router.get("/")
async def retrieve_all_events() -> List[Event]:
    """The base route for the vent_router route

    Returns:
        List[Event]: Returns a list of events
    """
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
async def create_event(_body: Event = Body(...)) -> dict:
    """The crate event function

    Args:
        _body (Event, optional): The event data. Defaults to Body(...).

    Returns:
        dict: The message to show the function has been successfully executed
    """
    events.append(_body)

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
