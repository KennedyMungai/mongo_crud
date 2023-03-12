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


def verify_access_token(token: str) -> dict:
    """A function to verify the access token

    Args:
        token (str): The access token

    Raises:
        HTTPException: An exception for when there is no access token
        HTTPException: An exception for when the token has expired
        HTTPException: An exception for when the token is invalid

    Returns:
        dict: _description_
    """
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="No access token supplied")

        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Token expired")

        return data
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
