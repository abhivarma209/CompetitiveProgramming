class Solution:
    def helper(self,nums,target) -> int:
        n = len(nums)
        count = nums.count(target)
        if count==0 or count == n:
            return 0
        
        curr_count = 0
        res = 100001
        
        for i in range(count):
            if nums[i] == target:
                curr_count += 1
        
        res = min(res,count-curr_count)
        for i in range(count,n):
            if nums[i-count] == target:
                curr_count -= 1
            if nums[i] == target:
                curr_count += 1
            print(i,curr_count)
            res = min(res,count-curr_count)

        return res


    def minSwaps(self, nums: List[int]) -> int:
        return min(self.helper(nums,1),self.helper(nums,0))