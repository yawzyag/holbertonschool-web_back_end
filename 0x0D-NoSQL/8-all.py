#!/usr/bin/env python3
"""[list all dbs]
"""


def list_all(mongo_collection):
    """[list all from db]

    Args:
        mongo_collection ([type]): [description]
    """
    return mongo_collection.find({})
