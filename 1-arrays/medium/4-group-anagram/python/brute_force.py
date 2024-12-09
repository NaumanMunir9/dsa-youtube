def groupAnagrams(strs):
    result = []

    for str1 in strs:
        found_group = False

        for group in result:
            if sorted(str1) == sorted(group[0]):
                group.append(str1)
                found_group = True
                break

        if not found_group:
            result.append([str1])

    return result

input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_strings))