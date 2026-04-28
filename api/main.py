from fastapi import FastAPI
from pydantic import BaseModel
from automation.workflows.deploy_vlan import run_dynamic

app = FastAPI()

class VLANRequest(BaseModel):
    vlan_id: int
    vlan_name: str

@app.post("/vlan/provision")
def provision_vlan(data: VLANRequest):
    return run_dynamic(data.vlan_id, data.vlan_name)
