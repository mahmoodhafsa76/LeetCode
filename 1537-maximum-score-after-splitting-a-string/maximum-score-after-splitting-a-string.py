class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_sum = 0
        for i in range(1, n):
            zeros = 0
            for j in range(0, i):
                if s[j] == '0':
                    zeros += 1

            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

            sum01 = zeros + ones
            max_sum = max(max_sum, sum01)
        return max_sum