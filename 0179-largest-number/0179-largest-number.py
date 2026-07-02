from functools import cmp_to_key
class Solution:
    def custome_sort_rule(self,a,b):
        str_a,str_b=str(a),str(b)
        if str_a+str_b > str_b+str_a:
            return -1
        else:
            return 1

    def sorted_approach(self,nums):
        sorted_numbers = sorted(nums,key=cmp_to_key(self.custome_sort_rule))
        res= ""
        for num in sorted_numbers:
            if len(res)==0 and num==0:
                continue
            res+=str(num)
        return res if res else "0"
    
    def larger(self,a,b):
        return str(a) + str(b) > str(b) + str(a)

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1,len(nums)):
            curr = nums[i]
            j=i-1
            while j>=0 and self.larger(curr,nums[j]):
                nums[j+1],nums[j]=nums[j],nums[j+1]
                j-=1
        res= ""
        for num in nums:
            if len(res)==0 and num==0:
                continue
            res+=str(num)
        return res if res else "0"