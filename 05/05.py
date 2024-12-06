from typing import TypeVar

T = TypeVar("T")

type _2DArray[T] = list[list[T]]

with open("inp.txt", "r") as f:
    content = f.read().split("\n\n")

    rules: _2DArray[int]
    updates: _2DArray[int]

    def split(sep: str, idx: int) -> _2DArray[int]:
        return list(
            list(map(int, i))
            for i in list(j.split(sep) for j in content[idx].splitlines())
        )

    rules = split("|", 0)
    updates = split(",", 1)


def sum_middle(arr: _2DArray[int]) -> int:
    total = 0
    for i in arr:
        total += i[len(i) // 2]

    return total


def get_applicable_rules(
    update: list[int], rules_: _2DArray[int] = rules
) -> _2DArray[int]:
    applicable_rules: _2DArray[int] = []
    for rule in rules_:
        first, second = rule
        if first in update and second in update:
            applicable_rules.append(rule)

    return applicable_rules


def part_a() -> int:
    correct_updates: _2DArray[int] = []

    for update in updates:
        applicable_rules: _2DArray[int] = []
        for rule in rules:
            first, second = rule
            if first in update and second in update:
                applicable_rules.append(rule)

        correct: list[bool] = []
        for rule in applicable_rules:
            first, second = rule
            correct.append(update.index(first) < update.index(second))

        if all(correct):
            correct_updates.append(update)

    return sum_middle(correct_updates)


def part_b() -> int:
    incorrect_updates: _2DArray[int] = []

    for update in updates:
        applicable_rules = get_applicable_rules(update)

        correct: list[bool] = []
        for rule in applicable_rules:
            first, second = rule
            correct.append(update.index(first) < update.index(second))

        if not all(correct):
            incorrect_updates.append(update)

    for update in incorrect_updates:
        applicable_rules = get_applicable_rules(update)
        applicable_rules.sort(key=lambda i: i[0])
        for rule in applicable_rules:
            first, second = rule

            while update.index(first) > update.index(second):
                f_idx = update.index(first)
                a = update[f_idx]
                b = update[f_idx - 1]

                update[f_idx - 1] = a
                update[f_idx] = b

    return sum_middle(incorrect_updates)


print(f"Part A: {part_a()}")
print(f"Part B: {part_b()}")
