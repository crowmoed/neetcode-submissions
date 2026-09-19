"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for index,insert_interval in enumerate(intervals):
            s = insert_interval.start
            e = insert_interval.end
            for index_,interval_check in enumerate(intervals):
                if index == index_:
                    continue    
                a = interval_check.start
                b = interval_check.end
                if (s>=a and s<b) or  (e<=a and e>=b):
                    return False

        return True
            
