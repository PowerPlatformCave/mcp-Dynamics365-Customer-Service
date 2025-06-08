from fastapi import FastAPI
from .controllers.incidents_controller import router as incidents_router

app = FastAPI(title="MCP Server Dynamics 365 Customer Service")

app.include_router(incidents_router, prefix="/incident", tags=["Incident Management"])

