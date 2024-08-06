#!/usr/bin/env python3
"""
Asynchronous coroutine that collects random numbers.
"""

import asyncio
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects
    10 random numbers from async_generator.
    """
    return [i async for i in async_generator()]

