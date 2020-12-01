#!/usr/bin/env python3
"""[check if key is equal]
"""
Cache = __import__('exercise').Cache
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8"),
    "juanito": cache.get_str,
    456: cache.get_int,
    0: cache.get_int
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    # print(cache.get(key, fn=fn), value, fn)
    assert cache.get(key, fn=fn) == value

