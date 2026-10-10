class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapPattern = defaultdict(str)
        sList = s.split()
        seen = set()
        if len(sList) == len(pattern):
            for i in range(len(pattern)):
                if pattern[i] not in mapPattern and sList[i] in seen: return False
                if pattern[i] not in mapPattern:
                    mapPattern[pattern[i]] = sList[i]
                    seen.add(sList[i])
                else:
                    if mapPattern[pattern[i]] != sList[i]: return False
            return True
        return False