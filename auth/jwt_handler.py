"""Contains information to deal with JWT"""
import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import JWTError, jwt

from database.database import Settings


settings = Settings()
