"""The users route file"""
from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn


user_router = APIRouter(tags=["User"])

users = {}


@user_router.post('/signup')
async def signup_new_user(data: User) -> dict:
    """The user sign in endpoint

    Args:
        data (Class): The data template for the new user

    Returns:
        dict: A response to calling the API endpoint
    """
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with the supplied username exists"
        )

    users[data.email] = data

    return {
        "Message": "User successfully registered"
    }


@user_router.post("/signin")
async def signin_new_user(_user: UserSignIn) -> dict:
    """The sign in endpoint

    Args:
        user (UserSignIn): The data of the new user signing in

    Returns:
        dict: The message to show that the function has been successfully executed
    """
    if users[_user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user does not exist"
        )

    if users[_user.email].password != _user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    return {
        "Message": "User signed in successfully"
    }
