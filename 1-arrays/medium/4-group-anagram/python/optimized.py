from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)

    for str1 in strs:
        sorted_str = "".join(sorted(str1))
        result[sorted_str].append(str1)

    return list(result.values())