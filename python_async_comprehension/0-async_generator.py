#!/usr/bin/env python3
""" Este modulo tiene funciones acincronas y compresion. """

import asyncio
from random import uniform


async def async_generator():
    """ Esta funcion es un generador de rutinas. """

    for i in range(10):
        await asyncio.sleep(1)
        n = uniform(0, 10)
        yield (n)
