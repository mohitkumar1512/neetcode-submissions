class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parenthesis = {")":"(","]":"[","}":"{"}
        open_p = "([{"
        for c in s:
            if c in open_p:
                stack.append(c)
            else: 
                if not stack or parenthesis[c] != stack.pop():
                    return False
        return False if len(stack) else True