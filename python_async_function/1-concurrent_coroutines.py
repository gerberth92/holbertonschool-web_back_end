#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async."""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """corutina"""

    valor = random.uniform(0, max_delay)
    await asyncio.sleep(valor)
    return (valor)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """concurrecia"""

    task_list = []
    for i in range(n):
        tarea = await asyncio.gather(wait_random(max_delay))
        for i in tarea:
            task_list.append(i)
    return (sorted(task_list))
