# mcp-Dynamics365-Customer-Service

This project now includes a server built with the
[Model Context Protocol](https://modelcontextprotocol.io) Python SDK.
It acts as an intermediary between Copilot Studio and Dynamics 365 Customer Service.

## Requirements
- Python 3.10+
- The dependencies listed in `requirements.txt`

## Installation
```bash
pip install -r requirements.txt
```

## Running the server
The project exposes both the original FastAPI implementation and an MCP server
using the Python SDK.

### FastAPI
```bash
uvicorn mcp_server.main:app --reload
```
The API will be available at `http://localhost:8000`.

### MCP Server
```bash
mcp run mcp_server/mcp_server.py
```

## Endpoints
- `POST /incident/create`
- `POST /incident/status`
- `POST /incident/update`

The server uses placeholder implementations for authentication and Dynamics 365 interaction. Configure environment variables in a `.env` file when implementing real authentication.

