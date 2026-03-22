class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res,i=0,0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
            seen.add(s[j])
            res = max(res,len(seen))
        return res