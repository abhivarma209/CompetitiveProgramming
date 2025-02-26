class Solution:
    def maxPosSum(self,nums: List[int]) -> int:
        temp_sum = 0
        max_sum = [float(-inf)]* len(nums)
        for i,num in enumerate(nums):
            if num+temp_sum < 0:
                max_sum[i] = temp_sum
                temp_sum = 0
            else:
                max_sum[i] = max(temp_sum+num,num)
                temp_sum = max(temp_sum+num,num)
        return  max(max_sum)
            
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        neg_nums = [-num for num in nums]
        return max(self.maxPosSum(nums),self.maxPosSum(neg_nums))
        