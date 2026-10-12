class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        start, max_len = i, j - i + 1

        return s[start:start + max_len]
        # res = ""

        # def expand(l, r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     return s[l + 1:r]   # last valid window

        # for i in range(len(s)):
        #     odd = expand(i, i)
        #     even = expand(i, i + 1)
        #     res = max(res, odd, even, key=len)

        # return res