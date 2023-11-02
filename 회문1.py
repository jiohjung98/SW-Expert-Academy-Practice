# SWEA D3 회문1

T = 10

for i in range(1, T+1):
    cnt = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    
    row_arr, col_arr = [], []
    answer = 0
    
    # 가로 개수
    for j in range(0, 8):
        for k in range(0, 8-cnt+1):
            row_arr.append(arr[j][k:k+cnt])
            if row_arr == row_arr[::-1]:
                answer += 1      
    
    # 세로 개수
    for j in range(8-cnt+1):
        for k in range(8):
            col_arr = []
            for z in range(cnt):
                col_arr.append(arr[j+z][k])
            if col_arr == col_arr[::-1]:
                answer += 1    
            
    print('#'+str(i), answer)
            
            
            
