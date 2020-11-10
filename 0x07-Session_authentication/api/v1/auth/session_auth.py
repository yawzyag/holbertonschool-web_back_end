#!/usr/bin/env python3
""" class of Auth
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class SessionAuth(Auth):
    """[simple auth]

    Args:
        Auth ([class]): [class auth]
    """
