class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        retval = [0] * len(temperatures)
        stack = []

        for index , temp in enumerate(temperatures):
            print(stack)
            print(retval)
            while len(stack)> 0 and stack[-1][0]< temp:
                a = stack.pop()
                retval[a[-1]] = index - a[-1]

            stack.append([temp,index])
            
        return retval
            


