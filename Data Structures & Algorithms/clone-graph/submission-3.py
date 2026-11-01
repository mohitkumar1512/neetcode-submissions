"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        clones = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()                 # pop() instead of popleft()
            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)  # create clone on push
                    stack.append(nei)
                clones[curr].neighbors.append(clones[nei])

        return clones[node]