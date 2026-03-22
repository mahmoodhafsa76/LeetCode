class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101

        for h in heights:
            count[h] += 1

        expected_heights = []
        for num in range(len(count)):
            expected_heights.extend([num] * count[num])

        counter = 0
        for j in range(len(heights)):
            if expected_heights[j] != heights[j]:
                counter += 1 

        return counter