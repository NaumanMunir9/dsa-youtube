def isAnagram(s, t):
    if len(s) != len(t):
        return False

    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_s == sorted_t:
        return True
    else:
        return False