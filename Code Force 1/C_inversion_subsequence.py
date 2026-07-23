import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx+n]; idx += n
        b = data[idx:idx+n]; idx += n
        x = 0  # a=1, b=0
        y = 0  # a=0, b=1
        z = 0  # a=1, b=1
        w = 0  # a=0, b=0
        for ai, bi in zip(a, b):
            if ai == b'1' and bi == b'0':
                x += 1
            elif ai == b'0' and bi == b'1':
                y += 1
            elif ai == b'1' and bi == b'1':
                z += 1
            else:
                w += 1

        if x == 0 and y == 0:
            ans = 0
        elif x % 2 == 1:
            ans = 1
        elif x > 0:
            # x even and > 0
            ans = 2
        else:
            # x == 0, y > 0
            if z > 0 and w > 0:
                ans = 2
            else:
                ans = -1
        out.append(str(ans))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
