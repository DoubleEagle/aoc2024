# input_file = open('day01_dummyinput.txt')
input_file = open('day01_input.txt')

input = input_file.read().split('\n')
left_list = []
right_list = []

for line in input:
    line_left, line_right = line.split("   ")
    left_list.append(int(line_left))
    right_list.append(int(line_right))


def part_1(left_list, right_list):
    left_list.sort()
    right_list.sort()

    result_part1 = 0

    for i in range(len(left_list)):
        result_part1 += int(abs(left_list[i] - right_list[i]))

    return result_part1


def part_2(left_list, right_list):
    result = 0
    for i in left_list:
        result += i * right_list.count(i)
    return result


print("Part 1:", part_1(left_list, right_list))
print("Part 2:", part_2(left_list, right_list))