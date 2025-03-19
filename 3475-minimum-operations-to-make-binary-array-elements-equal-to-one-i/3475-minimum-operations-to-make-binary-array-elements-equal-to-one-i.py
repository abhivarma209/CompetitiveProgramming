class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if nums[i]==0:
                if i+1>=n or i+2>=n:
                    return -1
                nums[i+1] = 1 if nums[i+1]==0 else 0
                nums[i+2] = 1 if nums[i+2]==0 else 0
                res += 1
        return res