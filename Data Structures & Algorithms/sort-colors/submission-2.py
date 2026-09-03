class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)

        nums[:red] = [0] * red 
        nums[red:red+white] = [1] * white 
        nums[red+white :] = [2] * blue
