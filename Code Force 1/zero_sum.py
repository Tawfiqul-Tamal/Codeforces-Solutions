
import sys


def can_make_zero_sum(a: list[int]) -> bool:
    """Return True if the array's elements can be rearranged/flipped to sum to 0."""
    return sum(a) % 4 == 0


def solve(input_data: str) -> str:
    """Process all test cases from raw input text and return the combined output."""
    data = input_data.split()
    idx = 0
    t = int(data[idx]); idx += 1

    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx + n])); idx += n
        results.append("YES" if can_make_zero_sum(a) else "NO")

    return "\n".join(results)


def main() -> None:
    input_data = sys.stdin.read()
    print(solve(input_data))


if __name__ == "__main__":
    main()
