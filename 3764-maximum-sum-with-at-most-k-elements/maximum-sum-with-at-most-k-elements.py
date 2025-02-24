class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        result = []
        for i,row in enumerate(grid):
            limit = limits[i]
            temp_row = heapq.nlargest(limit,row)
            result.extend(temp_row)
        res = heapq.nlargest(k,result)
        return sum(res)
            
                
                
        