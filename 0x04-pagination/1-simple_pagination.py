#!/usr/bin/env python3
"""
pagination
"""

import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """[return the range of pagination]

        Args:
            page (int): [number page]
            page_size (int): [size of each page]

        Returns:
            Tuple[int, int]: [tuple of pagination parameters]
        """
        return ((page_size*page) - page_size, page_size*page)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """[get pagination]

        Args:
            page (int, optional): [value of page]. Defaults to 1.
            page_size (int, optional): [size of each page]. Defaults to 10.

        Returns:
            List[List]: [list dataset for pagination]
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)
        self.dataset()
        get_index = self.index_range(page, page_size)
        return self.__dataset[get_index[0]:get_index[1]]
