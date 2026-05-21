class Solution:
    def hoursTook(cls,piles: List[int], speed: int) -> int:
        return sum(math.ceil(p/speed) for p in piles)
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res=hi
        while lo<=hi:
            mid = (lo+hi)//2
            hours = self.hoursTook(piles,mid)
            if hours<=h:
                res=min(res,mid)
                hi = mid-1
            else:
                lo = mid+1
        return res
