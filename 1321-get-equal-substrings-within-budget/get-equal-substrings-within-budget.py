class Solution:
    def getCost( s: str, t: str, i: int) -> int:
        svalue = ord(s[i])
        tvalue = ord(t[i])
        cost = abs(svalue-tvalue)
        return cost
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i,j,res,temp=0,0,0,0
        
        while i<=j and j<len(s):
            curr_cost = Solution.getCost(s,t,j)
            temp += curr_cost
            while temp>maxCost:
                prev_cost = Solution.getCost(s,t,i)
                temp-=prev_cost
                i+=1
            res = max(res,j+1-i)
            j+=1
        
        return res
