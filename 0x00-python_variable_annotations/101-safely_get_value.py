#!/usr/bin/env python3
"""
This module contains a function to safely 
get a value from a dictionary with a default fallback.
"""

from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary with a default fallback.

    Parameters:
    dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
    key (Any): The key whose value to retrieve.
    default (Union[T, None]): The default value to return if the key is not found.

    Returns:
    Union[Any, T]: The value associated with the key 
    if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

