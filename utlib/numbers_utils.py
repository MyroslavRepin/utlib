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


def average(values: list, decimal_place: int = 1, get_nearest_value: bool = False):
    """
    Calculates the average of a list of numeric values.

    Args:
        values (list): A list of numeric values to average.
        decimal_place (int): The number of decimal places to round the result to.
        get_nearest_value (bool): If True, returns the value closest to the average instead of the average itself.

    Returns:
        float | int: The rounded average, or the value from the list closest to the average.

    Raises:
        ZeroDivisionError: If the input list is empty.
    """
    if not values:
        raise ZeroDivisionError("Empty list")

    raw_avg = sum(values) / len(values)

    if get_nearest_value:
        diffs = [(abs(v - raw_avg), v) for v in values]
        return min(diffs)[1]

    return round(raw_avg, decimal_place)
