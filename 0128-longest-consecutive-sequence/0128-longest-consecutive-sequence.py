class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=dict()
        se=set(nums)
        arr=list(se)
        for num in arr:
            p_start = d[num-1][0] if num-1 in d else num
            s_end = d[num+1][1] if num+1 in d else num
            d[num] = [p_start,s_end]
            d[p_start][1] = d[s_end][1]
            d[s_end][0] = d[p_start][0]
        res=0
        for x,y in d.values():
            res=max(res,abs(y+1-x))
        return res
