#!/usr/bin/env python3
"""
This module contains a function to
create an asyncio.Task for wait_random.
"""

import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the
    wait_random coroutine with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task
        object for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
