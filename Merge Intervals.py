### 56, merge intervals
        
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
        # idea, merge intervals based on start side; loop intervals, compare pre.end with curr.start, if
        # overlap, curr.end = max(curr.end, pre.end); no overlap, append curr to res. O(nlogn) time, O(1) space
        # corner case
        if not intervals:
            return []
        # merge
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]] # intialize res
        for i in range(1, len(intervals)):
            curr = intervals[i]
            pre = res[-1] # is the pre intervals
            if pre.end >= curr.start: # overlap
                curr.end = max(curr.end, pre.end)
            else:
                res.append(curr)
        return res

