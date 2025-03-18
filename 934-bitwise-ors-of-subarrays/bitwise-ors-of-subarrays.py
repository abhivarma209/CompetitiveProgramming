class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res,curr = set(),set()
        for i in arr:
            temp = set()
            for e in curr:
                temp.add(e|i)
                res.add(e|i)
            temp.add(i)
            res.add(i)
            curr=temp
        return len(res)
        