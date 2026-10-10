class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        res = set()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]: 
                    res.add(words[i])
                    break
        return list(res)
            