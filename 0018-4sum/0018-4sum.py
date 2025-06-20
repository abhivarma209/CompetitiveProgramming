class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                l,r = j+1,n-1
                while l<r:
                    tri = nums[i]+nums[j]+nums[l]+nums[r]
                    if tri<target:
                        l+=1
                    elif tri>target:
                        r-=1
                    else:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
        result = []
        for tup in res:
            result.append(list(tup))
        return result

        