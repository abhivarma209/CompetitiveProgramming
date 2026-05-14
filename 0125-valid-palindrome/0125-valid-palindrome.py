class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs= ''
        for ch in s:
            if 'A'<=ch<='Z':
                asc = ord('a')+ord(ch)-ord('A')
                ch = chr(asc)
            if 'a'<=ch<='z' or '0'<=ch<='9':
                fs+=ch
        return fs[::-1]==fs