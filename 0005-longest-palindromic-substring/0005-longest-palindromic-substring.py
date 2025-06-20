class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res = s[0]
        for i in range(n):
            j=n-1
            while i<j:
                if j-i+1<=len(res):
                    break
                if s[i]!=s[j]:
                    j-=1
                    continue
                l=(j-i+1)//2
                ss = s[i:j+1]
                lef = ss[0:l]
                rev = ss[::-1]
                rig = rev[0:l]
                if lef==rig:
                    res = ss
                j-=1
        return res