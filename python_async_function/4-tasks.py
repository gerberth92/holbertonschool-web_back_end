#!/usr/bin/env python3
""" Este modulo contiene varias rutinas. """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Esta funcion crea una corutina. """

    time = []

    for i in range(n):
        rt = await task_wait_random(max_delay)
        time.append(rt)

    time.sort()

    return (time)
