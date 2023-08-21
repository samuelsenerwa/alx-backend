#!/usr/bin/env python3

"""
A function that takes two integer argumets page and page_size

The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing 
    a start index and an end index corresponding to the range of indexes 
    to return in a list for those particular pagination parameters.

    Args:
    page(int): page number to return (pages are 1-indexed)
    page_size(int): number of items per page

    Return:
    tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    retrun (start, end)
