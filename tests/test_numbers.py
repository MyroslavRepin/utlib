from utlib import digit_sum, average


def test_digit_sum():
    assert digit_sum(12345) == 15
    assert digit_sum("102325") == 13
    assert digit_sum("1234")


def test_average():
    # assert average([1, 10, 20], 3) == 10.333
    pass
