def solution(numbers):
    answer = ''
    input_list = list(map(str, numbers))
    input_list.sort(key = lambda x: x*3, reverse = True)
    answer = answer.join(input_list)
    return str(int(answer))
