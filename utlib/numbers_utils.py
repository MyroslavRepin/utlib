from decimal import Decimal, getcontext


# Returns the sum of the digits of the given number n.
def digit_sum(n) -> int:
    """
    Calculates the sum of the digits of a given number.
    Args:
        n: The number whose digits will be summed. Can be an integer or a string representation of an integer.
    Returns:
        int: The sum of the digits of the input number.
    Examples:
        >>> digit_sum(123)
        6
        >>> digit_sum("456")
        15
    """

    n = str(n)
    result = []
    for char in n:
        result.append(int(char))
    return sum(result)


# Returns the average of the values list rounded to decimal_place decimals.
def average(values: list, decimal_place: int):
    """
    Calculates the average of a list of numeric values, rounded to a specified number of decimal places.
    Args:
        values (list): A list of numeric values to average.
        decimal_place (int): The number of decimal places to round the result to.
    Returns:
        float: The average of the input values, rounded to the specified decimal places.
    Raises:
        ZeroDivisionError: If the input list is empty.
    """

    if not values:
        raise ZeroDivisionError("Empty list")
    return round(sum(values) / len(values), decimal_place)
