class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for peak in range(1,n-1):
            if arr[peak-1]<arr[peak]>arr[peak+1]:
                l = r = peak
                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                while r<n-1 and arr[r+1]<arr[r]:
                    r+=1
                res = max(res,r-l+1)
        return res

           