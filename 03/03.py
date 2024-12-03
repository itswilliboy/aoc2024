import re

memory: str = ""
with open("inp.txt", "r") as f:
    memory = f.read()

MUL_PATTERN = re.compile(r"mul\((\d+),(\d+)\)")
DO_PATTERN = re.compile(r"(don't\(\))|(do\(\))")


def part_a():
    total: list[int] = []
    for match in MUL_PATTERN.findall(memory):
        total.append(int(match[0]) * int(match[1]))

    return sum(total)


def part_b():
    muls: list[tuple[tuple[int, int], int]] = []
    instrs: list[tuple[tuple[int, int], str]] = []

    for match in MUL_PATTERN.finditer(memory):
        muls.append((match.span(), int(match.groups()[0]) * int(match.groups()[1])))

    for match in DO_PATTERN.finditer(memory):
        instrs.append((match.span(), match.group()))

    total: list[int] = []
    is_do: bool
    for (start, end), product in muls:
        try:
            prev = list((a, b, c) for ((a, b), c) in instrs if b < end)[-1]
            print(f"Prev: {prev}\nStart: {start}\nEnd: {end}", end="\n\n")

            if prev[2] == "do()":
                is_do = True
            else:
                is_do = False

        except IndexError:
            is_do = True

        if is_do:
            print(f"Applying product: {product}")
            total.append(product)

    return sum(total)

print(f"Part B: {part_b()}")
print(f"Part A: {part_a()}")
