"""The umbrella test for the entire application"""
import asyncio

import httpx
import pytest

from database.connection import Settings
from main import app
from models.events import Event
from models.users import User
