import os
from pathlib import Path


def get_size(path):
    """Returns the size of a file or folder in bytes.
    Args:
        path (str): The path to the file.
    Returns:
        int: The size of the file in bytes.
        FileNotFoundError: If the specified file does not exist.
    """
    if type(path) == str:
        total_size = 0
        path = Path(path)

        for file in path.rglob('*'):
            if file.is_file():
                total_size += file.stat().st_size

        return total_size
    else:
        return ValueError
