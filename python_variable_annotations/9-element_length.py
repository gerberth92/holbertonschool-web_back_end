#!/usr/bin/env python3
"""
funcion que determina los elementos.
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Funcion que determina el tamaño de un iterable.
    """
    return [(i, len(i)) for i in lst]
