#!/usr/bin/env python3
""" class of exp session
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.session_exp_auth import SessionExpAuth
import base64
import uuid
from models.user_session import UserSession
from datetime import datetime, timedelta
import os


class SessionDBAuth(SessionExpAuth):
    """[simple auth]

    Args:
        Auth ([class]): [class auth]
    """

    def create_session(self, user_id=None):
        """[create sesion]

        Args:
            user_id ([type], optional): [id]. Defaults to None.
        """
        if user_id:
            session = super().create_session(user_id)
            if not session:
                return
            new_user = UserSession(user_id=user_id, session_id=session)
            new_user.save()
            return session
        return None

    def user_id_for_session_id(self, session_id=None):
        """[user id]

        Args:
            session_id ([type], optional): [sesion_id].
            Defaults to None.

        Returns:
            [type]: [user id]
        """
        if session_id:
            try:
                user = UserSession.search({session_id: session_id})
                for us_r in user:
                    created = us_r.get('created_at')
                    if created:
                        if (datetime.now() < created +
                                timedelta(seconds=self.session_duration)):
                            return us_r.get('user_id')
            except Exception:
                return None
        return None

    def destroy_session(self, request=None) -> bool:
        """[delete from db]

        Args:
            request ([type], optional): [req]. Defaults to None.

        Returns:
            bool: [tru if deleted]
        """
        if request:
            session = self.session_cookie(request)
            if session:
                if super().destroy_session(request):
                    try:
                        user = UserSession.search({session_id: session})
                        for us_r in user:
                            us_r.remove()
                            return True
                    except Exception:
                        return False
        return False
