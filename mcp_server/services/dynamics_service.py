"""Service layer for interacting with Dynamics 365 Customer Service."""

import httpx

from ..config.settings import get_settings
from ..utils.auth_dynamics import get_access_token

settings = get_settings()

async def create_incident_in_dynamics(user_id: str, description: str) -> str:
    token = await get_access_token()
    url = f"{settings.dynamics_base_url}/incidents"
    payload = {
        "customerid": user_id,
        "description": description,
    }
    # Here we would send a POST request to Dynamics. For demonstration we mock response.
    # async with httpx.AsyncClient() as client:
    #     resp = await client.post(url, json=payload, headers=_headers(token))
    #     resp.raise_for_status()
    #     return resp.json().get("incidentid")
    return "mock-incident-id"

async def get_incident_status(incident_id: str) -> dict:
    token = await get_access_token()
    url = f"{settings.dynamics_base_url}/incidents({incident_id})"
    # async with httpx.AsyncClient() as client:
    #     resp = await client.get(url, headers=_headers(token))
    #     resp.raise_for_status()
    #     data = resp.json()
    # return {
    #     "incidentId": incident_id,
    #     "status": data.get("statuscode"),
    #     "detail": data.get("description"),
    # }
    return {
        "incidentId": incident_id,
        "status": "Open",
        "detail": "Mock status",
    }

async def update_incident(incident_id: str, update_details: str) -> None:
    token = await get_access_token()
    url = f"{settings.dynamics_base_url}/incidents({incident_id})"
    payload = {"description": update_details}
    # async with httpx.AsyncClient() as client:
    #     resp = await client.patch(url, json=payload, headers=_headers(token))
    #     resp.raise_for_status()
    return


def _headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
    }
