class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res,i,j,sz=0,0,0,0
        while i<=j and j<len(s):
            if i==j:
                seen.add(s[j])
                j+=1
                res=max(res,1)
                continue
            if s[j] in seen:
                seen.remove(s[i])
                i+=1
            else:
                seen.add(s[j])
                j+=1
            res=max(res,len(seen))
        return res
            