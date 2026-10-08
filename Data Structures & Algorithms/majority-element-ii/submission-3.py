class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)

        for i in range(len(nums)): 
            count[nums[i]] = 1 + count.get(nums[i],0)
        
        result = []
        
        for num in count: 
            if count[num] > (n // 3) : 
                result.append(num)
        
        return result

    
        
