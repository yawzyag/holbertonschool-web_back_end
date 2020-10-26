#!/usr/bin/env python3
"""class for basic cache
MRUCache
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """[MRUCache cache]
    """

    def __init__(self):
        super().__init__()
        self.cache = OrderedDict()

    def put(self, key, item):
        """[put in the dictionary cache]

        Args:
            key ([key value]): [key of the value to add]
            item ([item value]): [item for cache]
        """
        if (not key or not item):
            return
        self.cache_data[key] = item
        self.cache[key] = item
        if (len(self.cache_data) > self.MAX_ITEMS):
            res = next(iter(self.cache))
            del self.cache_data[res]
            print("DISCARD: {}".format(res))

        if len(self.cache) > self.MAX_ITEMS:
            self.cache.popitem(last=False)

        self.cache.move_to_end(key, False)

    def get(self, key):
        """[metho to search a key in the cache]

        Args:
            key ([key to search]): [value to search]

        Returns:
            [value]: [item value in cache if exist]
        """
        if (not key):
            return None
        if key in self.cache:
            self.cache.move_to_end(key, False)
        return self.cache_data.get(key)
