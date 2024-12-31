import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean containsDuplicate([]int nums) {
        Set<Integer> set = new HashSet<>();

        for (i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                return true;
            } else {
                set.add(nums[i]);
            }
        }
        return false;
    }
}