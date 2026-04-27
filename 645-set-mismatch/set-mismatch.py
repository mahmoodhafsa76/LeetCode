class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]  # [duplicate, missing]

        for num in nums:
            num = abs(num)
            nums[num - 1] *= -1
            if nums[num - 1] > 0:
                result[0] = num


        for i, num in enumerate(nums):
            if num > 0 and i + 1 != result[0]:
                result[1] = i + 1
                return result 