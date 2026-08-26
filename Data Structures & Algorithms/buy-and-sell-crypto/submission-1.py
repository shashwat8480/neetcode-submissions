class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        mp = 0 

        for right in range(1,len(prices)): 
            if prices[left] > prices[right]: 
                left = right 
            
            else: 
                profit = prices[right] - prices[left]
                mp = max(mp,profit)

        return mp




        
        