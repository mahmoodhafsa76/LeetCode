class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = self.counting(s)   # total ones
        res = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1

            res = max(res, zero + one)

        return res

    def counting(self, arr):
        count = 0
        for n in arr:
            if n == '1':
                count += 1
        return count