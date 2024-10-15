#!/usr/bin/env python3
""" Executes multiple coroutines at the same time with async
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns wait_random n times with the specified
    max_delay.

    Args:
        n (int): The number of times to spawn wait_random coroutine
        max_delay (int): The maximum delay for each random wait time

    Returns:
        List[float]: list of all the delays (float values) in ascending order
    """
    # create list to store tasks
    tasks = []

    # spawn wait_random n times with the specified max_delay
    for s in range(n):
        tasks.append(wait_random(max_delay))

    # wait for all tasks to complete concurrently
    completed_tasks = await asyncio.gather(*tasks)

    # returns the list of delays sorted in ascending order
    return sorted(completed_tasks)
