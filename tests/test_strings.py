from utlib.strings_utils import is_palindrome, vowels, remove_vowels, count_words


def test_is_polindrome():
    assert is_palindrome('heeh') == True
    assert is_palindrome('Hello') == False


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
    text = "Good journey, not goodbye. - (Don't know where this came from, saw it on a headstone in a movie years ago and always stuck with me)."
    assert count_words(text) == 26
    assert count_words(text, min_length=4) == 16
    assert count_words(text, max_length=3) == 10
    assert count_words(text, min_length=3, max_length=4) == 10
    assert count_words("") == 0
    assert count_words(text, min_length=10) == 0
