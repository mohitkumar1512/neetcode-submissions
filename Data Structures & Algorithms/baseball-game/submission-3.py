class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if stack:
                curr = operations[i]
                if curr == "+":
                    stack.append(stack[-2] + stack[-1])
                elif curr == "C":
                    stack.pop()
                elif curr == "D":
                    stack.append(int(stack[-1]) * 2)
                else:
                    stack.append(int(operations[i]))
            else:
                stack.append(int(operations[i]))
        
        return sum(stack)