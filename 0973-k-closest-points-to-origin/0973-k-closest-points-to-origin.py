class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap,res = [],[]
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap,(-distance,point))
            if len(heap)>k:
                heapq.heappop(heap)
        for distance,point in heap:
            res.append(point)
        return res