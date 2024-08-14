#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve
written and write an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without
using sort() because of concurrency."""
import asyncio
import typing
from bisect import insort
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Executes multiple coroutines at the same time
    and returns a list of execution times in ascending order"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        insort(delays, delay)

    return delays
