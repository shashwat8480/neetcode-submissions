class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = {} #element : count

        for i in range(len(nums)): 
            count[nums[i]] = 1 + count.get(nums[i],0)
        
        result = []
        
        for i in sorted(count): 
            result.extend([i] * count[i])
        
        return result
