#!/usr/bin/env python3
"""class for basic cache
LFUCache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """[LFUCache cache]
    """

    def __init__(self):
        super().__init__()
        self.table = {}
        self.freq_bins = {}
        self.min_freq = 0
        self.count = 0

    def put(self, key, item):
        """[put in the dictionary cache]

        Args:
            key ([key value]): [key of the value to add]
            item ([item value]): [item for cache]
        """
        if (not key or not item):
            return

        if key in self.table:
            val, freq = self.table[key]
            self.table[key] = (item, freq+1)
            self.cache_data[key] = item

            freq_bin = self.freq_bins[freq]
            freq_bin.remove(key)

            next_freq_bin = self.freq_bins.get(freq+1, [])
            next_freq_bin.insert(0, key)
            self.freq_bins[freq+1] = next_freq_bin

            if len(freq_bin) == 0 and freq == self.min_freq:
                self.min_freq = freq+1

            return

        if self.count == self.MAX_ITEMS:
            freq_bin = self.freq_bins[self.min_freq]
            res = freq_bin.pop()
            del self.table[res]
            del self.cache_data[res]
            self.count -= 1
            print("DISCARD: {}".format(res))

        self.table[key] = (item, 1)
        self.cache_data[key] = item
        self.count += 1
        freq_bin = self.freq_bins.get(1, [])
        freq_bin.insert(0, key)
        self.freq_bins[1] = freq_bin
        self.min_freq = 1
        return

    def get(self, key):
        """[metho to search a key in the cache]

        Args:
            key ([key to search]): [value to search]

        Returns:
            [value]: [item value in cache if exist]
        """
        if (not key):
            return None
        if not self.table.get(key):
            return None
        val, freq = self.table[key]
        self.table[key] = (val, freq+1)
        self.cache_data[key] = val

        freq_bin = self.freq_bins[freq]
        freq_bin.remove(key)

        # can be optimized if instead of a list,
        # we use an actual LRU cache from here:
        # https://leetcode.com/problems/lru-cache/
        next_freq_bin = self.freq_bins.get(freq+1, [])
        next_freq_bin.insert(0, key)
        self.freq_bins[freq+1] = next_freq_bin

        if len(freq_bin) == 0 and freq == self.min_freq:
            self.min_freq = freq+1

        return self.cache_data[key]
