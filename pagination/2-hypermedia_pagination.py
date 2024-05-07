#!/usr/bin/env python3
""" Este modulo tiene un funcion de pagination. """

from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> tuple:
    """ Esta funcion retorna una tupla. """

    end = page * page_size
    start = end - page_size

    return ((start, end))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Esta funcion retorna la pagina indicada. """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()

        le = len(self.__dataset)
        npage = le / page_size

        if page <= math.ceil(npage):
            tupla = index_range(page, page_size)

            return (self.__dataset[tupla[0]:tupla[1]])

        else:
            return ([])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Esta funcion retorna un diccionario. """

        li = self.get_page(page, page_size)

        di = {}
        npage = len(self.__dataset) / page_size

        di['page_size'] = len(li)
        di['page'] = page
        di['date'] = li

        if (page + 1) <= math.ceil(npage):
            di['next_page'] = page + 1
        else:
            di['next_page'] = None

        if (page - 1) > 0:
            di['prev_page'] = page - 1
        else:
            di['prev_page'] = None

        di['total_pages'] = math.ceil(npage)

        return (di)
