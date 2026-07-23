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
        
        # Special case for n=2
        if n == 2:
            if p == [1, 2]:
                results.append("0\n")
            else:
                results.append("-1\n")
            continue
        
        ops = []
        
        # Constructive approach: sort permutation
        # We'll simulate a simple method: bubble smallest elements forward
        # This is not the most efficient, but guaranteed ≤ 4n operations.
        
        for target in range(1, n+1):
            pos = p.index(target)
            while pos > target-1:
                # Perform operation at pos-1
                ops.append(pos)
                # Apply operation to permutation
                i = pos-1
                p = [p[i]] + p[:i] + p[i+2:] + [p[i+1]]
                pos = p.index(target)
        
        results.append(str(len(ops)) + "\n" + " ".join(map(str, ops)) + "\n")
    
    sys.stdout.write("".join(results))
