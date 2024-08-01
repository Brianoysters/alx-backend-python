#!/usr/bin/env python3
"""
This module contains a function 
to zoom into a list of items.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom into the tuple by repeating each item a number of times.

    Parameters:
    lst (Tuple): The tuple of items to zoom into.
    factor (int): The number of times each item should be repeated.

    Returns:
    List: A list where each item is repeated 'factor' times.
    """
    if not isinstance(factor, int):
        raise TypeError("Factor must be an integer")

    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

