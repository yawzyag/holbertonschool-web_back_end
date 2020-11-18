#!/usr/bin/env python3
"""
auth module
"""
import bcrypt
import uuid

from sqlalchemy.orm.exc import NoResultFound
from user import User
from db import DB


def _hash_password(password: str) -> str:
    """[hash a pasw]

    Args:
        password (str): [pasw to hash]

    Returns:
        str: [hased pass]
    """
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())


def _generate_uuid() -> str:
    """[generate uuid]

    Returns:
        uuid: [uuid]
    """
    return uuid.uuid4()


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """[constructor]
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """[register user]

        Args:
            email (str): [email of user]
            password (str): [password]

        Returns:
            User: [user register]
        """
        if (email and password):
            try:
                user = self._db.find_user_by(email=email)
                if (user):
                    raise ValueError("User {} already exists"
                                     .format(email))
            except NoResultFound:
                return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """[validate user log]

        Args:
            email (str): [email of user]
            password (str): [his passsword]

        Returns:
            bool: [valid state]
        """
        if (email is not None and password is not None):
            try:
                user = self._db.find_user_by(email=email)
                db_password = user.hashed_password
                return bcrypt.checkpw(password.encode('utf-8'),
                                      db_password)
            except NoResultFound:
                return False
        return False
