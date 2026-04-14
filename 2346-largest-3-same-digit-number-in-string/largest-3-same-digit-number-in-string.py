class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(1, len(num) - 1):
            if num[i] == num[i+1] and num[i] == num[i-1]:
                candidate = num[i] * 3
                res = max(res, candidate )
        return res