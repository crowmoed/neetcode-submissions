class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        stack =[]

        for index, H in enumerate(heights):
            r = 1

            for i in heights[index+1::]:
                if i >= H:
                    r+=1
                else:
                    break

            for i in reversed(heights[0:index:]):
                
                if i >= H:
                    r+=1
                else:
                    break
            stack.append( H * r)

        return max(stack)