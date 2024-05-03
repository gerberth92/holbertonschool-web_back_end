#!/usr/bin/env python3
""" Este modulo define una funcion. """

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ Cambia documentos con un valor en especifico. """

    mongo_collection.update_many({'name': name},
                                 {'$set': {'topics': topics}})
