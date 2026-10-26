class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1 
        curr = 1
        prev = 0 

        for i in range(1,len(arr)): 
            if arr[i] > arr[i-1]: 
                sign = 1 
            
            elif arr[i] < arr[i-1]: 
                sign = - 1 
            
            else: 
                sign = 0 
        
            if sign == 0: 
                curr = 1 
            
            elif sign == -prev: 
                curr += 1 
            
            else: 
                curr = 2 
            
            prev = sign 
            best = max(best,curr)
        
        return best




            
