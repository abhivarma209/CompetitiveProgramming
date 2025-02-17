class Solution:
    def sortString(self, s: str) -> str:
        arr = [0] * 26
        for ch in s:
            arr[ord(ch)-ord('a')] += 1
        res = ""
        flag = True
        while sum(arr) != 0:
            temp =""
            for i,num in enumerate(arr):
                if num>0:
                    temp+=chr(ord('a')+i)
                    arr[i]-=1
            if flag:
                res+=temp
                flag = False
            else:
                res+=temp[::-1]
                flag = True

        return res
            
         