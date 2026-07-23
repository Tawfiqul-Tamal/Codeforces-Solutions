import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())  # q = 0 in easy version
    a = list(map(int, input().split()))

    if a == sorted(a):
        print(0)
        continue

    answer = 1

    while True:
        block_size = answer * 2
        ok = True

        prev_max = -1

        for start in range(0, n, block_size):
            block = a[start:min(start + block_size, n)]

            mn = min(block)
            mx = max(block)

            if prev_max > mn:
                ok = False
                break

            prev_max = mx

        if ok:
            print(answer)
            break

        answer <<= 1
        