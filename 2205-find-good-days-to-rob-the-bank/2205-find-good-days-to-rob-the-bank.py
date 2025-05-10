class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time==0:
            return [i for i in range(n)]
        res = []
        left = [1]
        right = [1]
        for i in range(1,n):
            if security[i]>security[i-1]:
                left.append(1)
            else:
                left.append(left[-1]+1)
        j=n-2
        while j>=0:
            if security[j]>security[j+1]:
                right.append(1)
            else:
                right.append(right[-1]+1)
            j-=1
        right = right[::-1]
        for i in range(time,n-time):
            if security[i-1]>=security[i]<=security[i+1] and left[i-1]>=time and right[i+1]>=time:
                res.append(i)
        return res

        
        