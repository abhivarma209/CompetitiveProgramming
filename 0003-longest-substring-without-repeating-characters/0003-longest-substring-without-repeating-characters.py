class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        i,j,res=0,0,0
        while i<=j and j<len(s):
            if s[j] in se:
                se.remove(s[i])
                i+=1
            else:
                se.add(s[j])
                j+=1
            res = max(res,len(se))
        return res