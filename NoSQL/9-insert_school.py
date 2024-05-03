#!/usr/bin/env python3
""" Este modulo contiene una funcion. """

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Inserta un documento en una colleccion. """

    resultado = mongo_collection.insert_one(kwargs)

    return (resultado.inserted_id)
