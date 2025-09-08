class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,white,blue=0,0,0
        for num in nums:
            if num==0:
                red+=1
            elif num==1:
                white+=1
            else:
                blue+=1
        i=0
        for idx,color in enumerate([red,white,blue]):
            while color>0:
                nums[i]=idx
                i+=1
                color-=1
        return