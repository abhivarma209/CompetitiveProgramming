# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.arr = []
        def helper(node,res):
            if not node: return
            char = chr(ord('a')+node.val)
            res=char+res
            if not node.left and not node.right:
                self.arr.append(res)
            helper(node.left,res)
            helper(node.right,res)
        helper(root,"")
        if not self.arr: return ""
        return min(self.arr)