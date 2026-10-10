class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == "+":
                stack.append(stack.pop() + stack.pop())
            elif tok == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a) 
            elif tok == "*":
                stack.append(stack.pop() * stack.pop())
            elif tok == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))        
            else:
                stack.append(int(tok))        
            
        return stack[0]