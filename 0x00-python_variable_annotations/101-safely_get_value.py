#!/usr/bin/env python3
"""duck type
duck typing
"""
from typing import Tuple, Union, Sequence, List, Any, \
    Mapping, Optional, TypeVar, Callable


T = TypeVar('T', bound=Callable[...,  Optional[int]])


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
