def same_frequency(int1, int2):
    str1 = str(int1)
    str2 = str(int2)

    if len(str1) != len(str2):
        return False

    total = 0

    for i in range(len(str1)):
        total += int(str1[i])
        total -= int(str2[i])

    return total == 0