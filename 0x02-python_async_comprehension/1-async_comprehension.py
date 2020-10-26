#!/usr/bin/env python3
"""async generator
basi use of async geenrators
"""


import asyncio
from random import uniform
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async values

    Returns:
        List[float]: [values to return of the asyn call]
    """
    async_call = [i async for i in async_generator()]
    return async_call