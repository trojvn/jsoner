import contextlib
import json
from pathlib import Path

import aiofiles
from tooler import str_to_path


async def json_read_async(file: Path | str) -> dict:
    """Асинхронная функция для чтения json
    Преобразование str -> Path"""
    with contextlib.suppress(Exception):
        async with aiofiles.open(str_to_path(file), "r", encoding="utf-8") as f:
            contents = await f.read()
        json_data = json.loads(contents)
        return json_data
    return {}


def json_read_sync(file: Path | str) -> dict:
    """Синхронная функция для чтения json
    Преобразование str -> Path"""
    with contextlib.suppress(Exception):
        with str_to_path(file).open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def json_write_sync(file: Path | str, json_data: dict):
    """Синхронная функция для записи в json (indent=4, ensure-ascii=False)
    Преобразование str -> Path"""
    with str_to_path(file).open("w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


async def json_write_async(file: Path | str, json_data: dict):
    """Асинхронная функция для записи в json (indent=4, ensure_ascii=False)
    Преобразование str -> Path"""
    async with aiofiles.open(str_to_path(file), "w", encoding="utf-8") as f:
        await f.write(f"{json.dumps(json_data, indent=4, ensure_ascii=False)}")
