class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0': return 0
        if len(s)==1: return 1
        first = 1
        second = 1
        for i in range(1,len(s)):
            ts=0
            if 10<=int(s[i-1:i+1])<27:
                ts+=first
            if 1<=int(s[i])<10:
                ts+=second
            if ts==0: return 0
            first,second=second,ts
        return second
                