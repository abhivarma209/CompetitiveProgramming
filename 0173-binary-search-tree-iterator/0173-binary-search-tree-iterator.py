# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # self.inorder,stack=[],[]
        # self.idx=0
        # node=root
        # while True:
        #     if node:
        #         stack.append(node)
        #         node=node.left
        #     else:
        #         if not stack:
        #             break
        #         top=stack.pop()
        #         self.inorder.append(top.val)
        #         node=top.right
        self.inorder,self.idx = [],0
        self.helper(root)

    def helper(self,root):
        if not root: return
        self.helper(root.left)
        self.inorder.append(root.val)
        self.helper(root.right)

    def next(self) -> int:
        temp=self.idx
        self.idx+=1
        return self.inorder[temp]

    def hasNext(self) -> bool:
        return False if self.idx>len(self.inorder)-1 else True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()