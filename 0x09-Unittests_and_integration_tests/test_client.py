#!/usr/bin/env python3
"""test client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import client


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
        ("google", {'repos_url': 'https://intranet.hbtn.io/projects/610'})
    ])
    def test_public_repos_url(self, name, expect):
        """
        Test _public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=expect)):
            response = client.GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, expect.get('repos_url'))

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, dict_val, key, expect):
        """[check license]

        Args:
            dict_val ([type]): [values]
            key ([type]): [key]
            expect ([type]): [expect]
        """
        status = GithubOrgClient.has_license(dict_val, key)
        self.assertEqual(status, expect)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """[Integration test]

    Args:
        unittest ([type]): [base]
    """
    @classmethod
    def setUpClass(cls):
        cls.mock_get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.mock_get_patcher.stop()

    def test_public_repos(self):
        """[public repos]

        Args:
            mock_method ([type]): [metodh get_json]
        """

    def test_public_repos_with_license(self):
        """[public with license]
        """


if __name__ == '__main__':
    unittest.main()
