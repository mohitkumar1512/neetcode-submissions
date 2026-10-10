class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        seen_vals = set()
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in seen_vals: return False  # two keys mapping to same value
                d[s[i]] = t[i]
                seen_vals.add(t[i])
            else:
                if d[s[i]] != t[i]: return False
        return True

            