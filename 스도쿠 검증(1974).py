T = int(input())
for i in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    valid = True
    
    for j in range(9):
        row_arr = []
        col_arr = []
        for k in range(9):
            row_arr.append(arr[j][k])
            col_arr.append(arr[k][j])
        row_arr.sort()
        col_arr.sort()
        if row_arr != [1,2,3,4,5,6,7,8,9] or col_arr != [1,2,3,4,5,6,7,8,9]:
            valid = False
            break

    for x in range(0, 9, 3):
        square_arr = []
        for y in range(9):
            square_arr.extend(arr[y][x:x+3])
            if y == 2 or y == 5 or y == 8:
                square_arr.sort()
                if square_arr != [1,2,3,4,5,6,7,8,9]:
                    valid = False
                    break
                
    if valid:
        print('#'+str(i), 1)
    else:
        print('#'+str(i), 0)
       

