"""The script that contains the authentication logic"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from auth.jwt_handler import verify_access_token


oath2_scheme = OAuth2PasswordBearer(tokenUrl="/user/signin")
