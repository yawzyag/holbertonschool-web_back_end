#!/usr/bin/env python3
""" class of exp session
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.session_auth import SessionAuth
import base64
import uuid
from models.user import User
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """[simple auth]

    Args:
        Auth ([class]): [class auth]
    """
    session_duration = 0

    def __init__(self):
        """[constructor]
        """
        env_session = os.getenv("SESSION_DURATION")
        if (env_session):
            try:
                self.session_duration = int(duration)
            except:
                pass

    def create_session(self, user_id=None):
        """[create session with time]

        Args:
            user_id ([type], optional): [id user]. Defaults to None.

        Returns:
            [type]: [sesion id]
        """
        if (user_id):
            session = super().create_session(user_id)
            user_id = self.user_id_by_session_id.get(session)
            session_dictionary = {'user_id': user_id,
                                  'created_at': datetime.now()}
            self.user_id_by_session_id[session] = session_dictionary
            return session
        return None

    def user_id_for_session_id(self, session_id=None):
        """[user_id from the session dictionary]

        Args:
            session_id ([type], optional): [sesion id].
            Defaults to None.
        """
        if (session_id):
            dict_ = self.user_id_by_session_id.get(session_id)
            if (dict_):
                user_id = dict_.get('user_id')
                if (self.session_duration <= 0):
                    return user_id
                created = dict_.get('created_at')
                if created:
                    if (datetime.now() < created +
                            timedelta(seconds=self.session_duration)):
                        return user_id

        return None
