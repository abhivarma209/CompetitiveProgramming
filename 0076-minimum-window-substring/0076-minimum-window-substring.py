class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        l,res=0,float('inf')
        w_l,w_r=0,0
        window = {}
        have = 0
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            if s[r] in need and window[s[r]]==need[s[r]]:
                have+=1
            while have == len(need):
                w_len = r-l+1
                if w_len<res:
                    res = w_len
                    w_l=l
                    w_r=r
                window[s[l]]-=1
                if s[l] in need and window[s[l]]<need[s[l]]:
                    have-=1
                l+=1
        
        return s[w_l:w_r+1] if res!=float(inf) else ""

