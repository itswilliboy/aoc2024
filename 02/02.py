import numpy as np
import numpy.typing as npt

reports_: list[list[int]] = []

with open("inp.txt", "r") as f:
    for line in f.readlines():
        reports_.append([int(i) for i in line.split()])

reports: npt.NDArray[np.int_] = np.array(reports_, dtype=object)


def check_adjacent(a: int, b: int) -> bool:
    if 1 <= abs(a - b) <= 3:
        return True
    return False


# Ran for each 1D-array
def check_increase(arr: npt.NDArray[np.int_]) -> bool:
    diff = np.diff(arr)
    is_increasing = np.all(diff > 0)
    is_decreasing = np.all(diff < 0)
    return (is_increasing or is_decreasing).astype(bool)


def run_tests(arr: npt.NDArray[np.int_]) -> bool:
    is_safe_increase = check_increase(arr)
    is_safe_adjacent: bool

    safe_levels: list[bool] = []
    for i in range(len(arr) - 1):
        safe_levels.append(check_adjacent(arr[i], arr[i + 1]))

    is_safe_adjacent = all(safe_levels)
    return is_safe_increase and is_safe_adjacent


def part_a() -> int:
    safes: list[bool] = []
    for arr in reports:
        safes.append(run_tests(arr))

    return sum(1 for i in safes if i)


def part_b() -> int:
    safes: list[bool] = []
    for arr in reports:
        if run_tests(arr):
            safes.append(True)
            continue

        to_remove = 0
        is_safe: bool = False

        for _ in range(len(arr)):
            new = np.delete(arr, to_remove)

            if run_tests(new):
                is_safe = True
                break

            to_remove += 1

        safes.append(is_safe)

    return sum(1 for i in safes if i)


print(f"Part A: {part_a()}")
print(f"Part B: {part_b()}")
