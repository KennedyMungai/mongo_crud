"""The route script for the users"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.connection import Database
from models.users import User, TokenResponse

user_router = APIRouter(tags=["User"])

user_database = Database(User)
hash_password = HashPassword()


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

    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password

    await user_database.save(user)

    return {"Message": "User created successfully"}


@user_router.post("/signin")
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    """The user sign in endpoint

    Args:
        user (UserSignIn): The sign in data for the user

    Raises:
        HTTPException: Exception raised incase of wrong email
        HTTPException: Exception raised incase of wrong password

    Returns:
        dict: A message to show successful data execution
    """
    user_exist = await User.find_one(User.email == user.username)

    if not user_exist:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="The user with the provided email does not exist")

    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)

        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
