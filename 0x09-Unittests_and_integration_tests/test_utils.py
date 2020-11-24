#!/usr/bin/env python3
"""test utils
"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """[test access nest map]

    Args:
        unittest ([type]): [test base]
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """[testing nested map]
        """
        access_nested_map = __import__('utils').access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """[exception test]
        """
        access_nested_map = __import__('utils').access_nested_map
        self.assertRaises(expected, access_nested_map, nested_map, path)


if __name__ == '__main__':
    unittest.main()
