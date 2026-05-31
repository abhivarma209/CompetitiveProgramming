# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isInvertedSame(self, a:Optional[TreeNode], b:Optional[TreeNode]) -> bool:
        if not a and not b: return True
        if a and not b: return False
        if not a and b: return False
        if a.val != b.val: return False
        return self.isInvertedSame(a.left,b.right) and self.isInvertedSame(a.right,b.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isInvertedSame(root.left,root.right)