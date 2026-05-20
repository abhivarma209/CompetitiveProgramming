class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        lm,rm = 0,0
        res = 0
        while l<r:
            if height[l]<=height[r]:
                if height[l]<lm:
                    res += lm-height[l]
                else:
                    lm=height[l]
                l+=1
            else:
                if height[r]<rm:
                    res += rm-height[r]
                else:
                    rm=height[r]
                r-=1
        return res