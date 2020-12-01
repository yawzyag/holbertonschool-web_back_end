#!/usr/bin/env python3
"""[redis]
    module of redis
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """[cache]
        class to set cache with redis
    """

    def __init__(self):
        """[constructor]
            constructor for redis instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """[store]

        Args:
            data ([type]): [data to save]

        Returns:
            str: [saved]
        """
        key = str(uuid.uuid4())

        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable])\
            -> Union[str, bytes, int, float]:
        """[get from redis]

        Args:
            key (str): [key to check]
            fn (Optional[Callable]): [convert the data]

        Returns:
            str: [data]
        """
        if (fn):
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, stringb: bytes) -> str:
        """[get a string]

        Args:
            string (bytes): [byte string]

        Returns:
            str: [string]
        """
        return stringb.decode("utf-8")

    def get_int(self, numberb: int) -> int:
        """[get int]

        Args:
            number (int): [byte int]

        Returns:
            int: [number]
        """
        result = 0
        result = result * 256 + int(numberb)
        return result
