#BFS 풀이
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for x in numbers:
        tmp = []
        for leaf in leaves:
            tmp.append(leaf + x)
            tmp.append(leaf - x)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

numbers	= [4, 1, 2, 1]
target = 4

solution(numbers, target)