#!/usr/bin/env python3
"""async await
basi use of concurrency
"""


import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[wait_random]:
    """date a number of times to execute (n) and max_delay to call"""
    list = []
    for i in range(0, n):
        value = await wait_random(max_delay)
        list.append(value)
    return list
