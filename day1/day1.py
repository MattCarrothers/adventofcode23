from file_reader import read_lines_from_file


def get_calibration_values_total(input_list: list[str], part_2: bool) -> int:
    calibration_values = []

    for line in input_list:
        if part_2:
            line = replace_substrings(line)

        first, current = None, None

        for char in line:
            if char.isnumeric():
                current = char
            if not first:
                first = current

        calibration_values.append(int(first + current))

    return sum(calibration_values)


def replace_substrings(input_string: str) -> str:
    number_dict = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "t3hree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "e8ight",
        "nine": "n9ine",
    }

    for key, value in number_dict.items():
        input_string = input_string.replace(key, value)

    return input_string


if __name__ == "__main__":
    part_1_list = read_lines_from_file(file_path='txts/day1.txt')
    part_1_ans = get_calibration_values_total(input_list=part_1_list, part_2=False)
    print(f"Part 1: {part_1_ans}")

    part_2_list = read_lines_from_file(file_path='txts/day1.txt')
    part_2_ans = get_calibration_values_total(input_list=part_2_list, part_2=True)
    print(f"Part 2: {part_2_ans}")
