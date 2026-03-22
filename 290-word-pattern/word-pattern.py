class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapSP, mapPS = {}, {}
        s = s.split()

        if len(s) == len(pattern):
            for c1, c2 in zip(s, pattern):
            
                if ((c1 in mapSP and mapSP[c1] != c2) or (c2 in mapPS and mapPS[c2] != c1)):
                    return False
                mapSP[c1] = c2
                mapPS[c2] = c1

            return True
        
        else :
             return False