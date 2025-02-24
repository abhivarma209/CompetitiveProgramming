class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        num_dict = {}
        for i,num in enumerate(temp):
            if num not in num_dict:
                num_dict[num] = i
        return [num_dict[num] for num in nums]
        