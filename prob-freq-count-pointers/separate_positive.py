def separate_positive(arr):
    l = 0
    r = len(arr) -1
    
    while l < r:
        if arr[l] < 0:
            if arr[r] < 0:
                r -= 1
            else:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
                l += 1
        else:
            l += 1
 
    return arr