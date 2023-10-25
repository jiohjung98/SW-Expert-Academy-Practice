T = int(input())
for i in range(1, T+1):
    tc = int(input())
    arr = []
    ans_arr = []
    for j in range(tc):
        alpha, num = map(str, input().split())
        num = int(num)
        
        for k in range(num):
            if len(arr) < 10:
                arr.append(alpha)
            else:
                new_val = ''.join(arr)
                ans_arr.append(new_val)
                arr = []
                arr.append(alpha)
    remain_val = ''.join(arr)
    ans_arr.append(remain_val)
    print("#"+str(i), *ans_arr, sep='\n')
    