#!/usr/bin/env python3
""" Este modulo tiene funciones acincronas y compresion. """

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """ Esta funcion es un generador de rutinas. """

    for i in range(10):
        await asyncio.sleep(1)
        yield (uniform(0, 10))
