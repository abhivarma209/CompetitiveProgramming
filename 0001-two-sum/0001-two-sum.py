class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict =  {num:i for i,num in enumerate(nums)}
        for i,num in enumerate(nums):
            check = target-num
            res = nums_dict.get(check,-1)
            if res == i or res == -1:
                continue
            else:
                return [i,res]