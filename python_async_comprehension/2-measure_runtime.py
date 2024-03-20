#!/usr/bin/env python3
""" define una corutina """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ mide el tiempo de ejecucion """

    inicio = time.time()
    await asyncio.gather(* (async_comprehension() for i in range(4)))
    fin = time.time()
    return (fin - inicio)
