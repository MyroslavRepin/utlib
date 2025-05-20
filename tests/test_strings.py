from utlib.strings_utils import word_count, is_polindrome, vowels, remove_vowels


def test_strings():
    assert word_count('Hello, im trying to debug this code') == 7
    assert word_count('') == 0
    assert is_polindrome('heeh') == True
    assert is_polindrome('Hello') == False

    assert vowels('eng', True) == [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    ]
    assert vowels('es', True) == [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    ]

    assert remove_vowels('I am removing vowels') == ' m rmvng vwls'
    assert remove_vowels('God is great', consonats=True) == 'o i ea'
    assert remove_vowels('AeI', consonats=True) == 'aei'
