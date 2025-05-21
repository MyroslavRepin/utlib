import os
import pytest
from utlib.files_utils import get_size


def test_get_size(tmp_path):
    test_file = tmp_path / "test_file.txt"
    content = "Things usually happen around us, not to us. - Unknown, found on Reddit"
    test_file.write_text(content)

    size = get_size(str(test_file))
    expected_size = len(content.encode())  # размер в байтах

    assert size == expected_size


def test_get_size_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_size("non_existent_file.txt")
