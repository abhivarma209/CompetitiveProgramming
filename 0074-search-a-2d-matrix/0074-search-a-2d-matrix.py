class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo,hi=0,len(matrix)-1
        idx=-1
        if target<matrix[0][0]:
            return False
        if target>matrix[-1][-1]:
            return False
        while lo<=hi:
            mid=(hi+lo)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                idx = mid
                break
            if matrix[mid][0]<target:
                lo=mid+1
            else:
                hi=mid-1
        lo,hi=0,len(matrix[0])-1
        print(idx)
        while lo<=hi:
            mid=(lo+hi)//2
            if matrix[idx][mid]<target:
                lo=mid+1
            elif matrix[idx][mid]==target:
                return True
            else:
                hi=mid-1
        return False