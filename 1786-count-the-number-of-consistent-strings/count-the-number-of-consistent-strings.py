class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_array = [False] * 26
        for c in allowed:
            allowed_array[ord(c) - ord('a')] = True                        

        res = len(words)
        for w in words:
            for c in w:
                if not allowed_array[ord(c) - ord('a')]:
                    res -= 1
                    break

        return res