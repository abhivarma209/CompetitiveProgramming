class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n
        write,read = 2,2
        while read<n and write<n:
            if nums[read]>nums[write]:
                nums[write],nums[read]=nums[read],nums[write]
            if not (nums[write-2]==nums[write-1]==nums[write] or nums[write-1]>nums[write]):
                write += 1
                continue
            while read<n and nums[read]<=nums[write]:
                read+=1
        return write
            