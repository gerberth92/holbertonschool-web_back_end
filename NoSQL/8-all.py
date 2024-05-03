#!/usr/bin/env python3
""" Este modulo se conecta a un servidor mongo. """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ Esta funcion lista todos los documentos. """

    documentos = mongo_collection.find()

    if documentos.count() == 0:
        return ([])

    return (documentos)
