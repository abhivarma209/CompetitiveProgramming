class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i,j,res,temp=0,0,0,0
        
        while i<=j and j<len(s):
            svalue = ord(s[j])
            tvalue = ord(t[j])
            curr_cost = abs(svalue-tvalue)
            temp += curr_cost
            while temp>maxCost:
                spvalue = ord(s[i])
                tpvalue = ord(t[i])
                prev_cost = abs(spvalue-tpvalue)
                temp-=prev_cost
                i+=1
            res = max(res,j+1-i)
            j+=1
        
        return res
