class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr = 0
        for i in range(len(s) -1, -1, -1):
            if curr and s[i] == ' ':
                return curr
            elif s[i] != ' ':
                curr += 1
        
        
        return curr
        # return len(s.split()[-1])