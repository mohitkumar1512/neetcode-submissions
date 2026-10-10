class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s_s = set()
        # res = 0
        # l = 0
        # for r, c in enumerate(s):

        #     while c in s_s:
        #         s_s.remove(s[l])
        #         l += 1
        #     s_s.add(c)
        #     res = max(res, r - l + 1)
        # return res

        char_index = {}
        res = 0
        l = 0
        
        for r, c in enumerate(s):
            # If c was seen inside the current window [l, r]
            if c in char_index and char_index[c] >= l:
                l = char_index[c] + 1
            
            char_index[c] = r
            res = max(res, r - l + 1)
            
        return res            