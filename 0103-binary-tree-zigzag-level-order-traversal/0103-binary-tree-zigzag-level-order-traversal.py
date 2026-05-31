# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q,res,rev=deque([root]),[],False
        while q:
            le,temp=len(q),[]
            for _ in range(le):
                left = q.popleft()
                temp.append(left.val)
                if left.left: q.append(left.left)
                if left.right: q.append(left.right)
            if rev:
                temp=temp[::-1]
            res.append(temp)
            rev = not rev
        return res 
