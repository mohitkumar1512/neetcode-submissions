class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # words.sort(key=lambda x: len(x))
        # res = []
        # for i in range(len(words)):
        #     for j in range(i + 1, len(words)):
        #         if words[i] in words[j]: 
        #             res.append(words[i])
        #             break
        # return res
        # intuition: if a word appears more than once in the combined string, we know it's a subst
        res = []
        joined = " ".join(words)
        for w in words:
            if joined.count(w) > 1:
                res.append(w)
        return res
            