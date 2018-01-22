# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 0:
            return []
        
        intervals.sort(key=lambda x: x.start)
        
        included = [True for _ in range(len(intervals))]
        prev = intervals[0]
        for idx, interval in enumerate(intervals[1:]):
            if interval.start <= prev.end:
                if interval.end > prev.end:
                    prev.end = interval.end
                included[idx + 1] = False
            else:
                prev = interval
                
        merged = []
        for idx, interval in enumerate(intervals):
            if included[idx]:
                merged.append(interval)
                
        return merged