"""A file containing the logic for testing CRUD endpoints"""
import httpx
import pytest

from auth.jwt_handler import create_access_token
from models.events import Event
