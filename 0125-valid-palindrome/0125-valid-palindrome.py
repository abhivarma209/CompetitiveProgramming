class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs= ''
        for ch in s:
            if ord('A')<=ord(ch)<=ord('Z'):
                asc = ord('a')+ord(ch)-ord('A')
                ch = chr(asc)
            if ord('a')<=ord(ch)<=ord('z'):
                fs+=ch
            if '0'<=ch<='9':
                fs+=ch
        return fs[::-1]==fs