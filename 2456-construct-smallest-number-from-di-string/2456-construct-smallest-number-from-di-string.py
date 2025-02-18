class Solution:
    def smallestNumber(self, pattern: str) -> str:
        strt = 1
        idx = 0
        max_used = 1
        res = ''
        while idx < len(pattern):
            rec = 0
            temp = pattern[idx]
            while idx < len(pattern) and pattern[idx] == temp:
                idx += 1
                rec += 1
            if temp == 'I':
                while rec>0:
                    res += str(strt)
                    max_used = max(max_used,strt)
                    strt = max_used+1
                    rec -= 1
            else:
                strt += rec
                while rec>0:
                    res += str(strt)
                    max_used = max(max_used,strt)
                    strt -= 1
                    rec -= 1
            
        res+=str(strt)
        return res

        