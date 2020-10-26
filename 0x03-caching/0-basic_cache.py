#!/usr/bin/env python3
"""class for basic cache
simple implementation
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """[basi cache]
    """

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """[put in the dictionary cache]

        Args:
            key ([key value]): [key of the value to add]
            item ([item value]): [item for cache]
        """
        if (not key or not item):
            return
        self.cache_data[key] = item

    def get(self, key):
        if (not key):
            return None
        return self.cache_data.get(key)
