#!/usr/bin/env python3
""" class of Auth
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
import uuid
from models.user import User


class SessionAuth(Auth):
    """[simple auth]

    Args:
        Auth ([class]): [class auth]
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """[create sesion for user]

        Args:
            user_id (str, optional): [id]. Defaults to None.

        Returns:
            str: [id]
        """
        if user_id and isinstance(user_id, str):
            id = str(uuid.uuid4())
            self.user_id_by_session_id[id] = user_id
            return id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[user id for session]

        Args:
            session_id (str, optional): [id]. Defaults to None.

        Returns:
            str: [User ID based on a Session ID]
        """
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """[get user with cookie]

        Args:
            request ([type], optional): [User instance].
            Defaults to None.
        """
        cookie = self.session_cookie(request)
        if cookie:
            return User.get(self.user_id_for_session_id(cookie))

    def destroy_session(self, request=None):
        """[delete session for user]

        Args:
            request ([type], optional): [req]. Defaults to None.
        """
        if (request):
            cookie = self.session_cookie(request)
            if (cookie):
                u_id = self.user_id_for_session_id(cookie)
                if u_id:
                    self.user_id_by_session_id.pop(cookie, None)
                    return True
        return False
