class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> nums_count;

        for (int i = 0; i < nums.size(); i++){
            int val = nums[i];
            if (nums_count.contains(target-val)){
                return {nums_count[target-val],i};
                }
            nums_count[val] = i;
        }

    }
};
