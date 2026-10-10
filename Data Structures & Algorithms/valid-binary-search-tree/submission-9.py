# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root or (not root.left and not root.right):
        #     return True
        
        
        # flag_left = False if root.left else True
        # flag_right = False if root.right else True
        # if root.left and root.val > root.left.val: 
        #     flag_left = self.isValidBST(root.left) 
        
        # if root.right and root.val < root.right.val:
        #     flag_right = self.isValidBST(root.right)
        
        # if flag_left and flag_right:
        #     return True
        # return False
  
        def validate(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return validate(node.left, min_val, node.val) and \
                   validate(node.right, node.val, max_val)
        
        return validate(root, float('-inf'), float('inf'))
