class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        increasing = True

        for i in range(1, n):
            if nums[i] < nums[i-1]:
                increasing = False

        if increasing:
            return increasing

        decreasing = True
        for i in range(1, n):
            if nums[i] > nums[i -1]:
                decreasing = False

        return decreasing 
        