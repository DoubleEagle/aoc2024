import numpy as np

# input_file = open('day04_dummyinput.txt')
input_file = open('day04_input.txt')

input_lines = input_file.read().split("\n")


def find_horizontals(lines):
    count = 0
    for line in lines:
        count += line.count("XMAS")
        count += line.count("SAMX")
    return count


def find_verticals(matrix):
    count = 0
    matrix_transposed = matrix.transpose()

    for line in matrix_transposed:
        line_concat = ''.join(line.tolist()[0])
        count += line_concat.count("XMAS")
        count += line_concat.count("SAMX")
    return count


def find_diagonals(matrix):
    count = 0
    for i in range(-matrix.shape[0], matrix.shape[0]):
        diagonal = np.diag(matrix, i)
        if len(diagonal) > 3:
            diagonal_concat = ''.join(diagonal.tolist())
            count += diagonal_concat.count("XMAS")
            count += diagonal_concat.count("SAMX")
    return count


def find_diagonals_up(matrix):
    matrix_transposed = np.fliplr(matrix)
    return find_diagonals(matrix_transposed)


def part_1(lines):
    count = 0
    count += find_horizontals(lines)
    matrix = np.matrix([list(x) for x in lines])
    count += find_verticals(matrix)
    count += find_diagonals(matrix)
    count += find_diagonals_up(matrix)
    print("Part 1: ", count)


def part_2(lines):
    count = 0
    for row in range(1, len(lines) - 1):
        for col in range(1, len(lines[row]) - 1):
            if lines[row][col] == "A":
                # S   S
                #   A
                # M   M
                if lines[row-1][col-1] == "S" and lines[row-1][col+1] == "S" and lines[row+1][col-1] == "M" and lines[row+1][col+1] == "M":
                    count += 1
                # S   M
                #   A
                # S   M
                if lines[row-1][col-1] == "S" and lines[row-1][col+1] == "M" and lines[row+1][col-1] == "S" and lines[row+1][col+1] == "M":
                    count += 1
                # M   M
                #   A
                # S   S
                if lines[row-1][col-1] == "M" and lines[row-1][col+1] == "M" and lines[row+1][col-1] == "S" and lines[row+1][col+1] == "S":
                    count += 1
                # M   S
                #   A
                # M   S
                if lines[row-1][col-1] == "M" and lines[row-1][col+1] == "S" and lines[row+1][col-1] == "M" and lines[row+1][col+1] == "S":
                    count += 1
    print("Part 2: ", count)


part_1(input_lines)
part_2(input_lines)
