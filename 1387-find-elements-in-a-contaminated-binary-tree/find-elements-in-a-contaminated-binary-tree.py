# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def helper(self,rootVal: int,root: Optional[TreeNode],arr: Optional[List[int]]):
        root.val = rootVal
        arr.append(rootVal)
        if root.left is not None:
            self.helper(2*rootVal+1,root.left,arr)
        if root.right is not None:
            self.helper(2*rootVal+2,root.right,arr)
        return arr

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.helper(0,root,self.arr)

    def find(self, target: int) -> bool:
        if target in self.arr:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)