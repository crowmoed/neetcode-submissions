"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = []
        end = []    

        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start = sorted(start)
        end = sorted(end)


        count = 0
        max_count = 0

        end_i = 0
        start_i = 0

        while(start_i< len(start)):
            print(count)
            if start[start_i] >= end[end_i]:
                end_i+=1
                count-=1
                max_count = max(max_count,count)
            else:
                count+=1
                start_i+=1
                max_count = max(max_count,count)


        return max_count       


