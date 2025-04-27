import contextlib
import json
from pathlib import Path

import aiofiles


async def json_read(file: Path | str) -> dict:
    """Асинхронная функция для чтения json
    Преобразование str -> Path"""
    with contextlib.suppress(Exception):
        async with aiofiles.open(Path(file), "r", encoding="utf-8") as f:
            contents = await f.read()
        json_data = json.loads(contents)
        return json_data
    return {}


async def json_write(file: Path | str, json_data: dict, ensure_ascii: bool = False):
    """Асинхронная функция для записи в json (indent=4, ensure_ascii=False)
    Преобразование str -> Path"""
    async with aiofiles.open(Path(file), "w", encoding="utf-8") as f:
        await f.write(f"{json.dumps(json_data, indent=4, ensure_ascii=ensure_ascii)}")
