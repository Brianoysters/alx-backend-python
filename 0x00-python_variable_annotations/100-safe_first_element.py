#!/usr/bin/env python3
"""
This module contains a function to 
safely get the first element of a sequence.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of a sequence if it exists.
    
    Parameters:
    lst (Sequence[Any]): The sequence from 
    which to get the first element.
    
    Returns:
    Union[Any, None]: The first element of the 
    sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

