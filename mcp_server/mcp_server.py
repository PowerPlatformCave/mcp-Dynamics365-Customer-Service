from mcp.server.fastmcp import FastMCP

from .services.dynamics_service import (
    create_incident_in_dynamics,
    get_incident_status,
    update_incident,
)

mcp = FastMCP("Dynamics 365 Customer Service")


@mcp.tool()
async def create_incident(userId: str, description: str) -> dict:
    """Create a new incident in Dynamics 365."""
    incident_id = await create_incident_in_dynamics(userId, description)
    return {
        "incidentId": incident_id,
        "status": "Creado",
        "message": "Incidencia registrada correctamente.",
    }


@mcp.tool()
async def incident_status(incidentId: str) -> dict:
    """Get the status for an incident."""
    return await get_incident_status(incidentId)


@mcp.tool(name="update_incident")
async def incident_update(incidentId: str, updateDetails: str) -> dict:
    """Update an existing incident."""
    await update_incident(incidentId, updateDetails)
    return {
        "incidentId": incidentId,
        "status": "Actualizado",
        "message": "Incidencia actualizada correctamente.",
    }


if __name__ == "__main__":
    mcp.run("streamable-http")
