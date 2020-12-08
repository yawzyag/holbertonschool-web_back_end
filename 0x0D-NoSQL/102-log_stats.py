#!/usr/bin/env python3
"""[log stats in db]
"""
from pymongo import MongoClient


def count_in_collection(collection, option=None):
    """[summary]

    Args:
        collection ([type]): [collection]
        option ([type], optional): [option to search].
        Defaults to None.

    Returns:
        [type]: [count]
    """
    items = {}
    if (option):
        val = nginx_collection.count_documents({"method": {"$regex": option}})
        print("\tmethod {}: {}".format(option, val))
        return

    return collection.count_documents(items)


def get_top_ips(collection):
    """[top ips]

    Args:
        collection ([type]): [ips]
    """
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}}, {
            "$sort": {"count": -1}}, {"$limit": 10}, {"$project": {
                "_id": 0,
                "ip": "$_id",
                "count": 1
            }}
    ]
    return collection.aggregate(pipeline)


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    results = count_in_collection(nginx_collection)
    print("{} logs".format(results))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_in_collection(nginx_collection, method)
    status_check = nginx_collection.count_documents({"path": "/status"})
    print("{} status check".format(status_check))
    print("IPs:")
    for ip in get_top_ips(nginx_collection):
        print("\t{} {}".format(ip.get("ip"), ip.get("count")))
