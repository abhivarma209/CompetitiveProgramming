class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        seen = {}
        i,j=0,0
        res=0
        while j<len(s):
            seen[s[j]] = seen.get(s[j],0)+1
            max_freq = max(max_freq,seen[s[j]])
            if j-i+1-max_freq<=k:
                res=max(res,j-i+1)
            else:
                seen[s[i]]-=1
                i+=1
            j+=1
        return res
