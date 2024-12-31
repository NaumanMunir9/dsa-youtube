class ContainsDuplicate {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var hashSet = Set<Int>()

        for num in nums {
            if hashSet.contains(num) {
                return true
            } else {
                hashSet.insert(num)
            }
        }
        return false
    }
}