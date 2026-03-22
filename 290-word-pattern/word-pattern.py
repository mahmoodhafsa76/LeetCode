class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapSP, mapPS = {}, {}
        words = s.split()

        if len(words) == len(pattern):
            for c, w in zip(words, pattern):
            
                if ((c in mapSP and mapSP[c] != w) or (w in mapPS and mapPS[w] != c)):
                    return False
                mapSP[c] = w
                mapPS[w] = c

            return True
        
        else :
             return False