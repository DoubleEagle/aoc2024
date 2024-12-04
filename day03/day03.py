import re
# input_file = open('day03_dummyinput.txt')
# input_file = open('day03_dummyinput2.txt')
input_file = open('day03_input.txt')

input = input_file.read()


def calculate_mul(input_string):
    left, right = input_string[4:-1].split(",")
    return int(left) * int(right)


def part_1(input_split_by_lines):
    result = 0
    for line in input_split_by_lines:
        instructions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)

        for mul in instructions:
            result += calculate_mul(mul)
    print("Part 1: ", result)


def part_2(input):
    result = 0
    # for line in input:
    instructions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\)", input)
    # print(instructions)
    do = True
    for instruction in instructions:
        # print(result, instruction, do)
        if instruction == "don't()":
            do = False
            continue
        if instruction == "do()":
            do = True
            continue
        if do:
            result += calculate_mul(instruction)
    print("Part 2: ", result)


part_1(input.split('\n'))
part_2(input)
