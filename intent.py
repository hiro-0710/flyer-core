from fastapi import APIRouter
from modules.intent_engine import parse_intent

router = APIRouter(tags=["intent"])


@router.post("/intent")
def intent_route(payload: dict):
    text = payload.get("text", "") or ""
    intent = parse_intent(text)
    return {"intent": intent}
