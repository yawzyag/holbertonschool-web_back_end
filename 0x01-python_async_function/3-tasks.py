#!/usr/bin/env python3
"""async await
basi use of concurrency
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """'IO' wait time is proportional to the max element."""
    t = asyncio.create_task(wait_random(max_delay))
    return t
