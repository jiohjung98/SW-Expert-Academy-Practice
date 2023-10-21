# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

# [예제]

# N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때
# 길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.

# [제약 사항]

# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for k in range(N):
        cnt = 0
        for x in range(N):
            if arr[k][x] == 1:
                cnt += 1
            if arr[k][x] == 0 or x == N-1:
                if cnt == K:
                    result += 1
                if arr[k][x] == 0:
                    cnt = 0
    
    for a in range(N):
        cnt = 0
        for b in range(N):
            if arr[b][a] == 1:
                cnt += 1
            if arr[b][a] == 0 or b == N-1:
                if cnt == K:
                    result += 1
                if arr[b][a] == 0:
                    cnt = 0
    print('#'+str(i), result)