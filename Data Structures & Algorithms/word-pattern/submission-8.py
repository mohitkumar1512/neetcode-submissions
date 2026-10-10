class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern): return False
        
        mapPattern = {}
        seen = set()
        
        for p, w in zip(pattern, words):
            if p not in mapPattern:
                if w in seen: return False
                mapPattern[p] = w
                seen.add(w)
            elif mapPattern[p] != w:
                return False
        
        return True