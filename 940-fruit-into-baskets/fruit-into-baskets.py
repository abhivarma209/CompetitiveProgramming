class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i,j,res=0,0,1
        d = {}

        while i<=j and j<len(fruits):
            d[fruits[j]] = d[fruits[j]] + 1 if d.get(fruits[j]) else 1
            while i<j and len(d)>2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i+=1
            temp =0
            for k in d:
                temp+=d[k]
            res=max(temp,res)
            j+=1
        return res