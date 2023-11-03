# SWEA D3 1220번 Magnetic

for i in range(1, 11):
    width = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    for j in range(100):
        arr2 = []
        for k in range(100):
            arr2.append(arr[k][j])
            if arr[k][j] == 2:
                arr[k][j], arr[k]
            
        for x in range(100):
            for y in range(x, 99):
                if arr[x][y] == 2:
                    arr[x]

                
            