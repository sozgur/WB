def two_array_object(arr1, arr2):
    val_num = len(arr2)
    key_val = {}

    for i in range(len(arr1)):
        val = arr2[i] if i < val_num else None
        key_val[arr1[i]] = val

    return key_val