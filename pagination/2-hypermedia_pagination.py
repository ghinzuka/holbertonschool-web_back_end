#!/usr/bin/env python3
"""mplement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10."""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those
    particular pagination parameters."""
    start_index = ((page - 1) * page_size)
    end_index = page * page_size
    return start_index, end_index


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
        """return the appropriate page of the dataset
        (i.e. the correct list of rows)"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if len(dataset) <= start_index or len(dataset) <= end_index:
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing the following key-value pairs:"""
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        page_data = self.get_page(page, page_size)
        return {'page_size': page_size,
                'page': page,
                'data': page_data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
