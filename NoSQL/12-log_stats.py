#!/usr/bin/env python3
""" Este modulo tiene una funcion mongo. """

from pymongo import MongoClient


def status():
    """ Muestra los stados de consulta. """

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs
    nginx = logs.nginx

    metodos = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs". format(nginx.count_documents({})))

    print("Methods:")

    for metodo in metodos:
        print("\tmethod {}: {}". format(
            metodo, nginx.count_documents({'method': metodo})))

    print("{} status check". format(
        nginx.count_documents({'method': 'GET', 'path': '/status'})))


    if __name__ == '__main__':
        status()
