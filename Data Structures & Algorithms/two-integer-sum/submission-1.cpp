#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Map to store: Key = the number seen, Value = its index position
        std::unordered_map<int, int> seen_numbers;
        
        for (int i = 0; i < nums.size(); i++) {
            int current_num = nums[i];
            int complement = target - current_num; // What we need to find
            
            // Check if the complement is in our map
            if (seen_numbers.count(complement) > 0) {
                // Found it! Return the stored index and the current index
                return {seen_numbers[complement], i};
            }
            
            // Otherwise, remember this number and its position for later
            seen_numbers[current_num] = i;
        }
        
        return {}; // Return empty if no answer found
    }
};