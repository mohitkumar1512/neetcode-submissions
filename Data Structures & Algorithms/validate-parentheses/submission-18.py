class Solution:
    def isValid(self, s: str) -> bool:
        parans = {'}':'{', ')':'(', ']':'['}
        stack = []
        for p in s: 
            
            if p in parans.values():
                stack.append(p)
            else: 
                if not stack or stack.pop() != parans[p]:
                    return False
        return True if not stack else False