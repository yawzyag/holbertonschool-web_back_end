#!/usr/bin/env python3
"""tuple typeanotation
create a tuple
"""
from typing import Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make a multiplier call

    Args:
        multiplier (float): [number to use]

    Returns:
        Callable[[float], float]: [function to make the operation]
    """
    def f(num: float) -> float:
        """return the multiplication

        Args:
            num (float): [float num to mult]

        Returns:
            float: [result of num * multiplier]
        """
        return num * multiplier
    return f
