"""
Provides some arithmetic functions
"""


def add(a: int, b: int) -> int:
    """
    Function that adds some numbers
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Function that subtracts some numbers
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Function that multiplies some numbers
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Function that divides some numbers
    """
    return a / b


def convert_to_binary(number) -> str:
    """
    Function that converts a number to binary
    """
    if number < 0 or number > 100:
        raise ValueError("Number must be between 0 and 100")
    if not isinstance(number, int):
        raise ValueError("Number must be an integer")
    res = ""
    n = number
    if n == 0:
        return "0"
    while n > 0:
        res = str(n % 2) + res
        n = n // 2
    return res
