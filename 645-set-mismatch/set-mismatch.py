class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]  # [duplicate, missing]
        count = Counter(nums)

        for i in range(1, len(nums) + 1):
            if i not in count:
                result[1] = i

            if count[i] == 2:
                result[0] = i

        return result