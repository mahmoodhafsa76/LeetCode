class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] *26
        n = len(words)
        
        for w in words:
            for c in w:
              freq[ord(c) - ord('a')]  += 1

        for count in freq:
            if count % n != 0:
                return False
        return True

            