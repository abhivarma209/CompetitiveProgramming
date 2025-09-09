class Solution:
    def minimumSteps(self, s: str) -> int:
        write,n=0,len(s)
        res=0
        for read in range(n):
            if s[read]=='0':
                res+=read-write
                write+=1
        return res