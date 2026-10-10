class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if stack:
                curr = operations[i]
                if curr == "+":
                    new = 0
                
                    new += int(stack[-1])
                    new += int(stack[-2])
                    stack.append(int(new))
                elif curr == "C":
                    stack.pop()
                elif curr == "D":
                    last = stack[-1]
                    stack.append(int(last) * 2)
                else:
                    stack.append(int(operations[i]))


            else:
                stack.append(int(operations[i]))
        
        return sum(stack)