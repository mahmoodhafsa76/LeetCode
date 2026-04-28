class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [0, 1]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                result[0] = nums[i]

            if nums[i] - nums[i - 1] == 2:
                result[1] = nums[i] - 1

        if nums[-1] != len(nums):
            result[1] = len(nums)
        return result
