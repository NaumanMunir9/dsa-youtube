#include <vector>
#include <unordered_set>
using std::unordered_set;
using std::vector;

class Solution {
    public bool containsDuplicate(vector<int> &nums) {
        unordered_set<int> set;

        for (i = 0; i < nums.size(); i++) {
            if (set.find(nums[i]) != set.end()) {
                return true;
            } else {
                set.insert(nums[i]);
            }
        }
        return false;
    }
}