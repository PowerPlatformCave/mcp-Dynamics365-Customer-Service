from fastapi import APIRouter, HTTPException

from ..models.incident import (
    IncidentCreateRequest,
    IncidentResponse,
    IncidentStatusRequest,
    IncidentStatusResponse,
    IncidentUpdateRequest,
)
from ..services.dynamics_service import (
    create_incident_in_dynamics,
    get_incident_status,
    update_incident,
)

router = APIRouter()


@router.post("/create", response_model=IncidentResponse)
async def create_incident(request: IncidentCreateRequest):
    try:
        incident_id = await create_incident_in_dynamics(request.userId, request.description)
        return IncidentResponse(
            incidentId=incident_id,
            status="Creado",
            message="Incidencia registrada correctamente."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/status", response_model=IncidentStatusResponse)
async def incident_status(request: IncidentStatusRequest):
    try:
        data = await get_incident_status(request.incidentId)
        return IncidentStatusResponse(**data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/update", response_model=IncidentResponse)
async def incident_update(request: IncidentUpdateRequest):
    try:
        await update_incident(request.incidentId, request.updateDetails)
        return IncidentResponse(
            incidentId=request.incidentId,
            status="Actualizado",
            message="Incidencia actualizada correctamente."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
