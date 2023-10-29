T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    
    start_idx, end_idx = N // 2, N // 2
    
    for j in range(0, N):
        for k in range(start_idx, end_idx + 1):
            ans += arr[j][k]
            
        if j < N // 2:
            start_idx -= 1
            end_idx += 1
        else:
            start_idx += 1
            end_idx -= 1
    print('#'+str(i), ans)