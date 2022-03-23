def pivot_index(arr):
    n = len(arr)
    if n < 3:
        return -1

    left = arr[0]
    right = sum(arr) - left

    for i in range(1, n-1):
        right -= arr[i] 

        if left == right:
            return i
        else:
            left += arr[i]

    return -1