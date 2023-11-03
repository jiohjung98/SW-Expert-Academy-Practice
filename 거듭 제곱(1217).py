# SWEA D3 1217번 거듭 제곱

for i in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    
    def power(N, M):
        if M == 0:
            return 1
        else:
            return N * power(N, M-1)
    
    print('#'+str(i), power(N, M))
