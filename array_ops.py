"""
contains array operations
"""
import numpy as np


def remove_odd_number_from_array(arr):
    """
    removes the element from the array
    :param arr: numpy array
    :return: array
    """
    # Incorrectly delete elements from the array
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr = np.delete(arr, i)

    return arr


def sum_of_squares_of_even_numbers(arr):
    """
    :param arr: numpy array
    :return:
    """
    result = 0
    for num in arr:
        if num % 2 == 0:
            result += num ** 2
    return result