#!/usr/bin/env python3
"""[search in db]
"""


def schools_by_topic(mongo_collection, topic):
    """[search by topic]

    Args:
        mongo_collection ([type]): [collection]
        topic ([type]): [topic to search]
    """
    return mongo_collection.find({"topics": {"$all": [topic]}})
