#!/usr/bin/env python3
"""tuple typeanotation
create a tuple
"""
from typing import Tuple, Union


def to_kv(a: str, v: Union[int, float]) -> Tuple[str, float]:
    """create a tuple with the values

    Args:
        a (str): [string]
        v (Union[int, float]): [value, int or float]

    Returns:
        Tuple[str, float]: [return the tuple of the values]
    """
    return (a, v*v)
