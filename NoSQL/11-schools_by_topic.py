#!/usr/bin/env python3
""" Este modulo tiene una funcion mongo. """

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ retorna una lista de un documento en especifico. """

    retorno = []

    docs = mongo_collection.find({'topics': topic})

    for doc in docs:
        retorno.append(doc)

    return (retorno)
