class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if stack:
                if operations[i] == "+":
                    stack.append(stack[-2] + stack[-1])
                elif operations[i] == "C":
                    stack.pop()
                elif operations[i] == "D":
                    stack.append(int(stack[-1]) * 2)
                else:
                    stack.append(int(operations[i]))
            else:
                stack.append(int(operations[i]))
        
        return sum(stack)