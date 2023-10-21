N, K = map(int, input().split())

result = 0

while True:
    # N이 K로 나눠떨어지는 수가 될 때까지 빼기
    target = (N // K) * K   # N = 25, K = 3이면 target = (25 // 3) * 3 = 24
    result += (N - target)  # result = 25 - 24 = 1
    N = result # N = 1
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break
    result += 1
    N //= K

# 마지막으로 남은 수에 대해 1씩 빼기
result += (N-1)
print(result)
    