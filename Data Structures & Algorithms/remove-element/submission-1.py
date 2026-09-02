class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       
        #return the number of elements that are not equal to the value.
        #change the array -> all elements that are not equal to the value should be brought to the front. 

        k = 0 
        for i in range(len(nums)): 
            if nums[i] != val: 
                nums[k] = nums[i]
                k += 1 
        
        return k