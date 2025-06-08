"""Utility functions for authenticating against Dynamics 365 via OAuth."""

import time
from pydantic import BaseModel
from typing import Optional

from ..config.settings import get_settings

class Token(BaseModel):
    access_token: str
    expires_at: float

# In a real implementation this would retrieve a token from Azure AD.
# Here we mock the behaviour for example purposes.
_token_cache: Optional[Token] = None

async def get_access_token() -> str:
    global _token_cache
    if _token_cache and _token_cache.expires_at > time.time():
        return _token_cache.access_token

    settings = get_settings()
    # TODO: implement real OAuth retrieval using aiohttp or httpx.
    # For now we return a placeholder token.
    access_token = "fake-token"
    _token_cache = Token(access_token=access_token, expires_at=time.time() + 3600)
    return access_token
