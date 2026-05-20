class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=[0]*26
        window=[0]*26
        for ch in s1:
            need[ord(ch)-ord('a')]+=1
        for r in range(len(s2)):
            window[ord(s2[r])-ord('a')]+=1
            if r>=len(s1):
                window[ord(s2[r-len(s1)])-ord('a')]-=1
            if window==need: return True
        return False
        