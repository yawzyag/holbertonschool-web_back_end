#!/usr/bin/env python3
"""
Helper
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """[return the range of pagination]

    Args:
        page (int): [number page]
        page_size (int): [size of each page]

    Returns:
        Tuple[int, int]: [tuple of pagination parameters]
    """
    return ((page_size*page) - page_size, page_size*page)
