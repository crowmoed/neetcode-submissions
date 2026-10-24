class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found = {} 
        for i in nums:
            if i in found:
                found[i]+=1 
            else:
                found[i] =1
        retval = []
        x = k
        for i in reversed(sorted(found, key=lambda x:found[x])):
            if x==0:
                break   
            x-=1         
            retval.append(i)

        return retval
            
            
        