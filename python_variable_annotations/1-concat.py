#!/usr/bin/env python3
"""
type-annotated function concat that takes a string str1 and
a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    function concat that takes a string str1 and a string str2
    as arguments and returns a concatenated string.

    Args:
        str1(str): parametro 1.
        str2(str): parametro 2.
    """
    return (str1 + str2)
