#!/usr/bin/env python3
"""[redis]
"""
import redis
import uuid
from typing import Union


class Cache():
    """[cache]
    """

    def __init__(self):
        """[constructor]
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
        self._redis.set(key, data)
        return key
