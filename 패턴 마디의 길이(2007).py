# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

# [제약 사항]
# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.

T = int(input())
for i in range(1, T+1):
    words = str(input())
    listed_words = list(words)
    arr = []
    for j in range(len(listed_words)):
        if listed_words[j] not in arr:
            arr.append(listed_words[j])
        else:
            if arr[0:j] == listed_words[j: j+j]:
                print('#'+str(i), len(arr))
            else:
                arr.append(listed_words[j])