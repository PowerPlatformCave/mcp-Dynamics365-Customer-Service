from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

from .controllers.incidents_controller import router as incidents_router

app = FastAPI(title="MCP Server Dynamics 365 Customer Service")

# Path to repository root so we can serve the OpenAPI manifest
BASE_DIR = Path(__file__).resolve().parent.parent

app.include_router(incidents_router, prefix="/incident", tags=["Incident Management"])


@app.get("/openapi.yaml", include_in_schema=False)
async def serve_openapi_spec() -> FileResponse:
    """Expose the OpenAPI document for MCP registration."""
    return FileResponse(BASE_DIR / "openapi.yaml", media_type="application/yaml")

