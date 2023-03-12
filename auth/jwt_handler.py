"""Contains information to deal with JWT"""
import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import JWTError, jwt

from database.database import Settings


settings = Settings()


def create_access_token(user: str) -> str:
    """The function to create access tokens

    Args:
        user (str): Not sure

    Returns:
        str: The token
    """
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return token
