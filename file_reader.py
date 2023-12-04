def read_lines_from_file(file_path: str, strip: bool = True) -> list[str]:
    with open(file_path) as file:
        if strip:
            file_list = [line.rstrip() for line in file if line]
        else:
            file_list = file.readlines()
        file.close()

    return file_list
