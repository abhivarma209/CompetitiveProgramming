class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=dict()
        se=set(nums)
        for num in se:
            p_start = d[num-1][0] if num-1 in d else num
            s_end = d[num+1][1] if num+1 in d else num
            d[num] = [p_start,s_end]
            d[p_start][1] = d[s_end][1]
            d[s_end][0] = d[p_start][0]
        res=0
        for x,y in d.values():
            res=max(res,abs(y+1-x))
        return res
        # ans = 0
        # se = set(nums)
        # for s in se:
        #     if s-1 not in se:
        #         len = 1
                
        #         while s + len in se:
        #             len += 1
                
        #         ans = max(len, ans)
        # return ans