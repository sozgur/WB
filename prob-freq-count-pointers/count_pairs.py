def count_pairs(arr, num):
    hash_map = {}
    total = 0
    
    for pair in arr:
        pair2 = num - pair 
        if pair2 in hash_map:
            total += 1
        else:
            hash_map[pair] = True
    
    return total