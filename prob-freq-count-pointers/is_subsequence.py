def is_subsequence(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if l1 > l2:
        return False

    p1 = 0
    p2 = 0

    while p1 < l1 and p2 < l2:
        if str1[p1] == str2[p2]:
            p1 += 1
            p2 += 1
        else:
            p2 += 1
    
    return p1 == l1