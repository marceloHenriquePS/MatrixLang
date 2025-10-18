import pytest

from src.validator import validate_matrix

def test_validate_matrix_valid():
    assert validate_matrix([[1, 2], [3, 4]]) is True

def test_validate_matrix_row_length_mismatch():
    with pytest.raises(ValueError):
        validate_matrix([[1, 2], [3]])

def test_validate_matrix_non_numeric():
    with pytest.raises(ValueError):
        validate_matrix([[1, 'a'], [3, 4]])
