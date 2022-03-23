def construct_note(str1, str2):
    if len(str1) > len(str2):
        return False

    counter_str1={}
    counter_str2={}

    for ch in str1:
        counter_str1[ch] = counter_str1.get(ch, 0) + 1
    
    for ch in str2:
        counter_str2[ch] = counter_str2.get(ch, 0) + 1

    for k in counter_str1:
        if k not in counter_str2 or counter_str2[k] != counter_str1[k]:
            return False
    
    return True