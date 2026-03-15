class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set() #[1, 0, 1, 1]

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i-k])
        return False