class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # We will follow a similar pattern for subsequence here 
        # and instead of checking if its a subsequence 
        # we need to count how many letters are already here for it to be a subsequence

        i = 0 
        j = 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                j += 1
            i += 1
        
        return len(t) - j