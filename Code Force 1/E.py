import sys

input = sys.stdin.readline


def build_group(nodes, extra, edges):
    m = len(nodes)
    if m == 0:
        return

    length = 0
    while (length + 1) * length // 2 <= extra:
        length += 1

    length -= 1

    for i in range(length):
        if i == 0:
            edges.append((1, nodes[i]))
        else:
            edges.append((nodes[i - 1], nodes[i]))

    if length < m:
        rem = extra - length * (length - 1) // 2

        if rem == 0:
            edges.append((1, nodes[length]))
        else:
            edges.append((nodes[rem - 1], nodes[length]))

        for i in range(length + 1, m):
            edges.append((1, nodes[i]))


t = int(input())

answer = []

for _ in range(t):
    n, k = map(int, input().split())

    mn = 2 * (n - 1)

    if k < mn or k % 2:
        answer.append("-1")
        continue

    req = (k - mn) // 2

    e = n // 2
    o = (n - 1) // 2

    mx = e * (e - 1) // 2 + o * (o - 1) // 2

    if req > mx:
        answer.append("-1")
        continue

    even_nodes = list(range(2, n + 1, 2))
    odd_nodes = list(range(3, n + 1, 2))

    use_even = min(req, e * (e - 1) // 2)
    use_odd = req - use_even

    edges = []

    build_group(even_nodes, use_even, edges)
    build_group(odd_nodes, use_odd, edges)

    answer.extend(f"{u} {v}" for u, v in edges)

sys.stdout.write("\n".join(answer))
