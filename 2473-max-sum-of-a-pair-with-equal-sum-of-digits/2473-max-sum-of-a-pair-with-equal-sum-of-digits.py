class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        sum_dict = {}
        for num in nums:
            sum_of_dig = 0
            for dig in str(num):
                sum_of_dig += int(dig) 
            if sum_of_dig not in sum_dict:
                sum_dict[sum_of_dig] = num
            else:
                res = max(res,sum_dict[sum_of_dig]+num)
                sum_dict[sum_of_dig] = max(sum_dict[sum_of_dig],num)

        return res
        