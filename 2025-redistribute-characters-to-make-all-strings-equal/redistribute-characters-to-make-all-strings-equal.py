class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = defaultdict(int)
        
        for w in words:
            for c in w:
                char_count[c] += 1

        for key in char_count:
            if char_count[key] % len(words):
                return False
        return True

            