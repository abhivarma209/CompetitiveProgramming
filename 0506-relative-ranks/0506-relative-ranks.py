class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a=score.copy()
        a.sort(reverse=True)
        d={}
        for i in range(len(a)):
            if i==0:
                d[a[i]]="Gold Medal"
            elif i==1:
                d[a[i]]= "Silver Medal"
            elif i==2:
                d[a[i]]="Bronze Medal"
            else:
                d[a[i]]=str(i+1)
        res=[]
        for num in score:
            res.append(d[num])
        return res