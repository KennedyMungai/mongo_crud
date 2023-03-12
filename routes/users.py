"""The route script for the users"""
from fastapi import APIRouter, HTTPException, status

from database.connection import Database
from models.users import User, UserSignIn


user_router = APIRouter(tags=["User"])

user_database = Database(User)


@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    """The user signup endpoint

    Args:
        user (User): The user data

    Raises:
        HTTPException: The exception raised incase of HTTP errors

    Returns:
        dict: A message shown incase of successful execution
    """
    user_exist = await User.find_one(User.email == user.email)

    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="The email provided is already in use")

    await user_database.save(user)

    return {"Message": "User created successfully"}
