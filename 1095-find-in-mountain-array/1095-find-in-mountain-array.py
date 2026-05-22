# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findPeak(self,mountainArr: 'MountainArray') -> int:
        lo,hi=1,mountainArr.length()-2
        while lo<hi:
            mid=(lo+hi)//2
            if mountainArr.get(mid-1)<mountainArr.get(mid):
                lo=mid+1
            else:
                hi=mid-1
        return lo
    
    def search(self,mountainArr:'MountainArr',target: int, lo: int, hi: int) -> int:
        is_asc = mountainArr.get(lo)<mountainArr.get(hi)
        while lo<=hi:
            mid = (lo+hi)//2
            if mountainArr.get(mid)==target:
                return mid
            if is_asc:
                if target<mountainArr.get(mid):
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if target<mountainArr.get(mid):
                    lo=mid+1
                else:
                    hi=lo-1
        return -1
    
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak = self.findPeak(mountainArr)
        left_search = self.search(mountainArr,target,0,peak)
        if left_search != -1:
            return left_search
        right_search = self.search(mountainArr,target,peak,mountainArr.length()-1)
        return right_search