class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        write = 2
        for read in range(2,n):
            if nums[write-2]!=nums[read]:
                nums[write]=nums[read]
                write+=1
        return write
            