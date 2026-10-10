class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                leftOp = stack.pop()
                rightOp = stack.pop()
                stack.append(leftOp + rightOp)
            
            elif token == "*":
                leftOp = stack.pop()
                rightOp = stack.pop()
                stack.append(leftOp * rightOp)

            elif token == "-":
                leftOp = stack.pop()
                rightOp = stack.pop()
                stack.append(rightOp - leftOp)
            
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else: 
                stack.append(int(token))

        return stack[0]
       
       
       
       
        # stack = []
        # for c in tokens:
        #     if c == "+":
        #         stack.append(stack.pop() + stack.pop())
        #     elif c == "-":
        #         a, b = stack.pop(), stack.pop()
        #         stack.append(b - a)
        #     elif c == "*":
        #         stack.append(stack.pop() * stack.pop())
        #     elif c == "/":
        #         a, b = stack.pop(), stack.pop()
        #         stack.append(int(float(b) / a))
        #     else:
        #         stack.append(int(c))
        # return stack[0]