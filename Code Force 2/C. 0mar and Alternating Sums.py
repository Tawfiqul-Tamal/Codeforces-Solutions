import sys

MOD = 1_000_000_007
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    distinct = len(set(a))
    base = pow(2, n - distinct, MOD)

    if a[0] != -1:
        print(base)
        continue

    values = set(x for x in a if x > 0)

    consecutive_pairs = 0
    for v in values:
        if v + 1 in values:
            consecutive_pairs += 1

    answer = base * (consecutive_pairs + 1)
    answer %= MOD

    print(answer)
    