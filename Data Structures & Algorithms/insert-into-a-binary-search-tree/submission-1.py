# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root, val):
            if not root:
                return
            
            if val > root.val and root.right:
                insert(root.right, val)
            elif val > root.val and not root.right:
                root.right = TreeNode(val)
                
            if val < root.val and root.left:
                insert(root.left, val)
            elif val < root.val and not root.left:
                root.left = TreeNode(val)
        insert(root, val)
        if not root:
            root = TreeNode(val)
        return root