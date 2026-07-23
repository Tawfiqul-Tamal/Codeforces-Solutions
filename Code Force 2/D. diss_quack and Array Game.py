def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx+n])); idx += n
        
        moves = sum(x.bit_length() for x in arr)
        results.append(str(moves))
    
    print("\n".join(results))


if __name__ == "__main__":
    solve()

