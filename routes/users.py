"""The route script for the users"""
from fastapi import APIRouter, HTTPException, status

from database.connection import Database
from models.users import User, UserSignIn
