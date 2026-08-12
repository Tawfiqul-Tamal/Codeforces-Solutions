MOD = 998244353

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    idx = 1

    results = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n

        # Base case
        if n == 1:
            if a[0] in (-1, 0):
                results.append("1")
            else:
                results.append("0")
            continue

        # DP table: dp[i][k] = ways after i steps with stack size k
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for k in range(n+1):
                if dp[i-1][k] == 0:
                    continue
                # If a[i-1] is specified
                if a[i-1] != -1:
                    c = a[i-1]
                    if c <= k:
                        dp[i][k-c+1] = (dp[i][k-c+1] + dp[i-1][k]) % MOD
                else:
                    # Try all possible c
                    for c in range(k+1):
                        dp[i][k-c+1] = (dp[i][k-c+1] + dp[i-1][k]) % MOD

        results.append(str(dp[n][1]))  # final stack must contain last element

    print("\n".join(results))


if __name__ == "__main__":
    solve()
