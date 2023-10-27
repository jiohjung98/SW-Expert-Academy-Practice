
# 크기가 N인 파스칼의 삼각형을 만들어야 한다.
# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

# 1. 첫 번째 줄은 항상 숫자 1이다.
# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

# [제약 사항]
# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

T = int(input())

for i in range(1, T+1):
    N = int(input())
    ans_arr = []
    for j in range(1, N+1):
        ans_arr.append([])
        for k in range(j):
            if k == 0 or k == j-1:
                ans_arr[j-1].append(1)
            else:
                ans_arr[j-1].append(ans_arr[j-2][k-1] + ans_arr[j-2][k])
    print('#'+str(i))
    for ans in ans_arr:
        print(*(ans), end=' ')
        print()