#!/usr/bin/env python3
"""async generator
basi use of async geenrators
"""


import asyncio
from random import uniform
from typing import List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """mesure time to execute

    Returns:
        float: [time execution]
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - start
