#!/usr/bin/env python3
"""duck type
duck typing
"""
from typing import Tuple, Union, Sequence, List, Any, Optional


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, Optional[Any]]:
    """get first element, if exist

    Args:
        lst (Sequence[Any]): [list to return his first element]

    Returns:
        Union[Any, Optional[Any]]: [return the val or none]
    """
    if lst:
        return lst[0]
    else:
        return None
