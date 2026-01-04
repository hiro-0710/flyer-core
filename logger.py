from datetime import datetime


def _prefix() -> str:
    return datetime.utcnow().strftime("[%Y-%m-%d %H:%M:%S]")


def log_info(message: str) -> None:
    print(_prefix(), "[INFO]", message)


def log_error(message: str) -> None:
    print(_prefix(), "[ERROR]", message)
