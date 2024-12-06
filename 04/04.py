with open("inp.txt", "r") as f:
    puzzle = f.read()

letters: list[list[str]] = list([] for _ in puzzle.splitlines())
for i, line in enumerate(puzzle.splitlines()):
    for j, char in enumerate(line):
        letters[i].append(char)


def check_xmas(arg: list[str]) -> bool:
    return "".join(arg) == "XMAS"


def check_x_mas(arg: list[str]) -> bool:
    return "".join(arg) in ("SAM", "MAS")


def check_sides(x: int, y: int) -> int:
    found = 0

    if x + 3 <= len(letters[y]):
        if check_xmas(letters[y][x : x + 4]):
            found += 1

    if x - 3 >= 0:
        if check_xmas(letters[y][x - 3 : x + 1][::-1]):
            found += 1

    return found

# Thanks Leo
def check_vertical(x: int, y: int) -> int:
    found = 0

    if y + 3 < len(letters):
        curr: list[str] = []
        for i in range(y, y + 4):
            curr.append(letters[i][x])

        if check_xmas(curr):
            found += 1

    if y - 3 >= 0:
        curr: list[str] = []
        for i in range(y - 3, y + 1):
            curr.append(letters[i][x])

        if check_xmas(curr[::-1]):
            found += 1

    return found


def check_diagonal(x: int, y: int) -> int:
    found = 0

    # 0 = NE, 1 = SE, 2 = SW, 3 = NW
    dirr = 0
    while dirr <= 3:
        chars: list[str] = []
        for i in range(4):
            next_coord: tuple[int, int]
            match dirr:
                case 0:
                    next_coord = y - i, x + i
                case 1:
                    next_coord = y + i, x + i
                case 2:
                    next_coord = y + i, x - i
                case 3:
                    next_coord = y - i, x - i

            new_y, new_x = next_coord

            if (
                any(c < 0 for c in next_coord)
                or new_x >= len(letters[y])
                or new_y >= len(letters)
            ):
                continue

            chars.append(letters[new_y][new_x])

        if check_xmas(chars):
            found += 1

        dirr += 1

    return found


def check_cross(x: int, y: int) -> int:
    found = 0

    TL = x - 1, y - 1
    TR = x + 1, y - 1
    BL = x - 1, y + 1
    BR = x + 1, y + 1

    chars: dict[int, str] = {}
    for i, (xx, yy) in enumerate((TL, TR, BR, BL)):
        if any(i < 0 for i in (xx, yy)):
            continue

        if yy >= len(letters) or xx >= len(letters[y]):
            return 0

        chars[i] = letters[yy][xx]

    a: list[str] = []
    b: list[str] = []
    for k, v in chars.items():
        if k % 2 == 0:
            a.append(v)
        else:
            b.append(v)

    a.insert(1, "A"), b.insert(1, "A")
    print(f"{y}:{x} -> {a} : {b}", check_x_mas(a) and check_x_mas(b))

    if check_x_mas(a) and check_x_mas(b):
        found += 1

    return found


def part_a() -> int:
    total = 0
    for y, line in enumerate(letters):
        for x, char in enumerate(line):
            if char == "X":
                total += check_sides(x, y)
                total += check_vertical(x, y)
                total += check_diagonal(x, y)

    return total


def part_b() -> int:
    total = 0
    for y, line in enumerate(letters):
        for x, char in enumerate(line):
            if char == "A":
                total += check_cross(x, y)

    return total


print(f"Part A: {part_a()}")
print(f"Part B: {part_b()}")
