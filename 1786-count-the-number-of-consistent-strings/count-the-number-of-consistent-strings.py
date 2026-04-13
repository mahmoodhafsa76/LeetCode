class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bitmask = 0
        for char in allowed:
            bitmask = bitmask | (1 << (ord(char) - ord('a')))

        res = len(words)
        for word in words:
            for w in word:
                bit_pos = 1 <<  (ord(w) - ord('a'))
                if bit_pos & bitmask == 0:
                    res -= 1
                    break

        return res