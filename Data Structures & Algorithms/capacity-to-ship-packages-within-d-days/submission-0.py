class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right

        def canship(capacity): 
            ships = 1 
            currcap = capacity 

            for weight in weights: 
                if currcap - weight < 0: 
                    ships += 1 
                    currcap = capacity
                currcap -= weight
            
            return ships <= days

        while left <= right: 
            capacity = (left + right) // 2 

            if canship(capacity): 
                res = min(res,capacity)
                right = capacity - 1 
            
            else : 
                left = capacity + 1 
        
        return res 
