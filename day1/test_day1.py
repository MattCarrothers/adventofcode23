import pytest

from day1 import get_calibration_values_total
from file_reader import read_lines_from_file


def test_file_reader():
    assert len(read_lines_from_file("day1_part1_example.txt")) == 4


def test_day1_example():
    expected_sum = 142

    example_list = read_lines_from_file('day1_part1_example.txt')
    actual_sum = get_calibration_values_total(example_list, False)

    assert actual_sum == expected_sum


def test_day1_part2_example():
    expected_sum = 281

    example_list = read_lines_from_file('day1_part2_example.txt')
    actual_sum = get_calibration_values_total(example_list, True)

    assert actual_sum == expected_sum
