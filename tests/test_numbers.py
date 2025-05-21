from utlib import digit_sum, average


def test_digit_sum():
    assert digit_sum(12345) == 15
    assert digit_sum("102325") == 13
    assert digit_sum("1234")


def test_average():
    assert average([1, 10, 20], 4) == 10.3333
    assert average([12, -2, 5267], 3) == 1759.0
    assert average([0, 0], 0) == 0.0
    assert average([1, 23, 4], 2) == 9.33
