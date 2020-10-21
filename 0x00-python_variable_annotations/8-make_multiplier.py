#!/usr/bin/env python3
"""tuple typeanotation
create a tuple
"""
from typing import Tuple, Callable


def f(my_float: float) -> float:
    return my_float * my_float


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make a multiplier call

    Args:
        multiplier (float): [number to use]

    Returns:
        Callable[[float], float]: [function to make the operation]
    """
    return f
