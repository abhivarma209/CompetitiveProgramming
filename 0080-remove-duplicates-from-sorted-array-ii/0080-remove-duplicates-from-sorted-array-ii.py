class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        write,read = 2,2
        for i in range(2,n):
            if nums[write-2]!=nums[i]:
                nums[write]=nums[i]
                write+=1
        return write
            