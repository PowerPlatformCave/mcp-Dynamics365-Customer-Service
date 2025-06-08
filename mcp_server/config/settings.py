import os
from dataclasses import dataclass

from dotenv import load_dotenv  
load_dotenv() 

@dataclass
class Settings:
    dynamics_tenant_id: str = os.getenv("DYNAMICS_TENANT_ID", "")
    dynamics_client_id: str = os.getenv("DYNAMICS_CLIENT_ID", "")
    dynamics_client_secret: str = os.getenv("DYNAMICS_CLIENT_SECRET", "")
    dynamics_resource: str = os.getenv("DYNAMICS_RESOURCE", "")
    dynamics_base_url: str = os.getenv("DYNAMICS_BASE_URL", "")

def get_settings() -> Settings:
    return Settings()
