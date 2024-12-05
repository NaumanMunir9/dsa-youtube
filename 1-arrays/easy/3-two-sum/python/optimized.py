def two_sum(nums, target):
    hash_map = {}

    for i, num in enumerate(num):
        complement = target - num

        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num] = 1

    return []