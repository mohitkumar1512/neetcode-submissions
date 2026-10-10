# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: An empty tree cannot contain any non-empty subRoot
        if not root:
            return False
        
        # Check if the tree rooted at the current node is identical to subRoot
        if self.isSameTree(root, subRoot):
            return True
            
        # If not, look for the subRoot in the left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are empty, they are the same
        if not p and not q:
            return True
        # If only one is empty, or values don't match, they aren't the same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
