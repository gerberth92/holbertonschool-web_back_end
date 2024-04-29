#!/usr/bin/env python3
""" Este modulo define tareas. """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Esta funcion crea tareas. """

    return (asyncio.create_task(wait_random(max_delay)))
