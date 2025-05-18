# Counting words
def word_count(text):
    if type(text) == str:
        text = text.split()
        return len(text)
    else:
        return TypeError


# Checking if polindrome and returning Bool
def is_polindrome(text: str):
    return text[::-1] == text
