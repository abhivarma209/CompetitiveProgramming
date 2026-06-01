# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def memoize_rob(self, root, res_dict):
        if not root: return 0
        if res_dict.get(root): return res_dict[root]
        res=0
        if root.left:
            res+=self.memoize_rob(root.left.left,res_dict)+self.memoize_rob(root.left.right,res_dict)
        if root.right:
            res+=self.memoize_rob(root.right.left,res_dict)+self.memoize_rob(root.right.right,res_dict)
        res = max(res+root.val, self.memoize_rob(root.left,res_dict)+self.memoize_rob(root.right,res_dict))
        res_dict[root]=res
        return res

    def rob(self, root: Optional[TreeNode]) -> int:
        return self.memoize_rob(root,{})
        
