"""A file containing the tests for the login"""
import httpx
import pytest


@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "test@user.com",
        "password": "testpassword"
    }
