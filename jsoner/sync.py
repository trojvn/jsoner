import contextlib
import json
from pathlib import Path


def json_read(file: Path | str) -> dict:
    """Синхронная функция для чтения json
    Преобразование str -> Path"""
    with contextlib.suppress(Exception):
        with Path(file).open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def json_write(file: Path | str, json_data: dict, ensure_ascii: bool = False):
    """Синхронная функция для записи в json (indent=4, ensure-ascii=False)
    Преобразование str -> Path"""
    with Path(file).open("w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=ensure_ascii)
