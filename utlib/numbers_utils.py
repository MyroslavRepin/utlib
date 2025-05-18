from decimal import Decimal, getcontext


# Returns the sum of the digits of the given number n.
def digit_sum(n) -> int:
    n = str(n)
    result = []
    for char in n:
        result.append(int(char))
    return sum(result)


# Returns the average of the values list rounded to decimal_place decimals.
def average(values: list, decimal_place: int):
    getcontext().prec = decimal_place + 1
    result = Decimal(str(sum(values))) / Decimal(str(len(values)))
    format_str = '1.' + '0' * decimal_place
    return result.quantize(Decimal(format_str))
