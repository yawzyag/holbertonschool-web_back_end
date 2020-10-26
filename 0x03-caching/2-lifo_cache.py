#!/usr/bin/env python3
"""class for basic cache
LIFOCache
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """[LIFOCache cache]
    """

    def __init__(self):
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """[put in the dictionary cache]

        Args:
            key ([key value]): [key of the value to add]
            item ([item value]): [item for cache]
        """
        if (not key or not item):
            return
        self.cache_list = self.cache_list[-4:]
        self.cache_list.append(key)
        self.cache_data[key] = item
        if (len(self.cache_data) > self.MAX_ITEMS):
            res = self.cache_list[-2]
            del self.cache_data[res]
            del self.cache_list[-2]
            print("DISCARD: {}".format(res))

    def get(self, key):
        """[metho to search a key in the cache]

        Args:
            key ([key to search]): [value to search]

        Returns:
            [value]: [item value in cache if exist]
        """
        if (not key):
            return None
        return self.cache_data.get(key)
