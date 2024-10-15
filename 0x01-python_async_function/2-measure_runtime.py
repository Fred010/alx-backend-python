#!/usr/bin/env python3
""" Measures the runtime
"""

import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.

    Args:
        n(int): number of measures of total execution time
        max_delay(int): delays with the total execution time

    Returns:
        List[float]: total_time / n
    """

    # record start time
    start_time: float = time.time()
    completed_tasks: List[float] = asyncio.run(wait_n(n, max_delay))

    # record end time
    end_time: float = time.time()

    # calc. total time
    total_time: float = end_time - start_time

    # retruns average time per iteration
    return total_time / len(completed_tasks)
