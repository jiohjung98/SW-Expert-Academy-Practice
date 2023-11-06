p, k = map(int, input().split())

if p >= k:
    print(p - k + 1)
else:
    print(k - p + 1)