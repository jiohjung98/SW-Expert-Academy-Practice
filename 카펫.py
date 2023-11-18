def solution(brown, yellow):
    square = brown + yellow
    arr = []
    for i in range(1, square+1):
        if square % i == 0:
            arr.append(i)
    if len(arr) % 2 == 0:
        front_arr = arr[:len(arr)//2]
        back_arr = arr[len(arr)//2:]
    else:
        front_arr = arr[:len(arr)//2+1]
        back_arr = arr[len(arr)//2:]
    front_arr.sort(reverse=True)
    
    
    print(front_arr, back_arr)
    
    for x, y in zip(front_arr, back_arr):
        print(x, y)
        print(2*x + 2*y - 2)
        if 2*x + (y-2)*2 == brown:
            break
    return [y, x]