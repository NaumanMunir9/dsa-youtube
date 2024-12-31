package main

func containsDuplicate(nums []int) bool {
	seenNumbers := make(map[int]struct{})

	for _,num := range(nums) {
		if _, exists := seenNumbers[num]; exists {
			return true
		} else {
			seenNumbers[num] = struct{}{}
		}
	}
	return false
}