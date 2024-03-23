#!/usr/bin/env python3
""" pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ define un funcion que retorna una tupla """
    end = page * page_size
    start = end - page_size
    return ((start, end))
