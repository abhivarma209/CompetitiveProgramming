class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write,read = 0,0
        while read<len(nums) and write<len(nums):
            if nums[write]==0 and nums[read]!=0:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
            elif nums[write]!=0:
                write+=1
            read+=1
        