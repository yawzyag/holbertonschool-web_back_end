#!/usr/bin/env python3
"""basic operation
sum list values int and float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes input list and returns his sum"""
    return sum(mxd_lst)
