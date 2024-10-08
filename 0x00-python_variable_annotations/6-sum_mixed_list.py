#!/usr/bin/env python3
"""
This module contains a function to
sum a list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and floats and return the result as a float.
    
    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and floats to sum.
    
    Returns:
    float: The sum of the list as a float.
    """
    return sum(mxd_lst)

