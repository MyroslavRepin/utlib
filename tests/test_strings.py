from utlib.strings_utils import word_count, is_polindrome, vowels, remove_vowels, count_words


def test_word_count():
    assert word_count('Hello, im trying to debug this code') == 7
    assert word_count('') == 0


def test_is_polindrome():
    assert is_polindrome('heeh') == True
    assert is_polindrome('Hello') == False


def test_vowels():
    assert vowels('eng', True) == [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    ]
    assert vowels('es', True) == [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    ]


def test_remove_vowels():
    assert remove_vowels('I am removing vowels') == ' m rmvng vwls'
    assert remove_vowels('God is great', consonats=True) == 'o i ea'
    assert remove_vowels('AeI', consonats=True) == 'aei'


def test_count_words():
    assert count_words('Hello, my name is') == 4
    assert count_words('') == 0
    assert count_words('One') == 1
    assert count_words('Two words') == 2
    assert count_words('Multiple    spaces   between words') == 4
    assert count_words('Punctuation! Should, not: affect; count?') == 5
    assert count_words('   Leading and trailing spaces   ') == 4
