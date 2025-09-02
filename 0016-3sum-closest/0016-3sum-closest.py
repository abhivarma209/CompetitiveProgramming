class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0]+nums[1]+nums[2]
        for i in range(n):
            j,k=i+1,n-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if abs(temp-target)<abs(res-target):
                    res = temp
                if temp==target:
                    return res
                elif temp<target:
                    j+=1
                else:
                    k-=1
        return res
