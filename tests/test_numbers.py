from utlib import digit_sum, average
import pytest


def test_digit_sum():
    assert digit_sum(12345) == 15
    assert digit_sum("102325") == 13
    assert digit_sum("1234")


def test_average_simple():
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([1, 2, 3, 4, 5], decimal_place=2) == 3.00


def test_average_empty_list():
    with pytest.raises(ZeroDivisionError):
        average([])


def test_average_get_nearest_value():
    values = [1, 4, 6, 9, 12]
    assert average(values, get_nearest_value=True) == 6


def test_average_get_nearest_value_with_ties():
    values = [1, 4, 7, 10, 13]
    assert average(values, get_nearest_value=True) == 7


def test_average_negative_numbers():
    values = [-5, -1, 0, 1, 5]
    assert average(values) == 0.0
    assert average(values, get_nearest_value=True) == 0


def test_floats_numbers():
    assert average([1, 2.1, 3, 4.34]) == 2.6
    assert average([15235, -1346237872, 832637.83672920973]) == -448463333.1
