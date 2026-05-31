class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0

        oscelate = False

        while left<right:
            y = min(heights[left],heights[right])

            x = right-left

            a = x * y

            if a > area:
                area = a

            if heights[left]> heights[right]:
                right-=1
            else:
                left+=1


        return area 
        