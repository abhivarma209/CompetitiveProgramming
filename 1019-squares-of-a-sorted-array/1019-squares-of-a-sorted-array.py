class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pivot = -1
        low = float("inf")
        for i,num in enumerate(nums):
            if abs(num)<low:
                low = abs(num)
                pivot = i
        i,j=pivot,pivot+1
        res = []
        n = len(nums)
        while i>=0 or j<n:
            if j==n:
                res.append(nums[i]**2)
                i-=1
                continue
            if i==-1:
                res.append(nums[j]**2)
                j+=1
                continue
            if abs(nums[i])<abs(nums[j]):
                res.append(nums[i]**2)
                i-=1
            else:
                res.append(nums[j]**2)
                j+=1
        return res
                 