N = int(input())
plans = input().split()
x, y = 1, 1

# L, R, U, D로 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_direction = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_direction)):
        if plan == move_direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x,y)