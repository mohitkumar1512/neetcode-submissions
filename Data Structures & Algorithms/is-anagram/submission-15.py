class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        for c in s:
            freq_s[ord(c) - ord('a')] += 1

        
        for c in t:
            freq_t[ord(c) - ord('a')] += 1

        return freq_t == freq_s
        