# input_file = open('day02_dummyinput.txt')
input_file = open('day02_input.txt')

input_lines = input_file.read().split('\n')


def check_extra_safe(levels, i):
    safe = False
    if check_safe(levels[:i - 1] + levels[i:]):
        safe = True
    elif check_safe(levels[:i] + levels[i + 1:]):
        safe = True
    return safe

def check_safe(levels, dampener=False):
    ascending = None
    safe = True
    for i in range(1, len(levels)):
        # check if consecutive are the same
        if levels[i] == levels[i - 1]:
            safe = False
            if dampener:
                safe = check_extra_safe(levels, i)
            break
        # check if consecutive have a step too big
        if abs(levels[i] - levels[i - 1]) > 3:
            safe = False
            if dampener:
                safe = check_extra_safe(levels, i)
            break
        if ascending is None:
            if levels[i] < levels[i - 1]:
                ascending = False
            else:
                ascending = True
        # check if all ascending
        if levels[i] < levels[i - 1] and ascending:
            safe = False
            if dampener:
                safe = check_extra_safe(levels, i)
            break
        # check if all descending
        if levels[i] > levels[i - 1] and not ascending:
            safe = False
            if dampener:
                safe = check_extra_safe(levels, i)
            break
    return safe


def part_1(input_lines):
    safe_counter = 0
    for line in input_lines:
        levels = [int(x) for x in line.split(" ")]
        safe = check_safe(levels)
        if safe:
            safe_counter += 1
    return safe_counter


def part_2(input_lines):
    safe_counter = 0
    for line in input_lines:

        levels = [int(x) for x in line.split(" ")]
        safe = check_safe(levels, True)
        if safe:
            safe_counter += 1
    return safe_counter


print("Part 1: ", part_1(input_lines))
print("Part 2: ", part_2(input_lines))
