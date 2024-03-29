#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
     function sum_list which takes a list input_list of floats as
     argument and returns their sum as a float.

     Args:
        input_list(list[float]): argumento.

    Return:
        float: suma de los elementos del argumento.
    """
    suma = 0
    for i in input_list:
        suma += i
    return (suma)
