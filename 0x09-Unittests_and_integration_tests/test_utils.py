#!/usr/bin/env python3
"""test utils
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
memoize = __import__('utils').memoize


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


class TestGetJson(unittest.TestCase):
    """[testing get json class]

    Args:
        unittest ([type]): [base]
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """[test json]

        Args:
            test_url ([type]): [url]
            test_payload ([type]): [response]
        """
        get_json = __import__('utils').get_json
        with patch('requests.get') as mock_requests:
            mock_requests.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """[memoize]

    Args:
        unittest ([type]): [base]
    """

    def test_memoize(self):
        """[test_memo]

        Returns:
            [type]: [test]
        """
        class TestClass:
            """[test class]
            """

            def a_method(self):
                """[test method]

                Returns:
                    [type]: [number]
                """
                return 42

            @memoize
            def a_property(self):
                """[memoize function]

                Returns:
                    [type]: [meoize data]
                """
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            classInst = TestClass()
            classInst.a_property
            classInst.a_property
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
