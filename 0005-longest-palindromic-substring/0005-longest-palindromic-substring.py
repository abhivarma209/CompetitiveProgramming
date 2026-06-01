class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len,idx=0,0
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>res_len:
                    res_len = right-left+1
                    idx = left
                left-=1
                right+=1
            left,right=i,i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>res_len:
                    res_len = right-left+1
                    idx = left
                left-=1
                right+=1
        return s[idx:idx+res_len]