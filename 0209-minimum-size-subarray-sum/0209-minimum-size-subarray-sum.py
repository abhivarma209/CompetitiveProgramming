class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j,res,curr_sum=0,0,10**5+1,0
        while j<len(nums) or curr_sum>=target:
            if curr_sum<target:
                curr_sum+=nums[j]
                j+=1
            if curr_sum >= target:
                res = min(res,j-i)
                print(j,i)
                curr_sum-=nums[i]
                i+=1
        return res if res<10**5+1 else 0

        