#!/usr/bin/env python3
"""
Coroutine that measures the runtime of
async_comprehension executed four times in parallel.
"""

import asyncio
import time

from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.
    """
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()
    return end_time - start_time
