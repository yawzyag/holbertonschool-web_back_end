#!/usr/bin/env python3
"""[insert in db]
"""


def insert_school(mongo_collection, **kwargs):
    """[insert in collection]

    Args:
        mongo_collection ([type]): [collection]
    """
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
