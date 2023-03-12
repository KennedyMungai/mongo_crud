"""The umbrella test for the entire application"""
import asyncio

import httpx
import pytest

from database.connection import Settings
from main import app
from models.events import Event
from models.users import User


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

    await test_settings.initialize_database()
