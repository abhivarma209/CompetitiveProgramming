# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def helper(targetSum,node,arr):
            arr.append(node.val)
            if node.left is None and node.right is None:
                if node.val == targetSum:
                    self.res.append(arr)
                return
            if node.left:
                helper(targetSum-node.val,node.left,arr.copy())
            if node.right:
                helper(targetSum-node.val,node.right,arr.copy())
            arr.pop()
            return
        helper(targetSum,root,[])
        return self.res

                