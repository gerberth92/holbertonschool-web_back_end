#!/usr/bin/env python3
"""
funcion que determina los elementos.
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Funcion que determina el tamaño de un iterable.
    """
    return [(i, len(i)) for i in lst]
