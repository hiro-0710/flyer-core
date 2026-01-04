from typing import Literal


Intent = Literal[
    "next_step",
    "previous_step",
    "status_check",
    "greeting",
    "unknown",
]


def parse_intent(text: str) -> Intent:
    """
    非常にシンプルなプレースホルダ実装。
    後で LLM / ルールベースに差し替え可能。
    """
    t = (text or "").strip().lower()

    if not t:
        return "unknown"

    if "次" in text or "進" in text:
        return "next_step"
    if "戻" in text or "前" in text:
        return "previous_step"
    if "状態" in text or "ステータス" in text or "今" in text:
        return "status_check"
    if any(g in text for g in ["こんにちは", "やあ", "おはよう", "こんばんは"]):
        return "greeting"

    return "unknown"
