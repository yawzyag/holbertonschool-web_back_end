#!/usr/bin/env python3
"""[insert in db]
"""


def update_topics(mongo_collection, name, topics):
    """[udpdate]

    Args:
        mongo_collection ([type]): [collection]
        name ([type]): [name]
        topics ([type]): [to update]
    """
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update_many(myquery, newvalues)
