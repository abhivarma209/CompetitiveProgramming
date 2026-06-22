class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        houses = [0] * 10001
        for num in nums:
            houses[num]+=num
        first,second=0,houses[0]
        res=houses[0]
        for i in range(1,10001):
            first,second=second,max(first+houses[i],second)
            res=max(res,second)
        return res