class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res_diff,res = float('inf'),nums[0]+nums[1]+nums[2]
        n = len(nums)
        nums.sort()
        for i in range(n):
            j,k=0,n-1
            while j<k:
                if i==j:
                    i+=1
                    continue
                if k==i:
                    k-=1
                    continue
                tri = nums[i]+nums[j]+nums[k]
                if tri==target:
                    return tri
                elif tri<target:
                    j+=1
                    if target-tri<res_diff:
                        res = tri
                        res_diff = target-tri
                else:
                    k-=1
                    if tri-target<res_diff:
                        res = tri
                        res_diff = tri-target
        return res
        