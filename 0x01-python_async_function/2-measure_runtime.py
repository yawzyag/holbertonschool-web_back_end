#!/usr/bin/env python3
"""async await
basi use of concurrency
"""


import random
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """'IO' wait time is proportional to the max element."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return time.time() - start
