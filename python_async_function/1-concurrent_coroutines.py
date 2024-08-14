#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve
written and write an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without
using sort() because of concurrency."""
import asyncio
from bisect import insort
from basic_async_syntax import wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait for a coroutine"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        insort(delays, delay)
    return delays
