from typing import Dict
from .knowledge_layer import (
    get_status_knowledge,
    get_greeting_message,
    get_unknown_message,
)


def execute_action(decision: Dict[str, str]) -> str:
    """
    抽象的な decision を、UI に返す “言語化されたアウトプット” に変換。
    """
    dtype = decision.get("type")
    action = decision.get("action")

    if dtype == "navigation" and action == "go_next":
        return "次のフェーズに静かに移行します。"
    if dtype == "navigation" and action == "go_previous":
        return "ひとつ前のフェーズに戻ります。"
    if dtype == "status" and action == "report":
        status = get_status_knowledge()
        return f"現在は {status['phase']} フェーズ。{status['description']}。"
    if dtype == "greeting" and action == "respond":
        return get_greeting_message()

    return get_unknown_message()
