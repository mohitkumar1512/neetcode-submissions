class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_s = set()
        res = 0
        l = 0
        for r, c in enumerate(s):

            while c in s_s:
                s_s.remove(s[l])
                l += 1
            s_s.add(c)
            res = max(res, r - l + 1)
        return res
            