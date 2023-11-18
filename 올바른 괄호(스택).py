# def solution(s):
#     answer = True
    
#     s = list(s)
    
#     while s:
#         cnt = 0
#         while s and s[0] == '(':
#             s.pop(0)
#             cnt += 1

#         print("".join(s[:cnt]))
#         print('(' * cnt)

#         if "".join(s[:cnt]) == ')' * cnt:
#             # while s and s[0] == ')':
#             #     s.pop(0)
#             [s.pop(0) for i in range(cnt)]
#             if len(s) >= 1 and s[0] == ')':
#                 return False
#         else:
#             return False

#     return True

def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:  
            if not stack:  
                return False
            stack.pop()  
            
    return len(stack) == 0  

s = "(())())"

solution(s)