#!/usr/bin/env python3
""" Este modulo tiene anotaciones. """

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Esta funcion retorna un iterable de sequencias. """

    return [(i, len(i)) for i in lst]
