#!/usr/bin/env python3
"""async generator
basi use of async geenrators
"""


import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator

    Yields:
        Generator[float, None, None]: [description]
    """
    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
