from utlib.strings_utils import word_count, is_polindrome


def test_strings():
    assert word_count('Hello, im trying to debug this code') == 7
    assert word_count('') == 0
    assert is_polindrome('heeh') == True
    assert is_polindrome('Hello') == False
