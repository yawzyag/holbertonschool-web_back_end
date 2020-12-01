#!/usr/bin/env python3
"""[web]
    obtain the HTML content of a
    particular URL and returns it.
"""
import requests
import redis
from datetime import timedelta
from typing import Callable
from functools import wraps


def web_count(method: Callable) -> Callable:
    """[count number of calls]

    Args:
        method (Callable): [method]

    Returns:
        Callable: [method]
    """
    r = redis.Redis()

    @wraps(method)
    def wrapper(*args, **kwds):
        """[wrapper of decorator]

        Returns:
            [type]: [description]
        """
        key = "count:" + args[0]
        # print('Calling decorated function')
        r.incr(key)
        r.expire(key, timedelta(seconds=10))
        return method(*args, **kwds)
    return wrapper


@web_count
def get_page(url: str) -> str:
    """[get page]

    Args:
        url (str): [url]
    """
    r = requests.get(url)
    return r.text
