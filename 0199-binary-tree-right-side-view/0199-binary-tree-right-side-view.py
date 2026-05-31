# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q=deque([root])
        res=[]
        while q:
            le,ri=len(q),None
            for _ in range(le):
                temp = q.popleft()
                ri=temp.val
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
            res.append(ri)
        return res