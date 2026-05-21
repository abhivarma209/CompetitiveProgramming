class Solution:
    def mySqrt(self, x: int) -> int:
        lo,hi=0,x//2
        while lo<=hi:
            mid =(hi+lo)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                lo=mid+1
            else:
                hi=mid-1
        return lo-1 if lo*lo>x else lo