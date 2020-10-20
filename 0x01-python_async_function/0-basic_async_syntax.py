#!/usr/bin/env python3
"""async await
tip for basic use of async await
"""
import random
import asyncio


async def wait_random(max_delay=10):
    """take a delay and await randomly for the result"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
