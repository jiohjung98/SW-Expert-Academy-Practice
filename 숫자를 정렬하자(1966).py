# SWEA D2 1966번 숫자를 정렬하자

T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print('#'+str(i), end=' ')
    for j in arr:
        print(j, end=' ')