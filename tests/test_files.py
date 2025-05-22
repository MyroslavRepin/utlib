from utlib.files_utils import get_size
import pytest
from pathlib import Path


def test_single_file(tmp_path):
    file = tmp_path / "file.txt"
    content = b"abcdefghij"
    file.write_bytes(content)

    assert get_size(file) == 10


def test_directory_with_files(tmp_path):
    (tmp_path / "folder").mkdir()
    file1 = tmp_path / "folder" / "file1.txt"
    file2 = tmp_path / "folder" / "file2.txt"
    file1.write_text("12345")
    file2.write_text("67890")

    total_size = get_size(tmp_path / "folder")
    assert total_size == 10


def test_nonexistent_path():
    with pytest.raises(FileNotFoundError):
        get_size("non_existent_file.txt")


def test_invalid_path(tmp_path):
    weird_path = tmp_path / "some_weird_thing"
    with pytest.raises(FileNotFoundError):
        get_size(weird_path)
