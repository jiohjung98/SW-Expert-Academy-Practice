# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

T = int(input())
for i in range(1, T+1):
    nums = list(map(int, input().split()))
    max_num = max(nums)
    min_num = min(nums)
    nums.remove(max_num)
    nums.remove(min_num)
    avg = round(sum(nums) / 8)
    print('#'+str(i), avg)