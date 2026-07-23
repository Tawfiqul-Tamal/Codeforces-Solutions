import sys


def build_good_array(n: int, k: int, m: int) -> list[int] | None:
    """Return a good array of length n, or None if no such array exists."""
    if k > m:
        return None

    wrap_value = m - (k - 1)  # value used whenever the residue wraps back to 0
    a = [1] * n
    for i in range(k, n + 1, k):
        a[i - 1] = wrap_value  # a is 0-indexed; position i (1-indexed) -> a[i-1]
    return a


def solve(input_data: str) -> str:
    """Process all test cases from raw input text and return the combined output."""
    data = input_data.split()
    idx = 0
    t = int(data[idx]); idx += 1

    out_lines = []
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx + 1]); m = int(data[idx + 2])
        idx += 3

        arr = build_good_array(n, k, m)
        if arr is None:
            out_lines.append("NO")
        else:
            out_lines.append("YES")
            out_lines.append(" ".join(map(str, arr)))

    return "\n".join(out_lines)


def main() -> None:
    input_data = sys.stdin.read()
    sys.stdout.write(solve(input_data) + "\n")


if __name__ == "__main__":
    main()
