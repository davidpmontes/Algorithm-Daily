from operator import itemgetter

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if intervals == None or len(intervals) < 2:
            return True
        
        intervals.sort(key=itemgetter(1))
        
        endTime = -1
        for interval in intervals:
            if endTime > interval[0]:
                return False
            else:
                endTime = interval[1]
        return True
