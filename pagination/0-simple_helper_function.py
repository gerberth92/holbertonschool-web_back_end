#!/usr/bin/env python3
""" Este modulo tiene un funcion de pagination. """

from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """ Esta funcion retorna una tupla. """

    end = page * page_size
    start = end - page_size

    return ((start, end))
