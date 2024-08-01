#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.
    
    Parameters:
    multiplier (float): The multiplier value.
    
    Returns:
    Callable[[float], float]: A function that multiplies a float by the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function

