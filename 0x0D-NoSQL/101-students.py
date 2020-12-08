#!/usr/bin/env python3
"""[sorted results]
"""
from pymongo import ASCENDING, DESCENDING
update_topics = __import__('10-update_topics').update_topics


def top_students(mongo_collection):
    """[sorted result form collection]

    Args:
        mongo_collection ([type]): [collection]
    """
    all_items = mongo_collection.find({})
    for item in all_items:
        count = 0
        new_topics = item
        for sta in item.get("topics"):
            count += sta.get("score")
        averageScore = count/len(item.get("topics"))

        myquery = {"name": item.get("name")}
        newvalues = {"$set": {"averageScore": averageScore}}
        mongo_collection.update_many(myquery, newvalues)

    order = mongo_collection.find().sort("averageScore", DESCENDING)

    return order
