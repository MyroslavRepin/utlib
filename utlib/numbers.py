from decimal import Decimal, ROUND_HALF_UP


# Returns the sum of the digits of the given number n.
def digit_sum(n) -> int:
    n = str(n)
    result = []
    for char in n:
        result.append(int(char))
    return sum(result)

# Returning an average number from an array


def average(values: list, decimal: int):
    if decimal <= 27:
        try:
            result = Decimal(sum(values)) / Decimal(len(values))
            return result.quantize(Decimal("1." + "0" * decimal), rounding=ROUND_HALF_UP)
        except ZeroDivisionError:
            return None
    else:
        return 'Decimal point out of bound'
