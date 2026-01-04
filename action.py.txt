from fastapi import APIRouter
from modules.action_executor import execute_action

router = APIRouter(tags=["action"])


@router.post("/action")
def action_route(payload: dict):
    decision = payload.get("decision", "") or ""
    result = execute_action(decision)
    return {"result": result}
