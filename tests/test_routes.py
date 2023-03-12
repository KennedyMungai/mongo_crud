"""A file containing the logic for testing CRUD endpoints"""
import httpx
import pytest

from auth.jwt_handler import create_access_token
from models.events import Event


@pytest.fixture(scope="module")
async def access_token() -> str:
    return create_access_token("test@user.com")


@pytest.fixture(scope="module")
async def mock_event() -> Event:
    new_event = Event(
        creator="test@user.com",
        title="Last time that I checc'd",
        image="https://linktomyimage.com/image.png",
        description="Nipsey Hussle hustling in a nipsey way",
        tags=["crip", "hiphop", "blood"],
        location="Google Meet"
    )

    await Event.insert-one(new_event)

    yield new_event
