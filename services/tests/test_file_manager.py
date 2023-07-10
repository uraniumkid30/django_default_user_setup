import pytest
from services.file_manager import FileProcessingTool


def test_is_file_exists():
    res = FileProcessingTool.is_file_exists("none.txt")
    assert res == False


def test_is_folder_exists():
    res = FileProcessingTool.is_folder_exists("folder/test")
    assert res == False


def test_get_extension():
    res = FileProcessingTool.get_extension("none.txt")
    assert res == ".txt"