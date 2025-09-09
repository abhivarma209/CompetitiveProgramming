class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        high=len(nums)-1
        i=0
        while i<high:
            if nums[i]%2==0:
                i+=1
            else:
                nums[high],nums[i]=nums[i],nums[high]
                high-=1
        return nums