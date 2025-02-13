class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        left_nums = [num for num in nums if num<k]
        heapify(left_nums)
        res= 0
        while len(left_nums)>0:
            res+=1
            if len(left_nums) == 1:
                return res
            smallest = heappop(left_nums)
            second_smallest = heappop(left_nums)
            new_val = min(smallest,second_smallest)*2 + max(smallest,second_smallest)
            if new_val<k:
                heappush(left_nums,new_val)
        return res