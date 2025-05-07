class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        res = []
        while l<=r:
            absl = abs(nums[l])
            absr = abs(nums[r])
            if absl>absr:
                res.append(absl**2)
                l+=1
            else:
                res.append(absr**2)
                r-=1
        return res[::-1]
        