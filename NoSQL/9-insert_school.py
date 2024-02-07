#!/usr/bin/env python3
""" Python function that inserts a new document in a collection based on kwargs """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ function that inserts a new document in a collection """
    mongo_collection.insert_one(kwargs)
    return (list(mongo_collection.find({})))
