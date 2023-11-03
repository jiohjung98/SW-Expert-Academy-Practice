# SWEA D3 1219번 Sum

for i in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    max_value = []
    
    for row in arr:
        max_value.append((sum(row)))
        
    for j in range(100):
        col_value = []
        for k in range(100):
            col_value.append(arr[k][j])
        max_value.append(sum(col_value))
        
    diagonal_value = []
    for x in range(100):
        diagonal_value.append(arr[x][x])
    
    max_value.append(sum(diagonal_value))
        
    diagonal_value2 = []
    for y in range(99, -1, -1):
        diagonal_value2.append(arr[y][y])
        
    max_value.append(sum(diagonal_value2))
    
    print('#'+str(tc), max(max_value))