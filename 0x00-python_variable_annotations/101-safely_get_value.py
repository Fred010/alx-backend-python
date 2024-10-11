#!/usr/bin/env python3
""" Adds type annotations using TypeVar
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Adds type annotations using TypeVar

    Args:
        dct (Mapping[Any, Any]): dictionary
        key (Any): key of dictionary
        default (Union[T, None]): default value

    Returns:
        Union[Any, T]: values
    """
    if key in dct:
        return dct[key]
    else:
        return default
