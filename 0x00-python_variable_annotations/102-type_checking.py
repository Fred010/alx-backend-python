#!/usr/bin/env python3
""" Adds type annotations to the function
"""

from typing import List, Tuple


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Adds type annotations to the function

    Args:
        lst (List[int]): A list fo integers
        factor (int): integer factors

    Returns:
        List[int]: A list of integers
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Changed from 3.0 to 3 (integer)
