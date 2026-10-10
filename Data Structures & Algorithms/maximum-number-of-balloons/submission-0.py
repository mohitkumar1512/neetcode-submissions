class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = {'b':1, 'a' : 1, 'l' : 2, 'o' : 2, 'n' : 1}
        mapText = Counter(text)
        
        return min(mapText[c] // target[c] for c in target)