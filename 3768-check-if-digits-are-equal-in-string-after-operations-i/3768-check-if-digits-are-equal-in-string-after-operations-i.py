class Solution:
    def hasSameDigits(self, s: str) -> bool:
        idx = 1
        temp = ""
        while len(s)>0:
            if idx<len(s):
                num = int(s[idx])+int(s[idx-1])
                new_ch = num%10
                temp+=str(new_ch)
            if idx == len(s)-1:
                s = temp
                temp = ""
                idx = 0
            if len(s) == 2:
                if s[-1] == s[-2]:
                    return True
                else:
                    return False
            idx+=1
        return False
            