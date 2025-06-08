# mcp-Dynamics365-Customer-Service

This project provides a minimal MCP (Microsoft Copilot Protocol) server that acts as an intermediary between Copilot Studio and Dynamics 365 Customer Service.

## Requirements
- Python 3.10+
- The dependencies listed in `requirements.txt`

## Installation
```bash
pip install -r requirements.txt
```

## Running the server
```bash
uvicorn mcp_server.main:app --reload
```
The API will be available at `http://localhost:8000`.

## Endpoints
- `POST /incident/create`
- `POST /incident/status`
- `POST /incident/update`

The server uses placeholder implementations for authentication and Dynamics 365 interaction. Configure environment variables in a `.env` file when implementing real authentication.

