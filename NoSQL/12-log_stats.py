#!/usr/bin/env python3
""" Este modulo tiene una funcion mongo. """

from pymongo import MongoClient


def status():
    """ Muestra los stados de consulta. """

    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs
    nginx = logs.nginx

    metodos = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(nginx.count(), "logs")

    print("Methods:")

    for metodo in metodos:
        print("\tmethod {}: {}"
              .format(metodo, nginx.count({'method': metodo})))

    print("{} status check"
          .format(nginx.count({'method': 'GET', 'path': '/status'})))
    
    if __name__ == '__main__':
        status()
