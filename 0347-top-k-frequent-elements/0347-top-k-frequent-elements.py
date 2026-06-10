class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        heap,res = [],[]
        for key,val in d.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        for val,key in heap:
            res.append(key)
        return res