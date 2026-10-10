class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 201            
        for s in strs:
            minLength = min(len(s), minLength)
        
        res = ""
        for i in range(minLength):
            first = strs[0][i]
            for j in range(1, len(strs)):
                if first != strs[j][i]: 
                    return res
            res += first
        return res