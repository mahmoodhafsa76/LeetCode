class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_map = set(allowed)
        res = len(words)

        for word in words:
            for w in word:
                if w not in  allowed_map:
                    res -= 1
                    break

        return res
        