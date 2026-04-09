class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        res = True
        i = 0
        while i < n:
            num = nums.count(nums[i])
            if (num & 1) == 1:
                res = False

            i += num 

        return res