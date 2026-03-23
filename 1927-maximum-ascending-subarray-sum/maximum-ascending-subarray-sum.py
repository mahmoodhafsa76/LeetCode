class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = cur_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                cur_sum = 0

            cur_sum += nums[i]
            res = max(cur_sum, res)

        return res
        