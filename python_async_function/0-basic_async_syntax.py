#!/usr/bin/env python3
"""Write an asynchronous coroutine"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Funcion que retorna un float"""
    valor = random.uniform(0, max_delay)
    await asyncio.sleep(valor)
    return (valor)
