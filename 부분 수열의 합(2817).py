# SWEA D# 2817번 부분 수열의 합

from itertools import combinations

T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    answer = 0
    cnt = 0
            
    for j in range(1, N+1):
        for value in combinations(arr, j):
            answer = sum(value)
            if answer == K:
                cnt += 1
            
    print('#'+str(i), cnt)