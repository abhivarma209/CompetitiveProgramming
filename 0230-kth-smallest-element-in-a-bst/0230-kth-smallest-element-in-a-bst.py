# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder,stack=[],[]
        node = root
        while True:
            if node:
                stack.append(node)
                node=node.left
            else:
                top=stack.pop()
                inorder.append(top.val)
                node=top.right
                if len(inorder)==k:
                    return top.val
        return inorder[-1]