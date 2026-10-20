class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minL = len(min(strs, key=len)) 
        res = []
        for i in range(minL):
            first = strs[0][i]
            for j in range(1, len(strs)):
                if first != strs[j][i]:
                    return ''.join(res)
            res.append(first)
        return ''.join(res)
