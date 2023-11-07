# SWEA D1 2043번 서랍의 비밀번호

p, k = map(int, input().split())

if p >= k:
    print(p - k + 1)
else:
    print(k - p + 1)