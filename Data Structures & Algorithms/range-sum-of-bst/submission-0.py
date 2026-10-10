# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sumV = 0
        def dfs(node):
            if not node: return
            if node.val <= high and node.val >= low:
                self.sumV += node.val
            dfs(node.right)
            dfs(node.left)
        
        dfs(root)
        
        return self.sumV