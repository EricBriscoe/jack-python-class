def print_grid(outer_list):
    for i in range(len(outer_list[0])):
        print(f"Working on column: {i}")
        for inner_list in outer_list:
            print(inner_list[i], end='')
        print('')

def print_zip_grid(outer_list):
    for column in zip(*outer_list):
        for char in column:
            print(char, end='')
        print('')

if __name__ == "__main__":
    test_case = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
    ]
    print_zip_grid(test_case)
