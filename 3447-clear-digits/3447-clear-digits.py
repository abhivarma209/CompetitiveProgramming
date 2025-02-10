class Solution:
    def clearDigits(self, s: str) -> str:
        res = ""
        
        for ch in s:
            if not ch.isdigit():
                res+=ch
            else:
                if len(res)>0:
                    res = res[:-1]

        return res