from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        available = Counter(text)
        required = Counter('balloon')
        res = len(text)
        for char in required:
            res = min(res, available[char]//required[char])

        return res