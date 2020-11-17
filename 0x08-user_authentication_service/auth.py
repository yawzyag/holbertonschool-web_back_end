#!/usr/bin/env python3
"""
auth module
"""
import bcrypt


def _hash_password(password: str) -> str:
    """[hash a pasw]

    Args:
        password (str): [pasw to hash]

    Returns:
        str: [hased pass]
    """
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())
