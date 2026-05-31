# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        res,res_level,level=float('-inf'),1,1
        while q:
            le,add=len(q),0
            for _ in range(le):
                temp = q.popleft()
                add+=temp.val
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
            if res<add:
                res=add
                res_level=level
            level+=1
        return res_level