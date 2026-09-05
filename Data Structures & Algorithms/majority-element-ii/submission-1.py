class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {} 

        for i in range(len(nums)): 
            count[nums[i]] = 1 + count.get(nums[i],0)
        
        res = [] 
        
        for num in count: 
            if count[num] > len(nums) // 3: 
                res.append(num) 
        
        return res

   
