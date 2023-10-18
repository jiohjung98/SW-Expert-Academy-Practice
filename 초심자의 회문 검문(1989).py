# "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.


# [제약 사항]
# 각 단어의 길이는 3 이상 10 이하이다.

T = int(input())
for i in range(1, T+1):
    word = list(map(str, input()))
    if (len(word) %2 != 0):
        left_word = word[:len(word)//2]
        right_word = word[len(word)//2+1:]
        right_word.reverse()
    else:
        left_word = word[:len(word)//2]
        right_word = word[len(word)//2:]
        right_word.reverse()
    if left_word == right_word:
        print('#'+str(i), 1)
    else:
        print('#'+str(i), 0)
