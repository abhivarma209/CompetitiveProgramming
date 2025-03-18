class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res,curr = set(),set()
        for i in arr:
            if len(curr)>0:
                curr = {i|j for j in curr}
            curr.add(i)
            for e in curr:
                res.add(e)
        return len(res)
        