#!/usr/bin/env python3
""" Este modulo contiene varias rutinas. """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Esta funcion crea una corutina. """

    time = []

    for i in range(n):
        rt = await wait_random(max_delay)
        time.append(rt)

    time.sort()

    return (time)
