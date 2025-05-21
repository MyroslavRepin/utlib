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


# Removing vowels
def remove_vowels(text: str, lang: str = 'eng', consonats: bool = False):
    """
    Removes vowels or consonants from the given text based on the specified parameters.

    Args:
        text (str): The input string from which vowels or consonants will be removed.
        lang (str, optional): The language code to determine the set of vowels or consonants. Defaults to 'eng'.
        consonats (bool, optional): If False (default), removes vowels from the text. If True, removes consonants.

    Returns:
        str: The resulting string after removing the specified characters.

    Note:
        - The function retuns lowercasse only.
        - The function relies on an external `vowels` function to determine the set of vowels or consonants.
        - Prints each character as either 'Vowels' or 'Consonants' during processing.
        - String do not have any integers or special characters
    """
    text = text.lower()
    if consonats == False:
        output = []
        for char in text:
            if char in vowels('eng'):
                pass            # Might add a functionality to check if posible to convert to int
            else:
                output.append(char)
        return ''.join(output)
    else:
        output = []
        for char in text:
            if char in vowels('eng', True):
                pass
            # Might add a functionality to check if posible to convert to int
            else:
                output.append(char)
        return ''.join(output)


# Counting words, and can put minimum lenght of a word
def count_words(text: str, min_lenght: int = -1) -> int:
    """
    Counts the number of words in a given text, optionally filtering by minimum word length.
    Args:
        text (str): The input string to analyze.
        min_lenght (int, optional): Minimum length a word must have to be counted. 
            If set to -1 (default), all words are counted.
    Returns:
        int: The number of words that meet the criteria, as a number.
    """
    counts = 0
    words_list = text.split()
    for word in words_list:
        if min_lenght == -1 or len(word) >= min_lenght:
            counts += 1

    return counts
