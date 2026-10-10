class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        subStr = {} 
        maxSubStr = 0
        l, r = 0, 1
        subStr[s[l]] = l
        while r < len(s):
            while s[r] in subStr:
                subStr.pop(s[l])
                l += 1
        
            subStr[s[r]] = r
            maxSubStr = max(r - l + 1, maxSubStr)
            r += 1

        return maxSubStr