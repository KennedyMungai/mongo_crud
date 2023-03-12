"""The script that contains the authentication logic"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
