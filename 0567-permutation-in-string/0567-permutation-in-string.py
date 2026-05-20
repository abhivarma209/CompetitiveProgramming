class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=[0]*26
        window=[0]*26
        for ch in s1:
            need[ord(ch)-ord('a')]+=1
        l,r=0,0
        while r<len(s1) and r<len(s2):
            idx = ord(s2[r])-ord('a')
            window[idx]+=1
            r+=1
        if window==need: return True
        while r<len(s2):
            l_idx = ord(s2[l])-ord('a')
            window[l_idx]-=1
            l+=1
            idx = ord(s2[r])-ord('a')
            window[idx]+=1
            r+=1
            if window==need: return True
        return False
        