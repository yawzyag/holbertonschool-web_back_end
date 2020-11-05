#!/usr/bin/env python3
""" class of Auth
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """[user cred]

        Args:
            self ([type]): [self]
            str ([type]): [base 64 string]
        """
        if (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ":" in decoded_base64_authorization_header):
            arr = decoded_base64_authorization_header.split(":")
            return (arr[0], arr[1])
        return (None, None)

    def user_object_from_credentials(self,
                                     user_email:
                                     str, user_pwd: str) -> TypeVar('User'):
        """[user obj]

        Args:
            self ([type]): [self]
        """
        if (user_email is None or not isinstance(user_email, str)):
            return None
        if (user_pwd is None or not isinstance(user_pwd, str)):
            return None
        user = None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return None
        if (user):
            if (user[0].is_valid_password(user_pwd)):
                return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[current user]
        """
        auth_header = self.authorization_header(request)
        base64_a = self.extract_base64_authorization_header(auth_header)
        decoded_base64 = self.decode_base64_authorization_header(base64_a)
        user_cred = self.extract_user_credentials(decoded_base64)
        user = self.user_object_from_credentials(user_cred[0], user_cred[1])
        return user
