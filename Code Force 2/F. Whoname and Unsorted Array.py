def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        p = list(map(int, data[idx:idx+n])); idx += n
        
        # Special case
        if n == 2 and p == [2, 1]:
            results.append("-1")
            continue
        
        ops = []
        
        # Greedy constructive approach
        for target in range(1, n+1):
            pos = p.index(target)
            while pos > target-1:
                i = pos
                ops.append(i)
                # Apply operation
                p = [p[i-1]] + p[:i-1] + p[i+1:] + [p[i]]
                pos = p.index(target)
        
        results.append(str(len(ops)) + "\n" + " ".join(map(str, ops)) if ops else "0")
    
    print("\n".join(results))


if __name__ == "__main__":
    solve()



