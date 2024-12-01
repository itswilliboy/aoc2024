l1: list[int] = []
l2: list[int] = []

with open("inp.txt", "r") as f:
    for line in f.readlines():
        left, right = line.split()
        l1.append(int(left))
        l2.append(int(right))

l1.sort()
l2.sort()

res: int = 0
for left, right in zip(l1, l2):
    res += abs(left - right)

print("Result:", res, end="\n")

# Part 2

res: int = 0
for i in l1:
    res += i * l2.count(i)

print(f"Result 2: {res}")
