class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) -1, -1, -1):
            if length and s[i] == ' ':
                return length
            elif s[i] != ' ':
                length += 1
        
        
        return length
        # return len(s.split()[-1])