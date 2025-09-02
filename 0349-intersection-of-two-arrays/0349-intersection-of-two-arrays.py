class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i,j=0,0
        m,n=len(nums1),len(nums2)
        nums1.sort()
        nums2.sort()
        res = set()
        while i<m and j<n:
            if i==m-1 and nums2[j]>nums1[i]:
                return list(res)
            if j==n-1 and nums1[i]>nums2[j]:
                return list(res)
            if nums1[i]==nums2[j]:
                res.add(nums1[i])
                i+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return list(res)