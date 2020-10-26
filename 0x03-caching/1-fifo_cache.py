#!/usr/bin/env python3
"""class for basic cache
fif cache
"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """[FIFO cache]
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """[put in the dictionary cache]

        Args:
            key ([key value]): [key of the value to add]
            item ([item value]): [item for cache]
        """
        if (not key or not item):
            return
        self.cache_data[key] = item
        if (len(self.cache_data) > self.MAX_ITEMS):
            res = sorted(self.cache_data.keys())[0]
            del self.cache_data[res]
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
