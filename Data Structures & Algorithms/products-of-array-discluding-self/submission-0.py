class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_combo= [1]* len(nums)
        
        x = 1
        for index , y in enumerate(nums):
            left_combo[index] = x 
            x= x * y
        
        right_combo= [1]* len(nums)
        
        x = 1
        for index , y in enumerate(reversed(nums)):
            right_combo[index] = x 
            x= x * y
        
        retval = [1]*len(nums)

        for i in range(len(retval)):
            retval[i] = right_combo[len(right_combo)- i-1]* left_combo[i]

        return retval

