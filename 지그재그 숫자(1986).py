# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.


# [예제 풀이]

# N이 5일 경우,

# 1 – 2 + 3 – 4 + 5 = 3

# N이 6일 경우,

# 1 – 2 + 3 – 4 + 5 – 6 = -3

N = int(input())
for i in range(1, N+1):
    arr = []
    ans_arr = []
    tmp = int(input())
    for j in range(1, tmp+1):
        arr.append(j)
    for k in arr:
        if k % 2 == 0:
            ans_arr.append(k-2*k)
        else:
            ans_arr.append(k)
    print('#'+str(i), sum(ans_arr))