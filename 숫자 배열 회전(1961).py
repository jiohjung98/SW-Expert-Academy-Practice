T = int(input())

for m in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] 
    
    arr_90 = []
    arr_180 = []
    arr_270 = []
    
    for i in range(N):
        for j in range(N-1, -1, -1):
            arr_90.append(arr[j][i])
    
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            arr_180.append(arr[i][j])
            
    for i in range(N-1, -1, -1):
        for j in range(N):
            arr_270.append(arr[j][i])
         
    ans_90 = []
    ans_180 = []
    ans_270 = []   
    
    for x in range(0, len(arr_90), len(arr_90) // N):
        ans_90.append(''.join(map(str, arr_90[x:x+N])))
    for x in range(0, len(arr_180), len(arr_180) // N):
        ans_180.append(''.join(map(str, arr_180[x:x+N])))
    for x in range(0, len(arr_270), len(arr_270) // N):
        ans_270.append(''.join(map(str, arr_270[x:x+N])))

    print('#'+str(m))
    for y in range(N):
        print(ans_90[y], ans_180[y], ans_270[y])