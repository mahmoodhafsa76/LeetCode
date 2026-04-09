class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1

        res = True

        for val in count.values():
            if val & 1 == 1:
                res = False

        return res
            