import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        arr = [1, 2, 3]

        for i in range(1, n - 2):
            arr.append(3 * (1 << i))

        print(*arr)