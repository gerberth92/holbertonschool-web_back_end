#!/usr/bin/env python3
""" Este modulo tiene anotaciones. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Esta funcion retorna una funcion. """

    def mul(m: float = multiplier) -> float:
        """ Esta funcion realiza una multiplicacion """

        return (m * multiplier)

    return (mul)
