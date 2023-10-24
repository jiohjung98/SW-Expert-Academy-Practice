# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.
# 아래는 N =3 인 Ai 와 M = 5 인 Bj 의 예이다.

# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.

# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
# 위 예제의 정답은 아래와 같이 30 이 된다.
 
# [제약 사항]
# N 과 M은 3 이상 20 이하이다.

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    ans = 0
    arr =[]
    
    if N <= M:
        min_num = N
        range_value = M-N+1
    else:
        min_num = M
        range_value = N-M+1
        
    for j in range(range_value):
        for k in range(min_num):
            if min_num == N:
                val = a_arr[k] * b_arr[j+k]
                ans += val
            else:
                val = b_arr[k] * a_arr[j+k]
                ans += val
        arr.append(ans)
        ans = 0
    print('#'+str(i), max(arr))