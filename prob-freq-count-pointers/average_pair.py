def average_pair(nums, avg):
    pair_of_total = avg * 2
    check_hash = {}

    for num in nums:
        target = pair_of_total - num
        if target in check_hash:
            return True
        check_hash[num] = True

    return False

# this soltuion for sorted arr
def average_pair_pointer(nums, avg):
    left = 0
    right = len(nums)-1

    while left < right:
        num = (nums[left] + nums[right]) / 2
        if avg == num:
            return True
        elif avg > num:
            left += 1
        else:
            right -= 1

    return False
