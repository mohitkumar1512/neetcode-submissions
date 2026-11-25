class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {"]":"[", ")":"(", "}":"{"}

        stack = []
        for c in s:
            if c in p_map.values():
                stack.append(c)
            else: 
                if not stack or stack.pop() != p_map[c]:
                    return False
        return True if not stack else False
