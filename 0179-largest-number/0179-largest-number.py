from functools import cmp_to_key
class Solution:
    def custome_sort_rule(self,a,b):
        str_a,str_b=str(a),str(b)
        if str_a+str_b > str_b+str_a:
            return -1
        else:
            return 1
        
    def largestNumber(self, nums: List[int]) -> str:
        sorted_numbers = sorted(nums,key=cmp_to_key(self.custome_sort_rule))
        res= ""
        for num in sorted_numbers:
            if len(res)==0 and num==0:
                continue
            res+=str(num)
        return res if res else "0"