class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # O(n log k)
        # s1 = sorted(s1)
        # l = 0
        # r = len(s1)
        # while r <= len(s2):
        #     substr = sorted(s2[l:r])
        #     if substr == s1: 
        #         return True
        #     l += 1
        #     r += 1
        # return False

        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if window == need:
                return True

        return False