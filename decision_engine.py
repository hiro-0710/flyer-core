from typing import Dict
from .intent_engine import Intent


def decide_action(intent: Intent) -> Dict[str, str]:
    """
    Intent をもとに、抽象的な action を決定。
    """
    if intent == "next_step":
        return {"type": "navigation", "action": "go_next"}
    if intent == "previous_step":
        return {"type": "navigation", "action": "go_previous"}
    if intent == "status_check":
        return {"type": "status", "action": "report"}
    if intent == "greeting":
        return {"type": "greeting", "action": "respond"}

    return {"type": "unknown", "action": "none"}
