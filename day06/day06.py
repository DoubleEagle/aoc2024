import copy

# input_file = open('day06_dummyinput.txt')
input_file = open('day06_input.txt')

initial_floorplan = [list(row) for row in input_file.read().split('\n')]


def pretty_print_floorplan(to_print, steps=[]):
    for step in steps:
        if step[2] == 0 or step[2] == 180:
            to_print[step[0]][step[1]] = "|"
        else:
            to_print[step[0]][step[1]] = "-"
    for row in to_print:
        print(''.join(row))


def find_guard(plan):
    for y in range(len(plan)):
        if "^" in plan[y]:
            return y, plan[y].index("^")
    return -1


# pretty_print_floorplan(initial_floorplan)

# Start positions
guard_row, guard_col = find_guard(initial_floorplan)
initial_direction = 0


def take_step(floorplan, direction, step_ids, steps, test_loops=False):
    # print("================== Step...", len(steps_taken))
    y, x = find_guard(floorplan)

    loops = False

    if direction == 0:
        to_y, to_x = y - 1, x
    elif direction == 90:
        to_y, to_x = y, x + 1
    elif direction == 180:
        to_y, to_x = y + 1, x
    else:           # 270
        to_y, to_x = y, x - 1

    # out of bounds
    if to_y < 0 or to_y >= len(floorplan) or to_x < 0 or to_x >= len(floorplan):
        floorplan[y][x] = "."
        step_ids.append(str(y) + "|" + str(x))
        steps.append([y, x, direction])
    # normal step
    elif floorplan[to_y][to_x] == ".":
        floorplan[y][x] = "."
        floorplan[to_y][to_x] = "^"
        step_ids.append(str(y) + "|" + str(x))
        if test_loops and [y, x, direction] in steps:
            loops = True
        steps.append([y, x, direction])
    # change direction because obstacle
    elif floorplan[to_y][to_x] == "#":
        direction = (direction + 90) % 360

    return floorplan, direction, step_ids, steps, loops


def part_1(floorplan, direction):
    fp = copy.deepcopy(floorplan)
    step_ids = []
    steps_list = []
    while find_guard(fp) != -1:
        fp, direction, step_ids, steps_list, loops = take_step(fp, direction, step_ids, steps_list)

    print("Part 1: ", len(set(step_ids)))


def part_2(floorplan, direction):
    step_ids_1 = []
    steps_1 = []
    floorplan_1 = copy.deepcopy(floorplan)
    i = 0
    # pretty_print_floorplan(floorplan_1)
    while find_guard(floorplan_1) != -1:
        floorplan_1, direction, step_ids_1, steps_1, loops = take_step(floorplan_1, direction, step_ids_1, steps_1)
        i += 1


    obstacle_ids = []
    counter = 0
    print(len(steps_1))
    for step in steps_1:
        if str(step[0]) + "|" + str(step[1]) in obstacle_ids:
            continue
        # print(step)
        floorplan_2 = copy.deepcopy(floorplan)
        floorplan_2[step[0]][step[1]] = "#"
        direction = 0
        step_ids_1 = []
        steps_1 = []
        while find_guard(floorplan_2) != -1:
            # print(len(np.where(initial_floorplan == "G")[0]))
            # pretty_print_floorplan(floorplan_2)
            floorplan_2, direction, step_ids_1, steps_1, loops = take_step(floorplan_2, direction, step_ids_1, steps_1, True)
            if loops:
                print("Found one!", counter, step)
                obstacle_ids.append(str(step[0]) + "|" + str(step[1]))
                # pretty_print_floorplan(floorplan, [step])
                break
        counter += 1
        if counter % 1000 == 0:
            print(counter)
        # print(stepperdistep_counter)
    print("Part 2: ", len(set(obstacle_ids)))


part_1(initial_floorplan, initial_direction)
part_2(initial_floorplan, initial_direction)
