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
        data = r.get(args[0])
        if (data is not None):
            return data.decode("utf8")

        method_return = method(args[0])
        r.set(args[0], method_return)
        r.expire(args[0], timedelta(seconds=10))
        return method_return
    return wrapper


@web_count
def get_page(url: str) -> str:
    """[get page]

    Args:
        url (str): [url]
    """
    r = requests.get(url)
    return r.text
