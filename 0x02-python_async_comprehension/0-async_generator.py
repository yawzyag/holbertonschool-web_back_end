#!/usr/bin/env python3
"""async generator
basi use of async geenrators
"""


import asyncio
from random import uniform
from typing import List


async def async_generator() -> List[float]:
    """generate values async

    Returns:
        List[float]: [list of randome values]

    Yields:
        Iterator[List[float]]: [list of generated values]
    """
    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
