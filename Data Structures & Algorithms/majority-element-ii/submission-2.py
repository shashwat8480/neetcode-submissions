class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {} 

        for num in nums: 
            count[num] = 1 + count.get(num,0)
        
        result = [] 
        n = len(nums)

        for num in count: 
            if count[num] > ( n // 3): 
                result.append(num)

        return result 
        
