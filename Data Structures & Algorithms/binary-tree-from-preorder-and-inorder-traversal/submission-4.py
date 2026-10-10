# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val: i for i, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            mid = pos[root_val]
            root.left = build(lo, mid - 1)   # must build left first
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)