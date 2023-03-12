"""The script that contains the authentication logic"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from auth.jwt_handler import verify_access_token


oath2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")


async def authenticate(token: str = Depends(oath2_scheme)) -> str:
    """The authenticating function

    Args:
        token (str, optional): The access token for the API endpoint. Defaults to Depends(oath2_scheme).

    Raises:
        HTTPException: The raised exception for authentication

    Returns:
        str: The decoded token
    """
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Sign in for access")

    decoded_token = verify_access_token(token)
    return decoded_token["user"]
