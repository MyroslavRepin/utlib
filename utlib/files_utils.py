from pathlib import Path
from typing import Union


def get_size(path: Union[str, Path]) -> int:
    """
    Returns the size of a file or folder in bytes.

    Args:
        path (str | Path): The path to a file or directory.

    Returns:
        int: The size in bytes.

    Raises:
        FileNotFoundError: If the path does not exist.
        ValueError: If the path is not a file or directory.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    if path.is_file():
        return path.stat().st_size
    elif path.is_dir():
        return sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
    else:
        raise ValueError(f"Invalid path: {path}")
