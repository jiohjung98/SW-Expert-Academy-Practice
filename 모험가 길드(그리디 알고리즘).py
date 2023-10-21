N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 1 2 2 2 3
group_cnt = 0 # 총 그룹 수
cnt = 0 # 현재 그룹에 포함된 사람 수

for data in arr:
    cnt += 1
    if cnt >= data:
        group_cnt += 1
        cnt = 0

print(group_cnt)