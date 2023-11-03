# SWEA D3 회문1
for i in range(1, 11):
    cnt = int(input())
    # arr = [list(map(str, input())) for _ in range(8)]
    List = list(input() for _ in range(8))
    
    row_arr, col_arr = [], []
    answer = 0
    
    # 가로 개수
    for j in range(0, 8):
        for k in range(0, 8-cnt+1):
            # row_arr.append(arr[j][k:k+cnt])
            A = List[j][k:cnt+k]
            if A == A[::-1]:
                answer += 1      
    
    # 세로 개수
    # for j in range(8-cnt+1):
    #     for k in range(8):
    #         col_arr = []
    #         for z in range(cnt):
    #             # col_arr.append(arr[j+z][k])
    #         if col_arr == col_arr[::-1]:
    #             answer += 1    
    
    for y in range(8-cnt+1):
        for x in range(8):
            A = ''
            for z in range(cnt):
                A += List[y+z][x]
            if A == A[::-1]:
                answer += 1   
            
    print('#'+str(i), answer)
            
            
for Count in range(10):
    N = int(input())
    List = list(input() for _ in range(8))
    Answer = 0
    
    # 가로 확인
    for y in range(8):
        for x in range(8-N+1):
            A = List[y][x:x+N]
            if A == A[::-1]:
                Answer += 1
 
    # 세로 확인
    for y in range(8-N+1):
        for x in range(8):
            A = ''
            for z in range(N):
                A += List[y+z][x]
            if A == A[::-1]:
                Answer += 1    
    print("#{} {}".format(Count+1,Answer))
