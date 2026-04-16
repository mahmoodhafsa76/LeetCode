class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left_zeros = [0] * (n)
        right_ones = [0] * (n)

        left_zeros[0] = 1 if s[0] =='0' else 0
        for i in range(1, n):
                left_zeros[i] = left_zeros[i - 1] + (1 if s[i] == '0' else 0)

        right_ones[-1] = 1 if s[-1] == '1' else 0
        for i in range(n - 2, -1, -1):
                right_ones[i] = right_ones[i + 1] + (1 if s[i] == '1' else 0)
        
        max_score = 0
        for i in range(1, n):
            max_score = max(max_score, left_zeros[i-1] + right_ones[i] )
        return max_score
