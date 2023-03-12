"""The events route logic"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

from database.connection import Database
from models.events import Event
