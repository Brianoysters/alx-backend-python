#!/usr/bin/env python3
"""
This module contains a function to 
get the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Get the length of each element in the iterable.

    Parameters:
    lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each 
    tuple contains an element and its length.
    """
    return [(i, len(i)) for i in lst]

