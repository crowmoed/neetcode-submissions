class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1
        i = int((len(nums)-1)/2)
        iteration = i/2
        count = 0
        while(i< len(nums) and count< len(nums)):
            compare_val = nums[i]  
            if compare_val == target: 
                return i
            elif compare_val< target:
                if (i == 0):
                    i = 1
                i = i + int(iteration+.5)
            else:
                i = i - int(iteration+.5)

            iteration = iteration/2 +.5
            count+=1
        
        return -1