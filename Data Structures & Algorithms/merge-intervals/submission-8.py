class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        start = None
        end = None
        retval = []
        for i in sorted(intervals,key= lambda x: x[0]):
            print(i)
            if start is None:
                start= i[0]
                end= i[1]
            else:
                if i[0]>end:
                    retval.append([start,end])
                    end = i[1]
                    start = i[0]
                else:
                    
                    start = min(i[0],start)
                    end = max(i[1],end)

        if not (start is None) :
            retval.append([start,end])
        return retval