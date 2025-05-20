# Counting words
def word_count(text):
    """
    Counts the number of words in a given text string.

    Parameters:
        text (str): The input string to count words from.

    Returns:
        int: The number of words in the input string if input is a string.
        TypeError: If the input is not a string.

    Note:
        The function splits the input string by whitespace to determine word boundaries.
    """
    if type(text) == str:
        text = text.split()
        return len(text)
    else:
        return TypeError


# Checking if polindrome and returning Bool
def is_polindrome(text: str):
    """
    Checks if the given text is a palindrome.
    A palindrome is a string that reads the same forwards and backwards.
    Args:
        text (str): The string to check.
    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """

    return text[::-1] == text


# Returning vowels of 3 supported languages: English, Russian, Spanish
def vowels(lang: str, consonants=False):
    """
    Returns a list of vowels or consonants for the specified language.

    Args:
        lang (str): The language code. Supported values are:
            - 'eng' for English
            - 'ru' for Russian
            - 'es' for Spanish
            - 'fr' for French
            - 'de' for German
        consonants (bool, optional): If False (default), returns vowels. If True, returns consonants.

    Returns:
        list: A list of vowel or consonant characters for the specified language.

    Raises:
        KeyError: If the provided language code is not supported.

    Examples:
        >>> vowels('eng')
        ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        >>> vowels('ru', consonants=True)
        ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
    """
    letters = {
        'eng': {
            'vowels': ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'],
            'consonants': [
                'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
            ]
        },
        'ru': {
            'vowels': ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
                       'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я'],
            'consonants': [
                'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
                'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
            ]
        },
        'es': {
            'vowels': ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'],
            'consonants': [
                'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
            ]
        },
        'fr': {
            'vowels': ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'],
            'consonants': [
                'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z',
            ]
        },
        'de': {
            'vowels': ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü', 'A', 'E', 'I', 'O', 'U', 'Ä', 'Ö', 'Ü'],
            'consonants': [
                'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ß',
            ]
        }
    }
    if consonants == False:
        return letters[lang]['vowels']
    else:
        return letters[lang]['consonants']
