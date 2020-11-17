#!/usr/bin/env python3
"""
db module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


types = ['id', 'email', 'hashed_password', 'session_id',
         'reset_token']


class DB:
    """[db class]
    """

    def __init__(self):
        """[constructor]
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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
        session.commit()
        return new_user

    def find_user_by(self, **kw: str) -> User:
        """[summary]

        Args:
            val (any): [description]

        Returns:
            User: [description]
        """
        if not kw or any(x not in types for x in kw):
            raise InvalidRequestError
        session = self._session
        try:
            return session.query(User).filter_by(**kw).one()
        except Exception:
            raise NoResultFound
