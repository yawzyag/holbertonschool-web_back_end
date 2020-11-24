#!/usr/bin/env python3
"""test client
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ("google", {'repos_url': 'google'})
    ])
    def test_public_repos_url(self, client, expect):
        # _public_repos_url
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_method:
            mock_method.return_value = expect
            res = GithubOrgClient(client)._public_repos_url
            self.assertEqual(res, expect.get('repos_url'))
            mock_method.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_method):
        """[public repos]

        Args:
            mock_method ([type]): [metodh get_json]
        """
        GithubOrgClient = __import__('client').GithubOrgClient
        mock_method.return_value = [{"name": "google"},
                                    {"name": "abc"}]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public:
            mock_public.return_value = 'google'
            response = GithubOrgClient("google").public_repos()
            self.assertEqual(response, ['google', 'abc'])
            mock_method.assert_called_once()
            mock_public.assert_called_once()
