class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = {} 
        maxSubStr = 0
        l, r = 0, 0
        while l < len(s) and r < len(s):
            if s[r] in subStr:
                l = max(subStr[s[r]] + 1, l)
        
            subStr[s[r]] = r
            maxSubStr = max(r - l + 1, maxSubStr)
            r += 1

        return maxSubStr