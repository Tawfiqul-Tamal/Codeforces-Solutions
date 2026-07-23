def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        perm = []
        for i in range(1, n+1, 2):
            perm.append(i+1)
            perm.append(i)
        results.append(" ".join(map(str, perm)))
    
    print("\n".join(results))


if __name__ == "__main__":
    solve()
