class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j,res = 0,0,0
        temp = k
        while i<=j and j<len(nums):
            if nums[j] == 0:
                if temp>0:
                    temp-=1
                else:
                    if nums[i] == 0 and temp<k:
                        temp+=1
                    if i==j:
                        j+=1
                    i+=1
                    continue
            res = max(res,j+1-i)
            j+=1
        return res
            