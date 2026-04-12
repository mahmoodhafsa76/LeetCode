class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = Counter(chars)
        res = 0
        
        for i in range(len(words)):
            word_map = Counter(words[i])
            for c in word_map:
                if word_map[c] > char_map[c]: 
                    good = False
                    break

                else:
                    good = True

            if good:
                res += len(words[i])

        return res