l1: list[int] = []
l2: list[int] = []

with open("inp.txt", "r") as f:
    for line in f.readlines():
        left, right = line.split()
        l1.append(int(left))
        l2.append(int(right))

l1.sort()
l2.sort()


def part_a():
    res = 0
    for left, right in zip(l1, l2):
        res += abs(left - right)

    return res


def part_b():
    res = 0
    for i in l1:
        res += i * l2.count(i)

    return res


print(f"Part A: {part_a()}")
print(f"Part B: {part_b()}")
