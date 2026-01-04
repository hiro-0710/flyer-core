from typing import Dict, Any


def get_status_knowledge() -> Dict[str, Any]:
    # 本来はシステム状態やタスク状況を参照
    return {
        "phase": "development",
        "description": "Flyer OS core running",
    }


def get_greeting_message() -> str:
    return "こんにちは、Flyerです。必要なときだけ静かに最適化します。"


def get_unknown_message() -> str:
    return "意図をまだうまくつかめていないけれど、続けてくれれば解像度を上げていきます。"
