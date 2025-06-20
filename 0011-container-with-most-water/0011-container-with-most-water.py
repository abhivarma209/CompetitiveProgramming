class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i,j,res = 0,n-1,0
        while i<j:
            x = j-i
            y = min(height[i],height[j])
            res = max(res,x*y)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return res