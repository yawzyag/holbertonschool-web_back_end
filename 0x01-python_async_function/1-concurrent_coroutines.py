#!/usr/bin/env python3
"""async await
basi use of concurrency
"""


import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))


async def wait_n(n: int, max_delay: int) -> List[float]:
    """date a number of times to execute (n) and max_delay to call"""
    listValues = []
    listResults = []
    for i in range(n):
        listValues.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(listValues):
        listResults.append(await task)
    return listResults
