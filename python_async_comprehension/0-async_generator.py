#!/usr/bin/env python3
""" define una corutina """

import asyncio
import random


async def async_generator():
    """ corutina """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
