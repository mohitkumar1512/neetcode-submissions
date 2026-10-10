# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        def dfs(currNode, currValue):
            if not currNode: return
            if not currNode.left and not currNode.right and currNode.val + currValue == targetSum:
                self.res = True
                return
            dfs(currNode.left, currNode.val + currValue)
            dfs(currNode.right, currNode.val + currValue)
        
        dfs(root, 0)
        return self.res
            
