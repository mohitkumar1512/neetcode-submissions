# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            def isSimilar(root, subRoot):
                if not subRoot and not root:
                    return True
                
                if (not subRoot and root) or (not root and subRoot) or subRoot.val != root.val:
                    return False
                
                return isSimilar(root.left, subRoot.left) and isSimilar(root.right, subRoot.right)
            if (isSimilar(root, subRoot)):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
