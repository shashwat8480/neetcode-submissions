class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() 

        res = [intervals[0]]

        for i in range(1,len(intervals)): 
            last = res[-1]
            current = intervals[i]

            if current[0] <= last[1]: 
                if current[1] > last[1]: 
                    last[1] = current[1]

            else: 
                res.append(current)

        return res        
