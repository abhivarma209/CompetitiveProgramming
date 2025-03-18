class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j,res = 0,0,0
        temp = 0
        while i<=j and j<len(nums):
            if nums[j] == 0:
                temp += 1
            while temp>k:
                if nums[i]==0:
                    temp-=1
                i+=1
            res = max(res,j+1-i)
            j+=1
        return res
            