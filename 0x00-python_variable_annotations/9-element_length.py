#!/usr/bin/env python3
"""duck type
duck typing
"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """elementh length

    Args:
        lst (Iterable[Sequence]): [value to iterae]

    Returns:
        List[Tuple[Sequence, int]]: [list of element]
    """
    return [(i, len(i)) for i in lst]
