#!/usr/bin/env python3
"""
type-annotated function floor which takes a float n as argument
and returns the floor of the float
"""
import math


def floor(n: float) -> int:
    """
    function floor which takes a float n as argument and returns
    the floor of the float.

    Args:
        n(float): argumento.

    Return:
        int: entero hacia abajo.
    """
    return (math.floor(n))
