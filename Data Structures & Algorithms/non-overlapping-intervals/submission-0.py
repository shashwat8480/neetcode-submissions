class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0 

        curr = intervals[0]
        for i in range(1,len(intervals)): 
            if intervals[i][0] < curr[1]: 
                count += 1 
                if intervals[i][1] < curr[1]: 
                    curr = intervals[i]
            else: 
                curr = intervals[i]

        return count 