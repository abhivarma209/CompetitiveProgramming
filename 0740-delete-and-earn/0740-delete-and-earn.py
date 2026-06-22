class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)
        houses = [0] * (n+1)
        for num in nums:
            houses[num]+=num
        first,second=0,houses[0]
        res=houses[0]
        for i in range(1,n+1):
            first,second=second,max(first+houses[i],second)
            res=max(res,second)
        return res