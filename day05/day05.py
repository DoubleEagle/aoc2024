import numpy as np

# input_file = open('day05_dummyinput.txt')
input_file = open('day05_input.txt')

rule_lines, order_lines = input_file.read().split('\n\n')

rules_pairs = [[int(x) for x in line.split("|")] for line in rule_lines.split("\n")]
# rules_pairs = np.matrix(rules.split("\n"))
# print(rules_pairs)


def part_1(orders, rules_pairs):
    result = 0

    # look at each order
    for order in orders.split("\n"):
        # loop through page numbers
        correct_order = True
        page_numbers = [int(x) for x in order.split(',')]
        for i in range(len(page_numbers)):

            # check every rule if it applies
            for rule in rules_pairs:
                if page_numbers[i] in rule:
                    # print("applied rule and page nr: ", rule, page_numbers[i])
                    # if first number, check if second number is not in front
                    if page_numbers[i] == rule[0]:
                        if rule[1] in page_numbers[:i]:
                            print("", page_numbers[:i])
                            correct_order = False
                            break
                    # if second number, check if first number is not after it
                    if page_numbers[i] == rule[1]:
                        if rule[0] in page_numbers[i+1:]:
                            # print(page_numbers[i+1:])
                            correct_order = False
                            break
            if not correct_order:
                break
            # print(page_numbers, correct_order)
        # print("ORDER CORRECT DECISION: ", correct_order, order)
        if correct_order:
            # print(page_numbers[len(page_numbers)//2])
            result += int(page_numbers[len(page_numbers)//2])
    return result


def fix_new_order(new_order, left, right):
    new_order.remove(left)
    new_order.insert(new_order.index(right), left)
    return new_order


def check_all_rules(rules_pairs, order):
    new_order = order.copy()
    order_changed = False
    for rule in rules_pairs:
        left, right = rule[0], rule[1]

        if left in order and right in order:
            # print("rule applies!", rule, new_order)
            if new_order.index(left) > new_order.index(right):
                # print("BROKEN RULE")
                new_order = fix_new_order(new_order, left, right)
                order_changed = True
    if order_changed:
        return check_all_rules(rules_pairs, new_order)
    else:
        return new_order


def part_2(orders, rules_pairs):
    result = 0

    # look at each order
    for order in orders.split("\n"):
        # print("========= Looking at order: ", order)

        page_numbers = [int(x) for x in order.split(',')]

        new_order = check_all_rules(rules_pairs, page_numbers)

        # print("===== Final new order: ", new_order, page_numbers, new_order == page_numbers)

        if new_order != page_numbers:
            result += int(new_order[len(new_order) // 2])
            # print("intermediate result: ", result)

    return result


print("Part 1: ", part_1(order_lines, rules_pairs))
print("Part 2: ", part_2(order_lines, rules_pairs))
