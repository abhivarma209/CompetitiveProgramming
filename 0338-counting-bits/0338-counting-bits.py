class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        bits = [0]*(n+1)
        bits[1] = 1
        cp = 1
        i = 2
        while i<=n:
            temp = 1
            while i<=n and temp<cp:
                bits[i]=bits[cp]+bits[temp]
                temp+=1
                i+=1
            if temp==cp and i<=n:
                cp=i
                bits[i]=1
                i+=1
        return bits

        