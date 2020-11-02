#!/usr/bin/env python3
"""
proces password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """[hash a pasword]

    Args:
        password (str): [pswword to process]

    Returns:
        str: [hash pass]
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str)-> bool:
    """[check valid password]

    Args:
        hashed_password (bytes): [hashed password of user]
        password (str): [password to check]

    Returns:
        bool: [true if is valid false if not]
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)