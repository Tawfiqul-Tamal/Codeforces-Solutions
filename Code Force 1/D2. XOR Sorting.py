import sys

input = sys.stdin.readline

INF = 10**18


class SegmentTree:
    def __init__(self, arr):
        n = len(arr)

        size = 1
        while size < n:
            size <<= 1

        self.size = size

        self.mn = [INF] * (2 * size)
        self.mx = [-INF] * (2 * size)
        self.ans = [0] * (2 * size)

        for i in range(n):
            self.mn[size + i] = arr[i]
            self.mx[size + i] = arr[i]

        for i in range(size - 1, 0, -1):
            self.pull(i)

    def pull(self, v):
        l = v * 2
        r = l + 1

        self.mn[v] = min(self.mn[l], self.mn[r])
        self.mx[v] = max(self.mx[l], self.mx[r])

        cur = max(self.ans[l], self.ans[r])

        seg_len = self.size // (1 << (v.bit_length() - 1))

        if self.mx[l] > self.mn[r]:
            cur = max(cur, seg_len // 2)

        self.ans[v] = cur

    def update(self, pos, val):
        v = self.size + pos

        self.mn[v] = val
        self.mx[v] = val
        self.ans[v] = 0

        v //= 2

        while v:
            self.pull(v)
            v //= 2

    def answer(self):
        return self.ans[1]


def solve():
    t = int(input())

    out = []

    for _ in range(t):
        n, q = map(int, input().split())

        a = list(map(int, input().split()))

        st = SegmentTree(a)

        out.append(str(st.answer()))

        for _ in range(q):
            idx, x = map(int, input().split())

            st.update(idx, x)

            out.append(str(st.answer()))

    sys.stdout.write("\n".join(out))


solve()
