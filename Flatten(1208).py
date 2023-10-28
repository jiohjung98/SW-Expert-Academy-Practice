T = 10

for i in range(1, T+1):
    dump = int(input())
    arr = list(map(int, input().split()))
    
    while (dump != 0):
        max_val = max(arr)
        max_val_index = arr.index(max_val)
        min_val = min(arr)
        min_val_index = arr.index(min_val)
        
        arr[max_val_index] -= 1
        arr[min_val_index] += 1
        dump -= 1
    
    print('#'+str(i), max(arr) - min(arr))