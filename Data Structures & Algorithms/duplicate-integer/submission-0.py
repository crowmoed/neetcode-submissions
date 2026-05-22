class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_dict= {}
        for i in nums:
            if i in seen_dict:
                return True
            seen_dict[i] = 0

        return False
        