class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in nums:
            if (target-i) in seen:
                return [nums.index(target-i),nums.index(i,nums.index(target-i)+1)]
            seen[i] = True


        return []