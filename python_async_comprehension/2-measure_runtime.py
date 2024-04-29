#!/usr/bin/env python3
""" Este modulo tiene compresion. """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Esta funcion crea tareas y calcula el tiempo de ex. """

    inicio = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    fin = time.time()

    return (fin - inicio)
