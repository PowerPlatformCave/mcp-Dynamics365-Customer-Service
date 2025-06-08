"""Utility functions for authenticating against Dynamics 365 via OAuth."""

import time
from typing import Optional

import httpx
from pydantic import BaseModel

from ..config.settings import get_settings


class Token(BaseModel):
    access_token: str
    expires_at: float


_token_cache: Optional[Token] = None


async def get_access_token() -> str:
    """Retrieve an OAuth token from Azure AD using client credentials."""
    global _token_cache

    if _token_cache and _token_cache.expires_at > time.time():
        return _token_cache.access_token

    settings = get_settings()
    if not all(
        [
            settings.dynamics_tenant_id,
            settings.dynamics_client_id,
            settings.dynamics_client_secret,
            settings.dynamics_resource,
        ]
    ):
        # In development or test environments credentials may be absent.
        access_token = "fake-token"
        _token_cache = Token(access_token=access_token, expires_at=time.time() + 3600)
        return access_token
    token_url = (
        f"https://login.microsoftonline.com/{settings.dynamics_tenant_id}/oauth2/v2.0/token"
    )
    data = {
        "client_id": settings.dynamics_client_id,
        "client_secret": settings.dynamics_client_secret,
        "grant_type": "client_credentials",
        "scope": f"{settings.dynamics_resource}/.default",
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(token_url, data=data)
        resp.raise_for_status()
        payload = resp.json()

    access_token = payload["access_token"]
    expires_in = int(payload.get("expires_in", 3599))
    _token_cache = Token(
        access_token=access_token,
        expires_at=time.time() + expires_in - 60,
    )
    return access_token
