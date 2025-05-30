from pathlib import Path
from typing import Union
import os
import shutil


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


class FileManager:
    """A class for managing file operations.

    This class provides methods for basic file operations such as checking existence,
    deletion, and duplication of files and directories.

    Args:
        path (str): The file system path to manage.

    Methods:
        exists(): Check if the path exists.
        delete(): Delete the file or directory at the path.
        duplicate(output_path): Create a copy of the file or directory.

    Raises:
        PermissionError: If there are insufficient permissions to perform the operation.
        FileNotFoundError: If the specified path does not exist.
        OSError: If an operating system level error occurs during operations.

    Examples:
        >>> fm = FileManager("/path/to/file.txt")
        >>> fm.exists()
        True
        >>> fm.delete()
        'File deleted'
    """

    def __init__(self, path):
        self.path = path

    def exists(self):
        """
        Check if the path exists.

        Returns:
            bool: True if the path exists, False otherwise.
        """
        return os.path.exists(self.path)

    def delete(self):
        """
        Delete the file or folder at the given path.

        Raises:
            PermissionError: If there is no permission to delete the file or folder.
            FileNotFoundError: If the file or folder does not exist.
            OSError: If an OS-related error occurs during deletion.

        Returns:
            str: Confirmation message if the deletion is successful.
        """
        if os.path.isfile(self.path):
            try:
                os.remove(self.path)
                return "File deleted"
            except PermissionError:
                raise PermissionError('No permission to delete the file')
            except FileNotFoundError:
                raise FileNotFoundError('File not found')

        elif os.path.isdir(self.path):
            if os.path.exists(self.path):
                try:
                    shutil.rmtree(self.path)
                    return "Folder deleted"
                except PermissionError:
                    raise PermissionError('No permission to delete the folder')
                except FileNotFoundError:
                    raise FileNotFoundError('Folder not found')
                except OSError as e:
                    raise OSError(f"OS error: {e}")
            else:
                raise FileNotFoundError("Folder does not exist")

        else:
            raise FileNotFoundError(
                "Path does not exist or is not a file/folder")

    def duplicate(self, output_path):
        pass
