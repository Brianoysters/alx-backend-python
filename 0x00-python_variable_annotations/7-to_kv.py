#!/usr/bin/env python3
"""
This module contains a function to create 
a tuple with a string and the square of a number.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an int or float.
    
    Parameters:
    k (str): The string element.
    v (Union[int, float]): The number to be squared.
    
    Returns:
    Tuple[str, float]: A tuple with the string and the square of the number.
    """
    return (k, float(v ** 2))

