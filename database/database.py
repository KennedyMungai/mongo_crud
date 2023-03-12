"""The database config file"""
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = None
