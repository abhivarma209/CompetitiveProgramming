# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.arr=[]
        def helper(node,res:str):
            if not node: return
            res+="->"
            res+=str(node.val)
            if not node.left and not node.right:
                self.arr.append(res[2:])
                return
            helper(node.left,res)
            helper(node.right,res)
        helper(root,"")
        return self.arr