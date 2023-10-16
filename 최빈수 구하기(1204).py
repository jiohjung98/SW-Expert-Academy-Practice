# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

# 다음과 같은 수 분포가 있으면,

# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

# 최빈수는 8이 된다.

# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

# [제약 사항]

# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
 
 
T = int(input())

for i in range(1, T+1):
    n = int(input())
    ans_arr = [0] * 101
    scores = list(map(int, input().split()))
    scores.sort()
    for score in scores:
        ans_arr[score] += 1
    # ans = ans_arr.index(max(ans_arr[::-1]))
    # print(max(ans_arr))
    # print(ans)
    max_ans = 0
    max_index = 0
    for j in range(len(ans_arr)):
        if (ans_arr[j] >= max_ans):
            max_ans = ans_arr[j]
            max_index = j
    print('#'+str(i), max_index)