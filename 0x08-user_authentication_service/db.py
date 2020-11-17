#!/usr/bin/env python3
"""
user module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:
    """[db class]
    """

    def __init__(self):
        """[constructor]
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """[session]

        Returns:
            [type]: [description]
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """[add user to db]

        Args:
            email (str): [email of user]
            hashed_password (str): [passsword]

        Returns:
            User: [user object]
        """

        session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        new_user = session.query(User).filter_by(
            email=email, hashed_password=hashed_password).first()
        return new_user
