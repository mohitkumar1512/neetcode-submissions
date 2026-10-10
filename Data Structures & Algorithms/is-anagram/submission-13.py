class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = [0] * 26
        t_c = [0] * 26
        for c in s: 
            s_c[ord(c) - ord('a')] += 1
        
        for c in t: 
            t_c[ord(c) - ord('a')] += 1

        return t_c == s_c