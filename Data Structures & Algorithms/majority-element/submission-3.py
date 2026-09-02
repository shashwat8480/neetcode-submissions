class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {} # element : count 
        n = len(nums) // 2 

        for i in range(len(nums)): 
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for num in nums: 
            if hashmap[num] > n: 
                return num 