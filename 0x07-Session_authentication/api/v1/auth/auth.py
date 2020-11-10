#!/usr/bin/env python3
""" class of Auth
"""
from flask import request
from typing import List, TypeVar
import re
import os


class Auth:
    """[Auth manage]
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[requiere auth class]

        Args:
            path (str): [actual path]
            excluded_paths (List[str]): [escluded paths]

        Returns:
            bool: [posible access]
        """
        if (path is None):
            return True
        if (excluded_paths is None or len(excluded_paths) == 0):
            return True
        clean_paths = []
        for path_item in excluded_paths:
            clean_paths.append(path_item.strip("/"))
            if ("*" in path_item and path_item[-1] == "*"):
                wildcard = path_item.split("/")[-1].replace("*", "")
                if (re.search('{}'.format(wildcard),
                              path.strip("/").split("/")[-1])):
                    return False

        if(path.strip("/") in clean_paths):
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """[authorization_header]

        Args:
            request ([type], optional): [Flask request object].
            Defaults to None.

        Returns:
            str: [header]
        """
        if (request is None):
            return None
        if (request.headers.get("Authorization")):
            return request.headers.get("Authorization")
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[curent user]

        Returns:
            [type]: [user]
        """
        return None

    def session_cookie(self, request=None):
        """[session cookie]

        Args:
            request ([type], optional): [cookie value from a request].
            Defaults to None.
        """
        if request:
            env = os.getenv("SESSION_NAME")
            return request.cookies.get(env)
        return None
