class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> nums_count;

        for (int i = 0; i < nums.size(); i++){
            if (nums_count.contains(target-nums[i])){
                return {nums_count[target-nums[i]],i};
                }
            nums_count[nums[i]] = i;
        }
        return {0,0};
    }
};
