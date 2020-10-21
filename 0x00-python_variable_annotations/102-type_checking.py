#!/usr/bin/env python3
"""duck type
duck typing
"""
from typing import Tuple, Union, Sequence, List, Any, \
    Mapping, Optional, TypeVar, Callable


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """check range in array

    Args:
        lst (Tuple): [list to check]
        factor (int, optional): [value range]. Defaults to 2.

    Returns:
        List: [list range]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
