class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority = 0 
        count = 0 

        for n in nums:
            if count == 0:
                majority = n
            if n == majority:
                count += 1
            else:
                count -= 1

        left_count = 0
        right_count = nums.count(majority)

        for i in range(len(nums)):
            if nums[i] == majority:
                left_count += 1
                right_count -= 1
            left_len = i+1
            right_len = len(nums) - i - 1
            if  left_count > left_len//2 and right_count > right_len//2:
                return i

        return -1