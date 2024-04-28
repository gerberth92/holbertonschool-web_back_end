#!/usr/bin/env python3
""" Este modulo tiene anotaciones. """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Esta funcion retorna datos combinados. """

    return (k, v ** 2)
