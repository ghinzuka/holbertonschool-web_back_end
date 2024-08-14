#!/usr/bin/env python3
"""Contains asynchronous coroutine task_wait_n"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Executes multiple coroutines at the same time
    and returns a list of execution time in ascending order.
    """

    tasks = [task_wait_random(max_delay) for i in range(0, n)]
    delay_list = await asyncio.gather(*tasks)
    asc_lst = []
    for i in range(0, len(delay_list)):
        asc_lst.append(min(delay_list))
        delay_list.remove(min(delay_list))

    return asc_lst
