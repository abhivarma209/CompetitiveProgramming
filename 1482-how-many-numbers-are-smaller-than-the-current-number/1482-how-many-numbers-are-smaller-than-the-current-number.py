class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mv = max(nums)
        check = [0] * (mv+1)
        for num in nums:
            check[num] += 1
        cum_sum = 0
        for i,c_sum in enumerate(check):
            cum_sum += c_sum
            check[i] = cum_sum
        return [check[num-1] if num != 0 else 0 for num in nums]
        