def longest_fall(arr):
    n = len(arr)
    if n < 1:
        return n

    longest = 0
    last_long = 1
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            last_long += 1
            longest = max(last_long, longest)
        else:
            last_long = 1
    
    return longest or 1


