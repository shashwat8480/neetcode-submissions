class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0 

        for i in range(len(nums) + 1): 
            expected += 1 
        
        actual = sum(nums)
        
        return sum(range(expected)) - actual
        
        
        