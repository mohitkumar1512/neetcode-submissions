class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # res = 0
        # curr = 0
        # for c in s:
        #     if c != ' ':
        #         curr += 1
        #     else:
        #         if curr: res = curr
        #         curr = 0
        # if curr: res = curr
        
        # return res
        return len(s.split()[-1])