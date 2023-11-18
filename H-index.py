def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

citations = [3, 0, 6, 1, 5]

solution(citations)