from _heapq import heappushpop
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        retVal = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while((stack) and stack[-1][0]<t):
                retVal[stack[-1][1]] = i-stack[-1][1]
                stack.pop()
            stack.append([t,i])
        return retVal