class Solution:
    def isValid(self, s: str) -> bool:
        # # have to use stack
        # stack = []

        # # we will keep a dictionary to map paranthesis
        # hashMap = {')':'(', '}':'{', ']':'['}

        # for char in s:
        #     if char in hashMap:
        #         if stack and hashMap[char] == stack[-1]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(char)
        
        # if len(stack):
        #     return False
        # return True


        stack = []

        mapBrackets = {')' : '(', ']' : '[', '}' : '{'}        

        for char in s:
            if char in mapBrackets:
                if stack and mapBrackets[char] == stack[-1]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)
        if stack: return False
        return True
