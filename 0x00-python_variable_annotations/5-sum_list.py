#!usr/bin/env python3
""" takes a list input_list of floats as argument
and returns their sum as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(input_list)
