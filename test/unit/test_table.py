import pytest

from table import Table, OutOfBoundsException, NotFoundException

mock_table = Table([["0", "1", "2"], ["3", "4", "5"]])


def test_row_heading():
    assert mock_table.row_heading(0) == "0"
    assert mock_table.row_heading(1) == "3"


def test_row_heading_raises_if_invalid_row_idx():
    with pytest.raises(OutOfBoundsException):
        mock_table.row_heading(100)


def test_column_heading():
    assert mock_table.column_heading(0) == "0"
    assert mock_table.column_heading(1) == "1"
    assert mock_table.column_heading(2) == "2"


def test_row_heading_raises_if_invalid_column_idx():
    with pytest.raises(OutOfBoundsException):
        mock_table.column_heading(100)


def test_get_position_matching_str():
    assert mock_table.get_position_matching_str("1") == (0, 1)
    assert mock_table.get_position_matching_str("3") == (1, 0)
    assert mock_table.get_position_matching_str("4") == (1, 1)


def test_get_position_matching_str_raises_if_not_found():
    with pytest.raises(NotFoundException):
        mock_table.get_position_matching_str("999")
