import os


def get_size(path: str):
    """Returns the size of a file in bytes.
    Args:
        path (str): The path to the file.
    Returns:
        int: The size of the file in bytes.
        FileNotFoundError: If the specified file does not exist.
    """

    try:
        size = os.path.getsize(path)
        return size
    except FileNotFoundError:
        raise FileNotFoundError
