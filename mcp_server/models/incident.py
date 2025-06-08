from pydantic import BaseModel

class IncidentCreateRequest(BaseModel):
    userId: str
    description: str

class IncidentStatusRequest(BaseModel):
    incidentId: str

class IncidentUpdateRequest(BaseModel):
    incidentId: str
    updateDetails: str

class IncidentResponse(BaseModel):
    incidentId: str
    status: str
    message: str

class IncidentStatusResponse(BaseModel):
    incidentId: str
    status: str
    detail: str
