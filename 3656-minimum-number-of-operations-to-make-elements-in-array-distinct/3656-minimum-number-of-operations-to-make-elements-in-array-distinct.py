class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if d.get(num) is None:
                d[num] = 0
            d[num] += 1
        i,res,n=0,0,len(nums)
        while i<n:
            if  n-i == len(d):
                return res
            for _ in range(3):
                if i<n:
                    d[nums[i]] -= 1
                    if d[nums[i]]==0:
                        del d[nums[i]]
                i+=1
            res += 1
        return res
