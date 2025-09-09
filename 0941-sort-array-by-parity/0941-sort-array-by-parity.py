class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left,right=0,len(nums)-1
        while left<right:
            if nums[left]%2==0:
                left+=1
            else:
                nums[right],nums[left]=nums[left],nums[right]
                right-=1
        return nums