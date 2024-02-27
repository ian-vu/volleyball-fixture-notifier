import pytest

from src.utils.string_utils import int_to_position


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, "1st"),
        (2, "2nd"),
        (3, "3rd"),
        (4, "4th"),
        (9, "9th"),
        (10, "10th"),
        (11, "11th"),
        (12, "12th"),
        (13, "13th"),
        (21, "21st"),
        (22, "22nd"),
        (23, "23rd"),
        (99, "99th"),
    ],
)
def test_int_to_position(input: int, expected: str):
    assert int_to_position(input) == expected
