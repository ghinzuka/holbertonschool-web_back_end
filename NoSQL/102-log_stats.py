#!/usr/bin/env python3
"""Write a Python script that provides some stats
about Nginx logs stored in MongoDB:"""
from pymongo import MongoClient


def log_stats():
    """log stats"""
    client = MongoClient()
    collection = client.logs.nginx

    total_log_count = collection.count_documents({})
    print(f"{total_log_count} logs")
    print("Methods:")
    METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in METHODS:
        meth = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {meth}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
