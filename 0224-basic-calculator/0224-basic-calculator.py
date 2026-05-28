class Solution:
    def calculate(self, s: str) -> int:
        res,curr,sign=0,0,1
        st=[]
        for ch in s:
            if '0'<=ch<='9':
                curr=curr*10+int(ch)
            elif ch=='+':
                res+=curr*sign
                sign = 1
                curr=0
            elif ch=='-':
                res+=curr*sign
                sign=-1
                curr=0
            elif ch=='(':
                st.append(res)
                st.append(sign)
                res=0
                sign=1
            elif ch==')':
                res+=sign*curr
                curr=0
                res*=st.pop()
                res+=st.pop()
            else:
                continue
        return res + sign*curr