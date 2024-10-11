#!/usr/bin/env python3
""" Augments the correct duck-typed annotations
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Augments the correct duck-typed annotations

    Args:
        lst (Sequence[Any]): A list of Sequence

    Returns:
        Union[Any, None]: A list of either Any or None
    """
    if lst:
        return lst[0]
    else:
        return None
