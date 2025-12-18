"""
input = 3
opt ->  1
        3 2
        6 5 4


"""

# solution
n = 3
num = 1
for i in range(1, n+1):
    row = []
    for _ in range(i):
        row.append(num)
        num += 1

    row.reverse()
    print(*row)
