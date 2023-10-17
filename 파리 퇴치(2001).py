# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

# 아래는 N=5 의 예이다.
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 죽은 파리의 개수를 구하라!
# 예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
 

# [제약 사항]
# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.

T = int(input())
for i in range(1, T+1):
    N, M = input().split(" ")
    arr = []
    ans_arr = []
    for j in range(0, int(N)):
        nums = list(map(int, input().split()))
        arr.append(nums)
    for k in range(0, int(N)-int(M)+1):
        for x in range(0,int(N)-int(M)+1):
            flies = 0
            for y in range(int(M)):
                for z in range(int(M)):
                    flies += arr[k+y][x+z]
            ans_arr.append(flies)
    print('#'+str(i), max(ans_arr))
    


                    
            
            
            
        