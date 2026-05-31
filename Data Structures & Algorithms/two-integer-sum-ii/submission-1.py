class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            t = target-i
            if t != i and t in numbers:
                return [numbers.index(i)+1,numbers.index(t)+1]

