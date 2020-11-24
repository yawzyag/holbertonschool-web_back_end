#!/usr/bin/env python3
"""test client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """[testing client org]

    Args:
        unittest ([type]): [base]
    """

    @parameterized.expand([
        ("google", {'login': 'google'}),
        ("abc", {'login': 'google'}),
    ])
    @patch("client.get_json")
    def test_org(self, client, expect, mock_method):
        """[test org]

        Args:
            client ([type]): [url]
            expect ([type]): [value to excpect]
        """
        mock_method.return_value = expect
        res = GithubOrgClient(client).org
        self.assertEqual(res, expect)
        mock_method.assert_called_once()
