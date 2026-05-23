class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        seen = {}

        for i in nums:
            seen[i] = True
        
        def findlonginnums_ (x):
            if (x+1) in seen:
                return findlonginnums_(x+1)+1
            else:
                return 1
        
        
        max = 1
        for i in nums:
            val = findlonginnums_(i)
            if val > max:
                max =val

        return max