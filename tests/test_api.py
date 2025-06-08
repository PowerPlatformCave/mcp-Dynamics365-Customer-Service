import os
import sys
import pytest
from httpx import AsyncClient, ASGITransport

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from mcp_server.main import app

@pytest.mark.asyncio
async def test_create_incident():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/incident/create",
            json={"userId": "1", "description": "Test"},
        )
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == {"incidentId", "status", "message"}


@pytest.mark.asyncio
async def test_status_incident():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/incident/status",
            json={"incidentId": "1"},
        )
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == {"incidentId", "status", "detail"}


@pytest.mark.asyncio
async def test_update_incident():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/incident/update",
            json={"incidentId": "1", "updateDetails": "update"},
        )
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == {"incidentId", "status", "message"}

