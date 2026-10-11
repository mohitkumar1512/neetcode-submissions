"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: return None
        new_node = Node(node.val)
        

        q = deque()
        visited = {node: new_node}
        q.append(node)
        while q: 
            curr_node = q.popleft()
            node_copy = visited[curr_node]
            for nei in curr_node.neighbors:
                if nei not in visited: 
                    visited[nei] = Node(nei.val)   # CHANGED: store the clone so we can reuse it
                    q.append(nei)
                node_copy.neighbors.append(visited[nei])
                    
        return new_node