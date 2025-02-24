class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res_nums = [0] * (n+1)
        for num in nums:
            res_nums[num] = 1
        return [i for i in range(1,n+1) if res_nums[i] == 0]