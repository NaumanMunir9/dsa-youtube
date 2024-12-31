use std::collections::HashSet;

impl Solution {
    pub fn containsDuplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new();

        for &num in nums.iter() {
            if set.contains(&num) {
                return true;
            } else {
                set.insert(num);
            }
        }
        false
    }
}