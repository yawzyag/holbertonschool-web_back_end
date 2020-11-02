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
