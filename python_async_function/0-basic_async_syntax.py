#!/usr/bin/env python3
""" Este modulo tiene una funcion asincrona. """

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Esta es una corutina. """

    tiempo = uniform(0, max_delay)
    await asyncio.sleep(tiempo)

    return (tiempo)

asyncio.run(wait_random())
