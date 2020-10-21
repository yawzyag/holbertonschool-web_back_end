#!/usr/bin/env python3
"""async await
basi use of concurrency
"""


import random
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """date a number of times to execute (n) and max_delay to call"""
    listValues = []
    listResults = []
    for i in range(n):
        listValues.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(listValues):
        listResults.append(await task)
    return listResults
