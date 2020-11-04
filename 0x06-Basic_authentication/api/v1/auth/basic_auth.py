#!/usr/bin/env python3
""" class of Auth
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """[simple auth]

    Args:
        Auth ([class]): [class auth]
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """[base 64 header]

        Args:
            authorization_header (str): [header]

        Returns:
            str: [base 64 string]
        """
        if (authorization_header and isinstance(authorization_header, str)):
            array = authorization_header.split(" ")
            if (len(array) > 1):
                if (array[0] == "Basic"):
                    return(array[1])
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """[decode]

        Args:
            base64_authorization_header (str): [header in base 64]

        Returns:
            str: [decoded string]
        """
        if (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            try:
                base64_bytes = base64_authorization_header.encode('utf8')
                message_bytes = base64.b64decode(base64_bytes)
                return message_bytes.decode('utf8')
            except Exception:
                return None
        return None
